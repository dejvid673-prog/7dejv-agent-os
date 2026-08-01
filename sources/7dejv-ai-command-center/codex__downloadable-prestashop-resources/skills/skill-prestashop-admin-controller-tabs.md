# Skill: PrestaShop Admin Controller Tabs

Data utworzenia: 2026-06-06
Źródło wzorca: `_external/prestashop-example-modules/democontrollertabs`

---

## Cel skillu

Ten skill służy do projektowania własnych stron Back Office w modułach PrestaShop 9.

Najważniejsze zastosowania:

- osobny panel `orderpanelmvp`,
- strona konfiguracji lub diagnostyki `dpdshipmvp`,
- kontrolery admin,
- zakładki/tabs,
- routing,
- uprawnienia,
- `_legacy_controller` i `_legacy_link`.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- własnego kontrolera Back Office,
- menu/zakładki modułu,
- route admin,
- przekierowania z konfiguracji do panelu,
- uprawnień administratora,
- linków generowanych w Back Office.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `.ai/CONTEXT.md`
4. `.ai/GOTCHAS.md`
5. `.ai/PRESTASHOP_MODULE_FACTORY.md`
6. `docs/sources/prestashop-example-modules-map.md`
7. `_external/prestashop-example-modules/democontrollertabs/`
8. opcjonalnie `_external/prestashop-example-modules/demo_grid/`

---

## Minimalna struktura kontrolera

```text
config/routes.yml
config/services.yml
src/Controller/AdminExampleController.php
views/templates/admin/example.html.twig
```

Dla modułu używaj nazw dopasowanych do domeny, nie nazw demo.

---

## Reguły route

Route powinna być:

- jednoznaczna,
- powiązana z modułem,
- zgodna z Back Office,
- zabezpieczona,
- możliwa do linkowania z menu lub konfiguracji.

Codex ma sprawdzić, czy potrzebne są:

- `_legacy_controller`,
- `_legacy_link`,
- wymagane uprawnienia,
- przekierowanie po zapisie konfiguracji.

---

## Reguły kontrolera

Kontroler powinien:

- być lekki,
- delegować logikę do serwisów,
- walidować wejście,
- nie wykonywać ciężkich operacji przy GET,
- nie znać szczegółów API DPD,
- renderować template z danymi przygotowanymi przez serwis.

---

## Reguły dla tabs/menu

Przed dodaniem zakładki ustal:

- gdzie ma się pojawić,
- dla kogo jest widoczna,
- czy potrzebna jest osobna pozycja menu,
- czy wystarczy link z konfiguracji,
- czy uprawnienia są zgodne z rolą administratora.

---

## Zastosowanie dla `orderpanelmvp`

`orderpanelmvp` powinien mieć osobny panel Back Office, np.:

```text
AdminOrderPanelMvpController
```

Cel:

- lista zamówień do pakowania,
- filtry,
- statusy,
- przejście do DPD jako link.

Nie dodawać DPD API.

---

## Zastosowanie dla `dpdshipmvp`

`dpdshipmvp` może mieć:

- stronę konfiguracji,
- stronę diagnostyki,
- kontrolery akcji dla DPD,
- linki z panelu zamówienia.

Nie robić z niego głównej listy zamówień.

---

## Procedura pracy Codex

```text
Etap 1: Sprawdź, czy moduł wymaga osobnego kontrolera.
Etap 2: Sprawdź przykład democontrollertabs.
Etap 3: Zaprojektuj route.
Etap 4: Zaprojektuj controller.
Etap 5: Zaprojektuj template.
Etap 6: Sprawdź uprawnienia i linkowanie.
Etap 7: Wykonaj audyt bezpieczeństwa.
```

---

## Czego unikać

- nie kopiować nazw demo,
- nie dodawać zakładek bez potrzeby,
- nie robić ciężkiej logiki w kontrolerze,
- nie wykonywać API w GET,
- nie pomijać uprawnień,
- nie mieszać panelu zamówień z panelem DPD.

---

## Wynik końcowy

Codex powinien zwrócić:

- proponowane routes,
- kontroler,
- template,
- sposób linkowania,
- wymagane uprawnienia,
- ryzyka,
- testy ręczne.
