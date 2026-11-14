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

## Fiverr gig evolution (13 Nov)
Prepared by a parallel agent. Assets are on the Mac in Pictures/Fiverr Samples/evolve and in /mnt/user-data/outputs/fiverr-evolve.
- **12 new gallery images** (1280x769, rendered at 2x):
  - Songs: hero, how it works, packages
  - Logo: hero, kit, how it works
  - Web: hero, included, how it works
  - Plan, ghostwriting and ads: one "how it works" image each
- **3 new gig videos** (1920x1080), built only from real work and the existing song ad clips. No AI generation.
  - Songs: 32 s, with Aviel's song "The Quiet I Was Searching For" underneath
  - Logo: 26.5 s, silent
  - Web: 30 s, silent, a walkthrough of the live EBV site and Aventi
- **Copy:** COPY.md has a paste-ready title, description and FAQ for songs, logo and web, plus opening lines for the other three gigs.
- **Status:** the upload to Fiverr was blocked by Fiverr's "Press & Hold" human check on the first video upload. Aviel needs to clear it and do the uploads himself, following the plan at the bottom of COPY.md. Nothing on Fiverr was changed by this pass.
- **Watch after upload:** gig impressions to clicks to orders, per gig, in the next cycle.

## Christmas campaign (added 13 Nov)
- 52667179778913 joins the loop. Same kill rule (xmas-a vs xmas-b siblings), same CA$50 retire rule.
- Hard stop: after Dec 20 orders can't deliver for Christmas, so pause any spend left after 18 Dec.
- 13 Nov: organic Christmas Reel posted to the Ascension Technologies FB Page (utm_medium=organic, utm_content=reel1). Instagram left off (the linked IG is Aventi's).
- 13 Nov: songs gig occasion swapped Wedding → Christmas (pending save after a Press & Hold check). Swap back after 25 Dec.
- Fiverr buyer replies: drafts-only scheduled task trig_01Az1zhs6LfyFc6ADSMN8HU8 (9:47, 14:47, 19:47 PT). Nothing is sent without Aviel's "send N".
