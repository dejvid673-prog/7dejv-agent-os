# Repository Quality Gate

## Cel

Blokować merge i deklaracje gotowości, gdy repozytorium nie ma wymaganych dowodów jakości.

## Przebieg

```text
START
→ INVENTORY
→ STRUCTURE_CHECK
→ DOCUMENTATION_COMPARE
→ AGENT_AUDIT
→ SKILL_AUDIT
→ WORKFLOW_AUDIT
→ SCHEMA_AUDIT
→ TEST_EVIDENCE_CHECK
→ SECURITY_CHECK
→ READINESS_CALCULATION
→ PASS / HOLD / BLOCKED
```

## Reguły decyzji

### `BLOCKED`
- aktywny problem bezpieczeństwa o wadze krytycznej,
- sekret w repozytorium,
- destrukcyjna akcja bez bramki człowieka,
- dokumentacja celowo ukrywa rzeczywisty stan.

### `HOLD`
- brak wykonanych testów,
- dokumentacja nie zgadza się z plikami,
- brak kontraktów lub wymaganych artefaktów,
- brak dowodu gotowości runtime,
- wynik ogólny poniżej 8/10.

### `PASS`
- brak problemów krytycznych i wysokich,
- wymagane testy wykonane,
- dokumentacja zgodna ze stanem faktycznym,
- wszystkie wymagane kontrakty przechodzą walidację,
- wynik ogólny co najmniej 8/10.

## Wynik

Raport zawiera status, ocenę ogólną, oceny kategorii, dowody, blokery, listę napraw oraz datę kolejnego audytu.
