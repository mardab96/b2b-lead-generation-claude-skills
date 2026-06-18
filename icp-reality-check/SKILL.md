---
name: icp-reality-check
description: Compares your stated ICP against actual closed-won and closed-lost customers. Use when B2B ads, landing pages, CRM data or sales notes show a lead quality problem that needs a decision before campaign, scoring or follow-up changes.
---

# Icp Reality Check

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user shares lead source, CRM stage, sales note, form, landing page or campaign data tied to icp reality check.
- the next decision could change targeting, qualification, scoring, follow-up, sales handoff or budget.
- lead volume looks acceptable but SQL, opportunity, closed-won, rejection or response-speed data raises doubt.

Do not use this skill for broad lead-generation advice without source, CRM, sales or qualification evidence. Use it when a real B2B lead quality decision is on the table.

## Required input

- business model, ICP, offer, ACV or deal value range, sales cycle and main conversion goal.
- ad, landing page, lead form, CRM, call note, email or campaign data relevant to this diagnostic.
- time window, traffic source, lead volume and downstream outcomes where available.
- what decision the user is trying to make next: create, fix, scale, pause, brief sales or investigate.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Write the stated ICP as a short profile: company type, buyer role, pain, budget, urgency and exclusion rules.
2. Build a comparison table for closed-won, closed-lost, disqualified and no-show leads by source, company size, role, industry, use case and deal value.
3. Identify ICP drift: segments that produce cheap leads but weak SQL/opportunity/closed-won rates.
4. Find ICP blind spots: segments with low lead volume but high sales acceptance or deal value.
5. Separate targeting problems from offer, page, qualification and follow-up problems before recommending a change.
6. Return an ICP action: keep, narrow, split into segments, exclude, or collect more data.

## Diagnostic rubric

Use this table when the user provides CRM or sales outcome data:

| Segment | Lead volume | SQL rate | Opportunity rate | Closed-won rate | Rejection pattern | ICP verdict |
|---|---:|---:|---:|---:|---|---|
| Company size / role / industry / use case | Count and source mix | Percent or missing-data marker | Percent or missing-data marker | Percent or missing-data marker | Sales reason, no-show pattern or lost reason | Keep / narrow / split / exclude / collect more data |

Then summarize:

- ICP drift: segments that create leads but weak pipeline.
- ICP blind spot: segments with low volume but strong downstream quality.
- ICP change: the one targeting or qualification change worth testing first.

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

User: "Here are CRM stages, source data and sales notes for icp reality check. What should we change before the next campaign move?"

Assistant should: use the supplied evidence, run the workflow above, produce the skill-specific rubric or diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
