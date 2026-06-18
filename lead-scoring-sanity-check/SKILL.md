---
name: lead-scoring-sanity-check
description: Tests B2B lead scoring rules against real CRM outcomes, sales feedback, qualification stages and revenue signals. Use when scores look high but SQL, opportunity or closed-won quality is weak.
---

# Lead Scoring Sanity Check

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user has lead scores, MQL rules or qualification rules and doubts their quality.
- high-scoring leads are rejected by sales or do not become opportunities.
- the team needs to distinguish engagement bias from revenue likelihood.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- business model, ICP, offer, ACV or deal value range, sales cycle and main conversion goal.
- ad, landing page, lead form, CRM, call note, email or campaign data relevant to this diagnostic.
- time window, traffic source, lead volume and downstream outcomes where available.
- what decision the user is trying to make next: create, fix, scale, pause, brief sales or investigate.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Inventory current scoring factors, point values, thresholds and MQL/SQL handoff rules.
2. Compare score buckets with MQL, SQL, opportunity, closed-won, closed-lost and disqualified outcomes.
3. Calculate or estimate false positives, false negatives, source bias, firmographic bias and activity bias.
4. Use sales rejection reasons to identify misleading scoring signals.
5. Recommend keep, recalibrate, split scoring by segment, remove weak factors or add missing revenue-linked signals.

## Decision rules

- If the data does not connect to revenue, pipeline, qualified leads or conversion quality, label the recommendation as a hypothesis.
- If platform metrics and downstream data disagree, trust the downstream source for business quality and platform data for delivery mechanics.
- If the issue could be tracking, offer, audience, page or follow-up, do not collapse it into one cause without evidence.
- Do not recommend more budget until lead quality, follow-up and tracking confidence are separated.

## Output format

| Finding | Evidence | Lead quality impact | Recommended action | Confidence |
|---|---|---|---|---|
| Specific diagnostic claim | Data, screenshot, report, note or missing-data marker | Business or signal consequence | Smallest useful next step and owner | High / Medium / Low |

End with:

- `Decision:` fix / test / monitor / ask for data / do not act yet
- `Approval needed:` yes/no and what would change if approved
- `Missing data:` only the inputs that would materially change the recommendation

## Practical example

User: "Can you check this lead scoring sanity check before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
