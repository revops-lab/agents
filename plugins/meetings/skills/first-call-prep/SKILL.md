---
name: first-call-prep
description: >
  Prepares a one-screen briefing before a first sales call (discovery or qualification).
  Use when a seller is getting ready to meet a prospect and gives any starting point: a
  company name, a person's name, a LinkedIn URL, a calendar invite or a CRM contact, even
  with very little context. Trigger phrases: "prep my call with", "brief me on", "research
  this prospect", "who is this person at", "first call prep", "disco prep". The skill first
  confirms the right company and person, pulls your existing relationship from the CRM,
  checks what the person has posted recently, researches the account, and writes a
  fixed-format brief. Do NOT use for post-call write-ups, CRM data entry, or research that
  is not tied to a call.
---

# First call prep

You prepare a seller for a first call. Sellers often give you the bare minimum. Your job is
to fill the gaps yourself, confirm you have the right company and person, and produce a brief
the seller can read in five minutes.

Work in this order:
**confirm who → what we already know → what they say publicly → research → write.**

Read `references/setup.md` before the first run. It holds the only inputs you customise:
what you sell, who you sell to and the tools you connect.

---

## Step 0: confirm the company and the person

Never start deep research until you have a confirmed company and contact, and you know
whether a relationship already exists in the CRM. Match the input to one case:

- **A. Only a personal LinkedIn URL.** Treat the profile as the source of truth for name, role
  and employer. Look the person up in the CRM for history. If not found, note "net-new". No
  confirmation question needed.
- **B. Only a name.** Names are ambiguous. Search the CRM, show the best matches (company,
  title, owner, last activity) and ask the seller to confirm. If the record belongs to a
  colleague, say so, so the seller can align first. No match: ask for the company or a link.
- **C. A CRM contact without LinkedIn.** Use your data tool to find the person at that company
  (name, title, company) and enrich the profile. If several match, pick the one whose title
  best fits the roles in `setup.md` and state the assumption.
- **D. Only a company.** Ask who the meeting is with. Do not guess a person. You may pull
  existing CRM contacts and the owner for context.
- **E. Full input.** Proceed, and still check the CRM for history, deals and owner.

Rule: confirm whenever identity is inferred or ambiguous; proceed silently when it is certain.
End Step 0 knowing the confirmed company, the confirmed person and the relationship status.

## Step 1: what we already know (CRM)

Capture before any web research:
- Prior contact by anyone on your team: meetings, notes, lifecycle stage.
- **Replies from their side.** Do not report opens or clicks. Only replies count.
- Other intent: form fills, event attendance, content downloads.
- The record owner.
- Open or past deals with stage and outcome.

This goes in section 8 of the brief, not woven through it. No history means "net-new account,
no prior relationship".

## Step 2: what they say publicly (last 60 days)

1. Find the LinkedIn URL: CRM property first, then your data tool. If neither finds it, say
   "LinkedIn URL not found" and keep the section.
2. Look for **posts** the person wrote and **comments** they left in the last 60 days: topic,
   one-line summary, link, and visible engagement.
3. Likes and reshares without their own words do not count.
4. Nothing found is a finding too: a quiet profile means they read but do not publish.

## Step 3: research the account

Be specific. Industry boilerplate is the main failure mode. Prefer a dated event, a number or
a quote over a trend.

- **Snapshot:** what they do, size, ownership, HQ, main products or brands.
- **Structure:** business units, subsidiaries, regions.
- **Recent moves that matter:** dated acquisitions, leadership changes, new strategy, cost
  programmes, new sites, regulatory actions.
- **The person:** role, background, decision authority, what they likely care about. Flag it
  clearly when their role owns the problem you solve.
- **Digital maturity:** current tools, transformation programmes, recent vendor decisions.
- **Competitive position:** who they compete with and how they are positioned.
- **Pressures on their business:** a short PESTEL pass (political, economic, social,
  technological, environmental, legal) framed to *their* industry, each force tied to
  something that actually affected this company.
- **Why they would care now:** the specific need or initiative that makes a conversation
  about your category relevant today (see `setup.md`). Do not pitch; make the relevance clear.

When role accuracy matters and you only have search fragments, trust the LinkedIn profile or
enriched data over guesses.

## Step 3b: the thinking behind the questions
Prepare questions that make the call useful for the buyer, not a checklist:
- **Ask about the past, not opinions** (*The Mom Test*): "Tell me about the last time this went
  wrong" beats "Would you find this useful?".
- **Cover the four forces** (Bob Moesta): what pushes them now, what better future they picture,
  what worries them about changing, what habit keeps them where they are.
- **Find the critical event** (SPICED): a date that matters to them, and what happens if they
  miss it.
- **Bring one insight** (*The Challenger Sale*): something useful they may not have considered,
  backed by evidence.
- **Map the group:** who else will be involved, because complex purchases involve several people
  and stall when one is missing (Gartner; Forrester State of Business Buying 2024).

## The methodology
If the team uses a sales methodology (read "Sales methodology" in `company-context.md`, or ask once),
add a section to the brief with that methodology's elements from `references/methodologies.md`:
what is already known from the CRM and research (marked Evidenced, with source), what is assumed,
and the question to ask on this call for each gap. For a first call, focus on Situation, Pain,
Impact, Critical event (SPICED) or Pain, Metrics, Champion (MEDDPICC); the rest comes later.

## If you use HubSpot
Read the contact: Owner (`hubspot_owner_id`), Lifecycle stage (`lifecyclestage`), Lead status
(`hs_lead_status`), Buying role (`hs_buying_role`), Last contacted (`notes_last_contacted`),
Recent sales email replied date (`hs_sales_email_last_replied`), Date of last meeting booked
(`engagements_last_meeting_booked`), Recent conversion (`recent_conversion_event_name`,
`recent_conversion_date`), Original traffic source (`hs_analytics_source`,
`hs_analytics_source_data_1`), Number of associated deals (`num_associated_deals`). Then the
company: Number of open deals (`hs_num_open_deals`), Total revenue (`total_revenue`), Number of
associated contacts (`num_associated_contacts`). Report replies and meetings, never opens.
Confirm internal names with the connector's property search.

## Step 4: write the brief

Always use `references/brief-template.md`, in that order. Bullets only. Every non-obvious claim
carries a numbered citation [1] with full sources at the bottom. Mark anything unsourced as
"Inference:". Keep it to one screen where possible.

## Guardrails

- Blank beats guessed. If you could not verify something, say so in the brief.
- Never contact the prospect, and never write to the CRM. This skill only reads.
- Keep tool use lean: do not re-enrich data you already have.
- No em dashes in the output.

## Quality bar

A good brief lets the seller open the call already knowing who this person is, what is
happening at their company right now, why the conversation is timely, what has already
happened between you, and what the person has been saying publicly. If a section could apply
to any company in the sector, it is not done.

Research behind this skill: Rob Fitzpatrick, *The Mom Test*; Bob Moesta, forces of progress;
Winning by Design, SPICED; Dixon and Adamson, *The Challenger Sale*; Gartner and Forrester on
buying groups. See RESEARCH.md.
