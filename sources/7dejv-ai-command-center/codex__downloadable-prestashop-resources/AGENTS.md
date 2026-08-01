# AGENTS.md — instrukcja główna dla Codex

## Rola repozytorium

To repozytorium jest centrum pracy 7DEJV. Codex ma traktować je jako źródło instrukcji, katalog decyzji, bazę promptów i miejsce porządkowania pracy.

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
