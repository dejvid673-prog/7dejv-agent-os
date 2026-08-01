# Skill: PrestaShop Module Skeleton Builder

Data utworzenia: 2026-06-06
Główne zastosowanie: tworzenie powtarzalnego szkieletu modułów PrestaShop 9

---

## Cel skillu

Ten skill służy do tworzenia minimalnego, uporządkowanego szkieletu modułu PrestaShop 9.

Ma sprawić, że Codex nie zaczyna modułu od zera i nie wymyśla za każdym razem innej struktury.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- tworzenia nowego modułu,
- przygotowania struktury katalogów,
- dodania `modulename.php`,
- przygotowania `config/routes.yml`,
- przygotowania `config/services.yml`,
- stworzenia kontrolera Back Office,
- dodania templates/CSS/JS,
- przygotowania podstawowego `install()` i `uninstall()`.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `.ai/CONTEXT.md`
4. `.ai/GOTCHAS.md`
5. `.ai/PRESTASHOP_MODULE_FACTORY.md`
6. `templates/brief-modulu-prestashop.md`
7. `templates/struktura-modulu-prestashop9.md`
8. `templates/checklista-instalacji-modulu.md`
9. `docs/sources/prestashop-official-docs-index.md`
10. `docs/sources/prestashop-example-modules-map.md`

---

## Dane wejściowe wymagane przed tworzeniem szkieletu

Codex musi znać:

- nazwę modułu,
- cel modułu,
- czy moduł działa w Back Office,
- czy ma stronę konfiguracji,
- czy ma osobny kontroler admin,
- czy ma hooki,
- czy wymaga tabel bazy danych,
- czego moduł nie robi.

Jeśli brakuje danych, Codex ma najpierw wypełnić `templates/brief-modulu-prestashop.md`.

---

## Minimalna struktura modułu

```text
modulename/
  modulename.php
  composer.json
  config/
    routes.yml
    services.yml
  src/
    Controller/
    Service/
    Repository/
    Dpd/
  views/
    templates/
      admin/
    css/
      admin.css
    js/
      admin.js
  sql/
    install.sql
    uninstall.sql
  docs/
    README.md
  tests/
```

Nie każdy katalog jest obowiązkowy w MVP. Codex ma dodać tylko to, co jest potrzebne.

---

## Minimalny plik główny modułu

Plik `modulename.php` powinien zawierać:

- klasę modułu,
- nazwę modułu,
- wersję,
- autora,
- `ps_versions_compliancy`,
- `install()`,
- `uninstall()`,
- rejestrację wymaganych hooków,
- brak sekretów i danych lokalnych.

---

## Reguły dla `install()`

`install()` powinien:

- wywołać `parent::install()`,
- zarejestrować tylko potrzebne hooki,
- utworzyć tabele, jeśli są konieczne,
- dodać neutralne konfiguracje domyślne,
- nie dodawać prawdziwych danych API,
- nie ładować ciężkich zależności.

---

## Reguły dla `uninstall()`

`uninstall()` powinien:

- wywołać `parent::uninstall()`,
- usunąć konfiguracje techniczne,
- ostrożnie podchodzić do danych historycznych,
- nie usuwać danych przesyłek bez decyzji,
- nie zostawiać śmieci konfiguracyjnych.

---

## Reguły dla Back Office

Jeżeli moduł ma panel Back Office:

- użyj osobnego kontrolera,
- dodaj route,
- dodaj usługę w `services.yml`,
- CSS/JS ładuj tylko dla widoku modułu,
- nie mieszaj widoku z ciężką logiką,
- nie wykonuj API przy samym ładowaniu strony.

---

## Procedura pracy Codex

```text
Etap 1: Wypełnij lub sprawdź brief modułu.
Etap 2: Wybierz minimalne katalogi i pliki.
Etap 3: Zaprojektuj install/uninstall.
Etap 4: Zaprojektuj route, controller, services.
Etap 5: Zaprojektuj minimalny template.
Etap 6: Sprawdź granice odpowiedzialności modułu.
Etap 7: Wykonaj checklistę instalacji.
```

---

## Czego unikać

- nie tworzyć dużej architektury przed briefem,
- nie dodawać ciężkich bibliotek,
- nie kopiować całych przykładów,
- nie tworzyć tabel bez uzasadnienia,
- nie dodawać API DPD do `orderpanelmvp`,
- nie modyfikować core,
- nie używać override bez mocnego powodu.

---

## Wynik końcowy

Codex powinien zwrócić:

- strukturę katalogów,
- listę plików,
- krótkie uzasadnienie każdego pliku,
- plan install/uninstall,
- ryzyka,
- decyzję, czy można utworzyć szkielet.
