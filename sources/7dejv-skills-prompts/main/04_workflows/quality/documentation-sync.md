# Documentation Sync

## Cel

Utrzymywać README, statusy i katalogi repozytorium zgodne ze stanem faktycznym.

## Przebieg

```text
SCAN_REPOSITORY
→ GENERATE_REGISTRIES
→ VALIDATE_UNIQUE_NAMES
→ CHECK_REFERENCED_PATHS
→ CALCULATE_READINESS
→ COMPARE_DOCUMENTATION
→ GENERATE_DIFF_REPORT
→ PASS / HOLD / BLOCKED
```

## Reguły

- automatycznie generowane rejestry są źródłem liczby elementów,
- deklaracja gotowości bez dowodu daje `HOLD`,
- brak ścieżki lub zduplikowana nazwa daje co najmniej `HOLD`,
- celowo mylący status albo ukrycie krytycznego braku daje `BLOCKED`,
- aktualizacja README wymaga przeglądu człowieka przed merge.

## Artefakty

```text
registry/agents.json
registry/skills.json
registry/workflows.json
registry/schemas.json
registry/audits.json
registry/readiness.json
artifacts/repository-governance-report.json
```
