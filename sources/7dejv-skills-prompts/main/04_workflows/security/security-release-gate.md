# Security Release Gate

## Cel

Blokować merge, wdrożenie i wykonanie runtime, gdy wykryto sekret, niebezpieczne uprawnienie, podatną zależność albo niezaliczony test odporności.

## Przebieg

```text
SECRET_SCAN
→ DEPENDENCY_REGISTRY_CHECK
→ TOOL_PERMISSION_AUDIT
→ DOMAIN_ALLOWLIST_CHECK
→ PROMPT_INJECTION_TESTS
→ DESTRUCTIVE_ACTION_REVIEW
→ LICENSE_REVIEW
→ HUMAN_SECURITY_REVIEW
→ PASS / HOLD / BLOCKED
```

## `BLOCKED`
- aktywny sekret lub prywatny klucz,
- destrukcyjna akcja bez human gate,
- nieznane źródło wykonywalnej zależności,
- próba ujawnienia chronionych danych,
- nieuzasadnione uprawnienia zapisu, publikacji, usuwania lub zakupu.

## `HOLD`
- zależność bez przypiętej wersji,
- brak informacji o licencji,
- domena poza allowlistą,
- brak wyników testów odporności,
- uprawnienie wymaga dodatkowego uzasadnienia.

## `PASS`
- brak aktywnych problemów krytycznych i wysokich,
- wszystkie zależności mają źródło, wersję i status licencji,
- narzędzia używają minimalnych uprawnień,
- wymagane testy bezpieczeństwa zakończyły się powodzeniem,
- człowiek zatwierdził ryzyka wymagające decyzji.
