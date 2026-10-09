---
name: deal-review
description: >
  Reviews one deal honestly: what is evidenced and what is only assumed (MEDDICC), where it could
  stall, a premortem of how it might be lost, and the three actions that most raise the chance to
  win. Also rescues stalled deals. Use for "review this deal", "is this deal real", "deal health",
  "why is this deal stuck", "what am I missing on", "prepare for my deal review". Do NOT use for a
  whole team's pipeline (use pipeline-review).
---

# Deal review

Deals are rarely lost at the end. They are lost earlier, quietly, when a key person was never
met, the reason to act was never dated, or the buyer got scared of choosing wrong. Forrester
found 86 percent of B2B purchases stall at some point. Your job is to see that early and say it
plainly, with evidence.

## Context first
Read `company-context.md` (buying group, typical cycle, proof). Read the deal, its contacts,
emails, meetings and call notes.

## Questions (only what the CRM does not show)
1. "What do you believe is the next step, and has the buyer agreed to it with a date?"
2. "Who have you met, and who have you not met but know is involved?"
3. "What does the buyer lose if they do nothing?"

## Step 1: evidence check (your methodology, MEDDPICC by default)
Use the team's methodology from `company-context.md` (ask once if missing) and the elements in
`references/methodologies.md`. If the deal already has methodology properties in HubSpot (for
example a MEDDPICC property group), read them first and check them against the evidence. For
MEDDPICC, mark each element Evidenced (with the source: a call, an email, a document), Assumed, or
Unknown:
- Metrics: the result the buyer expects, in numbers.
- Economic buyer: the person who controls the budget. Met or not?
- Decision criteria: how they will compare options.
- Decision process: the steps and people to a signature, with dates.
- Paper process: legal, security, procurement. Started or not?
- Identify pain: the problem driving action, in their words.
- Champion: someone inside who sells for you and has power. Tested how?
- Competition: including "do nothing" and building it themselves.
"Assumed" is the most dangerous answer, because it feels like knowledge.

## Step 2: where could it stall?
Check the usual stall points: no critical event (no date that matters to them); single-threaded
(one contact); late new stakeholders (IT, legal, procurement, and for AI purchases a bigger
group, per Forrester 2026); proposal sent and silence; champion lacks access to the budget.
Look for indecision (JOLT research): many questions, requests for more options, "we need to
think" after a good demo. That is fear of getting it wrong, not a need for more information.

## Step 3: premortem
"It is three months from now and we lost this deal. What happened?" Write the three most likely
stories, each tied to evidence in the deal. Imagining a failure that already happened surfaces
more risks than asking what could go wrong (Gary Klein's premortem).

## Step 4: three actions
The three actions that most raise the chance to win this month, each with owner, date and the
risk it removes. Prefer actions that reduce the buyer's risk (a smaller first step, success
criteria, a reference call with a peer) over pushing harder.

## If you use HubSpot
Read the deal: Deal stage (`dealstage`), Amount (`amount`), Close date (`closedate`), Create date
(`createdate`), Forecast category (`hs_forecast_category`), Deal probability
(`hs_deal_stage_probability`), Next step (`hs_next_step`), Last activity date
(`notes_last_updated`), Last contacted (`notes_last_contacted`), Next activity date
(`notes_next_activity_date`), Number of associated contacts (`num_associated_contacts`), Time in
current stage, and each contact's Buying role (`hs_buying_role`) and Recent sales email replied
date (`hs_sales_email_last_replied`). Flag: close date in the past, no next activity, more time in
the current stage than usual for won deals, one associated contact. Propose updates (close date,
next step, forecast category) with evidence; write only after approval. Confirm internal names
with the connector's property search.

## Output
1. Verdict in one line: on track, at risk, or not real, and why.
2. MEDDICC table with evidence.
3. Stall risks.
4. Premortem: three stories.
5. Three actions with owners and dates.
6. Proposed CRM updates, old and new side by side, including the methodology properties and
   their status (Evidenced, Assumed, Unknown). If the properties do not exist yet, propose them
   as described in `references/methodologies.md` and create them only after approval.

## Guardrails
- Be honest, not harsh. Every judgement points to evidence.
- Never move a deal stage or close date without approval.
- No em dashes.

Research behind this skill: MEDDICC; Forrester, State of Business Buying 2024 and 2026; Dixon and
McKenna, *The JOLT Effect*; Gary Klein, premortem (HBR). See RESEARCH.md.
