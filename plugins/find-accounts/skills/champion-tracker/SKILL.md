---
name: champion-tracker
description: >
  Watches the people who championed your won deals and drafts a warm note when one moves to a new
  company that fits your ideal customer profile. Use for "champion tracking", "job changes of
  customers", "former customers who moved", "warm outbound from past champions". Do NOT use for
  cold prospect lists (use ideal-customer-finder).
---

# Champion tracker

A champion who changes jobs is one of the warmest signals in B2B: they already trust you, they
know the result, and new leaders often bring tools they know. Bought intent data reaches every
competitor; your own champions do not. Kyle Poyar describes champion tracking as one of the plays
that mix bought signals with data only you have.

## Context first
Read `company-context.md` for the ideal customer profile and proof. Read closed-won deals and
their contacts.

## Questions
1. "Where do job changes come from? (a list you export, your CRM, a data tool you use)"
2. "What did these champions achieve with you, in one line each?"

## Step 1: build the champion list
From closed-won deals, list contacts with the buying role Champion or Decision maker, plus anyone
the team names. Keep name, last company, role, the result they got and the deal date.

## Step 2: detect moves (from a source you provide)
Compare current company and title from the source the user provides (a CRM update, an export
from a data tool, or a list they check by hand) with the saved list. Never scrape LinkedIn or
any site against its terms.

## Step 3: score the new company
Score fit against the ideal customer profile (fit, not just size), seniority of the new role
(can they buy?), and time in role (the first 90 days are when people choose their tools).

## Step 4: draft the note
For each strong match: congratulate briefly, mention the result they got, ask one easy question
about their priorities in the new role. Under 80 words. Also suggest who now owns the old account,
because a champion leaving is a renewal risk there (see renewal-risk-check).

## If you use HubSpot
Read contacts on closed-won deals: Buying role (`hs_buying_role`), Job title (`jobtitle`),
Company (`company` and the associated company), and the deal's Close date (`closedate`). Propose
creating the new company and contact and associating them; write only after approval. Confirm
internal names with the connector's property search.

## Output
1. Moves found: person, old and new company, new role, fit score.
2. A draft note per strong match.
3. Old accounts now at risk, with an owner.
4. Proposed CRM updates.

## Guardrails
- No scraping, no personal data beyond business role and company.
- Nothing is sent without approval. No em dashes.

Research behind this skill: Kyle Poyar, Growth Unhinged, "The new battleground in GTM"
(September 2026). See RESEARCH.md.
