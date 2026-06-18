---
name: lead-scoring-sanity-check
description: Tests B2B lead scoring rules against real CRM outcomes, sales feedback, qualification stages and revenue signals. Use when B2B ads, landing pages, CRM data or sales notes show a lead quality problem that needs a decision before campaign, scoring or follow-up changes.
---

# Lead Scoring Sanity Check

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user shares lead source, CRM stage, sales note, form, landing page or campaign data tied to lead scoring sanity check.
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

1. Inventory current scoring factors, point values, thresholds and MQL/SQL handoff rules.
2. Compare score buckets with MQL, SQL, opportunity, closed-won, closed-lost and disqualified outcomes.
3. Calculate or estimate false positives, false negatives, source bias, firmographic bias and activity bias.
4. Use sales rejection reasons to identify misleading scoring signals.
5. Recommend keep, recalibrate, split scoring by segment, remove weak factors or add missing revenue-linked signals.

## Diagnostic rubric

Use this table when the user provides scoring and CRM outcome data:

| Score bucket | Lead volume | MQL rate | SQL rate | Opportunity rate | Closed-won rate | Rejection pattern | Scoring verdict |
|---|---:|---:|---:|---:|---:|---|---|
| Score range or lifecycle tier | Count and source mix | Percent or missing-data marker | Percent or missing-data marker | Percent or missing-data marker | Percent or missing-data marker | Common sales reason or disqualification reason | Keep / lower / raise / split / remove factor |

Then call out:

- False positives: high-score leads rejected by sales or stuck before opportunity.
- False negatives: low-score leads that become SQLs, opportunities or closed-won.
- Bias source: activity, source, firmographic, title, company size or form type.

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

User: "Here are CRM stages, source data and sales notes for lead scoring sanity check. What should we change before the next campaign move?"

Assistant should: use the supplied evidence, run the workflow above, produce the skill-specific rubric or diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
