# Prompt dla Codex — audyt całego warsztatu PrestaShop

Data utworzenia: 2026-06-06
Cel: sprawdzenie, czy warsztat Codex jest gotowy do bezpiecznego tworzenia modułów PrestaShop 9.

---

## Prompt do wklejenia w Codex

```text
Pracuj w repozytorium 7dejv-ai-command-center.

Tryb pracy: AUDYT WARSZTATU CODEX.

Nie twórz jeszcze modułów.
Nie implementuj orderpanelmvp.
Nie implementuj dpdshipmvp.
Nie zmieniaj kodu modułów.
Najpierw przeprowadź pełny audyt przygotowania warsztatu do budowy modułów PrestaShop 9.

====================================================================
1. PLIKI DO PRZECZYTANIA
====================================================================

Najpierw przeczytaj:

1. README.md
2. AGENTS.md
3. .ai/CONTEXT.md
4. .ai/GOTCHAS.md
5. .ai/PRESTASHOP_MODULE_FACTORY.md
6. docs/codex/resource-download-workflow.md
7. docs/sources/downloadable-assets.md
8. docs/sources/prestashop-example-modules-map.md
9. docs/sources/prestashop-official-docs-index.md
10. docs/prestashop/moduly-prestashop.md
11. docs/prestashop/hooki-back-office.md

Następnie sprawdź katalogi:

- docs/modules/orderpanelmvp/
- docs/modules/dpdshipmvp/
- skills/
- templates/
- prompts/
- tools/
- _external/prestashop-example-modules/
- _external/prestashop-docker/

Jeśli `_external/` nie istnieje, zgłoś to jako brak lokalnej biblioteki i podaj komendę:

powershell -ExecutionPolicy Bypass -File .\tools\download-prestashop-resources.ps1

====================================================================
2. ZADANIE AUDYTU
====================================================================

Sprawdź, czy warsztat jest gotowy do powtarzalnego tworzenia modułów PrestaShop 9.

Oceń osobno:

1. kompletność `.ai/`,
2. kompletność `skills/`,
3. kompletność `templates/`,
4. kompletność `docs/sources/`,
5. kompletność `docs/modules/orderpanelmvp/`,
6. kompletność `docs/modules/dpdshipmvp/`,
7. jakość skryptów w `tools/`,
8. zgodność warsztatu z PrestaShop 9,
9. granicę między `orderpanelmvp` i `dpdshipmvp`,
10. ryzyka bezpieczeństwa,
11. ryzyka wydajności,
12. ryzyka chaosu architektonicznego,
13. brakujące skille,
14. brakujące checklisty,
15. brakujące prompty dla Codex.

====================================================================
3. SPRAWDŹ, CZY WARSZTAT ZAWIERA PROCEDURĘ
====================================================================

Sprawdź, czy repo prowadzi Codex przez etapy:

Brief -> Architektura -> Szkielet -> UI/BO -> Logika -> DB -> Testy -> Audyt -> ZIP

Jeśli któryś etap jest słabo opisany, wypisz konkretnie:

- czego brakuje,
- jaki plik trzeba utworzyć,
- co powinien zawierać,
- jaki ma mieć priorytet.

====================================================================
4. SPRAWDŹ SKILLE
====================================================================

Przejrzyj wszystkie pliki w `skills/`.

Dla każdego skillu oceń:

- do czego służy,
- czy ma jasny zakres,
- czy nie dubluje się z innym,
- czy ma źródła referencyjne,
- czy ma procedurę pracy,
- czy ma sekcję „czego unikać”,
- czy zabezpiecza przed typowymi błędami,
- czy nadaje się do użycia przez Codex bez dodatkowych wyjaśnień.

Na końcu przygotuj tabelę:

| Skill | Ocena | Problem | Poprawka |

====================================================================
5. SPRAWDŹ TEMPLATES
====================================================================

Przejrzyj wszystkie pliki w `templates/`.

Dla każdego template oceń:

- kiedy go używać,
- czy jest wystarczająco konkretny,
- czy ma checklistę bezpieczeństwa,
- czy ma checklistę wydajności,
- czy pomaga zatrzymać chaos,
- czy wymusza decyzję końcową.

Na końcu przygotuj tabelę:

| Template | Ocena | Problem | Poprawka |

====================================================================
6. SPRAWDŹ BRAKI
====================================================================

Wypisz brakujące elementy, np.:

- brak skillu,
- brak template,
- brak promptu,
- brak dokumentu technicznego,
- brak checklisty testów,
- brak zasad ZIP,
- brak zasad CI,
- brak zasad pracy z Dockerem,
- brak zasad wersjonowania modułu.

Każdy brak oznacz priorytetem:

- P1 — potrzebne przed pierwszym modułem,
- P2 — przydatne przed DPD,
- P3 — późniejsza optymalizacja.

====================================================================
7. AUDYT GRANICY MODUŁÓW
====================================================================

Sprawdź, czy dokumentacja jasno pilnuje granicy:

orderpanelmvp:
- lista zamówień,
- pakowanie,
- status problemu,
- przejście do DPD jako link.

Nie może:
- wywoływać DPD API,
- generować etykiet,
- zapisywać FID.


dpdshipmvp:
- panel DPD w zamówieniu,
- konfiguracja DPD,
- API DPD,
- FID,
- etykiety,
- tracking.

Nie może:
- być główną listą zamówień,
- obciążać sklepu globalnie,
- wykonywać API bez świadomej akcji admina.

====================================================================
8. WYNIK KOŃCOWY
====================================================================

Przygotuj raport końcowy w takiej strukturze:

1. Podsumowanie w 10 zdaniach.
2. Ocena gotowości warsztatu w skali 1–10.
3. Najmocniejsze elementy warsztatu.
4. Największe braki.
5. Błędy krytyczne, jeśli są.
6. Lista poprawek P1.
7. Lista poprawek P2.
8. Lista poprawek P3.
9. Czy można zaczynać `orderpanelmvp`?
10. Co trzeba zrobić przed `dpdshipmvp`?
11. Jaki powinien być następny prompt dla Codex?

Na końcu dodaj decyzję:

Status: GOTOWE DO PIERWSZEGO MODUŁU / GOTOWE PO POPRAWKACH / NIEGOTOWE

Nie naprawiaj jeszcze plików. Najpierw tylko raport.
```
