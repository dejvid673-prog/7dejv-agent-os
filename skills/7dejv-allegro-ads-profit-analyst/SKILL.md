---
name: 7dejv-allegro-ads-profit-analyst
description: Analyse Allegro Ads exports and attributable order lines against verified per-SKU variable costs for STAW EXPERT. Use for CPC, CTR, CVR, ACoS, ROAS, margin after Ads, budget and placement diagnostics, campaign reviews, or safe optimisation proposals. Never change campaigns or spend.
---

# 7DEJV Allegro Ads Profit Analyst

Status: CANDIDATE FOR REVIEW (canonical registry entry proposed in this PR; NOT verified as installed in Codex).

## Purpose and trigger
Use for a historical Allegro Ads audit, offer/group/campaign performance diagnosis, profitable CPC threshold calculation, or controlled campaign experiment recommendation. This is a **read-only / PROPOSE** skill, not an Ads API client or automation.

## Authoritative references
- Product-specific rules: `dejvid673-prog/allegro/AGENTS.md`, `BUSINESS_RULES.md`, and `docs/08-operations/ads-and-promotion.md`.
- Technical and data contract: `dejvid673-prog/allegro/docs/08-operations/allegro-ads-profit-analytics-2026-11-05.md`.
- Allegro official sources: https://help.allegro.com/pl/sell/a/jakie-statystyki-moge-sprawdzac-w-panelu-reklamowym-allegro-ads-1nPyDZo9qUe , https://developer.allegro.pl/news/zamowienia-dodalismy-informacje-o-atrybucji-allegro-ads-Pg8glADgbT5 , https://allegro.pl/regulaminy/regulamin-allegro-ads-a1EnOgMxWfa .
- Verify changed regulations, scope, fee tables and metrics anew before a real decision (last research: 2026-11-05).

## Inputs
Required for a money-backed evaluation:
1. Account identifier, marketplace, currency, time zone, date range, export timestamp, report granularity, advertised metric basis (gross/net), and source file SHA or reference.
2. Ads spend, impressions, clicks, attributed revenue and attributed orders/units **as individually available**, with campaign/group/offer/placement IDs where the export actually supplies them.
3. SKU mapping, gross paid selling price, discounts/refunds, purchase/production cost, inbound transport, commission and fixed Allegro fees, actual shipping/Smart/surcharges, packaging/labor, returns reserve and applicable taxes; each cost has status `KNOWN`, `ZERO_CONFIRMED`, `NOT_APPLICABLE`, or `UNKNOWN`, plus evidence.
4. Explicit attribution definition and cohort period. Do not invent order IDs or infer item-to-click relationships.

Optional: search terms/planner data, seasonality, history of bids, budget report, placement, organic comparison, attribution flag from checkout-form line items, competitor observations.

## Dependencies and permission model
Allowed: official seller UI reports/XLSX, authorized order REST GET operations, verified local cost records, offline deterministic calculations, GitHub docs, human-provided sources. No credential collection in prompt. Read-only access sufficient. No direct Ads REST write, session scraping, browser interaction, account connection, spend, campaign creation, or silent changes.

API caveat: `allegro:api:campaigns` in the public auth tutorial is **not** a general Ads campaign-management permission. Allegro Ads REST access is restricted by its regulations; check actual account eligibility. The `lineItems[].allegroAds.attributed` boolean is attribution evidence, not campaign ID, cost-per-order, or independent proof of incrementality.

