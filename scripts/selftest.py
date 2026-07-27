#!/usr/bin/env python3
"""Regression tests for the analysis scripts.

    python3 scripts/selftest.py

Each case is a defect that was found by running a script against a fixture
rather than by reading it. They live here so the same defect cannot come back
unnoticed. Run this before and after changing anything in scripts/.

exit 0 = every guarantee holds, 1 = one broke.
"""
import csv
import json
import os
import subprocess
import sys
import tempfile
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
FAILURES = []


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)


def run(script, *args):
    proc = subprocess.run([sys.executable, os.path.join(HERE, script)] + list(args),
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def run_json(script, *args):
    rc, out, err = run(script, *(args + ("--json",)))
    return (rc, json.loads(out), err) if rc == 0 else (rc, None, err)


def check(name, condition, detail=""):
    if condition:
        print("  pass  %s" % name)
    else:
        print("  FAIL  %s %s" % (name, detail))
        FAILURES.append(name)


def test_pipeline(tmp):
    print("pipeline_hygiene.py")
    today = date(2026, 7, 20)

    # A future close date must not become the reference date for "now".
    # It did once, and it marked 117 of 120 healthy deals as overdue.
    path = os.path.join(tmp, "future.csv")
    write_csv(path, [
        ["Deal name", "Stage", "Amount", "Created date", "Last activity date", "Close date"],
        ["A", "Proposal", 1000, (today - timedelta(days=20)).isoformat(),
         (today - timedelta(days=2)).isoformat(), (today + timedelta(days=180)).isoformat()],
        ["B", "Proposal", 1000, (today - timedelta(days=20)).isoformat(),
         (today - timedelta(days=2)).isoformat(), (today + timedelta(days=200)).isoformat()],
    ])
    rc, data, err = run_json("pipeline_hygiene.py", path)
    if rc != 0:
        return check("future close dates do not anchor now", False, err)
    check("a future close date does not become the reference date",
          data["as_of"] == (today - timedelta(days=2)).isoformat(), data["as_of"])
    check("healthy deals are not flagged as overdue",
          data["flags"]["close_date_passed"]["deals"] == 0,
          data["flags"]["close_date_passed"])
    check("nothing is removed from defensible pipeline without cause",
          data["defensible_pipeline"] == data["reported_pipeline"],
          "%s vs %s" % (data["defensible_pipeline"], data["reported_pipeline"]))

    # A deal flagged twice must only be subtracted once.
    path = os.path.join(tmp, "double.csv")
    write_csv(path, [
        ["Deal name", "Stage", "Amount", "Created date", "Last activity date", "Close date"],
        ["Quiet and overdue", "Proposal", 5000, (today - timedelta(days=300)).isoformat(),
         (today - timedelta(days=200)).isoformat(), (today - timedelta(days=50)).isoformat()],
        ["Healthy", "Proposal", 5000, (today - timedelta(days=10)).isoformat(),
         today.isoformat(), (today + timedelta(days=30)).isoformat()],
    ])
    rc, data, _ = run_json("pipeline_hygiene.py", path)
    check("a deal with two flags is subtracted once, not twice",
          data["defensible_pipeline"] == 5000, data["defensible_pipeline"])

    # No activity column at all must warn rather than silently pass everything.
    path = os.path.join(tmp, "noactivity.csv")
    write_csv(path, [["Deal name", "Stage", "Amount"], ["A", "Proposal", 1000]])
    rc, out, _ = run("pipeline_hygiene.py", path)
    check("a missing activity column is called out",
          rc == 0 and "no last-activity column" in out.lower(), out[:120])

    rc, _, _ = run("pipeline_hygiene.py", os.path.join(tmp, "nope.csv"))
    check("a missing file exits 2", rc == 2, "rc=%d" % rc)


def test_email_auth(tmp):
    print("email_auth_check.py")

    # Eleven lookups breaks SPF entirely. Ten is the limit and it is easy to pass.
    spf_11 = "v=spf1 " + " ".join("include:v%d.com" % i for i in range(11)) + " ~all"
    rc, data, err = run_json("email_auth_check.py", "--spf", spf_11)
    if rc != 0:
        return check("spf lookup limit", False, err)
    check("an SPF record over the lookup limit is critical, not a warning",
          any(sev == "critical" and "limit" in msg for sev, msg in data["spf"]["issues"]),
          data["spf"]["issues"])

    # +all authorises the whole internet.
    rc, data, _ = run_json("email_auth_check.py", "--spf", "v=spf1 +all")
    check("'+all' is reported as critical",
          any(sev == "critical" for sev, _ in data["spf"]["issues"]), data["spf"]["issues"])

    # A complete, healthy set must not be reported as broken.
    rc, data, _ = run_json(
        "email_auth_check.py",
        "--spf", "v=spf1 include:_spf.google.com -all",
        "--dkim", "v=DKIM1; k=rsa; p=" + "A" * 300,
        "--dmarc", "v=DMARC1; p=reject; rua=mailto:dmarc@example.com")
    check("a healthy configuration reports as authenticated",
          data["authenticated"] and data["critical_count"] == 0,
          "critical=%s" % data["critical_count"])

    # p=none monitors and enforces nothing; that must be visible.
    rc, data, _ = run_json("email_auth_check.py", "--dmarc", "v=DMARC1; p=none; rua=mailto:a@b.c")
    check("p=none is flagged as monitoring only",
          data["dmarc"]["policy"] == "none"
          and any("enforces nothing" in msg for _, msg in data["dmarc"]["issues"]),
          data["dmarc"]["issues"])

    # Nothing supplied at all is a usage error, not a clean bill of health.
    rc, _, _ = run("email_auth_check.py")
    check("supplying no records exits 2 rather than passing", rc == 2, "rc=%d" % rc)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for fn in (test_pipeline, test_email_auth):
            fn(tmp)
            print()
    if FAILURES:
        print("FAIL: %d guarantee(s) broken: %s" % (len(FAILURES), ", ".join(FAILURES)))
        return 1
    print("OK: every documented guarantee holds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
