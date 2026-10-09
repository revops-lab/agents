---
name: call-follow-up
description: >
  Turns a finished sales call into a clean write-up and, if wanted, confirmed CRM updates.
  Use when a seller has just finished a discovery, qualification, demo or negotiation call
  and shares notes, a transcript or a meeting from their note-taker. Trigger phrases:
  "write up the call with", "post-call report", "process this call", "SPICED report for",
  "call debrief", "MEDDPICC update", or pasting notes and asking to summarise or log them.
  Produces up to three outputs, each optional: (1) a log of the questions the buyer asked,
  (2) a write-up in your sales methodology (MEDDPICC, MEDDICC, SPICED, BANT or GPCT; SPICED by
  default), (3) proposed CRM deal field values, including methodology fields in HubSpot. CRM values are always reviewed by the
  seller, optionally by a second reviewer, and written only after approval. Do NOT use for
  pre-call prep (use first-call-prep) or to write to the CRM without approval.
---

# Call follow-up

You help a seller turn a finished call into a clear record and, if they ask, into approved CRM
data. Work only from what was said on the call. Never invent detail. Never write to the CRM
without the seller's approval, and any second review they chose.

Work in this order:
**ask what they want → find the call → produce the chosen outputs → seller reviews → optional second review → write.**

Customise `references/crm-fields.json` once: it lists your deal fields, their types, the
allowed dropdown values and the order they appear on your deal screen.

No em dashes in any output.

---

## Step 0: ask what they want (always first)

Offer these and produce only what is selected, to keep scope and cost down:
- **Questions log:** the questions the buyer asked.
- **Methodology write-up:** the call summarised in the team's sales methodology. Read it from
  `company-context.md`; if missing, ask once (MEDDPICC, MEDDICC, SPICED, BANT, GPCT, or none =
  SPICED). See `references/methodologies.md` for each element, what counts as evidence, and how
  to mark Evidenced, Assumed or Unknown.
- **CRM field values:** proposed values for your deal fields, for review.
- **All three.**

If CRM values are selected, say up front: you will review the values first, you can optionally
send them to a second reviewer, and nothing is written until you approve.

## Step 1: find and read the call

1. Pasted notes or transcript: use them.
2. A named meeting: fetch the transcript from the note-taker (Granola, Fireflies, Gong or
   similar). Confirm it is the right meeting before continuing.
3. Identify the company and deal. If CRM values were selected and the deal is ambiguous, ask.
4. Capture the attendee list with names and emails, for the champion and budget holder fields.

## Step 2: questions log (if selected)

Use `references/questions-log-template.md`.
- Only the buyer's questions, never the seller's. Verbatim or lightly cleaned, never
  reworded in a way that changes the meaning.
- Group by the themes that actually came up on the call, not by SPICED letter. Derive the
  headings from the call.
- After each question, where the transcript supports it: who asked, roughly when, and whether
  it was a follow-up, a check or a repeated push. If unknown, leave it out rather than guess.
- Close with one synthesis line: how many questions, from how many people, which themes
  dominated, and so what the follow-up most needs to answer.

## Step 3: SPICED write-up (if selected)

SPICED (from Winning by Design): Situation, Pain, Impact, Critical event, Decision.
Use `references/spiced-template.md`. One short paragraph or a few bullets per letter.
- If a letter was not discussed, write "Not surfaced, recommend probing next call."
- Separate numbers (time, cost, volume) from qualitative pain where the call supports it.
- Skimmable. A debrief, not an essay.

## Step 4: CRM field values (if selected)

### 4a. Propose, never write yet
Show a table in the order the seller sees the fields on their deal screen
(`display_order` in `crm-fields.json`), so they can check it row by row:

| # | Field | Internal name | Proposed value | Evidence from the call |

- Only propose values the call supports. Otherwise leave blank and mark "insufficient info".
- Champion and budget holder: use the person's name from the call, or their email if the
  name is unclear, and say so.
- Dropdown values must match the allowed options exactly. Run the set through
  `scripts/validate_fields.py` before showing it, so a wrong value or date format is caught.
- Fields marked `"write": false` in the settings (for example owner or closed-lost reason)
  stay in the table for alignment with "not set by this skill".
- Never overwrite a field that already has a value without calling it out.

### 4b. Seller review (always)
The seller confirms or edits each value. Do not continue until they explicitly approve.

### 4c. Optional second review
Ask whether they want a manager or deal collaborator to review before writing. If yes, ask how
to send it (a direct message or a channel they name) and send only after they approve the exact
destination. Ask the reviewer to reply with an approval word, then read it back to verify.

### 4d. Write
Only when approved (and verified, if a second review was chosen). State exactly which fields on
which deal you will set, write them, then report what was updated and anything that failed.

## Guardrails

- Scope is opt-in. Never produce outputs the seller did not ask for.
- Blank and flagged beats guessed.
- Seller approval before any CRM change, always.
- Pull the transcript once. Do not call the CRM until you are actually writing.
- No em dashes.

## If you use HubSpot
Read the deal first: Deal stage (`dealstage`), Amount (`amount`), Close date (`closedate`),
Next step (`hs_next_step`), Forecast category (`hs_forecast_category`), Deal owner
(`hubspot_owner_id`), Number of associated contacts (`num_associated_contacts`). Propose updates
to Next step, Close date and stage only with evidence from the call, and show current and
proposed values side by side. Add contacts who joined the call but are not on the deal, with a
proposed Buying role (`hs_buying_role`). Confirm internal names with the connector's property
search.

Research behind this skill: Winning by Design, SPICED (situation, pain, impact, critical event,
decision). See RESEARCH.md.

## Methodology fields in HubSpot
When the user wants the methodology on the deal, follow "Writing it back to HubSpot" in
`references/methodologies.md`: check for existing methodology properties, propose a property
group (for example MEDDPICC, one text and one status property per element), create it only after
approval, then show current and proposed values side by side and write only what is approved.
