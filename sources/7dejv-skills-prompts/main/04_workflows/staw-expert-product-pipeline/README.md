# STAW EXPERT Product Pipeline

Kompletna specyfikacja projektowa procesu od analizy rynku do audytu produktu oraz cyklu tworzenia skilli.

## Status

- `DESIGN_READY`
- `SKILL_PACK_READY_FOR_REVIEW`
- nie jest jeszcze `N8N_IMPORT_READY`
- nie jest jeszcze `PRODUCTION_READY`

## Kolejność produktu

```text
DISCOVERED
→ SHORTLISTED
→ ANALYZED
→ COMPOSITION_EVIDENCE
→ FORMULATION_DRAFT
→ DOSAGE_TEST_PLAN
→ HUMAN_LAB_REVIEW
→ NAMING_DRAFT
→ COPY_DRAFT
→ FRONT_LABEL_DRAFT
→ BACK_LABEL_DRAFT
→ RELEASE_AUDIT
→ READY_FOR_PILOT
```

## Warstwa skilli

Przed każdym etapem router sprawdza dostępność zatwierdzonego skilla. Brak skilla uruchamia `7dejv-skill-factory` i `skill-lifecycle-workflow.md`.

## Pliki

- `workflow-master.md` — pełna logika produktu i skilli,
- `skill-lifecycle-workflow.md` — tworzenie, testowanie i zatwierdzanie skilli,
- `data-contract.schema.json` — wspólny kontrakt danych,
- `status-transition-matrix.md` — dozwolone przejścia,
- `n8n-node-map.md` — mapowanie na węzły n8n,
- `error-retry-policy.md` — retry, limity i eskalacje,
- `human-approval-gates.md` — obowiązkowe decyzje człowieka,
- `REPO_STATUS.md` — rzeczywista gotowość i pozostałe prace runtime.

## Zasada krytyczna

Automatyzacja przygotowuje analizę, hipotezy, projekty i raporty. Nie zatwierdza samodzielnie składu, instrukcji handlowych, etykiety produkcyjnej, publikacji, zakupów ani produkcji.
