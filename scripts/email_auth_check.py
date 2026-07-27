#!/usr/bin/env python3
"""Parse SPF, DKIM and DMARC records and report what actually protects the domain.

Used by: spam-folder-check

Why this exists: these three records are short strings with a lot of load-bearing
punctuation. The difference between `~all` and `-all`, between `p=none` and
`p=quarantine`, and between ten DNS lookups and eleven, is the difference between
a protected domain and one that merely looks configured. Reading them by eye is
how a domain passes an inspection and still lands in spam.

Input: the records, pasted. Either as a file with one record per line, or via
flags. Nothing here queries DNS, so it runs anywhere and touches nothing.

  python3 scripts/email_auth_check.py --spf "v=spf1 include:_spf.google.com ~all" \\
                                      --dmarc "v=DMARC1; p=none; rua=mailto:x@y.com"
  python3 scripts/email_auth_check.py records.txt --json

To collect the records:
  dig +short TXT example.com
  dig +short TXT selector._domainkey.example.com
  dig +short TXT _dmarc.example.com

exit 0 = ran, 2 = could not run.
"""
import argparse
import json
import re
import sys

# SPF permits at most 10 DNS-querying mechanisms. Exceeding it makes the record
# fail with permerror, which receivers treat as no SPF at all.
SPF_LOOKUP_MECHANISMS = ("include:", "a:", "mx:", "ptr", "exists:", "redirect=")
SPF_LOOKUP_LIMIT = 10


def find_record(lines, prefix):
    for line in lines:
        clean = line.strip().strip('"').strip()
        if clean.lower().startswith(prefix):
            return clean
    return None


def check_spf(record):
    out = {"record": record, "present": bool(record), "issues": [], "lookups": None, "policy": None}
    if not record:
        out["issues"].append(("critical", "No SPF record. Receivers cannot verify which servers may send for this domain."))
        return out
    lookups = 0
    for mech in SPF_LOOKUP_MECHANISMS:
        lookups += record.lower().count(mech)
    out["lookups"] = lookups
    if lookups > SPF_LOOKUP_LIMIT:
        out["issues"].append(("critical",
                              "%d DNS-querying mechanisms, over the limit of %d. The record fails with "
                              "permerror, which receivers treat as no SPF at all." % (lookups, SPF_LOOKUP_LIMIT)))
    elif lookups >= 8:
        out["issues"].append(("warning",
                              "%d DNS-querying mechanisms. The limit is %d and each new vendor adds one."
                              % (lookups, SPF_LOOKUP_LIMIT)))
    match = re.search(r"([-~+?])all\b", record)
    if not match:
        out["issues"].append(("warning", "No 'all' mechanism, so the record does not say what to do with everything else."))
    else:
        qualifier = match.group(1)
        out["policy"] = {"-": "fail", "~": "softfail", "+": "pass", "?": "neutral"}[qualifier]
        if qualifier == "+":
            out["issues"].append(("critical", "'+all' authorises the entire internet to send as this domain."))
        elif qualifier == "?":
            out["issues"].append(("warning", "'?all' is neutral, which provides no protection."))
        elif qualifier == "~":
            out["issues"].append(("info", "'~all' is softfail. Normal while testing, weaker than '-all' once the sending sources are known."))
    if record.lower().count("v=spf1") > 1:
        out["issues"].append(("critical", "More than one SPF record. Receivers treat this as permerror."))
    return out


def check_dkim(record):
    out = {"record": record, "present": bool(record), "issues": [], "key_bits": None}
    if not record:
        out["issues"].append(("critical", "No DKIM record supplied. Without a signature, the message body cannot be shown to be unaltered, and DMARC cannot pass on DKIM."))
        return out
    if "p=" not in record:
        out["issues"].append(("critical", "No public key in the record."))
        return out
    key = record.split("p=", 1)[1].strip().strip('"').split(";")[0].strip()
    if not key:
        out["issues"].append(("critical", "Empty public key, which means the selector is revoked."))
        return out
    # base64 length maps to key size closely enough to flag a 1024-bit key
    approx_bits = int(len(key) * 6 / 8 * 8 / 1.16) if key else 0
    out["key_bits"] = "2048 or higher" if len(key) > 250 else "likely 1024"
    if len(key) <= 250:
        out["issues"].append(("warning", "Key looks like 1024-bit. 2048 is the current norm."))
    if "t=y" in record.replace(" ", ""):
        out["issues"].append(("warning", "DKIM is in test mode (t=y), so receivers are told to ignore failures."))
    return out


