# Repository Classification

Data decyzji: 2026-08-01

## Cel

Ustalic, jak repozytoria `dejvid673-prog` maja byc traktowane przy migracji do `7dejv-agent-os`.

## Klasyfikacja

### 1. Canonical

- `7dejv-agent-os`

To jest jedyne docelowe repo kanoniczne dla:

- `agents`
- `skills`
- `workflows`
- `prompts`
- raportow inwentaryzacyjnych

### 2. Primary Migration Sources

- `7dejv-skills-prompts`
- `7dejv-ai-command-center`
- `7dejv.os`
- `7dejv-staw-expert`
- `airtable-agent`

To sa repo o najwyzszym sygnale dla artefaktow agentowych. Od nich nalezy zaczac migracje.

### 3. Secondary Sources

- `7dejv-prestashop`
- `n8n_7d`
- `repetytorium`

Te repo moga zawierac lokalne workflow, prompty albo procedury, ale nie sa pierwszym priorytetem.

### 4. Reference Or Low-Signal

- `Agent-repo`
- `7dejv-dawid`
- `bufor-github`

Te repo nie powinny byc ignorowane, ale na ten etap sa referencyjne albo pomocnicze.

### 5. No Current Migration Value

- `n8n`

Repo jest puste, wiec nie wnosi materialu do migracji.

## Reguly porzadkowania

1. Najpierw inwentaryzuj `Primary Migration Sources`.
2. Dopiero po ich opracowaniu sprawdzaj `Secondary Sources`.
3. `Reference Or Low-Signal` przegladac tylko wtedy, gdy brakuje potwierdzenia, zrodla albo historii.
4. Nie czyscic zadnego repo przed:
   - wskazaniem wersji kanonicznej,
   - zapisaniem dowodu pochodzenia,
   - przygotowaniem listy duplikatow,
   - osobna zgoda na cleanup.

## Następny krok

Uruchomic pierwsza inwentaryzacje tresci z:

- `7dejv-skills-prompts`
- `7dejv-ai-command-center`
- `7dejv.os`
- `7dejv-staw-expert`
- `airtable-agent`

i zapisac wynik do `docs/inventory/`.
