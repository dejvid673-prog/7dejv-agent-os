# Procedura pobierania zasobów dla Codex

Data: 2026-06-06
Cel: ustalić, jak Codex ma korzystać z zasobów zewnętrznych przy budowie modułów PrestaShop.

---

## Problem

Pobieranie wszystkiego do repo powoduje bałagan, ryzyko licencyjne i spowalnia pracę. Dlatego zewnętrzne repozytoria pobieramy lokalnie do `_external/`, ale nie commitujemy ich do repo.

---

## Dozwolone pobieranie

Codex może zasugerować lub uruchomić lokalnie:

```text
tools/download-prestashop-resources.ps1
tools/download-prestashop-resources.sh
```

Skrypty pobierają:

```text
_external/prestashop-example-modules/
_external/prestashop-docker/
```

---

## Czego Codex nie powinien robić

- nie commitować katalogu `_external/`,
- nie kopiować całych cudzych modułów do `modules/`,
- nie instalować losowych paczek bez uzasadnienia,
- nie pobierać nieznanych modułów DPD z przypadkowych repozytoriów,
- nie dodawać vendorów do repo,
- nie dodawać sekretów, tokenów, haseł ani danych klientów.

---

## Procedura użycia przykładu

Przed użyciem zewnętrznego przykładu:

```text
1. Określ zadanie.
2. Sprawdź docs/sources/prestashop-example-modules-map.md.
3. Wybierz przykład.
4. Przeczytaj strukturę przykładu.
5. Wypisz wnioski.
6. Stwórz własny kod na podstawie wniosków.
7. Zrób audyt bezpieczeństwa i wydajności.
8. Zapisz w raporcie, z jakiego przykładu korzystano.
```

---

## Kiedy używać jakiego źródła

| Sytuacja | Źródło |
|---|---|
| Buduję listę Back Office | `demo_grid`, dokumentacja Admin Controllers |
| Dodaję panel w zamówieniu | `demovieworderhooks`, dokumentacja Hooks |
| Dodaję konfigurację DPD | `demosymfonyform`, dokumentacja Services |
| Dodaję serwis API | dokumentacja Services, własny adapter |
| Dodaję CI | dokumentacja CI/CD, własny workflow |
| Buduję lokalny PrestaShop | `PrestaShop/docker` |

---

## Minimalny raport po użyciu zasobu

```text
Użyty zasób:
Cel użycia:
Co sprawdzono:
Co przeniesiono jako pomysł:
Czego nie kopiowano:
Ryzyko licencyjne:
Ryzyko techniczne:
Decyzja:
```

---

## Zasada końcowa

Zewnętrzne źródła mają przyspieszać zrozumienie architektury, a nie zastępować projektowanie. Kod finalny dla 7DEJV ma być prosty, lekki, kontrolowany i dopasowany do PrestaShop 9.
