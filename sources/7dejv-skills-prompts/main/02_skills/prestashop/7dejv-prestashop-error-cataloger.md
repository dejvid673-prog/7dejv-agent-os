# 7dejv-prestashop-error-cataloger

## Kategoria

PrestaShop / errors / audit

## Status

`v0.1 — do testu`

## Cel skilla

Porządkuje błędy PrestaShop, modułów, Back Office, PHP, Symfony, MySQL/MariaDB i API w jeden czytelny katalog błędów.

## Kiedy używać

- po błędzie HTTP 500,
- po błędzie instalacji modułu,
- po błędzie Back Office,
- po błędzie DPD/API,
- gdy Codex wygenerował niedziałającą zmianę,
- przed decyzją, czy moduł naprawiać, przepisać czy odłożyć.

## Czego skill nie robi

- nie poprawia kodu,
- nie zgaduje przyczyny jako faktu,
- nie usuwa plików,
- nie uruchamia modułów,
- nie wprowadza zmian w sklepie.

## Dane wejściowe

- pełny komunikat błędu,
- miejsce wystąpienia,
- nazwa modułu lub obszaru,
- ostatnia wykonana czynność,
- wersja PrestaShop/PHP/MariaDB, jeżeli znana,
- stack trace, jeżeli dostępny.

## Wynik

Wpis do katalogu błędów z:

- objawem,
- obszarem,
- wagą,
- podejrzaną przyczyną,
- ryzykiem,
- następnym krokiem,
- statusem.

## Kategorie błędów

- `symfony`
- `php`
- `mysql`
- `prestashop-bo`
- `module-installation`
- `dpd-api`
- `security-token`
- `performance`
- `configuration`

## Wagi błędów

- `niska`
- `średnia`
- `wysoka`
- `krytyczna`

## Format wpisu

```markdown
## Błąd: krótka nazwa

Data:
Repo/moduł:
Obszar:
Komunikat:
Objaw:
Ostatnia czynność:
Podejrzana przyczyna:
Waga:
Status:
Następny krok:
Czy blokuje dalsze prace:
```

## Zasada

Najpierw dokładny opis błędu. Dopiero potem naprawa. Brak opisu = brak poprawki.