def check_dmarc(record):
    out = {"record": record, "present": bool(record), "issues": [], "policy": None, "pct": 100}
    if not record:
        out["issues"].append(("critical", "No DMARC record. Nothing tells receivers what to do when SPF and DKIM fail, and nobody is being sent reports."))
        return out
    match = re.search(r"\bp=(none|quarantine|reject)\b", record, re.I)
    if not match:
        out["issues"].append(("critical", "No policy (p=) in the DMARC record."))
    else:
        out["policy"] = match.group(1).lower()
        if out["policy"] == "none":
            out["issues"].append(("warning", "p=none monitors but enforces nothing. Fine as a first step, not a destination."))
    pct = re.search(r"\bpct=(\d+)", record)
    if pct:
        out["pct"] = int(pct.group(1))
        if out["pct"] < 100:
            out["issues"].append(("info", "Policy applies to %s%% of mail." % out["pct"]))
    if "rua=" not in record.lower():
        out["issues"].append(("warning", "No rua= address, so aggregate reports go nowhere and nobody will notice a problem."))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("records_file", nargs="?", help="file with one DNS TXT record per line")
    ap.add_argument("--spf")
    ap.add_argument("--dkim")
    ap.add_argument("--dmarc")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    lines = []
    if args.records_file:
        try:
            with open(args.records_file, encoding="utf-8") as fh:
                lines = fh.readlines()
        except OSError as exc:
            print("could not read %s: %s" % (args.records_file, exc), file=sys.stderr)
            return 2

    spf = args.spf or find_record(lines, "v=spf1")
    dkim = args.dkim or find_record(lines, "v=dkim1")
    dmarc = args.dmarc or find_record(lines, "v=dmarc1")

    if not any([spf, dkim, dmarc]):
        print("no SPF, DKIM or DMARC record found. Pass them with --spf/--dkim/--dmarc "
              "or in a file, one record per line.", file=sys.stderr)
        return 2

    result = {"spf": check_spf(spf), "dkim": check_dkim(dkim), "dmarc": check_dmarc(dmarc)}
    all_issues = [(k, sev, msg) for k, v in result.items() for sev, msg in v["issues"]]
    result["critical_count"] = sum(1 for _, sev, _ in all_issues if sev == "critical")
    result["warning_count"] = sum(1 for _, sev, _ in all_issues if sev == "warning")

    # An authenticated domain needs DMARC to pass on an aligned SPF or DKIM.
    result["authenticated"] = (
        result["spf"]["present"] and result["dkim"]["present"] and result["dmarc"]["present"]
        and result["critical_count"] == 0)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print("SPF   %s" % ("present" if spf else "MISSING"))
    print("DKIM  %s" % ("present" if dkim else "MISSING or not supplied"))
    print("DMARC %s%s" % ("present" if dmarc else "MISSING",
                          "" if not result["dmarc"]["policy"] else " (p=%s)" % result["dmarc"]["policy"]))
    print()
    for record_name in ("spf", "dkim", "dmarc"):
        for sev, msg in result[record_name]["issues"]:
            print("%-9s %-6s %s" % (sev.upper(), record_name.upper(), msg))
    print()
    if result["authenticated"]:
        print("All three records are present with no critical problems. Authentication is")
        print("not the reason mail is being filtered; look at volume, list quality and")
        print("complaint rate next.")
    else:
        print("Fix the critical items before changing anything about copy or volume.")
        print("A domain that cannot prove who it is will be filtered regardless of what it sends.")
    print()
    print("This reads the records you supplied. It does not query DNS, and it cannot")
    print("measure inbox placement. Only a seed test or provider data can do that.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
