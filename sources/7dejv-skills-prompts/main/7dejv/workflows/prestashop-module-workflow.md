# PrestaShop module workflow

## Kiedy uzywac

Gdy zadanie dotyczy budowy, naprawy lub audytu modulu PrestaShop.

## Wejscie

Repo projektu, wersja PrestaShop/PHP, nazwa modulu, opis funkcji, przyklad istniejacego modulu.

## Skille

`zero-hallucination-coder`, `senior-backend`, `senior-fullstack`, `focused-fix`, `code-reviewer`, `security-guidance`.

## Procedury agentow

`cs-backend-engineer`, `cs-fullstack-engineer`, `karpathy-check`.

## Kroki

1. Znajdz realna strukture modulu i podobne moduly.
2. Sprawdz klasy, hooki, konfiguracje i sciezki.
3. Przygotuj plan zmian.
4. Wprowadz minimalny diff.
5. Sprawdz admin, front, logi i rollback.

## Weryfikacja

Test instalacji/konfiguracji, test funkcji, brak fatal error, review diff.

## Ryzyka

Zgadniete hooki, zly prefix tabel, niekompatybilna wersja PrestaShop, brak rollbacku.

## Output

Kod modulu lub plan naprawy, lista plikow, instrukcja testu i ryzyka.

