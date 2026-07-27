---
name: pipeline-hygiene-audit
description: Finds the dead deals, stale stages and missing dates that make a CRM pipeline unreliable, and separates real pipeline from wishful pipeline. Use when a forecast or board update is due, or when the number in the CRM has stopped resembling reality.
---

# Pipeline Hygiene Audit

## Use this skill when

The pipeline number is quoted in meetings and nobody quite believes it.

Pipeline decays quietly. A deal that was real in March sits in Proposal in August because nobody wants to be the person who closes it as lost. Multiply that by a year and the total at the top of the report stops meaning anything, which is usually discovered during a forecast conversation with someone senior.

Run this before the forecast, not after it goes wrong.

## Required input

- A deal export with, at minimum: deal name or id, stage, value, created date, and last activity date.
- What the stages are supposed to mean.

Better with:

- expected close date, and whether it has been changed before
- owner
- source
- historical conversion rate between stages
- typical sales cycle length

## Analysis workflow

1. Run `../scripts/pipeline_hygiene.py` over the export. Counting stale deals, measuring stage ageing and comparing close dates against the sales cycle are arithmetic, and doing it by eye across a few hundred deals produces numbers that feel right and are not.
2. Age every deal against the typical sales cycle for its stage. A deal that has been in one stage for three times the normal duration is not a slow deal, it is an unclosed one.
3. Find deals with no activity inside a reasonable window. No activity is the single strongest predictor of a deal that will never close, and it is usually visible months before anyone acts on it.
4. Check the close dates. Dates in the past, dates that have been pushed more than twice, and dates that cluster suspiciously on the last day of a quarter each tell a different story about how the forecast is being constructed.
5. Check stage definitions against stage behaviour. If deals routinely skip a stage or sit in one for a day, the stage is not doing any work and the pipeline reporting inherits that.
6. Split the pipeline into what is defensible and what is decoration, and give both numbers. The gap between them is the actual finding.
7. Produce a specific list to review, deal by deal, rather than a recommendation to "clean up the CRM", which never happens.

## Decision rules

- No activity plus stage age beyond the cycle equals a close-lost candidate, whatever the owner says about it.
- Never delete or alter deals. This produces a review list; a human decides.
- A pushed close date is information, not a problem in itself. Three pushes on the same deal is a pattern.
- If stage definitions are missing or contradictory, fix that before trusting any conversion rate calculated from them.
- Do not report a forecast number this skill has not been given the inputs to support. Quote the defensible subset instead.

## Output format

### Two numbers

Total pipeline as reported, and defensible pipeline after removing stale and inactive deals. State what was removed and why.

### Hygiene table

| Issue | Deals | Value | What it means |
|---|---|---|---|
| No activity beyond window | | | |
| Stage age beyond cycle | | | |
| Close date in the past | | | |
| Close date pushed 3+ times | | | |
| Missing required field | | | |

### Review list

The specific deals to look at, ordered by value, with a recommended action each: close lost, re-engage, re-date, or leave.

### Stage health

Where deals actually get stuck, and whether any stage is doing no work.

### What to fix in the process

The one or two changes that would stop this recurring, such as an activity-based ageing rule.

## Practical example

An export of 340 open deals showing 4.1M in pipeline.

The script finds 96 deals with no activity in over 90 days, worth 1.3M, and a further 40 whose close date has passed. The stage ageing shows Proposal holding deals for a median of 71 days against a stated 21-day cycle.

The defensible number is 2.4M, not 4.1M, and that gap is the whole finding. The review list leads with the eleven highest-value inactive deals rather than asking anyone to review all 96. The process fix is a rule that flags a deal at 45 days without activity, which would have caught most of these while they were still recoverable.

## Guardrails

- Do not modify CRM records.
- Do not report a hygiene-adjusted number as a forecast. It is a cleaner input to one.
- Do not name individual owners in a way that turns a data exercise into a performance review.
- Do not assume a missing field means a bad deal. Missing data is missing data.
- Do not treat a single quarter as the sales cycle if the data covers less than two full cycles.
