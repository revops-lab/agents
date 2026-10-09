# HubSpot: where the account history lives

Display names as they appear in HubSpot, with the default internal name. Confirm internal names
with the HubSpot connector's property search before querying: portals can rename, hide or add
properties. Never report a property you did not read; write "not read" instead of "blank".

## Company record
| What you want to know | Property (internal name) |
|---|---|
| Owner today | Company owner (`hubspot_owner_id`) |
| Where the account stands | Lifecycle stage (`lifecyclestage`), Lead status (`hs_lead_status`) |
| Fit | Ideal Customer Profile Tier (`hs_ideal_customer_profile`), Target account (`hs_is_target_account`) |
| How many people we know | Number of associated contacts (`num_associated_contacts`) |
| Buying roles mapped | Number of decision makers (`hs_num_decision_makers`), Number of blockers (`hs_num_blockers`), Number of contacts with a buying role (`hs_num_contacts_with_buying_roles`) |
| Open business | Number of open deals (`hs_num_open_deals`) |
| Money so far | Total revenue (`total_revenue`), Recent deal amount (`recent_deal_amount`), Recent deal close date (`recent_deal_close_date`), First deal created date (`first_deal_created_date`) |
| Last touch by us | Last contacted (`notes_last_contacted`) |
| Last activity of any kind | Last activity date (`notes_last_updated`) |
| What is planned | Next activity date (`notes_next_activity_date`) |
| Last sign of life from them | Last engagement date (one-to-one email open or click, revisit, meeting booked, form) |
| How they first found us | Original traffic source (`hs_analytics_source`) |

## Each contact at the company
| What you want to know | Property (internal name) |
|---|---|
| Role in the decision | Job title (`jobtitle`), Buying role (`hs_buying_role`) |
| Stage | Lifecycle stage (`lifecyclestage`), Lead status (`hs_lead_status`) |
| Did they reply? (the signal that counts) | Recent sales email replied date (`hs_sales_email_last_replied`) |
| Opened or clicked (weak, often automated) | Recent sales email open date (`hs_sales_email_last_opened`), Recent sales email clicked date (`hs_sales_email_last_clicked`) |
| Meetings | Date of last meeting booked in meetings tool (`engagements_last_meeting_booked`) (note: the booked meeting furthest in the future) |
| Last touch | Last contacted (`notes_last_contacted`), Last activity date (`notes_last_updated`), Number of sales activities (`num_notes`) |
| Marketing interest | Recent conversion (`recent_conversion_event_name`), Recent conversion date (`recent_conversion_date`), Number of pageviews (`hs_analytics_num_page_views`) |
| Source | Original traffic source (`hs_analytics_source`) and drill-downs (`hs_analytics_source_data_1`, `hs_analytics_source_data_2`), Latest traffic source (`hs_latest_source`) |
| Deals they are on | Number of associated deals (`num_associated_deals`) |

## Deals at the company
| What you want to know | Property (internal name) |
|---|---|
| Stage and pipeline | Deal stage (`dealstage`), Pipeline (`pipeline`) |
| Size and timing | Amount (`amount`), Close date (`closedate`), Create date (`createdate`) |
| Why it closed | Closed won reason (`closed_won_reason`), Closed lost reason (`closed_lost_reason`) |
| What happens next | Next step (`hs_next_step`), Next activity date (`notes_next_activity_date`) |
| Health | Last activity date (`notes_last_updated`), Last contacted (`notes_last_contacted`), Forecast category (`hs_forecast_category`), Time in current stage |
| Type | Deal type (`dealtype`): new business or existing business |

## Activities (engagements) to read, newest first
Meetings and calls (with outcome), emails with replies from their side, notes, and form
submissions. Opens and clicks are listed separately and never called interest.
