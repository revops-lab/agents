# The research behind the agents

Every agent in this library thinks with one or more of the ideas below. They are chosen because they change what you ask and what you do, not because they sound clever. Each line says where it comes from and how sure we are about the numbers. Researched October 2026.

Read it with sources, evidence types and links to each skill at https://revopslab.org/agents/research/

## How buyers really decide

| Idea | What it says | Source | How an agent uses it |
|---|---|---|---|
| Buying groups | Complex B2B purchases involve several people, often quoted as 6 to 10. Buyers spend most of their journey researching on their own and a small share with suppliers. | Gartner B2B buying research, via secondary summaries (figures vary by study and year) | Map roles, not just a contact. Ask who else is involved before writing anything. |
| No decision is the main competitor | In a study of about 2.5 million sales calls, 40 to 60 percent of deals ended in no decision. Most were indecision (fear of getting it wrong), not loyalty to the status quo. | Matthew Dixon and Ted McKenna, *The JOLT Effect* (2022), via summaries | Look for fear of failure, not missing ROI. Reduce risk: scope, proof, a clear first step. |
| Forces of progress | People switch when push (problem today) plus pull (better future) outweigh anxiety (fear of the new) plus habit (the way we do it now). | Bob Moesta, Jobs to Be Done, Switch interviews | Ask about all four forces. Most sellers only talk about pull. |
| Situation, pain, impact, critical event, decision | A shared language for discovery and hand-offs. The critical event is the buyer's deadline, not the seller's quarter. | Winning by Design, SPICED | Call notes and deal reviews use these five headings. Test a critical event: "what happens if you miss the date?" |
| MEDDICC | Metrics, economic buyer, decision criteria, decision process, paper process, pain, champion, competition. | Origin at PTC in the 1990s; many published variants | Deal reviews check which letters are evidenced, not assumed. |
| Ask about the past, not opinions | People are poor predictors of their own future behaviour and polite about your idea. Ask what they did last time. | Rob Fitzpatrick, *The Mom Test* | Discovery questions start with "Tell me about the last time…" |
| Prospective hindsight | Imagining a plan has already failed and explaining why surfaces more risks than asking "what could go wrong?" | Gary Klein, the premortem (HBR), citing Mitchell, Russo and Pennington (1989) | Deal reviews run a premortem: "It is March and we lost. Why?" |
| Sensemaking | Buyers drown in information. Sellers who help them make sense of it (fewer, clearer options) get more high-quality, low-regret deals. | Gartner buyer enablement research (around 2019), via trade press | Agents cut options down and explain trade-offs instead of adding more material. |

## How markets work

| Idea | What it says | Source | How an agent uses it |
|---|---|---|---|
| Most buyers are out of market | At any moment only a small share of B2B buyers (often quoted as about 5 percent) are in market. The rest will buy later. | John Dawes, Ehrenberg-Bass Institute, with the LinkedIn B2B Institute (2021) | Separate "reach out now" from "stay remembered". Signals decide which is which. |
| Category entry points | Buyers remember brands through the situations that trigger a need. Brands linked to more of those situations get thought of more often. | Jenni Romaniuk, Ehrenberg-Bass | Content and posts name the buying situation in the buyer's own words. |
| Positioning | Start from the real alternatives a customer would use, then the attributes only you have, the value they create, the customers who care most and the category that makes it obvious. | April Dunford, *Obviously Awesome* | Company context is built in this order. |
| Speed to lead | In an audit of 2,241 US companies, firms that tried to contact a web lead within an hour were nearly seven times more likely to qualify it than those that waited longer. | Oldroyd, McElheran and Elkington, HBR (2011) | Lead hand-off checks measure first response time. |
| Coverage follows win rate | The "3x pipeline" rule assumes about a one-in-three win rate. The honest target is roughly 1 divided by your own win rate, counting only deals that can close in the period. | Common forecasting practice; vendor write-ups | Pipeline reviews compute coverage from the team's own win rate. |
| Answer-first content | Content that states the answer, cites sources and includes statistics and quotes is more likely to be used by generative search engines. | Aggarwal et al., "GEO: Generative Engine Optimization" (2023) | Content briefs and AI visibility checks use this standard. |
| Short cold emails | Gong's data shows replies drop once cold emails pass about 100 words; 50 to 100 words performs best, and executives reply less often than others. | Gong, 2026 | Cold emails stay under 100 words, one question, no attachments. |
| Sender rules | Since February 2024, Gmail and Yahoo require bulk senders to authenticate (SPF, DKIM, DMARC), offer one-click unsubscribe and keep spam complaints below 0.3 percent. | Google and Yahoo sender requirements, via deliverability guides | Email checks verify authentication and complaint rate before volume. |
| Opens are unreliable | Apple Mail Privacy Protection and corporate security scanners trigger opens automatically. | Deliverability research and vendor guides | No agent treats an email open as interest. Replies and clicks from several people count. |

## Added October 2026 (new skills)

