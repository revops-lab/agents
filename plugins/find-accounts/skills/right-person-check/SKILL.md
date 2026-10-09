---
name: right-person-check
description: >
  Sorts a list of people by job title into your buyer personas or "not a fit", with the rule
  that decided it and their likely role in a purchase. Use before an outreach list goes live,
  when cleaning CRM contacts, or when someone says "which of these are our buyers", "classify
  these titles", "map the buying committee", "clean this list". Works on a pasted list, a CSV or
  CRM contacts. Do NOT use to research one person in depth (use first-call-prep).
---

# Right-person check

Job titles are messy. "Head of Growth" can be a marketer, a sales leader or a founder. Words
like "operations" or "strategy" appear in titles that have nothing to do with your buyer. You
apply written rules in a fixed order, so the same title always gets the same answer, and you
explain every verdict.

## Context first
Read `company-context.md` for the buying group and the "not a fit" list. If it is missing, ask
for the three to five titles they sell to and the titles they never want.

## Step 1: write the rules (once)
Turn the context into a rule list and show it before sorting. Order matters:
1. **Hard excludes first:** students, interns, assistants, recruiters, and any function the user
   excludes (e.g. "HR strategy", "wealth management").
2. **Seniority:** map words to levels (Chief, VP, Head, Director, Manager, Lead, Specialist).
   Ask the user the minimum level for each persona.
3. **Function words:** for each persona, the words that count (e.g. revenue leader: "revenue",
   "sales", "RevOps", "commercial") and the false friends that do not (e.g. "revenue
   accounting", "sales tax").
4. **Scope:** if the user only sells to global or regional roles, exclude country-only scope
   when the company is large (e.g. "Head of Sales, Belgium" at a 20,000-person company).
5. **Unclear:** anything no rule decides goes to "Review", never to a guess.

## Step 2: sort
For each person return: persona or "Not a fit" or "Review", the rule number that fired, the
likely buying role (signs, evaluates, uses, blocks, influences) and one short reason.

## Step 3: coverage per company
If the list has several people per company, show coverage: which roles are present and which
are missing. A company with only one contact is single-threaded, which is a known risk in
deals with several decision makers.

## If you use HubSpot
Read contacts with Job title (`jobtitle`), Buying role (`hs_buying_role`), Lifecycle stage
(`lifecyclestage`) and Associated company. Propose values for Buying role only where it is
empty, and show the list before writing. Never overwrite a role someone set by hand. Confirm
internal names with the connector's property search.

## Output
A table (name, title, company, verdict, persona, buying role, rule, reason), then the coverage
summary, then the "Review" list with the question you need answered.

## Guardrails
- Same input, same answer: never change a rule in the middle of a run.
- Log every rule that fired, so the user can fix rules, not results.
- No em dashes.

Research behind this skill: buying groups in complex B2B purchases (Gartner, via summaries).
See RESEARCH.md.
