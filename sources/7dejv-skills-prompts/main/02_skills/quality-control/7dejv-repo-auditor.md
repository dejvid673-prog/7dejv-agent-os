# 7dejv-repo-auditor

## Kategoria

Quality control / GitHub / repo audit

## Status

`v0.1 — do testu`

## Cel skilla

Audytuje repozytorium bez wprowadzania zmian. Ma pomóc sprawdzić, czy repo ma jasną rolę, aktualne README, TODO, CHANGELOG, DECISIONS, REPO_STATUS oraz czy nie miesza materiałów z innych obszarów.

## Kiedy używać

- przed większą migracją,
- po zmianie struktury repo,
- przed pracą z Codex,
- gdy repo zaczyna robić się chaotyczne,
- gdy trzeba sprawdzić, co jest jeszcze do uporządkowania.

## Czego skill nie robi

- nie usuwa plików,
- nie przenosi plików,
- nie zmienia kodu,
- nie robi automatycznego refaktoru,
- nie poprawia README bez osobnej decyzji.

## Dane wejściowe

- nazwa repozytorium,
- lista ważnych plików do sprawdzenia,
- aktualna mapa odpowiedzialności repo,
- opcjonalnie: konkretne pytanie audytowe.

## Wynik

Raport w Markdown z oceną:

- struktury repo,
- plików organizacyjnych,
- zgodności z mapą 7DEJV,
- braków,
- duplikatów,
- ryzyk,
- rekomendowanych kolejnych kroków.

## Procedura działania

1. Odczytaj `README.md`.
2. Odczytaj `TODO.md`, jeżeli istnieje.
3. Odczytaj `REPO_STATUS.md`, jeżeli istnieje.
4. Odczytaj `DECISIONS.md`, jeżeli istnieje.
5. Odczytaj `CHANGELOG.md`, jeżeli istnieje.
6. Sprawdź strukturę katalogów.
7. Sprawdź, czy repo nie miesza odpowiedzialności.
8. Wypisz braki i ryzyka.
9. Nadaj ocenę: `OK`, `DO POPRAWY`, `WYMAGA DECYZJI`, `CHAOS`.
10. Zakończ raportem, bez zmian w plikach.

## Format raportu

```markdown
# Audyt repozytorium

Repo:
Data:
Tryb: tylko odczyt

## Ocena ogólna

## Co jest uporządkowane

## Co wymaga poprawy

## Braki

## Ryzyka

## Rekomendowane następne kroki

## Decyzje wymagane od użytkownika
```

## Kryteria jakości

Repo jest dobrze uporządkowane, jeżeli:

- ma jasną rolę,
- ma aktualne README,
- ma TODO,
- ma REPO_STATUS,
- ma CHANGELOG,
- ma DECISIONS,
- nie miesza kodu, promptów, badań i produktów,
- ma wyraźne następne kroki.
