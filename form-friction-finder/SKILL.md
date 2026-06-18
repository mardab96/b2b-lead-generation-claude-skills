---
name: form-friction-finder
description: Finds fields, steps and UX patterns that kill form completion. Use when the user is diagnosing, planning, reviewing or deciding next actions for form friction finder in B2B lead generation.
---

# Form Friction Finder

Use the shared quality bar in `../references/output-standard.md` and `../references/skill-design-principles.md` when those files are available.

## Use this skill when

- the user asks for help with form friction finder in B2B lead generation.
- the user provides data, screenshots, exports, notes or a URL related to form friction finder.
- the user needs an approval-ready diagnosis before changing campaigns, pages, tracking, CRM or follow-up.

Do not use this skill for a generic brainstorming request. Use it when there is a concrete asset, setup, report, page, funnel, tracking issue or decision to diagnose.

## Required input

- business model, ICP, offer, ACV or deal value range, sales cycle and main conversion goal.
- ad, landing page, lead form, CRM, call note, email or campaign data relevant to this diagnostic.
- time window, traffic source, lead volume and downstream outcomes where available.
- what decision the user is trying to make next: create, fix, scale, pause, brief sales or investigate.
- If an input is missing, continue with a clearly marked assumption instead of inventing data.

## Analysis workflow

1. List every field, step, required answer, validation rule and hidden field in the form.
2. Classify each field as essential for routing, qualification, sales context, compliance or nice-to-have.
3. Compare form friction with buyer intent, offer value and traffic source temperature.
4. Look for mobile-specific friction: keyboard type, dropdown length, field order, error messages and page scroll.
5. Recommend remove, reorder, make optional, split, prefill or explain fields based on conversion and lead quality risk.

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

User: "Can you check this form friction finder before we make a change?"

Assistant should: ask for or use the relevant exports/screenshots/notes, run the workflow above, produce a ranked diagnostic table, and stop at approval-ready recommendations.

## Guardrails

- Do not make changes to live campaigns, pages, tags, containers, CRM fields or customer messages.
- Do not claim performance impact without evidence.
- Mark missing data clearly.
- Keep recommendations practical for a performance operator, founder or owner with a real advertising problem.
