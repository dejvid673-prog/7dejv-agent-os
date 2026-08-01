# 7dejv-codex-safety-gate

## Kategoria

Quality control / Codex / safety

## Status

`v0.1 — do testu`

## Cel skilla

Wymusza bezpieczny tryb pracy z Codex: najpierw rozpoznanie i raport, dopiero potem zmiany. Chroni repozytoria przed chaotycznym przepisywaniem, usuwaniem plików i kodowaniem bez audytu.

## Kiedy używać

- przed pracą Codex w repozytorium,
- przed refaktorem,
- przed migracją plików,
- przy modułach PrestaShop,
- przy narzędziach, których skutków nie znamy,
- gdy zadanie może narobić szkód.

## Czego skill nie robi

- nie koduje,
- nie instaluje paczek,
- nie uruchamia nieznanych skryptów,
- nie usuwa plików,
- nie przenosi plików bez zaakceptowanego planu.

## Zasady twarde

Codex ma:

1. przeczytać README,
2. przeczytać TODO/REPO_STATUS/DECISIONS,
3. sprawdzić zakres zadania,
4. wypisać ryzyka,
5. przygotować plan,
6. zatrzymać się na raporcie,
7. czekać na decyzję przed zmianami.

## Dane wejściowe

- repozytorium,
- cel zadania,
- ograniczenia,
- informacja, czy wolno modyfikować pliki.

## Wynik

Raport bezpieczeństwa przed pracą Codex.

## Format raportu

```markdown
# Safety Gate — Codex

Repo:
Zadanie:
Tryb: tylko audyt / zmiany dozwolone / zmiany zabronione

## Zakres

## Pliki do przeczytania

## Ryzyka

## Czego nie wolno robić

## Plan bezpiecznej pracy

## Decyzje wymagane przed działaniem
```

## Szczególne zasady dla PrestaShop

Przy `7dejv-prestashop` obowiązuje obecnie wstrzymanie implementacji modułów. Codex nie może tworzyć nowych wersji `orderpanelmvp`, `dpdshipmvp` ani `dpdpackoffice`, dopóki użytkownik nie wyda osobnej decyzji.
