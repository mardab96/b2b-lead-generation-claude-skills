# Review checklist

Use this checklist when reviewing the pack after changes.

## What this review checks

- Skill activation is clear from the YAML `description`.
- `## Use this skill when` names the right decision moment.
- `## Required input` asks for concrete data, exports, notes or screenshots.
- `## Analysis workflow` has skill-specific steps.
- `## Output format` produces a decision-ready artifact.
- Examples show the expected depth of output.

## Core skills covered by examples

- `icp-reality-check`
- `lead-scoring-sanity-check`

## Pass criteria

- A reviewer can tell when each skill should activate without reading the whole repository.
- The skill does not ask for generic "context" when a concrete input is needed.
- The workflow gives enough steps to run the analysis with real CRM and campaign data.
- The output ends with decision, approval needed and missing data.
- No placeholder language remains in any `SKILL.md`.

## Validator

Run this from the repository root:

```bash
python3 scripts/validate-skills.py
```

Expected result:

```text
OK: all skills passed validation
```

## Manual review questions

- Would this skill activate at the moment an operator actually needs it?
- Does the analysis separate lead volume from lead quality?
- Does the output connect ads, landing pages, CRM and sales feedback?
- Does the skill avoid making performance claims without data?
