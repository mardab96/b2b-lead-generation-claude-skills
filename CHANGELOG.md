# Changelog

## [2.0.0] - 2026-07-28

### Added

Skills 21 to 30. The first twenty all assume a lead arrives: an ad is clicked, a
form is filled, a record appears in the CRM. These ten cover the week when that
does not happen and you have to go out yourself, plus what happens after the
call that the first twenty never touched.

- 21 Spam Folder Check
- 22 What to Say to This Company
- 23 Meeting Prep in Five Minutes
- 24 Ghosted After the Demo
- 25 Write the Follow-Up
- 26 Objection Cheat Sheet
- 27 Won Deal to Case Study
- 28 Cold Outbound Sequence Review
- 29 Discovery Call Gap Analysis
- 30 Pipeline Hygiene Audit

Most of them need nothing exported. A pasted thread, a transcript or a company
name is enough, which is deliberate: the first twenty are gated on having CRM
data assembled, and that is where they stop being used.

- `scripts/pipeline_hygiene.py` separates defensible pipeline from decoration.
- `scripts/email_auth_check.py` reads SPF, DKIM and DMARC and says which of the
  three actually protects the domain.
- `scripts/selftest.py`, eleven regression checks over both scripts.
- MIT `LICENSE`, which the README had been claiming without the file.
- `AGENTS.md`.

### Changed

- The install command now creates the skills directory and copies the skill
  folders plus `scripts/` and `references/`, rather than copying the whole repo
  including its README into the skills directory.
- Removed em dashes from the README.

### Known

Skills 1 to 20 share a visible template: the same sentence closes the practical
example in all twenty, and the first section of each carries the skill's own
name pasted into a stock phrase. The new ten are not written that way. Rewriting
the original twenty is a separate job.
