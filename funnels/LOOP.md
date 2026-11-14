# Conversion loop · songs, logo, web (Fiverr + Meta)
Set up 13 Nov 2026 at Aviel's request ("make my fiverr and these ads into a neural evolving conversion loop", "as efficient & effective as possible").

## Signals read each cycle (since the last cycle)
1. Meta Ads Manager (act 1098014583061745): spend, impressions, CTR, landing page views, cost per LPV for each ad in the three campaigns:
   - Songs 52666091071313
   - Logo 52667151788313
   - Web 52667151791513
2. Pixel 2153021785300175: PageView, Lead, InitiateCheckout and Purchase, split by service, utm_content (creative) and v (headline).
3. Fiverr (pro.fiverr.com/users/mrandromeda/manage_gigs): impressions, clicks and orders for each gig, plus new inbox messages from real buyers.
4. Square (Ascension Technologies): song orders. Ignore the CA$99 test from 13 Nov.

## Fitness, per creative
Rank by orders, then InitiateCheckout per CA$, then LPV per CA$. One order beats any click count.

## Mutations Claude makes WITHOUT asking
All of these stay inside each service's CA$50 test.
- **Kill:** pause an ad when it has spent at least CA$6, its CTR is under half of its sibling's in the same ad set, and it has 0 InitiateCheckout. Its sibling keeps the ad set budget, so total spend does not change.
- **Page headlines:** once each variant has at least 30 views and one leads at 1.5x or more of the others, raise its weight to 3. A variant with 0 leads at 60+ views goes to weight 0.
  - Songs: change the FUNNEL block in public/songs/index.html.
  - Logo and web: change the weights in funnels/build_service_pages.py, rebuild, then push.
- **Retire a service:** once it reaches CA$50 with 0 orders, record "retired" here. The caps already stop the spend.

## Mutations that need Aviel's yes
Proposed with numbers each cycle.
- More spend on a winner, or a new test budget.
- A new creative to replace a killed one. Build the asset (lean-creative-generation, quality first), show it, and launch after his yes.
- Price changes on Fiverr or Square.

## Cadence
- Day 1 snapshot (Sat 14 Nov).
- Cycles on Tue 17 Nov, then every 3–4 days while any test runs.
- A final verdict on 20 Nov for songs and 25 Nov for logo and web.
- Each cycle appends a line to the table below, pushes, and schedules the next cycle.

## Cycle log
| Date | Service | Spend | LPV | IC | Orders | Action |
|---|---|---|---|---|---|---|
