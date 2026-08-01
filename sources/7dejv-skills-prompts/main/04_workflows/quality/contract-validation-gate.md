# Contract Validation Gate

## Cel

Walidować każdy rekord przed i po wykonaniu agenta oraz blokować nielegalne przejścia workflow.

## Przebieg

```text
INPUT
→ SCHEMA_VERSION_CHECK
→ STRUCTURAL_VALIDATION
→ BUSINESS_RULE_VALIDATION
→ STAGE_STATUS_VALIDATION
→ APPROVAL_VALIDATION
→ ROUTING_VALIDATION
→ PASS / HOLD / ERROR / BLOCKED
```

## Reguły

- `ERROR`: rekord nie przechodzi struktury JSON Schema,
- `HOLD`: rekord jest poprawny strukturalnie, ale brakuje danych wymaganych przez bieżący etap,
- `BLOCKED`: przejście jest zabronione, pomija human gate albo używa nieznanego skilla,
- `PASS`: rekord i proponowane przejście są zgodne ze schema i stage registry.

## Wymagane dowody

- wersja schematu,
- wersja rejestru etapów,
- lista błędów z pełnymi ścieżkami pól,
- bieżący etap i proponowany następny etap,
- wynik kontroli human gate,
- nazwa i wersja wybranego skilla.
