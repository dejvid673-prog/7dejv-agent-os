# Agent Definition Review

## Cel

Doprowadzić profil agenta do zatwierdzonego, jednoznacznego kontraktu wykonawczego.

## Przebieg

```text
AGENT_DRAFT
→ ROLE_AUDIT
→ CONTRACT_BUILD
→ TOOL_PERMISSION_AUDIT
→ OVERLAP_CHECK
→ SAFETY_CHECK
→ TEST_REFERENCE_CHECK
→ QUALITY_SCORE
→ HUMAN_REVIEW
→ APPROVED / HOLD / BLOCKED
```

## `APPROVED`
- jedna główna odpowiedzialność,
- pełny kontrakt wejścia i wyjścia,
- minimalne uprawnienia,
- brak nieuzasadnionego nakładania odpowiedzialności,
- jawne timeouty, retry, błędy i warunki STOP,
- istnieją testy lub plan testów,
- wynik co najmniej 8/10,
- człowiek zatwierdził wersję.

## `HOLD`
Brakujące metadane, testy, schematy, właściciel lub niejasna granica roli.

## `BLOCKED`
Konflikt uprawnień, duplikacja ryzykownej odpowiedzialności albo działanie sprzeczne z polityką bezpieczeństwa.
