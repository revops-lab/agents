---
name: sending-domain-audit
description: >
  Audits every domain you send email from: SPF, DKIM, DMARC and MX, which tools send as you,
  the SPF lookup count, blacklists, and a warm-up plan for new domains. Returns a fix list with
  the exact DNS records. Use for "check my sending domains", "set up cold email domains",
  "SPF DKIM DMARC", "why do my emails go to spam", "is my domain ready to send". Do NOT use to
  review email copy (use email-check).
---

# Sending domain audit

Copy only matters if the email lands. Since February 2024 Google and Yahoo require SPF or DKIM
from every sender, and SPF, DKIM, DMARC, alignment, one-click unsubscribe and a spam rate below
0.3 percent from bulk senders. Most cold email problems start here, before anyone reads a word.

## Context first
Read `company-context.md` for the main domain and the tools you use. Never ask for passwords or
DNS logins: you read public records and propose changes; a person makes them.

## Questions (only what DNS cannot show)
1. "Which domains do you send from, including cold email domains?"
2. "Which tools send email as you? (mailbox provider, sequencer, newsletter, CRM, help desk, invoices)"
3. "How many emails a day do you plan per domain?"

## Step 1: read the records (public DNS only)
For each domain look up MX, the TXT record starting `v=spf1`, `_dmarc.<domain>` and DKIM keys at
`<selector>._domainkey.<domain>`. Common selectors: `google` (Google Workspace), `selector1` and
`selector2` (Microsoft 365), `s1` and `s2` (SendGrid), `k2` and `k3` (Mailchimp), `hs1-` and
`hs2-` plus the account number (HubSpot). If a tool's selector is unknown, ask for an email
header and read `s=` in the DKIM-Signature line. If you cannot run DNS lookups, point the user to
https://revopslab.org/tools/email-authentication-checker/ and work from its result.

## Step 2: check against the rules
- SPF: exactly one record; ends with `~all` or `-all`, never `+all`; 10 DNS lookups at most,
  counting nested includes (RFC 7208); at most 2 includes that resolve to nothing.
- DKIM: a key for every tool that sends as the domain, 2048-bit where the provider allows; no
  `t=y` left from testing; the tool signs with your domain (d=), not its own, so DMARC aligns.
- DMARC: one record at `_dmarc`; `p=none` with a `rua` address to start; plan the move to
  `quarantine`, then `reject` after 2 to 4 weeks of clean reports.
- MX: present on every sending domain, so replies arrive.
- Cold email: never from the main domain; 2 to 3 mailboxes per domain; replies route to a
  monitored inbox.

## Step 3: blacklists
Check the domain and any dedicated sending IPs with
https://revopslab.org/tools/blacklist-check/ . Spamhaus refuses lookups through public DNS, so
check it on check.spamhaus.org. Google Workspace and Microsoft 365 IPs are shared and managed by
the provider; focus on domain reputation (Google Postmaster Tools).

## Step 4: warm-up plan for new domains
Week 1: 5 to 10 emails a day per mailbox, no cold email. Week 2: 10 to 20. Week 3: 20 to 30,
up to 10 cold. Week 4: 30 to 40, 10 to 20 cold. Then keep warm-up running and stay below about
30 cold emails per mailbox per day.

## Output
1. One line per domain: ready, fix first, or do not send.
2. Table per domain: MX, SPF (lookups used), DKIM per tool, DMARC policy, blacklists.
3. Fix list in order, each with the exact record (type, host, value) to add or replace.
4. Tools that send as you but are missing from SPF or DKIM.
5. Warm-up schedule with start and first-send dates.

## Guardrails
- Read-only. Never ask for DNS logins; a person publishes every change.
- Never suggest two SPF records or `+all`.
- No em dashes.

Research behind this skill: Google email sender guidelines (support.google.com/a/answer/81126);
Yahoo sender requirements; RFC 7208 (SPF lookup and void limits); RFC 7489 (DMARC). See RESEARCH.md.
