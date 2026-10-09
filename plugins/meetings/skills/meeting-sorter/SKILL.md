---
name: meeting-sorter
description: >
  Sorts a week of meeting transcripts or notes into sales, customer, product feedback and
  internal, links each to its account, and finds patterns across calls: top objections, feature
  requests, competitors named and questions buyers ask, with exact quotes. Use for "what did
  customers say this week", "sort my meetings", "patterns across calls", "voice of customer
  report", "top objections". Read-only. Do NOT use for one call's follow-up (use call-follow-up).
---

# Meeting sorter

The most valuable research a company owns is in its own calls, and most of it is never read
twice. You turn a pile of transcripts into a short report that sales, marketing and product can
act on, with the buyer's exact words.

## Context first
Read `company-context.md` (who the customers are, competitors, product areas). It decides how
you name themes.

## Questions (first run)
1. "Where are the transcripts?" (note-taker connector, a folder, pasted text)
2. "Which period?" (default: last 7 days)
3. "Who reads the report: sales, marketing, product, or everyone?"

## Step 1: sort each meeting
Use clear rules first, judgement only when rules do not decide:
- **External or internal:** any attendee outside the company email domain means external.
- **Customer or prospect:** match the external domain to the CRM. Customer if the company has
  Lifecycle stage Customer; prospect if there is an open deal; otherwise "unknown company".
- **Type:** sales (discovery, demo, negotiation), customer (onboarding, check-in, renewal),
  feedback (product research), internal.
Log which rule sorted each meeting.

## Step 2: extract from external meetings
- Objections and concerns, with who said them (role, company) and the exact quote.
- Requests and missing features.
- Competitors and alternatives named, and what was said about them.
- Questions buyers asked (these are content ideas and FAQ answers).
- Moments of strong reaction (positive or negative).

## Step 3: find patterns
Group by theme. A theme needs at least two separate companies to be called a pattern; one
company is an anecdote and is labelled so. Rank by number of companies, then by deal value if
known.

## If you use HubSpot
Match accounts by company domain. Read company Lifecycle stage (`lifecyclestage`), Owner
(`hubspot_owner_id`), Number of open deals (`hs_num_open_deals`), and for deals Deal stage
(`dealstage`) and Amount (`amount`), so themes can be weighted by pipeline. Confirm internal
names with the connector's property search. Do not write to the CRM.

## Output
1. The week in numbers: meetings by type.
2. Top patterns: theme, how many companies, two or three quotes with role and company.
3. Competitors: who came up and what buyers said.
4. Questions buyers asked, ready for marketing.
5. One recommended action per team (sales, marketing, product).

## Guardrails
- Quote exactly. Never paraphrase inside quotation marks.
- Internal meetings: count them, do not summarise them unless asked.
- Respect privacy: no personal details beyond role and company in shared reports.
- No em dashes.

Research behind this skill: Rob Fitzpatrick, *The Mom Test* (what people did, in their words);
Bob Moesta, switch interviews. See RESEARCH.md.
