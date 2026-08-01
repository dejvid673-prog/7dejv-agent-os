# Skills — biblioteka skilli 7DEJV

Ten folder zawiera skille, czyli gotowe instrukcje pracy dla Codex i AI-workflow.

---

## Cel folderu

Skille mają zmniejszyć liczbę powtarzanych instrukcji.

Zamiast za każdym razem opisywać cały proces, Codex może odwołać się do właściwego skilla i pracować według gotowej procedury.

---

## Zasada główna

Skill nie zastępuje myślenia.

Skill daje procedurę, ograniczenia i checklistę. Codex ma dobrać skill do celu zadania, przeczytać wymagane źródła i pracować etapami.

---

## Routing skilli — którego używać najpierw

| Sytuacja | Główny skill | Skille wspierające |
|---|---|---|
| Nowy moduł PrestaShop od zera | `skill-prestashop-module-skeleton-builder.md` | `skill-prestashop-module-audit.md`, `skill-prestashop-module-db-install.md`, `skill-prestashop-module-ci-and-zip.md` |
| Audyt dowolnego modułu PrestaShop | `skill-prestashop-module-audit.md` | `skill-error-log.md`, `skill-docs-and-reporting.md` |
| Osobny panel Back Office / kontroler admin | `skill-prestashop-admin-controller-tabs.md` | `skill-html-css-js-backoffice.md` |
| Grid / lista Back Office | `skill-prestashop-bo-grid-builder.md` | `skill-prestashop-admin-controller-tabs.md`, `skill-html-css-js-backoffice.md` |
| `orderpanelmvp` | `skill-orderpanelmvp-builder.md` | `skill-prestashop-bo-grid-builder.md`, `skill-prestashop-admin-controller-tabs.md`, `skill-prestashop-module-db-install.md` |
| Panel w szczegółach zamówienia | `skill-prestashop-order-hooks.md` | `skill-prestashop-admin-controller-tabs.md` |
| Formularz konfiguracji modułu | `skill-prestashop-symfony-config-form.md` | `skill-prestashop-module-audit.md` |
| Baza danych modułu / install / uninstall | `skill-prestashop-module-db-install.md` | `skill-prestashop-module-audit.md` |
| DPD API / adapter / mocki | `skill-dpd-api-adapter.md` | `skill-prestashop-order-hooks.md`, `skill-prestashop-symfony-config-form.md` |
| `dpdshipmvp` mock-first | `skill-dpd-api-adapter.md` | `skill-prestashop-order-hooks.md`, `skill-prestashop-symfony-config-form.md`, `skill-dpdshipmvp-audit.md` |
| Testy Docker | `skill-prestashop-docker-test-env.md` | `skill-prestashop-module-ci-and-zip.md` |
| CI / ZIP / wydanie paczki | `skill-prestashop-module-ci-and-zip.md` | `skill-prestashop-module-audit.md`, `skill-docs-and-reporting.md` |
| Naprawa HTML/CSS/JS Back Office | `skill-html-css-js-backoffice.md` | `skill-prestashop-bo-grid-builder.md`, `skill-prestashop-admin-controller-tabs.md` |
| Praca automatyczna etapami | `skill-codex-n0-automation.md` | dowolny skill specjalistyczny |
| Dokumentacja i raportowanie | `skill-docs-and-reporting.md` | `skill-error-log.md` |
| Porządek repozytoriów / struktura folderów / duplikaty / archiwizacja | `skill-github-repo-organizer.md` | `skill-docs-and-reporting.md`, `skill-error-log.md` |
| README repozytorium / modułu / skillu / promptów | `skill-readme-builder.md` | `skill-docs-and-reporting.md` |
| Katalogowanie błędów | `skill-error-log.md` | `skill-docs-and-reporting.md` |

---

## Krótka zasada routingu

Jeśli zadanie dotyczy porządku repozytoriów, struktury folderów, duplikatów lub archiwizacji, użyj `skill-github-repo-organizer.md`.

