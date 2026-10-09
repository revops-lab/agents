---
name: renewal-risk-check
description: >
  Flags customers at risk before the renewal conversation: falling usage, a champion who left,
  unresolved support issues, late payments, no executive contact, and competitor interest, with
  the reason and a save plan per account. Also finds expansion candidates. Use for "renewal risk",
  "churn risk", "which customers might leave", "customer health", "renewals next quarter",
  "expansion opportunities". Read-only.
---

# Renewal risk check

Customers rarely leave on the renewal date. They decide months earlier, when the champion moves
on, usage drops or a problem is not solved. A small rise in retention has an outsized effect on
profit (Frederick Reichheld's work at Bain is often quoted at 5 percent more retention giving 25
to 95 percent more profit), so early warning is revenue work.

## Context first
Read `company-context.md`: what success looks like for a customer and how value shows up.

## Questions
1. "Which customers: renewals in the next 90, 120 or 180 days, or all?"
2. "Which data do we have?" (CRM, product usage, support tickets, billing, survey scores)
3. "What has predicted churn here before?" (If nobody knows, the check will propose a test.)

## Signals to check, per account
- **Usage:** active users against seats; trend over 90 days; key feature adoption.
- **People:** champion or main contact left (email bounce, job change), no contact with a senior
  sponsor in the last six months, a new leader in the buyer role.
- **Support:** open high-severity tickets, ticket volume rising, slow resolutions. The pattern
  matters more than single tickets.
- **Money:** late or failed payments, downgrade requests, discount asked at last renewal.
- **Voice:** low recent survey scores, negative comments in calls, competitor named in calls.
- **Outcomes:** did they reach the result they bought for? Unknown is a risk.

## Score and explain
Give each account Green, Yellow or Red with the two or three reasons. Avoid false precision: a
decimal score looks more reliable than the data behind it. If the user has past renewals, test
which signals actually predicted churn and say so.

## Save plan (Red and Yellow)
For each: the person to talk to, the question to open with, what to fix first, and the date by
which it must be done (well before the notice period). Also: who in the account still believes in
the product, and who is new and needs to hear the story.

## Expansion (Green)
Accounts with growing usage, new teams or a new leader who succeeded with you before: name the
expansion idea and who to talk to.

## If you use HubSpot
Companies: Lifecycle stage (`lifecyclestage`) = customer, Owner (`hubspot_owner_id`), Total
revenue (`total_revenue`), Recent deal close date (`recent_deal_close_date`), Last contacted
(`notes_last_contacted`), Last activity date (`notes_last_updated`), Number of associated contacts
(`num_associated_contacts`), renewal date (often a custom property; ask its name). Contacts:
Buying role (`hs_buying_role`), Recent sales email replied date (`hs_sales_email_last_replied`),
email bounce status. Tickets: status, priority, create date. Confirm internal names with the
connector's property search.

## Output
A table of accounts with status, reasons, renewal date, value and owner; save plans for Red and
Yellow; expansion ideas for Green; and which data was missing.

## Guardrails
- Read-only. Never contact customers.
- Say which signals were not available rather than scoring them as fine.
- No em dashes.

Research behind this skill: Reichheld and Bain on the economics of retention (via summaries);
customer health practice (usage, support patterns, relationships, outcomes). See RESEARCH.md.
