---
name: spam-folder-check
description: Checks whether cold emails are actually reaching inboxes by reading SPF, DKIM and DMARC records, sending volume, bounce and complaint rates. Use when reply rates fall without the copy changing, when a new domain starts sending, or when someone asks whether their emails are going to spam.
---

# Spam Folder Check

## Use this skill when

Someone suspects their emails are not arriving, and nobody has checked.

The tell is almost always the same: reply rates drop, the copy did not change, the list did not change, and the team's first instinct is to rewrite the subject line. Subject lines do not matter to a message that never renders in an inbox.

Run this before anyone rewrites anything.

Do not use it to diagnose weak copy on a campaign that is demonstrably being delivered and opened. That is `cold-outbound-sequence-review`.

## Required input

At minimum, the sending domain. That alone gets you the authentication picture.

Better, add whatever of this exists:

- the DNS TXT records for SPF, DKIM and DMARC, pasted, or permission to read them
- sending volume per day per mailbox, and how long the domain has been sending
- bounce rate, split into hard and soft if the tool reports it
- spam complaint rate
- whether the sending domain is the main company domain or a lookalike bought for outbound
- the sending tool and whether mailbox warmup is switched on
- open rate history, with the caveat below

If someone hands over only a screenshot of a sequence dashboard, say what is missing and check what can be checked.

## Analysis workflow

1. Read the authentication trio and say plainly which of the three is missing, misconfigured or merely present but permissive. SPF that ends in `~all` with eleven includes, DKIM that does not verify, and DMARC set to `p=none` are three different problems with three different fixes.
2. Check the domain age and reputation posture. A domain that started sending in volume three weeks after registration behaves differently from one sending for four years, and the fix is patience, not configuration.
3. Compare volume per mailbox against a conservative ceiling. Most cold outbound problems are volume problems wearing a copy problem's clothes.
4. Read the bounce rate as a list-quality signal first and a reputation signal second. A hard bounce rate above a few percent is a list that was never verified, and it damages the domain for months after the campaign ends.
5. Read the complaint rate as the strongest available proxy for whether recipients consider this spam. It matters more than any other number here.
6. Separate what is broken from what is merely unproven. Open rates cannot confirm delivery reliably now that mail providers pre-fetch images, so do not build a delivery conclusion on them.
7. Name the one fix that comes first, and say what it will not fix.

## Decision rules

- Authentication failures outrank everything. There is no point tuning volume on a domain that cannot prove who it is.
- A brand new domain sending at volume is a warmup problem, and no configuration change substitutes for time.
- If the main company domain is being used for cold outbound, say so plainly: the downside is the entire company's email, not just the campaign.
- If nothing is technically wrong, say that too, and hand the problem back to targeting and copy rather than inventing a deliverability cause.
- Never state a deliverability rate as measured unless a seed test or provider data supports it. Everything else is inference.

## Output format

### Verdict

One line: are the emails likely arriving, likely filtered, or unknowable from what was supplied.

### Authentication

| Record | Present | Correct | Risk | Fix |
|---|---|---|---|---|
| SPF | | | | |
| DKIM | | | | |
| DMARC | | | | |

### Sending posture

Domain age, volume per mailbox, warmup status, bounce rate, complaint rate, each with a plain read.

### Fix order

Numbered, first fix first, with what each one will and will not solve.

End with:

- `Decision:` fix now / warm up and wait / stop sending / this is not a deliverability problem
- `Missing data:` only what would change the answer
- Where a seed test would settle the question, say so

## Practical example

Someone says replies fell from a steady trickle to nothing over two weeks, and nothing about the campaign changed.

The check finds DMARC absent, SPF technically valid, DKIM signing correctly, the domain four months old, and volume raised from 30 to 120 emails per mailbox per day eleven days ago.

The answer is not the missing DMARC record, even though it should be added. The answer is that the volume quadrupled on a young domain, and the fix is to drop back below the previous level, hold it, and stop treating send volume as a growth lever on a domain this young. The DMARC fix goes second, because it protects the domain rather than rescuing this campaign.

## Guardrails

- Do not change DNS records. Produce the record to add and hand it to whoever owns the domain.
- Do not promise an inbox placement rate. Nobody outside the receiving provider can measure it directly.
- Do not treat open rate as proof of delivery.
- Do not recommend buying more domains as the default fix. It hides the cause and multiplies it.
- Do not advise on cold outbound legality here. Deliverability and lawfulness are separate questions and this skill answers only the first.
