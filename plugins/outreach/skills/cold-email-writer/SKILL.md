---
name: cold-email-writer
description: >
  Writes a short cold email sequence (three to four steps) for one account or one segment,
  built on a real reason to reach out and the buyer's situation, not on your product. Use for
  "write a cold email", "build an outbound sequence", "draft outreach to", "prospecting emails
  for this list", "follow-up emails". Pairs with account-brief and buying-signal-monitor for the
  reason to reach out. Do NOT use to review an existing draft (use email-check).
---

# Cold email writer

A cold email earns a reply when it is about the reader's situation, short enough to read on a
phone, and asks for something small. Gong's data shows replies drop once emails pass about 100
words, and executives reply less often than others, so every word has to work.

## Context first
Read `company-context.md` (buying group, pain in their words, proof, voice). If there is an
account brief or a signal for this account, use it: the reason to write is the most important
line in the email.

## Questions (only what is missing)
1. "Who is this for: one named account, or a segment (e.g. 'new heads of sales at 50 to 200
   person software companies')?"
2. "What is the reason to write now?" (a signal, an event, a peer result). If there is none,
   say so: without a reason, the sequence should be shorter and lead with an insight.
3. "What is the smallest next step you want?" (a reply, a 15-minute call, permission to send
   something). Default: a reply.

## How the email is built
- **Subject:** two to four words, lowercase is fine, no clickbait, no "quick question".
- **Line 1, their situation:** what changed or what people in their role struggle with, in their
  words. Not "I noticed", not flattery, not their recent post unless it is the actual reason.
- **Line 2 to 3, an insight:** something they may not have considered, backed by evidence
  (a number, a peer example). This is the Challenger idea: teach something useful first.
- **Line 4, proof:** one relevant result from the context file, with a name if allowed.
- **The ask:** one low-effort question. One question per email.
- **Length:** 50 to 100 words. No attachments, no calendar link in the first email.

Write for the person, not only the company: what changes for them (less risk, time back, looking
good to their boss).

## The sequence
1. Day 1: the email above.
2. Day 3 or 4: a different angle on the same problem (another insight or a short example).
   Never "just following up" or "bumping this".
3. Day 8 to 10: a useful asset or a peer story, no ask beyond "worth a look?".
4. Day 14 to 21 (optional): a polite close: "Shall I stop here?" Respect the answer.
Mix channels where the user sells that way (McKinsey finds buyers split time evenly across
in-person, remote and digital channels): suggest where a LinkedIn connection or a call fits.

## Check before showing
Run every email through these checks and fix before showing: under 100 words; one question;
no claim without proof; no spam-trigger phrases ("free", "guarantee", "act now"); the reader's
name and company spelled correctly; nothing that only makes sense to the sender.

## If you use HubSpot
Before writing to a named contact, read: Lifecycle stage (`lifecyclestage`), Lead status
(`hs_lead_status`), Owner (`hubspot_owner_id`), Last contacted (`notes_last_contacted`),
Recent sales email replied date (`hs_sales_email_last_replied`), and whether they are in an
active sequence. If someone contacted them in the last 14 days, or they are a customer, stop
and tell the user. Confirm internal names with the connector's property search.

## Output
Each email with subject, body and word count, the reason it works in one line, and the
personalisation fields marked {like_this}. Then the timing and channel plan.

## Guardrails
- Drafts only. Never send, never enrol anyone in a sequence without approval.
- Never invent a mutual connection, a result or a "saw you at" moment.
- Respect opt-outs and local rules (for example GDPR in the EU: legitimate interest and an easy
  way to opt out).
- No em dashes.

Research behind this skill: Gong (2026) on email length and executive replies; Dixon and
Adamson, *The Challenger Sale* (teach first); McKinsey B2B Pulse 2024 (rule of thirds).
See RESEARCH.md.
