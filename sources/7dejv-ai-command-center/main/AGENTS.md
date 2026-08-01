# AGENTS.md — instrukcja główna dla Codex

## Rola repozytorium

To repozytorium jest centrum pracy 7DEJV. Codex ma traktować je jako źródło instrukcji, katalog decyzji, bazę promptów i miejsce porządkowania pracy.

## Najpierw czytaj `.ai/`

Przed większym zadaniem Codex ma najpierw sprawdzić katalog `.ai/`, bo jest to krótki, techniczny kontekst projektu.

Minimalna kolejność:

1. `.ai/CONTEXT.md`
2. `.ai/GOTCHAS.md`
3. `.ai/MODULE_RULES.md`
4. `.ai/PRESTASHOP_9_NOTES.md`
5. właściwy kontekst modułu:
   - `.ai/ORDERPANELMVP_CONTEXT.md`
   - `.ai/DPDSHIPMVP_CONTEXT.md`
6. `.ai/GENERATED_INDEX.md`
7. dopiero potem `README.md`, `docs/`, `prompts/`, `reports/`

## Zasady pracy Codex

1. Pracuj etapami.
2. Nie kończ pracy po pierwszym szkicu.
3. Po każdym etapie wykonaj audyt.
4. Jeśli audyt wykryje błąd, popraw wynik i ponów kontrolę.
5. Nie zmieniaj niepotrzebnie działających elementów.
6. Nie dodawaj ciężkich zależności bez uzasadnienia.
7. Nie mieszaj odpowiedzialności modułów.
8. Zapisuj wnioski w raportach.
9. Przy błędach krytycznych zatrzymaj się i opisz problem.
10. Nie zapisuj tokenów, haseł, danych klientów ani kluczy API.
11. Aktualizuj `.ai/`, jeśli odkryjesz ważną zasadę, pułapkę lub decyzję techniczną.

## Priorytety projektowe

1. PrestaShop 9.
2. Moduły Back Office.
3. Automatyzacja pracy.
4. Skille i agenci.
5. Prompty i procedury.
6. Raporty oraz dokumentacja.

## Ważne projekty

- `dpdshipmvp` — moduł DPD: API, FID, etykiety, tracking.
- `orderpanelmvp` — osobny panel zamówień do pakowania i nadawania.
- `7DEJV AI Command Center` — system organizacji pracy Codex.

## Zasada rozdzielenia modułów

`orderpanelmvp` nie powinien wykonywać zadań DPD.

`dpdshipmvp` nie powinien być główną listą zamówień.

Moduł zamówień ma być lekki i szybki. Moduł DPD ma uruchamiać się wtedy, kiedy realnie trzeba nadać przesyłkę.
