# Allegro Ads Profit Analysis Workflow

Status: \`canonical\`
Scope: global analytical workflow; STAW EXPERT cost specifics remain in product repository.
Research verified: 2026-11-05. Runtime activation: NOT VERIFIED.

## Purpose / trigger
Run for an Allegro Ads monthly/weekly audit, prior to bid/budget changes, or when evaluating paid campaign efficiency. Decisions are recommendations only until human approval.

## Roles
- HUMAN: authorizes data access, provides exports/costs, approves any campaign change.
- AI: source review, hypotheses, exception triage and recommendations.
- CODE: validates import schemas, reconciles figures, computes ratios and unit economics.
- AUTOMATION: schedules report preparation only after separate explicit approval; no Ads writes.

## Procedure
| Step | Owner | Input | Action | Output | Check |
| --- | --- | --- | --- | --- | --- |
| 1 | HUMAN/AI | account and date range | obtain official XLSX by placement/offer as available, order GET and verified cost ledger | versioned input manifest | dates, account, report currency, gross/net, source hash |
| 2 | CODE | exports | normalize dimensions, deduplicate, do NOT sum overlapping panel views | one fact grain per report | source totals reconcile |
| 3 | CODE | orders and SKU costs | map line-item attribution; avoid double counting; allocate costs per item/parcel | per-SKU contribution | missing costs flagged UNKNOWN |
| 4 | CODE | normalized data | compute CTR, CPC, CPA, CVR, ROAS, ACoS, TACoS, break-even CPC/ACoS | repeatable KPI table | independent arithmetic check |
| 5 | AI | KPI + calendar | identify likely causes, attribution maturity, seasonality, marketplace/placement effects | ranked diagnostic findings | label hypothesis vs observed |
| 6 | HUMAN | recommendations | approve one controlled test at a time | proposed change list | spend ceiling, rollback, owner |
| 7 | AI/CODE | later export and history of changes | compare pre/post and reconcile | evaluation report | never claim causality solely from attribution |

## Guardrails
- NO Ads REST API use without explicit permission and verified technical scope; \`allegro:api:campaigns\` is not generic Ads access.
- NO campaign/budget/CPC changes in this workflow. App/browser automation must be separately designed and approved.
- NO production credentials/PII in Git or AI reports.
- A campaign can have a high ROAS and negative post-Ads contribution. Cost unknown != zero.
- Keep revenue basis and tax treatment explicit. The Allegro UI gross/net toggle does not change sales value.
- Click-based attribution usually has a seven-day lookback; reporting windows are provisional while open.
- Attribution ≠ incrementality. Ads spend must only be subtracted once.
- Report snapshots need provenance and validation before comparison; do not sum multiple aggregates for one spend.

## Exceptions
Source unavailable → report observable subset and BLOCKED access.
Missing SKU cost → HOLD profit decision.
Late refunds → versioned restatement, never silent overwrite.
Duplicate campaign and offer totals → keep separate report grains.
Historical metric definition changed → start a new versioned comparison.

## Test record / acceptance
Before claiming PASS use a zero-click fixture, a no-cost fixture, a duplicated-export fixture, a paid-order/refund example and a real-data reconciliation. An unexecuted test stays NOT RUN. Record refs, commands, results and reconciliation delta. Skill: \`skills/7dejv-allegro-ads-profit-analyst/SKILL.md\`.
