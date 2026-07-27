---
name: cold-outbound-sequence-review
description: Reviews a cold email sequence for targeting fit, opening claim, ask size, cadence and personalisation depth, and says which step is killing it. Use when an outbound sequence gets opens but no replies, or before launching a new one.
---

# Cold Outbound Sequence Review

## Use this skill when

The sequence is written or running, and the replies are not coming.

Before this runs, confirm the emails are actually being delivered. A sequence with a deliverability problem produces the same symptom as a sequence with a copy problem, and rewriting copy fixes only one of them. That check is `spam-folder-check`.

Once delivery is not the issue, the cause is almost always one of four things, and they are not equally likely: who it went to, what the first line claims, how big the ask is, and how many times it lands.

## Required input

- The full sequence, every step, in order, as it actually sends.
- Who it targets: role, company size, industry, and how the list was built.
- The cadence, in days between steps.

Better with:

- reply rate, positive reply rate and unsubscribe rate per step
- open rate, treated as a soft signal because Apple Mail Privacy Protection fires the pixel on delivery
- examples of the replies, especially negative ones
- what you are actually selling and the deal size

## Analysis workflow

1. Read the opener as the recipient, who does not know you and did not ask. The first two lines decide everything after them, and most sequences spend both on the sender.
2. Check the claim in the opener. It usually falls into one of three shapes: a compliment, a statistic, or an observation about their business. Only the third earns a reply reliably, and only when it is specific.
3. Measure the ask. "Fifteen minutes to discuss how we help companies like yours" asks a stranger for a meeting on the strength of nothing. The first ask should be answerable in one line without a calendar.
4. Check whether personalisation is real or performed. A merge field with the company name is not personalisation, and recipients read it as the opposite: proof this went to a thousand people.
5. Walk the cadence. Steps that arrive too close together read as pressure, steps too far apart lose the thread, and steps that only say "bumping this up" teach the recipient that ignoring you works.
6. Look for the sequence's implicit theory of why they should care, and state it plainly. Many sequences do not have one, which is the finding.
7. Identify the single highest-leverage change, not a list of eleven improvements. Rewriting everything at once means learning nothing from the result.

## Decision rules

- Targeting outranks copy. A well-written email to the wrong list fails in a way no rewrite can rescue, so check the list first.
- One change at a time when the sequence is already running, or the result is uninterpretable.
- A negative reply is a good outcome and a better signal than silence. A sequence generating no responses of any kind has a delivery or relevance problem, not a persuasion problem.
- Unsubscribe rate above the reply rate means the list and the message disagree about who this is for.
- Do not add steps to fix a sequence that is not working. More impressions of a message nobody wants produces complaints, not meetings.

## Output format

### Verdict

Which of the four is killing it: list, opener, ask, or cadence. Pick one, with the evidence.

### Step by step

| Step | Day | What it does | Problem | Severity |
|---|---|---|---|---|

### The rewrite

The opener, rewritten, ready to send. Only the opener, because everything after it depends on what that produces.

### Cadence recommendation

Number of steps, days between, and where to stop.

### What to measure

The one number that tells you whether the change worked, and how long before it means anything.

## Practical example

A five-step sequence to heads of finance at companies with 50 to 200 staff, sending on days 1, 3, 5, 8 and 12.

The opener spends two sentences about the sender's company and a request for fifteen minutes. Steps two through five are progressively shorter versions of the same request, ending with a breakup email. Reply rate is 0.4%, unsubscribes 1.1%.

The verdict is the ask, not the copy. Nothing in the sequence asks a question that can be answered in a line, so every step demands the same expensive yes and the recipient has no cheap way to engage. The unsubscribe rate exceeding the reply rate confirms the message is arriving and being rejected rather than missed.

The opener is rewritten around a single answerable question about how they handle a specific month-end task. The cadence drops from five steps in twelve days to three in fifteen. The measure is positive reply rate, read after 200 sends, not before.

## Guardrails

- Do not send anything or modify a live sequence.
- Do not add fake personalisation tokens or invented trigger events.
- Do not promise a reply rate. Benchmarks vary by market, list quality and offer, and any number quoted here would be decoration.
- Do not advise on the legality of cold outreach. Jurisdictions differ and this is not legal advice.
- Do not recommend increasing volume as a fix for a low reply rate.
