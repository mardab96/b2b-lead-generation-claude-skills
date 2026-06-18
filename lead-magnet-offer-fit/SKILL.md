---
name: lead-magnet-offer-fit
description: Reviews a proposed or existing B2B lead magnet for buyer-stage fit, pain relevance, qualification strength and follow-up value. Use when creating, choosing, improving or diagnosing a free asset, gated resource, checklist, guide, template or webinar for lead generation.
---

# Lead Magnet Offer Fit

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user is creating a lead magnet and asks whether the offer is strong enough.
- a lead magnet gets downloads but weak leads, low reply quality or poor sales acceptance.
- the user needs to match an asset to ICP, buying stage, pain intensity and next-step intent.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- business model, ICP, offer, ACV or deal value range, sales cycle and main conversion goal.
- ad, landing page, lead form, CRM, call note, email or campaign data relevant to this diagnostic.
- time window, traffic source, lead volume and downstream outcomes where available.
- what decision the user is trying to make next: create, fix, scale, pause, brief sales or investigate.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Map the asset to buyer stage: problem-aware, solution-aware, vendor-aware or implementation-ready.
2. Check if the promise attracts the target buyer or broad low-intent researchers.
3. Identify the next commercial step the asset naturally earns: reply, demo, audit, trial, call or nurture.
4. Flag missing proof, weak specificity, generic AI content risk and follow-up gaps.
5. Score confidence as high, medium or low based on data quality, sample size and source reliability.
6. Produce the smallest useful next action, not a broad redesign or system rebuild.

## Decision rules

- If the data does not connect to revenue, pipeline, qualified leads or conversion quality, label the recommendation as a hypothesis.
- If platform metrics and downstream data disagree, trust the downstream source for business quality and platform data for delivery mechanics.
- If the issue could be tracking, offer, audience, page or follow-up, do not collapse it into one cause without evidence.
- Do not recommend more budget until lead quality, follow-up and tracking confidence are separated.

## Output format

| Finding | Evidence | Why it matters | Recommended action | Confidence |
|---|---|---|---|---|
| Short diagnostic claim | Data, quote, screenshot, export or missing-data note | Business impact or risk | Specific next step and owner | High / Medium / Low |

End with:

- `Decision:` fix / test / monitor / ask for data / do not act yet
- `Approval needed:` yes/no and what would change if approved
- `Missing data:` only the inputs that would materially change the recommendation

## Practical example

User: "Can you check this lead magnet offer fit before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
