# Skill: PrestaShop Module Audit

## Cel

Przeprowadzenie audytu modułu PrestaShop pod kątem struktury, działania, bezpieczeństwa, wydajności i zgodności z założeniami projektu.

## Kiedy używać

Używać przy:

- problemach z modułem,
- rozsypanym widoku Back Office,
- błędach PHP,
- problemach z hookami,
- przed większą przebudową,
- po zmianach w kodzie.

## Dane wejściowe

- nazwa modułu,
- wersja PrestaShop,
- wersja PHP,
- opis problemu,
- lista plików,
- logi błędów, jeśli dostępne.

## Procedura

1. Sprawdź strukturę modułu.
2. Sprawdź plik główny modułu.
3. Sprawdź instalację i deinstalację.
4. Sprawdź hooki.
5. Sprawdź kontrolery.
6. Sprawdź szablony.
7. Sprawdź JS/CSS.
8. Sprawdź bazę danych.
9. Sprawdź bezpieczeństwo.
10. Przygotuj raport.

## Wynik końcowy

Raport powinien zawierać:

- błędy krytyczne,
- błędy średnie,
- drobne poprawki,
- pliki do zmiany,
- rekomendowaną kolejność napraw,
- checklistę testów.

## Czego unikać

- przepisywania modułu bez diagnozy,
- dodawania ciężkich zależności,
- modyfikacji core PrestaShop,
- mieszania logiki modułów.
