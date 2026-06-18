---
name: landing-page-qualification-review
description: Diagnoses whether the page attracts the right leads or just more leads. Use when the user is diagnosing, planning, reviewing or deciding next actions for landing page qualification review in B2B lead generation.
---

# Landing Page Qualification Review

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user asks for help with landing page qualification review in B2B lead generation.
- the user provides data, screenshots, exports, notes or a URL related to landing page qualification review.
- the user needs an approval-ready diagnosis before changing campaigns, pages, tracking, CRM or follow-up.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- business model, ICP, offer, ACV or deal value range, sales cycle and main conversion goal.
- ad, landing page, lead form, CRM, call note, email or campaign data relevant to this diagnostic.
- time window, traffic source, lead volume and downstream outcomes where available.
- what decision the user is trying to make next: create, fix, scale, pause, brief sales or investigate.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. Identify what the page qualifies for: budget, urgency, company fit, role fit, pain, use case or implementation readiness.
2. Check whether the hero and offer attract the right buyer or just any interested visitor.
3. Review the form, proof, objections and CTA for qualification signals or lack of friction.
4. Compare page promise with sales acceptance, disqualification reasons and lead-to-opportunity drop-off.
5. Recommend qualification copy, form, proof or CTA changes that improve lead quality without adding unnecessary friction.

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

User: "Can you check this landing page qualification review before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
