---
name: ad-to-landing-promise-match
description: Verifies that ads, landing page and CTA promise the same thing. Use when B2B ads, landing pages, CRM data or sales notes show a lead quality problem that needs a decision before campaign, scoring or follow-up changes.
---

# Ad To Landing Promise Match

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user shares lead source, CRM stage, sales note, form, landing page or campaign data tied to ad to landing promise match.
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

1. Extract the exact promise, audience, pain, proof, CTA and next step from each ad.
2. Extract the same elements from the landing page hero, form, CTA and first proof block.
3. Mark mismatches by severity: audience mismatch, outcome mismatch, offer mismatch, proof gap, CTA gap or commitment mismatch.
4. Estimate the likely consequence: lower CVR, worse lead quality, higher bounce, form abandonment or sales confusion.
5. Prioritize the smallest copy, CTA or page section fix that restores promise continuity.

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

User: "Here are CRM stages, source data and sales notes for ad to landing promise match. What should we change before the next campaign move?"

Assistant should: use the supplied evidence, run the workflow above, produce the skill-specific rubric or diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
