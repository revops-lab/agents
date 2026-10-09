---
name: account-context
description: >
  Builds a one-page Account Context note from what is already in the CRM: the buying group
  by role, every meeting and reply, past deals and why they were won or lost, and the
  strongest signal on the account. Use before any call with an existing account, when an
  account changes owner, or when a seller says "what's our history with", "account
  context for", "catch me up on", "who do we know at". Reads the CRM only, never the web.
  Posts one pinned note per account and replaces it on every run instead of stacking.
  Do NOT use for web research on the account (use account-intelligence).
---

# Account context

You write what *we already know* about an account, in one place, in about a minute. When a
senior seller leaves or an account changes owner, this note is how the next person starts
with the full picture instead of from zero.

Use **only** CRM data. Do not search the web. Never invent a value: if a field is empty, leave
the line out.

Customise `references/setup.md` once: your buying-role ladder, the teams you sell to and where
signals live in your CRM.

---

## Step 0: confirm the account
Match by website domain first, then name. If several records match, list them and ask. Flag
possible duplicates in Review flags rather than merging anything.

## Step 1: gather from the CRM
- Every contact associated with the company: name, title, team, last activity.
- Meetings held, replies from their side (not opens or clicks), content downloads, event
  attendance, each with dates.
- Open and closed deals: stage, amount, dates, and for lost deals the reason in plain words.
- Signals already captured on the account (score, type, date).
- Current owner and any previous owners.

## If you use HubSpot
Read `references/hubspot.md`. It maps each part of the note to the exact HubSpot properties:
sales email reply, open and click dates, last contacted, last activity, next activity, number of
open deals, total revenue, buying-role counts, recent conversions and traffic sources. Use reply
dates and meetings to judge the relationship; treat opens and clicks as weak, because Apple Mail
Privacy Protection and security scanners trigger them automatically.

Add one line to the Coverage section from the buying-role counts (decision makers, blockers):
complex purchases involve several people, and single-threaded accounts are the most fragile.

## Step 2: write the note
Use `references/context-template.md`, in that order, under the heading ACCOUNT CONTEXT.
- Group contacts by buying role using the ladder in `setup.md`. If a role cannot be derived
  from the title, put the person under "Role unclear" rather than guessing.
- Coverage line: unique contacts, teams covered, roles present, roles missing.
- Mark the last real two-way conversation (a reply or a meeting), not the last email sent.
- Factual and compact. No recommendations beyond one suggested next step.

## Step 3: post it (only after approval)
Show the note first. After the seller approves:
1. Find the account's pinned note.
2. If it already holds an ACCOUNT CONTEXT block, **replace** that block. Keep anything below the
   divider (for example an intelligence brief).
3. If there is no note, create one, attach it to the company and pin it.
Exactly one pinned note per account. Re-running replaces, never stacks.

For many accounts: run in batches of five or six, highest priority first, and report after
each batch so the run can resume if interrupted.

## Guardrails
- CRM only. No web research, no guessing.
- Show before posting. The seller approves the first run of every batch.
- Never delete CRM records or merge companies. Flag instead.
- No em dashes in the output.

Research behind this skill: buying groups and stalled purchases (Gartner; Forrester State of
Business Buying 2024); unreliable email opens (Apple Mail Privacy Protection). See RESEARCH.md.
