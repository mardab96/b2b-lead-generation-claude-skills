# AGENTS.md: B2B lead generation skills

A pack of 30 Claude Skills for B2B lead generation. Each skill is a
self-contained `SKILL.md` in its own folder, following the Agent Skills
standard, so the pack runs in any Agent Skills tool, not only Claude Code.

## How these skills behave

- **Evidence first.** Every skill works from what you supply: a CRM export, a
  transcript, an email thread, a DNS record, a company website. Where evidence is
  missing the skill marks the finding as an assumption rather than filling the
  gap with a plausible number.
- **Nothing goes out.** No skill sends an email, edits a CRM record, changes a
  sequence or touches DNS. They produce text and recommendations that a human
  sends or applies.
- **No invented proof.** No fabricated customer quotes, trigger events, funding
  rounds, case study numbers or reply-rate promises. This matters more in B2B
  than elsewhere, because the buyer usually knows the truth about their own
  company and notices immediately.

## How the pack splits

Skills 1 to 20 are the inbound and paid machine: targeting, pages, forms,
scoring, source quality, handoff. They assume leads arrive and ask whether the
right ones are arriving.

Skills 21 to 30 are the outbound week and the sales side. They assume nothing
arrives and ask what you send, what you say on the call, and what you do with
the silence afterwards.

The two halves answer different questions and are rarely useful at the same
moment. A team with plenty of leads and a quality problem lives in the first
twenty. A team with an empty pipeline lives in the second ten.

## Order that matters

- `spam-folder-check` runs before `cold-outbound-sequence-review`, always. A
  delivery problem and a copy problem produce the same symptom, and rewriting
  copy fixes only one of them.
- `ghosted-after-the-demo` handles one silent deal. When the same silence
  appears across many deals at the same stage, it stops being a message problem
  and `discovery-call-gap-analysis` takes over.
- `pipeline-hygiene-audit` comes before any forecast conversation, not after one
  goes wrong.
- `objection-cheat-sheet` and `won-deal-to-case-study` both read historical
  deals, so they are cheap to run together on the same export.

## Where judgement shifts

- **Deal size.** Under a few thousand, most of the second ten are too heavy;
  the volume game is the first twenty. Above five figures, per-account work like
  `what-to-say-to-this-company` and `meeting-prep-five-minutes` pays for itself
  on a single meeting.
- **Sales cycle length.** A long cycle makes `pipeline-hygiene-audit` essential
  and makes stale-deal thresholds much more forgiving. Set `--cycle-days` rather
  than accepting a default.
- **Who does the selling.** A founder selling directly needs the prep and
  follow-up skills. A team with SDRs needs the sequence, transcript and pipeline
  skills, because the failure is consistency rather than capacity.
- **Regulated markets.** Cold outreach rules differ by jurisdiction. No skill in
  this pack gives legal advice, and several say so explicitly.

## Scripts

Two skills carry deterministic helpers, because their work is counting and dates
rather than judgement: `pipeline_hygiene.py` and `email_auth_check.py`.
`selftest.py` locks what they guarantee, including the defect where a future
close date was allowed to anchor the reference date and marked healthy deals as
overdue. Run it before and after changing anything in `scripts/`.

The other eight skills read text and produce text. A script there would add
ceremony, not rigour.

## What not to do

- Do not run a skill without its required input. Skip it and say what is missing.
- Do not present an inference about a prospect's internal situation as fact.
- Do not treat one ghosted deal, one bad call or one lost deal as a pattern.
- Do not send, publish or apply anything a skill produced without a human
  reading it first.