| Idea | What it says | Source | How an agent uses it |
|---|---|---|---|
| Buying roles | Economic buyer, user, technical buyer and coach (champion) play different parts in one decision. | Robert Miller and Stephen Heiman, *Strategic Selling* (1985) | The stakeholder map places every person in a role and flags missing ones. |
| Power and interest grid | Stakeholders differ in power and interest; each quadrant needs different handling. | Aubrey Mendelow, stakeholder mapping (1991) | The stakeholder map plots influence against stance. |
| Mobilisers | Deals move when a "mobiliser" inside the company pushes for change, not when the friendliest contact likes you. | Adamson, Dixon, Spenner and Toman, *The Challenger Customer* (2015) | The stakeholder map marks who mobilises and who only talks. |
| Champion moves | Champions who change jobs are a warm signal that competitors buying the same intent data cannot see. | Kyle Poyar, Growth Unhinged, "The new battleground in GTM" (September 2026) | The champion tracker watches past champions and drafts a note. |
| Lost deals return | Companies that said "not now" often come back, visible as pricing or comparison page visits after months of silence. | Snitcher, "Your lost deals are coming back" (October 2026, vendor view) | Closed-lost revival looks for a new signal before reopening. |
| SPF limits | SPF may trigger at most 10 DNS lookups and at most 2 void lookups, or it fails. | RFC 7208 | The sending domain audit counts lookups through nested includes. |
| DMARC | A policy (none, quarantine, reject) and reports, checked against SPF and DKIM alignment. | RFC 7489 | The audit plans a rollout from p=none to p=reject. |

## What the consultancies and research houses found

| Idea | What it says | Source | How an agent uses it |
|---|---|---|---|
| The rule of thirds | B2B buyers split their interactions about evenly between in-person, remote human and self-serve digital channels, and growth leaders use about ten channels. 41 percent prefer in-person with a new supplier. | McKinsey B2B Pulse 2024 (nearly 4,000 decision makers, 13 countries), "Five fundamental truths: How B2B winners keep growing" | Outreach plans mix channels. The first meeting with a new account is worth doing in person when the deal is large. |
| B2B elements of value | 40 kinds of value in five levels: table stakes, functional, ease of doing business, individual (for example reduced anxiety, career) and inspirational. Higher levels are what make suppliers stand out. | Almquist, Cleghorn and Sherer, Bain & Company, Harvard Business Review (2018) | Value hypotheses cover the person (career, less risk), not only cost and features. |
| Purchases stall | 86 percent of B2B purchases stall during buying, and 81 percent of buyers are dissatisfied with the provider they chose. Buying groups are large and include outside influencers. | Forrester, The State of Business Buying 2024 (press release) | Deal reviews look for the stall point and who outside the company the buyer trusts. |
| AI makes groups bigger | When a purchase includes generative AI features, the buying group is about twice as large, and buyers check AI research with peers and experts. | Forrester, The State of Business Buying 2026 | Expect IT, legal and security in any AI purchase. Give buyers something peers can verify. |
| Buyers prefer less rep time | 67 percent of B2B buyers say they prefer a rep-free experience. | Gartner survey of 646 buyers, 2025 | Make self-serve proof (pricing logic, case studies, security answers) easy to find before a call. |
| Personalisation pays, when right | 71 percent of customers expect personalised interactions and 76 percent are frustrated when they do not get them. Leaders get about 40 percent more revenue from personalisation. | McKinsey, "The value of getting personalization right, or wrong, is multiplying" (2021, mostly consumer data) | Personalise on the buyer's situation, not on surface facts like a first name or a recent post. |
| Retention compounds | A small rise in retention can raise profits sharply, often quoted as 5 percent more retention giving 25 to 95 percent more profit. | Frederick Reichheld, Bain & Company (via summaries) | Customer agents treat early warning on renewals as revenue work, not service work. |
| Commercial excellence | Revenue growth has been the largest driver of shareholder return for top performers, and most gains come from using existing resources better. AI in sales works when about 90 percent of the effort goes into people and process change. | BCG, Unlocking Growth Through Commercial Excellence (2025); BCG Executive Perspectives on the future of sales with AI (2024) | Agents fix the process and the hand-offs first, then automate. |
| Teach, tailor, take control | Top sellers bring a commercial insight that reframes the buyer's problem, tailor it to each stakeholder and lead the process. | Dixon and Adamson, *The Challenger Sale* (CEB, 2011) | Prep and outreach agents look for an insight the buyer has not considered, backed by evidence. |

## How good operations think

| Idea | What it says | How an agent uses it |
|---|---|---|
| A score must predict something | Lead and health scores are only useful if they predict a result you can check later (meetings, renewal). Weights come from your own history. | Scoring agents test the score against past wins and losses. |
| Measure what you will act on | Every report ends with one decision someone can make this week. | Reports name an owner and a next step. |
| Read first, write later | New automations start read-only, then propose, then write after approval. | Every agent here proposes before it saves. |

Numbers marked "via summaries" come from secondary sources that quote the original research. Check the original before quoting them in public.
