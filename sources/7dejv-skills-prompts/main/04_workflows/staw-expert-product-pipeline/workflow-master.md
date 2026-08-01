# Workflow Master — STAW EXPERT Product Pipeline

## Cel

Sterować procesem przez n8n, zachowując identyfikator produktu, historię decyzji, dowody, błędy, użyte skille i punkty akceptacji.

## Warstwa przygotowania systemu

Przed uruchomieniem etapu produktowego router sprawdza, czy wymagany skill istnieje i ma status `APPROVED`.

```text
SKILL MISSING OR NOT APPROVED
→ 7dejv-skill-factory
→ skill-lifecycle-workflow
→ tests and audit
→ human review
→ APPROVED
→ return to product pipeline
```

Skill w statusie `DRAFT`, `TESTING`, `HOLD` albo `BLOCKED` nie może być automatycznie użyty do zmiany etapu produktu.

## Etapy produktu

1. `DISCOVERED` — zebranie kandydatów przez `7dejv-market-research-skill`.
2. `SHORTLISTED` — wybór 3–5 ofert referencyjnych.
3. `ANALYZED` — porównanie przez `7dejv-offer-analysis-skill`.
4. `COMPOSITION_EVIDENCE` — raport przez `7dejv-composition-evidence-skill`.
5. `FORMULATION_DRAFT` — brief przez `7dejv-formulation-brief-skill`.
6. `DOSAGE_TEST_PLAN` — dokumentacja przeglądu przez `7dejv-dosage-test-planning-skill`.
7. `HUMAN_LAB_REVIEW` — obowiązkowa decyzja człowieka/laboratorium.
8. `NAMING_DRAFT` — nazwa przez `7dejv-product-naming-skill`.
9. `COPY_DRAFT` — opis przez `7dejv-product-copy-skill`.
10. `FRONT_LABEL_DRAFT` — front przez `7dejv-label-front-skill`.
11. `BACK_LABEL_DRAFT` — tył A6 przez `7dejv-label-a6-mono-skill`.
12. `RELEASE_AUDIT` — audyt przez `7dejv-product-release-audit-skill`.
13. `READY_FOR_PILOT` — gotowość do kontrolowanego pilotażu.

## Logika n8n

Każdy etap:

1. pobiera rekord produktu,
2. uruchamia `7dejv-product-data-contract-validator`,
3. uruchamia `7dejv-product-pipeline-router`,
4. sprawdza status i wersję wymaganego skilla,
5. sprawdza wymagane wejście,
6. uruchamia właściwy skill, agenta lub zewnętrzne narzędzie,
7. ponownie waliduje wynik,
8. zapisuje dowody, wersję skilla, raport i koszty,
9. nadaje `PASS`, `HOLD`, `BLOCKED`, `ERROR` albo `WAITING_APPROVAL`,
10. wybiera następny etap lub zatrzymuje proces.

## Warunki STOP

Proces zatrzymuje się, gdy:

- wymagany skill nie istnieje lub nie jest zatwierdzony,
- kontrakt wejścia lub wyjścia jest niepoprawny,
- brakuje źródeł dla kluczowej tezy,
- hipoteza składu jest traktowana jako fakt,
- nie ma oceny bezpieczeństwa,
- brakuje zatwierdzonej dokumentacji instrukcji użycia,
- nazwa lub etykieta zbyt mocno przypomina konkurencję,
- agent próbuje publikować, kupować, produkować lub usuwać dane,
- przekroczono limit prób, czasu, kosztów albo tokenów,
- wymagana jest decyzja człowieka.

## Idempotencja

Każdy etap używa klucza:

```text
product_id + stage + input_version + skill_name + skill_version
```

Identyczne wejście zakończone `PASS` nie jest wykonywane ponownie bez `force_rerun=true`. Zmiana skilla, jego wersji lub danych wejściowych tworzy nowe wykonanie i nie usuwa poprzedniego raportu.

## Raport końcowy

Raport zawiera:

- historię etapów,
- wersje użytych skilli,
- dowody i ich klasy,
- decyzje człowieka,
- błędy i ponowienia,
- koszty i czas,
- aktualne ryzyka,
- artefakty produktu,
- decyzję `READY_FOR_PILOT`, `HOLD` albo `BLOCKED`.
