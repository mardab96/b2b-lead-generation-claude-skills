# Scripts

Two of the thirty skills do arithmetic over dates and records rather than
reading text. Those two ship a script, because a model counting stale deals
across a few hundred rows produces a number that feels right and is not.

| Script | Used by | What it takes out of the model's hands |
|---|---|---|
| `pipeline_hygiene.py` | Pipeline Hygiene Audit | Deal ageing, inactivity windows, defensible versus reported pipeline |
| `email_auth_check.py` | Spam Folder Check | Parsing SPF, DKIM and DMARC, including the lookup limit and the policy qualifier |

Python 3 standard library only. No network, no writes, no credentials.

```bash
python3 scripts/pipeline_hygiene.py deals.csv --inactive-days 90 --cycle-days 45
python3 scripts/email_auth_check.py --spf "v=spf1 include:_spf.google.com -all" --dmarc "v=DMARC1; p=reject; rua=mailto:a@b.c"
```

Add `--json` to either for the full machine-readable output.

The other twenty-eight skills read text and produce text. A script there would
be ceremony rather than rigour, and this file says so rather than leaving the
asymmetry unexplained.

## The guarantees

**A projection never anchors the present.** `pipeline_hygiene.py` takes its
reference date from the newest created or last-activity date, never from a close
date. Close dates sit in the future, and letting one anchor "now" marked healthy
deals as overdue. That defect shipped, was caught by running the script against a
fixture, and is now a test.

**A deal is subtracted once.** A deal that is both quiet and past its close date
counts against defensible pipeline a single time.

**A missing signal is announced.** No last-activity column means the strongest
predictor of a dead deal is absent, and the output says so rather than quietly
reporting a clean bill of health.

**An SPF record over the lookup limit is critical, not cosmetic.** Eleven
DNS-querying mechanisms make the record fail with permerror, which receivers
treat as no SPF at all. A record can look configured and protect nothing.

**Nothing here measures inbox placement.** These scripts read what you paste.
Only a seed test or the receiving provider can tell you where mail landed, and
the output repeats that rather than implying otherwise.

## Testing

```bash
python3 scripts/selftest.py
python3 scripts/validate-skills.py
```

Eleven regression checks over the two analysis scripts, plus the pack validator
over all thirty skills. Run both before shipping any change.

## Exit codes

`0` ran, `2` could not run (file unreadable, required columns absent, or no
records supplied).
