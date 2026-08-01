# 7dejv-prestashop-module-builder

## Kategoria

prestashop

## Status

v0.1 — do testu

## Cel skilla

Pomaga zaprojektować bezpieczny moduł PrestaShop albo przygotować plan jego budowy, ale nie wymusza natychmiastowego kodowania.

Skill ma prowadzić od pomysłu do dokumentacji technicznej, checklisty bezpieczeństwa, planu testów i dopiero na końcu do decyzji, czy można przejść do implementacji.

## Kiedy używać

Używać, gdy trzeba:

- zaprojektować nowy moduł PrestaShop,
- ocenić, czy pomysł na moduł ma sens,
- rozdzielić odpowiedzialności między modułami,
- przygotować wymagania techniczne,
- przygotować prompt dla Codex do późniejszej pracy,
- sprawdzić ryzyka przed kodowaniem,
- przygotować plan MVP modułu.

## Czego skill nie robi

Skill nie robi:

- nie pisze od razu kodu modułu,
- nie tworzy paczki ZIP,
- nie instaluje modułu,
- nie zmienia istniejącego kodu,
- nie dotyka produkcyjnego sklepu,
- nie używa prawdziwych danych klientów,
- nie zapisuje haseł, tokenów ani kluczy API,
- nie omija decyzji o wstrzymaniu modułów,
- nie zastępuje audytu błędów.

## Dane wejściowe

Wymagane dane:

- nazwa robocza modułu,
- problem, który moduł ma rozwiązać,
- miejsce działania: Back Office, front, API, cron, panel zamówienia itd.,
- wersja PrestaShop, jeżeli znana,
- zależności od innych modułów,
- czego moduł nie ma robić,
- czy moduł ma być tylko MVP,
- czy istnieją wcześniejsze błędy lub dokumentacja.

Opcjonalne dane:

- lista hooków do sprawdzenia,
- wymagane tabele bazy danych,
- wymagane ustawienia konfiguracyjne,
- oczekiwany wygląd panelu,
- wymagania bezpieczeństwa,
- wymagania testowe.

## Wynik

Skill powinien zwrócić dokument projektowy w Markdown zawierający:

- cel modułu,
- zakres MVP,
- poza zakresem,
- strukturę plików,
- możliwe hooki,
- konfigurację,
- dane w bazie,
- akcje administratora,
- ryzyka,
- checklistę bezpieczeństwa,
- checklistę testów,
- decyzję: można kodować / wymaga doprecyzowania / wstrzymać.

## Procedura działania

1. Odczytaj cel modułu i problem użytkownika.
2. Sprawdź, czy moduł jest naprawdę potrzebny, czy wystarczy dokumentacja/procedura.
3. Ustal granice modułu: co robi i czego nie robi.
4. Sprawdź, czy moduł nie dubluje istniejącego modułu.
5. Ustal, czy działa w Back Office, froncie, API, cron lub konfiguracji.
6. Wypisz minimalny zakres MVP.
7. Wypisz ryzyka techniczne i bezpieczeństwa.
8. Przygotuj strukturę dokumentacji, nie kodu.
9. Przygotuj checklistę testów.
10. Zakończ decyzją, czy wolno przejść do implementacji.

## Format wyniku

```markdown
# Projekt modułu PrestaShop

## Nazwa robocza modułu

## Problem do rozwiązania

## Cel modułu

## Zakres MVP

## Poza zakresem

## Miejsce działania w PrestaShop

## Proponowane hooki / integracje

## Konfiguracja modułu

## Dane i baza danych

## Akcje administratora

## Bezpieczeństwo

## Ryzyka techniczne

## Checklista testów

## Decyzja

- [ ] można przejść do implementacji
- [ ] wymaga doprecyzowania
- [ ] wstrzymać
```

## Zasady bezpieczeństwa

- Jeżeli moduł dotyczy API, nie logować haseł, tokenów ani danych dostępowych.
- Jeżeli moduł dotyczy zamówień, nie używać prawdziwych danych klientów w repo.
- Jeżeli moduł dotyczy Back Office, każda akcja administracyjna musi mieć token.
- Nie wykonywać ciężkich operacji przy zwykłym wejściu na ekran Back Office.
- Nie modyfikować core PrestaShop.
- Nie dodawać override bez osobnej decyzji.
- Nie zmieniać checkoutu/frontu bez osobnej decyzji.
- API zewnętrzne uruchamiać tylko po akcji administratora albo według jawnej procedury.

## Kryteria jakości

Projekt modułu jest dobry, jeżeli:

- rozwiązuje konkretny problem,
- ma mały zakres MVP,
- ma jasno opisane granice,
- nie dubluje innych modułów,
- ma opisane ryzyka,
- ma checklistę testów,
- ma decyzję, czy można kodować,
- nie ukrywa niepewności,
- nie tworzy ciężkiego kombajnu.

## Minimalny test

Test skilla:

1. Podaj pomysł na moduł Back Office.
2. Sprawdź, czy skill nie zaczyna od kodowania.
3. Sprawdź, czy oddziela zakres od poza zakresem.
4. Sprawdź, czy tworzy checklistę bezpieczeństwa.
5. Sprawdź, czy kończy decyzją: można kodować / wymaga doprecyzowania / wstrzymać.

## Decyzja po teście

- `używać dalej` — jeżeli skill tworzy bezpieczny dokument projektowy.
- `poprawić` — jeżeli brakuje ryzyk, checklisty albo granic.
- `wstrzymać` — jeżeli skill zaczyna od kodu lub ignoruje decyzję o wstrzymaniu modułów.

## Uwagi

Ten skill jest builderem projektowym, nie generatorem kodu.

W aktualnym stanie projektu 7DEJV implementacja modułów PrestaShop jest wstrzymana. Dlatego skill może przygotować dokumentację i plan, ale nie powinien uruchamiać pracy kodowej bez osobnej decyzji użytkownika.
