# cs-backend-engineer

- Zrodlo: `alirezarezvani/claude-skills/agents/engineering/cs-backend-engineer.md`
- Typ: procedura agenta, nie natywny agent Codexa.
- Uzywaj gdy: API, baza, migracje, QPS, tenancy, SLO, kolejki, modul backendowy, integracje.
- Laczyc ze skillami: `senior-backend`, `sql-database-assistant`, `api-design-reviewer`, `database-schema-designer`, `migration-architect`, `observability-designer`, `slo-architect`.

## Pytania przed praca

1. Read/write ratio i roczny forecast p99 QPS?
2. Tenancy: single, shared multi-tenant, isolated?
3. Sync, async queue, event-driven: default i wyjatki?
4. Data sensitivity: public, internal, PII, PHI, PCI?
5. Monolith, modular monolith, services, microservices: jakie uzasadnienie zespolowe?
6. RPO i RTO?
7. SLO i kto konsumuje error budget?

## Workflow

Nie projektuj API ani bazy przed pytaniami. Najpierw SLO, potem API contract, schema, migracja, observability, CI/CD, security.

## Output

Matched profile, SLO, RPO/RTO, approver chain, sub-skill chain, plan weryfikacji.

## Ryzyka

Kafka/microservices bez drugiego zespolu, baza bez danych QPS, migracja bez rollbacku.

## Adaptacja do Codexa

Traktuj jako reczny grill backendowy i routing do skillow.

