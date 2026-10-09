---
name: ai-visibility-check
description: >
  Checks whether AI assistants (ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews)
  recommend your company for the questions your buyers ask, who they name instead, which sources
  they cite, and what to publish to change it. Use for "are we visible in ChatGPT", "AI search
  visibility", "GEO audit", "AEO check", "do AI tools recommend us", "LLM visibility". Read-only.
  Do NOT use for classic SEO rankings only.
---

# AI visibility check

More buyers start research by asking an AI assistant. If the assistant names three competitors
and not you, you are not on the shortlist. You measure that the same way every month, so changes
are real, and you find the sources the assistants trust.

## Context first
Read `company-context.md`: category, alternatives (competitors), buying situations and the
buyer's words. If missing, ask for the category, three competitors and the main buyer.

## Step 1: the question set (20 to 30 questions)
Write questions the way buyers ask, across three kinds:
- **Category:** "What are the best tools for {job} for a {size} company?"
- **Problem:** "How do I {solve pain} without {hiring / a big budget}?" (no brand named)
- **Comparison:** "{Competitor} alternatives", "{You} vs {competitor}".
Use the buying situations from the context file: assistants are asked in situations, not in
categories. If keyword data is available, use the search phrases with demand. Show the list
and let the user edit it.

## Step 2: run and score
Ask each question in each assistant the user can access, with web search on where available,
at least twice (answers vary between runs). For each answer record:
- Mentioned? (yes or no), position (first, in a list, in passing), sentiment (positive,
  neutral, negative), accuracy (is what it says about you correct?).
- Competitors named, in order.
- Sources cited (URLs).

## Step 3: findings
- Share of answers that mention you, overall and per question type.
- Most-named alternatives and how often.
- The sources assistants cite most, and whether you appear in them (review sites, "best
  tools" lists, forums, analyst pages, your own pages).
- Factual errors about you (wrong pricing, old features, wrong category).

## Step 4: what to do
Ranked actions, each tied to a finding:
- Pages to publish or fix, written answer first: the answer in the first two sentences, then
  steps, sources, statistics and quotes. Research on generative engines (Aggarwal et al., 2023)
  found that citing sources, adding statistics and adding quotations increased visibility.
- Third-party sources to be present on (the lists and sites the assistants cite).
- Technical checks: the site allows AI crawlers (robots.txt and any bot protection), has
  structured data (Organization, FAQ, HowTo where true), a sitemap and an llms.txt summary.
- Corrections to request where assistants repeat wrong facts.

## Output
A score table per assistant and question type, top competitors, the source map, errors found,
and the ranked action list. Save the question set so next month's run is comparable.

## Guardrails
- Read-only. Never post reviews or content anywhere.
- Report what the assistants said; do not claim to know how they rank.
- No em dashes.

Research behind this skill: Aggarwal et al., "GEO: Generative Engine Optimization" (2023);
Ehrenberg-Bass Institute on buying situations. See RESEARCH.md.
