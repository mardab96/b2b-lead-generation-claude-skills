# Example output: Lead Scoring Sanity Check

Sample data is fictional. Use this as a shape reference for the expected output, not as a benchmark.

## Input summary

Scoring model:

- +25 points for demo form submission
- +20 points for company size 100-500
- +15 points for target job title
- +10 points for visiting pricing page
- +10 points for opening 3 nurture emails
- +5 points for every asset download

90-day CRM data:

- 420 leads
- 38 SQLs
- 9 opportunities
- 2 closed-won deals
- Score buckets: 80+, 50-79, below 50

## Score bucket readout

| Score bucket | Leads | SQLs | Opportunities | Closed-won | Main issue |
|---|---:|---:|---:|---:|---|
| 80+ | 61 | 9 | 1 | 0 | Content activity is inflating scores. |
| 50-79 | 144 | 24 | 6 | 2 | Best balance of fit and intent. |
| Below 50 | 215 | 5 | 2 | 0 | Contains a few late-stage buyers that the score misses. |

## Findings

| Finding | Evidence | Scoring impact | Recommended action | Confidence |
|---|---|---|---|---|
| Asset downloads receive too much weight. | 7 of 9 leads in the 80+ bucket had 3+ downloads, but no sales notes showing active buying intent. | Research behavior looks like buying intent. | Cap asset-download points at +10 total per lead. | High |
| Company fit is underweighted. | 2 closed-won deals scored 58 and 64 because they had low content activity, despite strong role and company fit. | Good-fit buyers can sit below sales priority. | Increase company size and target role weight. | High |
| Demo submissions are treated the same across sources. | LinkedIn Lead Gen demo submissions had lower SQL rate than website demo submissions. | The same action does not mean the same intent. | Split demo form scoring by source and form type. | Medium |
| Pricing page visits work better as a timing signal. | Pricing visits within 7 days of form fill had 42% SQL rate. Older pricing visits had 11% SQL rate. | Stale intent is treated as current intent. | Add recency decay for pricing and product-page visits. | Medium |

## Revised scoring draft

| Signal | Current points | Suggested points | Reason |
|---|---:|---:|---|
| Target role | 15 | 25 | Stronger correlation with SQL and opportunity creation. |
| Company size 100-500 | 20 | 25 | Best-fit firmographic signal in current data. |
| Website demo form | 25 | 30 | Strong intent when submitted on owned site. |
| LinkedIn Lead Gen form | 25 | 15 | Needs sales confirmation before high score. |
| Asset downloads | 5 each | Max 10 total | Prevents research behavior from dominating score. |
| Pricing page visit within 7 days | 10 | 15 | Works as a recent timing signal. |

## Decision

Recalibrate the score before changing sales SLAs. The current model sends too many high-activity leads to sales and misses some good-fit buyers with lower content activity.

Use the revised score for 30 days, then compare SQL rate, opportunity rate and sales rejection reasons by bucket.

## Approval needed

- Confirm whether scoring changes can be pushed to CRM this week.
- Confirm who owns the 30-day readout: marketing ops or sales ops.

## Missing data

- Rejection reason by score bucket
- Time from lead creation to first sales touch
- Score history for leads that became opportunities after 30+ days
