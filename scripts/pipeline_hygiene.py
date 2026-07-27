#!/usr/bin/env python3
"""Separate defensible pipeline from decoration in a CRM deal export.

Used by: pipeline-hygiene-audit

Why this exists: the pipeline number quoted in meetings is a sum, and sums are
easy. What is hard is the ageing: which deals have been in a stage longer than
the cycle allows, which have gone quiet, which close dates have already passed.
Doing that by eye over a few hundred deals produces a number that feels right,
and feeling right is exactly the problem this skill exists to fix.

Input: one CSV with a row per OPEN deal.

  deal, stage, value                 required
  created_date                       strongly recommended
  last_activity_date                 the single best predictor of a dead deal
  close_date                         optional
  owner, source                      optional

usage:
  python3 scripts/pipeline_hygiene.py deals.csv
  python3 scripts/pipeline_hygiene.py deals.csv --inactive-days 90 --cycle-days 45 --json

The reference date is the newest CREATED or LAST-ACTIVITY date in the file, not
today and never a close date. Close dates are projections and sit in the future,
so anchoring on them would mark healthy deals as overdue. Using the file rather
than today means a stale export cannot make every deal look freshly touched. The
date used is printed.

exit 0 = ran, 2 = could not run.
"""
import argparse
import csv
import json
import sys
from datetime import datetime

ALIASES = {
    "deal": ["deal", "deal name", "name", "opportunity", "id", "deal id"],
    "stage": ["stage", "deal stage", "status", "pipeline stage"],
    "value": ["value", "amount", "deal value", "revenue", "acv", "arr"],
    "created_date": ["created date", "created", "create date", "created_at", "open date"],
    "last_activity_date": ["last activity date", "last activity", "last contacted",
                           "last touch", "last_activity", "last engagement"],
    "close_date": ["close date", "expected close date", "closing date", "close_date"],
    "owner": ["owner", "deal owner", "rep", "assigned to"],
    "source": ["source", "lead source", "channel"],
}
DATE_FORMATS = ["%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%m/%d/%Y", "%d.%m.%Y", "%Y-%m-%dT%H:%M:%S"]


def norm(s):
    return " ".join(str(s or "").strip().lower().replace("_", " ").split())


