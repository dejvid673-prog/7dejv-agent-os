---
name: codex-workflow-router
description: Main 7dejv work-mode router for Codex. Use when a task needs choosing the right skills, procedures, agent references, command procedures, or 7dejv workflow for PrestaShop, PHP modules, SQL/VAT reports, Allegro, BaseLinker, ecommerce operations, SEO/content, architecture decisions, pre-commit review, deployment checks, long tasks, or handoff. Routes to 1-3 skills, optionally one agent procedure or persona, and requires planning before larger code/database/API/configuration changes plus verification after changes.
---

# Codex workflow router

This is the 7dejv operating router for Codex. Use it before larger work to select a small, explicit stack of skills, optional agent procedures, optional command procedures, and a 7dejv workflow.

## Core rule

1. Recognize the task type.
2. Choose at most 1-3 skills.
3. Choose at most one agent procedure unless the task is strategic.
4. Do not guess APIs, classes, hooks, tables, prefixes, statuses, or paths.
5. Inspect real project files before changing code.
6. For SQL, show diagnostic `SELECT` first.
7. For code changes, show a plan before editing.
8. Verify after the change.
9. Before commit, use `code-reviewer` plus `karpathy-check`.
10. After a long task, create a handoff.

## Selection limits

- Simple task: 1 skill.
- Medium task: 2 skills.
- Larger task: maximum 3 skills plus one agent procedure.
- Strategic task: one persona plus 2-3 skills plus one 7dejv workflow.

## Modes

### A. PrestaShop, PHP, modules, ecommerce store

Use for PrestaShop, PHP modules, hooks, admin panel, storefront, orders, payments, invoices, stock, integrations, PrestaShop SQL, and store performance.

Candidate skills: choose 1-3 from `zero-hallucination-coder`, `senior-backend`, `senior-fullstack`, `sql-database-assistant`, `database-schema-designer`, `code-reviewer`, `focused-fix`, `performance-profiler`, `security-guidance`. Do not load the whole candidate list by default.

Procedures: `agent-procedures/engineering/cs-backend-engineer.md`, `agent-procedures/engineering/cs-fullstack-engineer.md`, `agent-procedures/engineering/cs-engineer-grill.md`, `agent-procedures/engineering/karpathy-check.md`.

Rules: inspect real module examples first; never guess PrestaShop classes, hooks, table prefix, or order status names; show database plan before schema/data changes; review after changes.

### B. SQL, VAT, reports, warehouse, sales data

Use for VAT reports, sales reports, income data, orders, statuses, products, stock, purchase invoices, goods receipts, margin, commissions, and shipping costs.

Candidate skills: choose 1-3 from `sql-database-assistant`, `database-designer`, `database-schema-designer`, `performance-profiler`. Do not load the whole candidate list by default.

Procedures: `agent-procedures/engineering/cs-backend-engineer.md`; add `agent-procedures/business/cs-commercial-orchestrator.md` for margin/pricing, or `agent-procedures/business/cs-bizops-orchestrator.md` for company process.

Rules: show diagnostic `SELECT`; never assume table structure or prefix; no update/delete without approval; every query must state purpose, risk, and verification.

### C. Ecommerce operations, Allegro, BaseLinker, shipping

Use for Allegro, BaseLinker, couriers, DPD, InPost, DHL, UPS, Geodis, pallets, COD, surcharges, claims, customer support, order automation, warehouse flow, packing, delays, and staff procedures.

Candidate skills: choose 1-3 from `process-mapper`, `knowledge-ops`, `runbook-generator`, `capacity-planner`, `procurement-optimizer`, `vendor-management`, `pricing-strategist`, `commercial-forecaster`. Do not load the whole candidate list by default.

Procedures: `agent-procedures/business/cs-bizops-orchestrator.md`, `agent-procedures/business/cs-commercial-orchestrator.md`, `command-procedures/business/cs-process-map.md`, `command-procedures/business/cs-procurement.md`, `command-procedures/business/cs-vendor-review.md`, `command-procedures/business/cs-capacity-plan.md`.

Rules: map the process first; separate system, human, courier, warehouse, and customer causes; produce checklists and operating procedures; include cost, time, error risk, and scalability.

### D. SEO, product descriptions, marketing, categories

Use for store SEO, product descriptions, categories, landing pages, blog, campaigns, Google, AEO, structured data, schema.org, copywriting, Allegro descriptions, banners, and promotions.

Candidate skills: choose 1-3 from `seo-audit`, `schema-markup`, `programmatic-seo`, `copywriting`, `content-strategy`, `campaign-analytics`, `ad-creative`, `landing-page-generator`. Do not load the whole candidate list by default.

Procedures/personas: `agent-procedures/personas/growth-marketer.md`.

Rules: identify user intent first, then content structure, phrases, description, CTA, and structured data; avoid filler; write to answer real customer questions and sell.

### E. Large technical decisions

Use for technology selection, architecture, larger modules, multi-system integration, API, security, migrations, performance, and long-term decisions.

Candidate skills: choose 1-3 from `zero-hallucination-coder`, `senior-architect`, `api-design-reviewer`, `database-schema-designer`, `performance-profiler`, `security-guidance`. Do not load the whole candidate list by default.

Procedures/personas: `agent-procedures/personas/startup-cto.md`, `agent-procedures/engineering/cs-engineer-grill.md`, `agent-procedures/engineering/cs-fullstack-engineer.md`, `agent-procedures/engineering/cs-backend-engineer.md`.

Rules: run forcing questions before deciding; separate facts from assumptions; show options; recommend the simplest working solution; do not recommend microservices when a monolith is enough.

### F. Before commit or deployment

Use before commit, push, deployment, larger change, database change, configuration change, or module publication.

Candidate skills: choose 1-3 from `code-reviewer`, `pr-review-expert`, `dependency-auditor`, `security-guidance`; add `performance-profiler` only for performance-sensitive changes. Do not load the whole candidate list by default.

Procedures: `agent-procedures/engineering/karpathy-check.md`, `command-procedures/engineering/focused-fix.md` if the work fixed a bug.

Checklist: minimal change, no dead code, no placeholders, no secrets, no guessed APIs, based on real project structure, rollback path exists, test evidence is described.

### G. Long tasks and continuation

Use when the task is long, has many files, must be resumed later, needs context transfer, or has multiple stages.

Candidate procedures/skills: choose 1-3 from `handoff`, `command-procedures/productivity/cs-handoff.md`, `llm-wiki` if available, project notes if available, `knowledge-ops`. Do not load the whole candidate list by default.

Rules: after major stages create handoff; record decisions, changed files, open questions, and next step; do not leave the project state undescribed.

## Output format

Start larger tasks with:

```text
Task type:
Selected skills:
Selected procedure/persona:
Workflow:
Plan:
Verification:
Risks:
```

End larger tasks with:

```text
What changed:
Files touched:
Verification performed:
Residual risks:
Next step:
```
