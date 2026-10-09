---
name: account-brief
description: >
  Writes a one-page brief on a company before the first outreach: what they do, what changed
  recently, who is likely in the buying group, which buying signals are live, and a first line
  worth sending. Use when someone says "brief me on this company", "research this account",
  "is this company a fit", "what's going on at", or gives a company name or website before
  prospecting. Do NOT use for existing customers' history (use account-context) or for a
  meeting already booked (use first-call-prep).
---

# Account brief

You give a seller a reason to reach out that is about the buyer, not about the seller. A good
brief answers three questions in one page: is this a fit, why would they care now, and who
should hear from us first.

## Context first
Read `company-context.md`. You need the ideal customer, the buying group and the buying
situations. Without it, ask: "In one line, what do you sell and to whom?"

## Step 0: confirm the company
Match by website domain. If the name is ambiguous (several companies, subsidiaries), list the
options and ask. Check the CRM for an existing record and owner; if a colleague owns it, say so
first.

## Step 1: fit
Compare the company with the ideal customer in the context file: industry, size, region, model.
Give a verdict (Strong, Possible, Weak) with the reason. If it is Weak, say so and stop unless
the user wants to continue.

## Step 2: what changed (the last 6 months)
Search for dated events that match the buying situations in the context file: leadership
changes, funding, acquisitions, new products, expansion, layoffs, regulation, hiring for the
problem you solve (job ads name tools and pains), website or rebrand changes. Every item gets a
date and a source. Older than 6 months only if it still shapes today.

## Step 3: the buying group
Name the likely roles from the context file's buying group and find real people only from
public sources (company site, press, public profiles). Mark each "found" or "role to find".
Never guess an email address.

## Step 4: the angle
Use the forces of progress: what is pushing them (problem now), what pull could we offer,
what anxiety would stop them, what habit keeps them where they are. Write one hypothesis per
force, marked as a hypothesis. Add one line on value for the person, not just the company
(less risk, career, time back), because that is what makes a supplier stand out (Bain's B2B
elements of value).

## Step 5: the first line
One opening line that names their situation in their words, tied to a dated finding. No
flattery, no "I noticed you…" filler, no product pitch in the first line.

## If you use HubSpot
Before researching, read the company record: Owner (`hubspot_owner_id`), Lifecycle stage
(`lifecyclestage`), Number of associated contacts (`num_associated_contacts`), Number of open
deals (`hs_num_open_deals`), Last contacted (`notes_last_contacted`), Last activity date
(`notes_last_updated`), Target account (`hs_is_target_account`). If there is recent activity,
say so at the top. Confirm internal names with the connector's property search.

## Output
Use `references/brief-template.md`. One page. Numbered sources at the bottom. Anything not
verified is marked "Not verified".

## Guardrails
- Read-only. Never send anything, never write to the CRM.
- Specific beats general: if a line could describe any company in the industry, delete it.
- No em dashes.

Research behind this skill: forces of progress (Bob Moesta); buying groups (Gartner); B2B
elements of value (Bain, HBR 2018);
answer-first writing (Aggarwal et al., 2023). See RESEARCH.md.
