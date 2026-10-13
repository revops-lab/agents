---
name: stakeholder-map
description: >
  Maps the buying group on one deal or account: who decides, who pays, who uses, who can block,
  who you have met, their stance and the gaps, with one next step per person. Reads contacts,
  buying roles and activity from the CRM. Use for "stakeholder map", "map the buying
  committee", "who else is involved", "are we single-threaded", "power interest grid",
  "org chart for this deal". Do NOT use for a whole-pipeline review (use pipeline-review).
---

# Stakeholder map

Complex purchases are decided by a group, not a person. Forrester reports buying groups that
include several outside influencers, and buying groups for purchases with generative AI are about
twice as large. A deal with one contact is one job change or one sceptic away from "no decision".

## Context first
Read `company-context.md` for the usual buying group (who signs, evaluates, uses and can block)
and the deal or account in the CRM: contacts, roles, emails, meetings and call notes.

## Questions (only what the CRM does not show)
1. "Who have you met, and who do you know is involved but have not met?"
2. "Who on their side is pushing for this, and how have you tested that?"

## Step 1: the roles
Place every known person in a role (Miller Heiman's Strategic Selling roles, extended):
- **Economic buyer:** controls the budget, can say yes when others say no.
- **Champion:** wants the change, has influence, and sells for you when you are not there.
  Test it: have they shared something they did not have to, or opened a door to the economic buyer?
- **Evaluator:** compares options (often IT, security, operations).
- **User:** lives with the result every day.
- **Blocker:** loses something if this goes ahead (budget, control, a project of their own).
- **Outside influencer:** consultant, partner or peer the buyer trusts.
Add the roles the company context says are usually involved but are missing here.

## Step 2: stance and power
For each person: influence (high, medium, low), stance (supporter, neutral, sceptic, unknown) and
last real contact. Plot them on a power and interest grid (Mendelow): high power and high interest
are managed closely; high power and low interest are kept satisfied. The Challenger Customer
research found that the best deals are driven by "mobilisers" who push for change inside the
company, not by the friendliest contact. Mark who is a mobiliser and who only talks.

## Step 3: gaps and risks
Flag: single-threaded (one contact); economic buyer not met; no one from IT, legal or
procurement yet in a deal heading to contract; champion untested; a known sceptic with power
and no plan.

## Step 4: one next step per gap
One step per missing person or risk, with owner and date. Prefer asking the champion to make the
introduction, with a reason that helps them (a business case for their manager, a security
summary for IT).

## If you use HubSpot
Read the deal's associated contacts and, per contact: Buying role (`hs_buying_role`), Job title
(`jobtitle`), Last contacted (`notes_last_contacted`), Recent sales email replied date
(`hs_sales_email_last_replied`) and meetings. Read Number of associated contacts
(`num_associated_contacts`) on the deal. Propose buying role updates and new contacts to
associate; write only after approval. Confirm internal names with the connector's property search.

## Output
1. One line: well covered, thin, or single-threaded, and why.
2. Stakeholder table: name, role, influence, stance, last contact, evidence.
3. A power and interest grid (text or simple table).
4. Gaps and risks.
5. Next steps per person, with owner and date.
6. Proposed CRM updates, old and new side by side.

## Guardrails
- Never guess a person's stance without evidence; mark it unknown.
- Do not research people's private lives. Work from the CRM, calls and public business sources.
- Never write to the CRM without approval. No em dashes.

Research behind this skill: Miller and Heiman, *Strategic Selling* (buying roles); Mendelow,
power and interest grid; Adamson, Dixon, Spenner and Toman, *The Challenger Customer*
(mobilisers); Forrester, The State of Business Buying 2024 and 2026. See RESEARCH.md.
