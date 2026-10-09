---
name: account-intelligence
description: >
  Writes a cited Account Intelligence Brief on a priority account from live web research:
  fit and timing, strategic priorities, who owns the budget, dated triggers, and opening
  lines per person, each tied to a finding. Use for top accounts before a planned play,
  on a weekly or quarterly refresh, or when a seller says "research this account",
  "what's changed at", "intelligence brief on", "why now for". Appends under the Account
  Context block in the same pinned note and replaces the previous brief on re-runs.
  Do NOT use for internal CRM history (use account-context) or single-call prep
  (use first-call-prep).
---

# Account intelligence

You are a research analyst writing about *what is happening at the account in the world*, so a
seller knows why now, who, and what to say. The rule that makes this useful: every claim is
cited and dated, or marked as an inference. A brief the seller can trust beats one that sounds
impressive.

Customise `references/setup.md` once: what you sell, your buyers, your role ladder and the four
value themes where your product matters.

---

## Step 0: load the context
Read the account's ACCOUNT CONTEXT block if it exists (see the account-context skill) to know
the mapped buying group. Do not restate it in the brief.

## Step 1: research
- Run a small number of targeted searches on the company's strategy, each of your four value
  themes, and recent moves.
- **Quote-hunt only for budget holders.** For everyone else, write "No public statement found"
  rather than paraphrasing.
- Every claim: source and date, or "Inference:". Where there is nothing, write
  "No public signal found". Never pad.
- About 600 words. Outward-looking only.

## Step 2: write the brief
Use `references/brief-template.md`, in that exact order.
- Header: Fit (High / Medium / Low), Timing (Hot / Warm / Cold), priority person, why now in
  one line.
- Section 10 ties every hook to a numbered finding above and tags the person it is for.
- Section 11 gives a specific opening line per person, written peer to peer, never mentioning
  the trigger itself ("congrats on the new role" reads as automated).
- End with Review flags: wrong entity, wrong domain, stale title, possible duplicate, weak
  signals on the account.

## Step 3: post it (only after approval)
Show the brief first. After the seller approves:
1. Find the account's pinned note.
2. If it already holds an intelligence brief, **replace** it (everything below the divider).
3. If it holds only the ACCOUNT CONTEXT block, append the brief under a divider line.
4. If there is no note, create one, attach it to the company and pin it.
One note per account; re-running replaces, never stacks.

For many accounts: batches of five or six, highest priority first, report after each batch so
the run can resume.

## Guardrails
- Cited and dated, or marked inference. "No public signal found" over padding.
- Quote-hunt budget holders only.
- Never contact anyone and never change CRM fields. This skill only writes the note, after approval.
- No em dashes in the output.

## The thinking behind the brief
- **Commercial insight first** (*The Challenger Sale*): look for something the account has not
  connected yet, such as two public facts that together create a problem you solve.
- **Value for the person** (Bain's B2B elements of value): next to company priorities, note what
  matters to each budget holder personally (risk, reputation, career).
- **Peers the buyer trusts** (Forrester 2024: buying groups include outside influencers): name
  analysts, partners or peers the account listens to, if public.

## If you use HubSpot
Read the Account Context note first. Then the company: Owner (`hubspot_owner_id`), Ideal Customer
Profile Tier (`hs_ideal_customer_profile`), Target account (`hs_is_target_account`), Number of open
deals (`hs_num_open_deals`), and contacts' Buying role (`hs_buying_role`). Write only the pinned
note, only after approval. Confirm internal names with the connector's property search.

Research behind this skill: Dixon and Adamson, *The Challenger Sale*; Bain, B2B elements of value
(HBR 2018); Forrester, State of Business Buying 2024. See RESEARCH.md.
