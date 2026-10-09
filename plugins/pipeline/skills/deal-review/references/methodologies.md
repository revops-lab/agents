# Sales methodologies: how to apply them, and where they live in HubSpot

Use the methodology the team already uses. Read it from `company-context.md` ("Sales methodology").
If it is not there, ask once: "Which sales methodology does your team use: MEDDPICC, MEDDICC, SPICED,
BANT, GPCT or none?" Save the answer to `company-context.md` with the user's approval. If the answer
is "none", use SPICED for discovery and MEDDPICC for deal reviews, and say so.

Never mix two methodologies in one output. Each element is marked **Evidenced** (with the source:
call, email, document), **Assumed** or **Unknown**.

## MEDDPICC (and MEDDICC, MEDDIC)
Best for complex deals with several decision makers. MEDDIC drops Paper process and Competition;
MEDDICC adds Competition; MEDDPICC has both.

| Element | Before the call: what to find out | After the call: what to record |
|---|---|---|
| Metrics | The result they need, in numbers ("cut quote time from 3 days to 1") | The number and who said it |
| Economic buyer | Who controls the budget; have we met them? | Name, title, met or not |
| Decision criteria | How they will compare options | Criteria in their words, ranked |
| Decision process | Steps and people to a signature, with dates | Steps, owners, dates |
| Paper process | Legal, security, procurement steps and lead times | Steps started or not, documents needed |
| Identify pain | The problem driving action and its cost | The pain in their words, and impact |
| Champion | Who sells for us inside, and how we tested them | Name, power, test passed or not |
| Competition | Alternatives, including doing nothing and building it themselves | Who, and where we stand |

## SPICED (Winning by Design)
Best for discovery and hand-offs between teams. Order is not fixed.

| Element | Ask | Record |
|---|---|---|
| Situation | Their context, tools, team, what triggers change | Facts that shape why this matters now |
| Pain | "What made you take this call?" | The friction in their words |
| Impact | "What does this cost you, or what would solving it give you?" | Rational and emotional impact |
| Critical event | "What date matters, and what happens if you miss it?" | The date and the consequence. If nothing happens, it is not critical |
| Decision | "Who else is involved, and how will you decide?" | Process, people, criteria |

## BANT
Best for quick qualification of inbound leads, not for complex deals.
Budget (is there money, and who owns it?), Authority (who decides?), Need (what problem?), Timeline
(by when, and why then?).

## GPCT (HubSpot's discovery framework, often extended to GPCTBA/C&I)
Goals (what they want to achieve), Plans (how they plan to get there), Challenges (what is in the
way), Timeline. The extended version adds Budget, Authority, negative Consequences and positive
Implications.

## Writing it back to HubSpot (after human approval only)

1. **Check what exists.** Search deal properties for the methodology (for example a property group
   called "MEDDPICC"). Use existing properties if they are there; never create duplicates.
2. **Propose the fields.** If none exist, propose a property group on the **deal** object, one
   multi-line text property per element, plus one status property per element (dropdown:
   Evidenced, Assumed, Unknown). Example for MEDDPICC:

   | Label | Internal name | Type |
   |---|---|---|
   | MEDDPICC · Metrics | `meddpicc_metrics` | Multi-line text |
   | MEDDPICC · Metrics status | `meddpicc_metrics_status` | Dropdown: Evidenced, Assumed, Unknown |
   | MEDDPICC · Economic buyer | `meddpicc_economic_buyer` | Multi-line text |
   | … one pair per element … | | |
   | MEDDPICC · Last reviewed | `meddpicc_last_reviewed` | Date |

   For SPICED use the prefix `spiced_` (situation, pain, impact, critical_event, decision) and add
   `spiced_critical_event_date` (date). For BANT use `bant_`.
3. **Ask before creating.** Show the full list and ask: "Create these deal properties in HubSpot?"
   Creating properties needs a HubSpot user with permission to edit properties. If the connector
   cannot create properties, give the list as a build sheet for an admin.
4. **Ask before writing values.** Show current and proposed values side by side, with the evidence
   for each. Never overwrite a filled value without saying so. Write only what was approved.
5. **Optional:** set Buying role (`hs_buying_role`) on contacts for the economic buyer, champion and
   decision makers, also after approval.

Confirm internal names with the HubSpot connector's property search before reading or writing.
