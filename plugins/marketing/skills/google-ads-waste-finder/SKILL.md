---
name: google-ads-waste-finder
description: >
  Finds where Google Ads budget is wasted (search terms that never convert, broad match drift,
  bad locations and hours, campaigns that bring leads but no pipeline) and proposes the fixes,
  with the money each one saves. Use for "which ads are burning money", "Google Ads audit",
  "wasted spend", "negative keywords", "why is our cost per lead so high". Needs the Google Ads
  API connected to Claude Code (see revopslab.org/playbooks/claude-code-google-ads) or a report
  export. Proposes only; changes nothing without approval.
---

# Google Ads waste finder

Wasted spend hides in the search terms report, not in the keyword list. People search in ways
you did not plan for, and broad and phrase match let the ads follow them. You find the waste,
put a number on it, and propose fixes that do not cut what works.

## Context first
Read `company-context.md` (who is not a fit, what a good customer looks like). Not-a-fit words
become negative keywords: students, jobs, free, templates, competitor careers, wrong industries.

## Questions
1. "Which account and period?" (default: last 90 days, enough data to judge)
2. "What counts as a conversion that matters: a lead, a qualified lead, or a deal?" If only form
   fills are tracked, say that cost per lead can look good while pipeline is zero.
3. "Any brand or competitor campaigns I should treat differently?"

## Data
With the Google Ads API: search term view, keyword view, campaign and ad group performance,
geographic and hour-of-day reports, conversion actions. With no API, ask for these as exports.
If the CRM is connected, match leads by click ID or email to see which became pipeline.

## Method
1. **Search terms with spend and no conversions,** above a threshold (for example twice the
   average cost per conversion). Group them into themes (jobs, free, DIY, wrong product,
   competitor brand, students). Each theme gets a negative keyword proposal and its match type.
2. **Match type drift:** broad or phrase keywords whose matched terms are mostly irrelevant.
3. **Leads without pipeline:** campaigns with a good cost per lead but no qualified leads or
   deals in the CRM. These are the most expensive waste, because they look healthy.
4. **Location, device, hours:** segments with spend and no conversions over enough clicks.
5. **Settings:** search partners and display expansion on search campaigns, location set to
   "presence or interest" when you only sell locally, auto-applied recommendations.
6. **Quantify:** for each fix, the spend in the period it would have saved and the conversions
   at risk (should be near zero).

## Output
A table of fixes ranked by money saved: fix, evidence, spend saved, risk, how to apply. Then the
negative keyword list ready to paste, with match types. Then one paragraph on what not to cut.

## Guardrails
- Propose only. Apply changes only after the user approves each one, through the API with a
  change log.
- Small numbers: a term with 3 clicks is not waste yet. Show clicks next to every verdict.
- Keep keys in a private file, never in chat.
- No em dashes.

Research behind this skill: Google Ads search terms and match type behaviour (Google Ads Help);
the RevOps Lab playbook "Connect Claude Code to Google Ads". See RESEARCH.md.
