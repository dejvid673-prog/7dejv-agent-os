# Error and Retry Policy

## Klasy błędów

- `TRANSIENT` — timeout, chwilowy błąd API, limit chwilowy.
- `DATA_INVALID` — brak wymaganych pól lub niezgodny JSON.
- `AUTH` — brak lub wygaśnięcie uprawnień.
- `SAFETY_BLOCK` — próba niedozwolonej akcji albo ryzykowna treść.
- `BUSINESS_HOLD` — brak decyzji, dowodu lub danych laboratoryjnych.
- `SYSTEM` — awaria kontenera, bazy, dysku albo workflow.

## Retry

| Klasa | Próby | Opóźnienie | Wynik końcowy |
|---|---:|---|---|
| TRANSIENT | 3 | 1 min, 5 min, 30 min | ERROR + eskalacja |
| DATA_INVALID | 1 po normalizacji | natychmiast | HOLD |
| AUTH | 0 | — | ERROR + administrator |
| SAFETY_BLOCK | 0 | — | BLOCKED |
| BUSINESS_HOLD | 0 | — | WAITING_APPROVAL/HOLD |
| SYSTEM | 2 | 5 min, 30 min | ERROR + administrator |

## Ochrona przed pętlą

- maksymalnie 3 automatyczne próby etapu,
- maksymalnie 10 przejść agentowych w jednym wykonaniu master,
- limit czasu każdego wywołania,
- limit kosztów/tokenów per produkt i etap,
- brak automatycznego retry dla publikacji, zakupu, usuwania i zmian produkcyjnych.

## Error Workflow

Centralny workflow zapisuje pełny kontekst błędu, ale usuwa sekrety. Następnie tworzy alert z `product_id`, etapem, klasą błędu, liczbą prób i rekomendowaną akcją.