Jeśli zadanie dotyczy pisania, poprawy lub audytu README, użyj `skill-readme-builder.md`.

---

## Lista skilli

| Plik | Zastosowanie |
|---|---|
| `skill-codex-n0-automation.md` | praca etapowa i automatyzacja N0 |
| `skill-github-repo-organizer.md` | porządkowanie repozytoriów, mapowanie ról, duplikaty, archiwizacja i struktura folderów |
| `skill-readme-builder.md` | pisanie, poprawa i audyt README dla repo, modułów, skilli, promptów i narzędzi lokalnych |
| `skill-prestashop-module-audit.md` | ogólny audyt modułu PrestaShop |
| `skill-prestashop-module-skeleton-builder.md` | tworzenie powtarzalnego szkieletu modułu PrestaShop 9 |
| `skill-prestashop-admin-controller-tabs.md` | kontrolery Back Office, taby, routing i uprawnienia |
| `skill-prestashop-bo-grid-builder.md` | grid/lista Back Office, filtry, sortowanie, paginacja |
| `skill-prestashop-order-hooks.md` | hooki w szczegółach zamówienia Back Office |
| `skill-prestashop-symfony-config-form.md` | formularze konfiguracji Symfony dla modułów |
| `skill-prestashop-module-db-install.md` | tabele modułu, indeksy, install/uninstall, migracje |
| `skill-prestashop-module-ci-and-zip.md` | CI, kontrola jakości i pakowanie ZIP |
| `skill-prestashop-docker-test-env.md` | testowanie modułów w lokalnym Docker/PrestaShop |
| `skill-orderpanelmvp-builder.md` | domenowy skill budowy panelu zamówień `orderpanelmvp` |
| `skill-dpdshipmvp-audit.md` | audyt modułu DPD `dpdshipmvp` |
| `skill-dpd-api-adapter.md` | adapter DPD API, mocki, timeouty, błędy, logowanie |
| `skill-html-css-js-backoffice.md` | naprawa i projektowanie HTML/CSS/JS Back Office |
| `skill-docs-and-reporting.md` | dokumentacja, raporty, decyzje techniczne |
| `skill-error-log.md` | katalogowanie błędów, priorytety, historia poprawek |

---

## Kolejność dla `orderpanelmvp`

```text
1. skill-prestashop-module-skeleton-builder.md
2. skill-orderpanelmvp-builder.md
3. skill-prestashop-bo-grid-builder.md
4. skill-prestashop-admin-controller-tabs.md
5. skill-prestashop-module-db-install.md, jeśli potrzebna tabela statusów pakowania
6. skill-html-css-js-backoffice.md
7. skill-prestashop-module-audit.md
8. skill-prestashop-module-ci-and-zip.md
```

Granica:

```text
orderpanelmvp nie używa DPD API, nie generuje etykiet i nie zapisuje FID.
```

---

## Kolejność dla `dpdshipmvp`

```text
1. skill-prestashop-module-skeleton-builder.md
2. skill-prestashop-symfony-config-form.md
3. skill-prestashop-order-hooks.md
4. skill-dpd-api-adapter.md
5. skill-prestashop-module-db-install.md
6. skill-dpdshipmvp-audit.md
7. skill-prestashop-module-ci-and-zip.md
```

Granica:

```text
dpdshipmvp nie jest główną listą zamówień i nie wykonuje API bez świadomej akcji administratora.
```

---

## Format dobrego skilla

Każdy skill powinien zawierać:

- cel,
- kiedy używać,
- źródła do sprawdzenia,
- dane wejściowe,
- procedurę,
- wynik końcowy,
- checklistę jakości,
- czego unikać.

---

## Zasada końcowa

Jeżeli Codex nie wie, którego skillu użyć, ma najpierw przeczytać:

```text
.ai/CONTEXT.md
.ai/PRESTASHOP_MODULE_FACTORY.md
```

a potem wrócić do tabeli routingu w tym pliku.
