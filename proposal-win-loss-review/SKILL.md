---
name: proposal-win-loss-review
description: Learns from won and lost deals to fix upstream targeting and messaging. Use when the user is diagnosing, planning, reviewing or deciding next actions for proposal win loss review in B2B lead generation.
---

# Proposal Win Loss Review

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user asks for help with proposal win loss review in B2B lead generation.
- the user provides data, screenshots, exports, notes or a URL related to proposal win loss review.
- the user needs an approval-ready diagnosis before changing campaigns, pages, tracking, CRM or follow-up.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- business model, ICP, offer, ACV or deal value range, sales cycle and main conversion goal.
- ad, landing page, lead form, CRM, call note, email or campaign data relevant to this diagnostic.
- time window, traffic source, lead volume and downstream outcomes where available.
- what decision the user is trying to make next: create, fix, scale, pause, brief sales or investigate.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Collect won/lost proposal notes, source, segment, deal size, competitor, objections and close reason.
2. Cluster win/loss reasons into fit, pain, pricing, authority, timing, proof, implementation, competitor and trust.
3. Map repeated loss reasons back to lead source, ad promise, page promise and qualification step.
4. Identify which upstream messages attract deals you can actually win.
5. Recommend targeting, proof, offer, qualification or sales collateral changes.

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

User: "Can you check this proposal win loss review before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