## Procedure
1. **Source check:** read existing 7DEJV business rules and current official rules. Record source URL/date, account, import and KPI bases. Verify that revenue and cost denominators match; default no invented VAT deduction.
2. **Data quality:** verify totals against source XLSX, unique keys and grain; detect duplicate report totals, overlap across views, missing/late dates, refunds, attribution lag, partial periods, time zones, cross-product attribution and missing order→SKU mapping. Aggregating offer/group/campaign/placement views into one sum can double-count: choose a single non-overlapping fact grain.
3. **Cost check:** mark incomplete variable costs as UNKNOWN; do not fill missing values with zero. For a seller not registered as an active VAT taxpayer, do not automatically deduct input VAT; document tax basis and reconciliation separately.
4. **Compute deterministic ratios** with named numerators/denominators and safe divide:
   - CTR = clicks/impressions; average CPC = ads_spend/clicks.
   - ROAS = attributed_revenue/ads_spend; ACoS = ads_spend/attributed_revenue.
   - CVR = attributed_orders/clicks **only where units and attribution align**; CPA = ads_spend/attributed_orders.
   - attributed contribution before Ads = attributed revenue - all applicable variable non-Ads costs allocated at *sold-item or order grain*. After Ads = contribution - *single* allocated ads spend.
   - break-even ACoS = contribution_before_ads / revenue; break-even mean CPC = contribution_per_attributed_order × assumed/observed paid-click-to-order CVR.
   - TACoS = ads_spend/all-channel-or-account-revenue for the **same account/period/currency**; mark differing scopes.
5. **Attribution boundaries:** distinguish sales credited by Ads from proven incremental sales. Do not add attributed order revenue to gross order revenue again. For incomplete 7-day windows show PROVISIONAL and avoid definitive pause decisions.
6. **Diagnose:** separate traffic/CTR, CPC, CVR, offer conversion, placement, stock, seasonality, price and margin issues. Assess sample size and uncertainty before recommending changes.
7. **Propose not execute:** classify candidate actions `KEEP`, `TEST`, `LOWER_BID`, `PAUSE_CANDIDATE`, `SCALE_CANDIDATE`, `HOLD_DATA` with metric evidence, expected loss ceiling, manual approval, rollback and review date. Neither recommend positive ROI solely on ROAS nor claim causal uplift from credited sales.
8. **Quality gate:** recalculate independently from raw sums, reconcile account totals and refund treatment, check negative/zero/unknown values, ensure all report claims carry sources and limitations.

## Output contract
Produce: scope/date/data freshness; source inventory; KPI definition and bases; per-account/campaign/group/offer table when observed; revenue and cost bridge with status flags; ranked actions with evidence and approval gates; caveats; reproducible formulas; `PASS/HOLD/BLOCKED` status. Missing critical cost → HOLD_DATA, not fabricated profit. When no actual Ads data, output readiness checklist and mock-only example, not fictitious performance.

## Errors and stop conditions
- Missing permission, unauthorized access, scope conflict → BLOCKED integration; offline analysis can continue.
- Inconsistent currency/basis, overlapping source views, incomplete costs, poor order mapping → HOLD for profitability conclusions; still report observable clicks/spend.
- Only 1–2 days after bid change, open attribution window or low volume → PROVISIONAL recommendations; no forced automated cutoff.
- No automatic read of PII; minimum necessary order-line fields only, IDs hashed/redacted in reports.

## Examples / expected behaviour
- Given attributed revenue PLN 1,000, ads spend PLN 100, and verified pre-Ads contribution PLN 180: ROAS 10x, ACoS 10%, after-Ads contribution PLN 80. This is *attributed contribution*, not guaranteed incremental profit.
- Given 5 clicks, spend PLN 5, zero attributed orders, attribution still open: report CPC PLN 1 and no mature CVR; do not immediately recommend pause.
- Given product acquisition cost UNKNOWN: compute spend/CPC/ROAS, mark net profit and break-even as HOLD.
- Given ads_spend=0, clicks=0: ratio ROAS/CPC is null, not 0 or infinity.

## Tests and acceptance criteria
For each version run positive/boundary/negative fixtures: zero denominators, missing cost, duplicate aggregate views, returns, single-line cross-SKU attribution, partial 7-day window, no VAT recovery, contradictory revenue bases, multiple accounts/marketplaces and order delays. Confirm deterministic totals with manual checks and reconciliation to export/settlement. Review external dependencies/licenses before adoption. Runtime installation and connection status must be independently verified; this file alone proves neither.
