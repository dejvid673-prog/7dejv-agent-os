# Skill: PrestaShop BO Grid Builder

Data utworzenia: 2026-06-06
Źródło wzorca: `_external/prestashop-example-modules/demo_grid`
Główne zastosowanie: `orderpanelmvp`

---

## Cel skillu

Ten skill służy do projektowania, budowy i audytu list Back Office opartych o wzorzec PrestaShop Grid.

Najważniejsze zastosowanie w 7DEJV:

- `orderpanelmvp` — osobny panel listy zamówień do pakowania, kontroli i przejścia do nadawania.

Skill ma pilnować, żeby lista była:

- lekka,
- czytelna,
- zgodna z PrestaShop 9,
- bez pomieszania z logiką DPD,
- łatwa do testowania,
- gotowa do dalszej rozbudowy.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- własnej listy Back Office,
- grida PrestaShop,
- filtrowania,
- sortowania,
- paginacji,
- akcji wiersza,
- akcji masowych,
- listy zamówień do pakowania,
- widoku `orderpanelmvp`,
- audytu tabeli/listy w Back Office.

---

## Czego nie robi ten skill

Ten skill nie służy do:

- nadawania paczek DPD,
- wywoływania API DPD,
- generowania etykiet,
- pobierania PDF etykiet,
- zapisywania FID,
- modyfikowania checkoutu,
- dodawania hooków frontowych,
- dekorowania core bez mocnego powodu.

Dla DPD użyj osobnego skillu `skill-dpd-api-adapter.md` albo `skill-prestashop-order-hooks.md`, gdy zostaną utworzone.

---

## Źródła, które Codex ma sprawdzić przed pracą

Przed pisaniem kodu przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `docs/modules/orderpanelmvp/wymagania.md`
4. `docs/modules/orderpanelmvp/granica-orderpanelmvp-dpdshipmvp.md`
5. `docs/modules/orderpanelmvp/ui-spec.md`
6. `docs/sources/prestashop-example-modules-map.md`
7. `_external/prestashop-example-modules/demo_grid/`
8. opcjonalnie `_external/prestashop-example-modules/demoextendgrid/`
9. opcjonalnie `_external/prestashop-example-modules/democontrollertabs/`

Jeżeli katalog `_external/` nie istnieje, nie zgaduj. Poproś o uruchomienie:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\download-prestashop-resources.ps1
```

---

## Minimalna architektura grida

Codex powinien dążyć do architektury podobnej do:

```text
modulename/
  config/
    routes.yml
    services.yml
  src/
    Controller/
      AdminOrderPanelController.php
    Grid/
      Definition/
        Factory/
          OrderPanelGridDefinitionFactory.php
      Query/
        OrderPanelQueryBuilder.php
    Service/
      OrderPanelDataProvider.php
  views/
    templates/
      admin/
        order_panel.html.twig
    css/
      admin.css
    js/
      admin.js
```

Dostosuj nazwy do konkretnego modułu.

---

## Dane wejściowe wymagane przed pracą

Przed implementacją ustal:

- nazwa modułu,
- wersja PrestaShop,
- wersja PHP,
- czy widok jest osobną stroną Back Office,
- jakie statusy zamówień pokazać,
- jakie kolumny są potrzebne,
- jakie filtry są potrzebne,
- czy lista ma akcje masowe,
- czy lista ma przejście do `dpdshipmvp`,
- czy moduł ma własne tabele statusów pakowania.

Jeżeli brakuje danych, przyjmij MVP i zapisz założenia.

---

## Minimalne kolumny dla `orderpanelmvp`

Startowy grid powinien rozważyć kolumny:

```text
checkbox
id_order / reference
klient
liczba produktów
status zamówienia
płatność
przewoźnik
COD / pobranie
status pakowania
problem
akcje
```

Nie dodawaj zbyt wielu kolumn na start. Lista ma pomagać pakować, nie być centrum analitycznym.

---

## Minimalne filtry

Startowe filtry:

```text
status zamówienia
status pakowania
przewoźnik
płatność
COD / pobranie
zakres dat
problem
wyszukiwarka
```

Jeżeli filtr wymaga ciężkiego zapytania, odłóż go do późniejszego etapu.

---

## Akcje wiersza

Dozwolone akcje dla `orderpanelmvp`:

- `Szczegóły`,
- `Oznacz jako spakowane`,
- `Problem`,
- `Cofnij`,
- `Przejdź do DPD`.

Akcja `Przejdź do DPD` może jedynie prowadzić do kontrolera `dpdshipmvp` z `id_order`.

Nie może:

- tworzyć przesyłki,
- wywoływać API DPD,
- generować etykiety,
- zapisywać FID.

---

## Akcje masowe

MVP może zawierać tylko proste akcje masowe:

- oznacz jako spakowane,
- oznacz problem,
- wyczyść zaznaczenie.

Nie dodawaj masowego nadawania DPD w `orderpanelmvp`.

---

## Reguły wydajności

Pilnuj:

- paginacji,
- sortowania po indeksowanych polach,
- ograniczenia liczby rekordów,
- braku ciężkich JOIN bez potrzeby,
- braku zapytań w pętli,
- braku wywołań API przy ładowaniu listy,
- braku globalnego ładowania CSS/JS,
- braku nadmiarowego logowania.

---

## Reguły bezpieczeństwa

Każda akcja administracyjna musi sprawdzać:

- uprawnienia administratora,
- poprawność `id_order`,
- token / zabezpieczenie akcji,
- brak ujawniania danych klientów poza Back Office,
- brak zapisu sekretów w repo,
- brak operacji DPD w module `orderpanelmvp`.

---

## Procedura pracy Codex

```text
Etap 1: Przeczytaj dokumentację i przykład demo_grid.
Etap 2: Wypisz wnioski z przykładu.
Etap 3: Zaprojektuj minimalny grid MVP.
Etap 4: Wypisz strukturę plików.
Etap 5: Dopiero potem zaproponuj kod.
Etap 6: Wykonaj audyt UI, wydajności i bezpieczeństwa.
Etap 7: Przygotuj raport końcowy.
```

---

## Audyt po implementacji

Po każdej implementacji sprawdź:

- czy panel ładuje się w Back Office,
- czy HTML nie jest rozsypany,
- czy filtry działają,
- czy sortowanie działa,
- czy paginacja działa,
- czy akcje nie wykonują DPD API,
- czy CSS/JS ładuje się tylko w tym widoku,
- czy nie ma błędów PHP,
- czy nie ma błędów JS,
- czy brak danych nie powoduje błędu krytycznego.

---

## Wynik końcowy pracy ze skillem

Codex powinien zwrócić:

- opis przyjętej architektury,
- listę plików do utworzenia lub zmiany,
- kod albo plan kodu,
- checklistę testów,
- raport ryzyk,
- decyzję, czy można przejść do implementacji.
