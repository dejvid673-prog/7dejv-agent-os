# Prompt dla Codex — audyt dpdshipmvp

## Zadanie

Przeskanuj i popraw moduł PrestaShop 9:

`dpdshipmvp`

## Cel modułu

Moduł ma odpowiadać wyłącznie za DPD:

- nadawanie przesyłek,
- komunikację z API DPD,
- zapis FID,
- etykiety,
- tracking,
- integrację z zamówieniem.

## Tryb pracy

Działaj etapami. Po każdym etapie wykonaj audyt i popraw błędy.

Nie przepisuj całego modułu bez powodu. Najpierw znajdź przyczynę problemu.

## Środowisko

- PrestaShop 9.1.1
- PHP 8.4.x
- MariaDB
- Back Office

## Zakres audytu

1. Struktura modułu.
2. Plik główny modułu.
3. Kontrolery.
4. Hooki Back Office.
5. Widok panelu w zamówieniu.
6. Obsługa konfiguracji.
7. Bezpieczeństwo danych API.
8. Zapis FID.
9. Generowanie i pobieranie etykiet.
10. Tracking.

## Ważne hooki do sprawdzenia

- `displayAdminOrderMain`
- `displayAdminOrderSide`
- `displayAdminOrderSideBottom`
- `displayAdminOrder`
- `displayAdminOrderTop`
- `displayAdminOrderTabContent`

## Zasada rozdzielenia

Nie dodawaj do `dpdshipmvp` funkcji głównej listy zamówień. Do tego służy osobny moduł `orderpanelmvp`.

## Raport końcowy

Raport ma zawierać:

- wykryte błędy,
- naprawione błędy,
- zmienione pliki,
- ryzyka,
- instrukcję testowania,
- listę rzeczy do dalszego rozwoju.
