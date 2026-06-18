# 20 Claude Skills for B2B Lead Generation

A pack of 20 production-ready Claude Skills for B2B lead generation: targeting, landing pages, lead quality, CRM feedback, follow-up and sales handoff.

Each skill is a self-contained `SKILL.md` with explicit triggers, required inputs, analysis workflow, decision rules, a practical example, output format, and guardrails. Drop them into Claude Code and they activate automatically when their use case matches the conversation.

## What is inside

| # | Skill | Folder | Purpose |
|---|---|---|---|
| 1 | Icp Reality Check | `icp-reality-check` | Compares your stated ICP against actual closed-won and closed-lost customers. |
| 2 | Lead Magnet Offer Fit | `lead-magnet-offer-fit` | Checks if your free asset matches the buyer stage and real pain. |
| 3 | Ad To Landing Promise Match | `ad-to-landing-promise-match` | Verifies that ads, landing page and CTA promise the same thing. |
| 4 | B2b Audience Signal Audit | `b2b-audience-signal-audit` | Reviews targeting signals for job titles, industries, intent and exclusions. |
| 5 | Landing Page Qualification Review | `landing-page-qualification-review` | Diagnoses whether the page attracts the right leads or just more leads. |
| 6 | Form Friction Finder | `form-friction-finder` | Finds fields, steps and UX patterns that kill form completion. |
| 7 | Lead Scoring Sanity Check | `lead-scoring-sanity-check` | Tests scoring rules against real CRM outcomes and sales feedback. |
| 8 | Crm Lead Source Quality Audit | `crm-lead-source-quality-audit` | Ranks lead sources by downstream stage, value and close rate. |
| 9 | Sales Follow Up Speed Audit | `sales-follow-up-speed-audit` | Measures response time impact on qualification and conversion. |
| 10 | Disqualification Reason Miner | `disqualification-reason-miner` | Extracts why sales rejects leads and maps it back to targeting or creative. |
| 11 | Lead To Opportunity Drop Off Review | `lead-to-opportunity-drop-off-review` | Finds where qualified leads stall before becoming pipeline. |
| 12 | Linkedin Ads Lead Quality Audit | `linkedin-ads-lead-quality-audit` | Diagnoses LinkedIn campaign quality using CRM feedback and cost per qualified lead. |
| 13 | Google Ads Lead Quality Audit | `google-ads-lead-quality-audit` | Separates search intent quality from keyword bloat and match-type leaks. |
| 14 | Meta Ads Lead Quality Audit | `meta-ads-lead-quality-audit` | Reviews Meta lead forms and ads for qualification strength and signal fit. |
| 15 | Email Nurture Sequence Review | `email-nurture-sequence-review` | Checks follow-up emails for relevance, timing and call-to-action clarity. |
| 16 | Sdr Handoff Brief Generator | `sdr-handoff-brief-generator` | Produces context for sales: source, intent signals, likely objections, next question. |
| 17 | Proposal Win Loss Review | `proposal-win-loss-review` | Learns from won and lost deals to fix upstream targeting and messaging. |
| 18 | Competitor Lead Angle Review | `competitor-lead-angle-review` | Reverse-engineers competitor angles you are losing to. |
| 19 | Weekly B2b Lead Gen Readout | `weekly-b2b-lead-gen-readout` | Summarizes facts, hypotheses, next actions and approvals for the week. |
| 20 | Scale Readiness Check Lead Gen | `scale-readiness-check-lead-gen` | Decides if you should add budget or fix qualification and follow-up first. |

## How to install

### Option A — Claude Code (recommended)

1. Clone or download this repository.
2. Copy the skill folders into your project's `.claude/skills/` directory, or into the user-level skills directory at `~/.claude/skills/`.
3. Start a new Claude Code session in that project. Skills will activate automatically when their description matches the conversation.

```bash
git clone https://github.com/mardab96/b2b-lead-generation-claude-skills.git
cp -r b2b-lead-generation-claude-skills/* ~/.claude/skills/
```

### Option B — Other Claude environments

The skills are plain Markdown with YAML frontmatter and work anywhere Claude can read files. Paste the relevant `SKILL.md` content into context when you want to use it.

## How to use

Once installed, describe what you want in natural language. Skills self-trigger on the patterns documented in their `## Use this skill when` section.

## Activation and trigger reliability

Claude Skills usually activate from the YAML `description` field first, then use the full `SKILL.md` instructions after activation. Each skill in this pack now names the moment it should be used in both places:

- `description` explains the business situation that should trigger the skill.
- `## Use this skill when` lists concrete request patterns and decision moments.
- `## Required input` tells the user what data makes the skill reliable.

For best results, ask for the job and include the object being diagnosed. Example: "Check if this lead magnet offer fits our ICP before I publish it" will trigger `lead-magnet-offer-fit` more reliably than "What do you think?"

## Bring your data

Every skill is data-first. They work best when you provide actual exports, reports, screenshots or notes. Each `SKILL.md` documents exactly which inputs it expects under `## Required input`.

## Guardrails

These skills are designed for diagnosis and approval-ready recommendations. By default they do not:

- publish ads
- change budgets
- pause campaigns
- edit tracking setup
- change optimization events
- modify landing pages
- modify CRM fields
- send customer messages
- make performance claims without data

Use them to structure the work, not to hand over control of the account.

## Validate the pack

Run the validator before publishing changes:

```bash
python3 scripts/validate-skills.py
```

It checks for placeholder text, missing required sections, weak activation descriptions and workflows that are too short to be useful.

## License and attribution

Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) — performance marketing infrastructure for AI-native operators.
