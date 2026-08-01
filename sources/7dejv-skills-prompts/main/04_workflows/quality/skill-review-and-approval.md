# Skill Review and Approval

## Cel

Ujednolicić przejście skilla od wersji roboczej do zatwierdzenia.

## Przebieg

```text
SKILL_DRAFT
→ SKILL_LINT
→ CONTRACT_AUDIT
→ DUPLICATE_CHECK
→ SAFETY_AUDIT
→ TEST_DEFINITION_CHECK
→ TEST_RESULT_CHECK
→ BASELINE_COMPARISON
→ QUALITY_SCORE
→ HUMAN_REVIEW
→ APPROVED / HOLD / BLOCKED
```

## Warunki

### `APPROVED`
- linter nie zwraca błędów,
- kontrakt wejścia i wyjścia jest kompletny,
- zakres nie dubluje istniejącego skilla bez uzasadnienia,
- brak problemów bezpieczeństwa,
- wymagane testy są wykonane i udokumentowane,
- skill poprawia wynik lub dostarcza mierzalną wartość,
- ocena co najmniej 8/10,
- człowiek zatwierdził wersję.

### `HOLD`
- brakuje testów lub wyników,
- kontrakt wymaga uzupełnienia,
- opis uruchamiania jest nieprecyzyjny,
- ocena poniżej 8/10 bez problemu krytycznego.

### `BLOCKED`
- skill zawiera niebezpieczne lub nieoczekiwane działanie,
- wymaga nieuzasadnionych uprawnień,
- zawiera sekret lub niezweryfikowany kod zewnętrzny,
- jego rzeczywiste działanie jest sprzeczne z opisem.

## Artefakty

- raport lintera,
- raport kontraktu,
- raport bezpieczeństwa,
- definicje testów,
- wyniki testów,
- wynik baseline,
- karta akceptacji człowieka.