def parse_date(raw):
    s = str(raw or "").strip()
    if not s:
        return None
    s = s.replace("Z", "").split("+")[0].strip()
    if " " in s and "T" not in s:
        s = s.split(" ")[0]
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def money(raw):
    s = str(raw or "").strip()
    if not s:
        return 0.0
    neg = s.startswith("(") and s.endswith(")")
    for ch in "()$£€ ,":
        s = s.replace(ch, "")
    try:
        v = float(s)
    except ValueError:
        return 0.0
    return -v if neg else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--inactive-days", type=int, default=90,
                    help="days without activity before a deal is flagged (default 90)")
    ap.add_argument("--cycle-days", type=int, default=None,
                    help="typical sales cycle in days; stage age is judged against it")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        with open(args.csv_path, newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
    except OSError as exc:
        print("could not read %s: %s" % (args.csv_path, exc), file=sys.stderr)
        return 2
    if not rows:
        print("no rows", file=sys.stderr)
        return 2

    header = {norm(h): h for h in rows[0].keys()}
    cm = {}
    for key, aliases in ALIASES.items():
        for alias in aliases:
            if alias in header:
                cm[key] = header[alias]
                break
    missing = [k for k in ("deal", "stage", "value") if k not in cm]
    if missing:
        print("missing required columns: %s" % ", ".join(missing), file=sys.stderr)
        print("columns found: %s" % ", ".join(rows[0].keys()), file=sys.stderr)
        return 2

    deals, skipped = [], 0
    all_dates = []
    for row in rows:
        name = str(row.get(cm["deal"], "")).strip()
        if not name:
            skipped += 1
            continue
        created = parse_date(row.get(cm["created_date"])) if cm.get("created_date") else None
        activity = parse_date(row.get(cm["last_activity_date"])) if cm.get("last_activity_date") else None
        close = parse_date(row.get(cm["close_date"])) if cm.get("close_date") else None
        # Only dates describing something that already happened can anchor "now".
        # close_date is a projection and is usually in the future, so including it
        # would push the reference date forward and mark live deals as overdue.
        for d in (created, activity):
            if d:
                all_dates.append(d)
        deals.append({
            "deal": name,
            "stage": str(row.get(cm["stage"], "")).strip() or "(no stage)",
            "value": money(row.get(cm["value"])),
            "created": created, "activity": activity, "close": close,
            "owner": str(row.get(cm.get("owner", ""), "")).strip() if cm.get("owner") else "",
        })
    if not deals:
        print("no usable deals", file=sys.stderr)
        return 2

    # Reference date comes from the file. Using today would make a three-month-old
    # export look like every deal was touched recently.
    past_dates = [d for d in all_dates if d]
    as_of = max(past_dates) if past_dates else None

    total_value = sum(d["value"] for d in deals)

    flags = {"no_activity": [], "close_date_passed": [], "stage_age_over_cycle": [],
             "missing_activity_date": [], "missing_value": []}

    for d in deals:
        if not cm.get("last_activity_date") or d["activity"] is None:
            flags["missing_activity_date"].append(d)
        elif as_of and (as_of - d["activity"]).days > args.inactive_days:
            d["days_inactive"] = (as_of - d["activity"]).days
            flags["no_activity"].append(d)
        if d["close"] and as_of and d["close"] < as_of:
            flags["close_date_passed"].append(d)
        if args.cycle_days and d["created"] and as_of:
            age = (as_of - d["created"]).days
            if age > args.cycle_days:
                d["days_open"] = age
                flags["stage_age_over_cycle"].append(d)
        if d["value"] == 0:
            flags["missing_value"].append(d)

    # A deal counts against defensible pipeline once, however many flags it has.
    undefendable = {id(d) for d in flags["no_activity"]} | {id(d) for d in flags["close_date_passed"]}
    removed_value = sum(d["value"] for d in deals if id(d) in undefendable)
    defensible = total_value - removed_value

    by_stage = {}
    for d in deals:
        s = by_stage.setdefault(d["stage"], {"deals": 0, "value": 0.0, "ages": []})
        s["deals"] += 1
        s["value"] += d["value"]
        if d["created"] and as_of:
            s["ages"].append((as_of - d["created"]).days)
    for s in by_stage.values():
        s["median_age_days"] = sorted(s["ages"])[len(s["ages"]) // 2] if s["ages"] else None
        del s["ages"]

    review = sorted((d for d in deals if id(d) in undefendable),
                    key=lambda d: -d["value"])

    result = {
        "as_of": as_of.isoformat() if as_of else None,
        "deals": len(deals), "rows_skipped": skipped,
        "reported_pipeline": round(total_value, 2),
        "defensible_pipeline": round(defensible, 2),
        "removed_value": round(removed_value, 2),
        "inactive_days_threshold": args.inactive_days,
        "flags": {k: {"deals": len(v), "value": round(sum(x["value"] for x in v), 2)}
                  for k, v in flags.items()},
        "by_stage": {k: {"deals": v["deals"], "value": round(v["value"], 2),
                         "median_age_days": v["median_age_days"]}
                     for k, v in sorted(by_stage.items(), key=lambda kv: -kv[1]["value"])},
        "review_list": [{"deal": d["deal"], "stage": d["stage"], "value": round(d["value"], 2),
                         "days_inactive": d.get("days_inactive"),
                         "close_date_passed": bool(d["close"] and as_of and d["close"] < as_of)}
                        for d in review[:50]],
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print("deals: %d   reference date from file: %s" % (len(deals), as_of or "none found"))
    if not cm.get("last_activity_date"):
        print("WARNING: no last-activity column. The strongest predictor of a dead "
              "deal is missing, so this audit can only check dates and values.")
    print()
    print("reported pipeline:   %14.2f" % result["reported_pipeline"])
    print("defensible pipeline: %14.2f" % result["defensible_pipeline"])
    print("difference:          %14.2f" % -result["removed_value"])
    print()
    print("%-28s %8s %14s" % ("flag", "deals", "value"))
    for k, v in result["flags"].items():
        if v["deals"]:
            print("%-28s %8d %14.2f" % (k, v["deals"], v["value"]))
    print()
    print("%-24s %8s %14s %12s" % ("stage", "deals", "value", "median age"))
    for stage, s in result["by_stage"].items():
        print("%-24s %8d %14.2f %12s"
              % (stage[:24], s["deals"], s["value"],
                 "-" if s["median_age_days"] is None else "%dd" % s["median_age_days"]))
    if result["review_list"]:
        print()
        print("review these first (highest value, flagged):")
        for d in result["review_list"][:12]:
            why = []
            if d["days_inactive"]:
                why.append("%dd quiet" % d["days_inactive"])
            if d["close_date_passed"]:
                why.append("close date passed")
            print("  %-32s %12.2f  %s" % (d["deal"][:32], d["value"], ", ".join(why)))
        if len(review) > 12:
            print("  ... %d more, use --json for the full list" % (len(review) - 12))
    print()
    print("Defensible pipeline is not a forecast. It is what is left after removing")
    print("deals that have gone quiet or whose close date has already passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
