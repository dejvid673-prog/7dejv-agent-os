# Skill: PrestaShop Docker Test Env

Data utworzenia: 2026-06-06

---

## Cel skillu

Ten skill służy do planowania i audytu lokalnego środowiska testowego Docker dla modułów PrestaShop 9.

Nie służy do projektowania samego modułu. Docker ma potwierdzić, że moduł działa w praktyce.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- uruchomienia PrestaShop 9 lokalnie,
- testu instalacji modułu,
- testu deinstalacji,
- testu widoku Back Office,
- testu hooków zamówienia,
- testu konfiguracji,
- testu ZIP modułu,
- sprawdzania logów PHP/SQL/JS.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `.ai/CONTEXT.md`
2. `.ai/GOTCHAS.md`
3. `.ai/PRESTASHOP_MODULE_FACTORY.md`
4. `docs/prestashop/docker-test-env.md`
5. `templates/checklista-instalacji-modulu.md`
6. `templates/checklista-bezpieczenstwa-modulu.md`
7. `_external/prestashop-docker/`

Jeśli `_external/prestashop-docker/` nie istnieje, podaj komendę:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\download-prestashop-resources.ps1
```

---

## Minimalny scenariusz

```text
1. Sprawdź, czy Docker działa.
2. Sprawdź lokalne źródło _external/prestashop-docker/.
3. Przygotuj minimalne środowisko PrestaShop 9.
4. Skopiuj moduł do katalogu modules/.
5. Zainstaluj moduł w Back Office.
6. Otwórz widok modułu.
7. Sprawdź główną funkcję MVP.
8. Sprawdź logi PHP, SQL i JS.
9. Odinstaluj moduł.
10. Zainstaluj ponownie.
11. Zapisz raport.
```

---

## Czego nie robić

- nie zgaduj gotowego `docker-compose.yml` bez sprawdzenia źródła,
- nie mieszaj środowiska testowego z produkcją,
- nie wkładaj sekretów do plików Docker,
- nie zapisuj danych klientów w obrazie/kontenerze,
- nie traktuj Dockera jako dowodu bezpieczeństwa modułu,
- nie pomijaj testu instalacji z paczki ZIP.

---

## Wynik końcowy

Codex powinien zwrócić:

- wymagania środowiska,
- plan uruchomienia,
- listę komend,
- test instalacji modułu,
- test deinstalacji,
- miejsca logów,
- raport błędów,
- decyzję: środowisko gotowe / wymaga poprawek.
