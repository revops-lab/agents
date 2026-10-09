---
name: email-check
description: >
  Reviews a cold email or a sequence before it goes out: scores it, shows the lines a busy reader
  will skip, checks the sending domain is set up so the email lands in the inbox, and returns a
  tighter version. Use for "check my email", "review this sequence", "why is nobody replying",
  "is this too long", "will this land in spam". Do NOT use to write from scratch (use
  cold-email-writer).
---

# Email check

Two things decide whether a cold email works: whether it lands in the inbox, and whether the
first two lines earn the third. You check both, explain every finding, and fix what you can.

## Context first
Read `company-context.md` for the buyer, their pain and the voice. If missing, ask who the email
is for.

## Part 1: will it be read? (the copy)
Score out of 100 using these checks, each with points and a one-line reason:
1. **About them first (20):** the first line is about the reader's situation, not the sender.
2. **Reason to write now (15):** a real trigger or insight, not "I wanted to reach out".
3. **Length (15):** 50 to 100 words is the target; over 125 loses most points.
4. **One clear ask (15):** one question, low effort. Two questions halve the score here.
5. **Proof (10):** one specific, believable result. Claims without proof lose points.
6. **Plain language (10):** no jargon walls, no hype words, readable on a phone.
7. **Subject (10):** two to four words, honest, no "quick question" or "re:" tricks.
8. **No auto-pilot phrases (5):** "hope you are well", "just following up", "touching base",
   "I know you are busy", fake familiarity.
Quote each weak line and give the fix.

## Part 2: will it land? (the sending setup)
If the user shares the sending domain, check public DNS (or ask them to paste the records):
- SPF record exists and includes the sending service.
- DKIM is set up for the sending service.
- DMARC record exists (at least `p=none`) and the From domain aligns with SPF or DKIM.
- Outreach is sent from a separate domain or subdomain, not the main company domain.
- For marketing or bulk email: one-click unsubscribe, and spam complaints below 0.3 percent
  (aim for under 0.1 percent). Google and Yahoo have required this of bulk senders since
  February 2024.
- Volume: a new mailbox warms up gradually; sudden volume harms delivery.
Say what passed, what failed and the exact fix. If you cannot check DNS, list what to verify.

## Part 3: a better version
Rewrite the email keeping the user's voice and facts. Show the word count before and after.
Never add claims that were not in the original or in the context file.

## Output
Score and breakdown, the weak lines with fixes, the sending checklist, the rewrite. For a
sequence, do this per email and add: does each step bring a new angle, or just repeat?

## Guardrails
- Never send anything.
- Do not judge success by open rates: Apple Mail Privacy Protection and security scanners make
  opens unreliable. Judge by replies and positive replies.
- No em dashes.

Research behind this skill: Gong (2026) on email length; Google and Yahoo bulk sender
requirements (2024). See RESEARCH.md.
