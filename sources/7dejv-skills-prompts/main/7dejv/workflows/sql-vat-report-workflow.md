# SQL VAT report workflow

## Kiedy uzywac

Dla raportow VAT, sprzedazy, kosztow, zamowien, faktur i danych magazynowych.

## Wejscie

Opis raportu, zakres dat, waluta, stawki VAT, statusy zamowien, dostep do schematu lub dump struktury.

## Skille

`sql-database-assistant`, `database-designer`, `database-schema-designer`, `performance-profiler`.

## Procedury agentow

`cs-backend-engineer`; `cs-commercial-orchestrator` przy marzy.

## Kroki

1. Pokaz SELECT diagnostyczne dla tabel i kolumn.
2. Potwierdz prefix i statusy.
3. Zbuduj raport SELECT bez modyfikacji danych.
4. Dodaj walidacje sum kontrolnych.
5. Opisz ryzyka ksiegowe i techniczne.

## Weryfikacja

Porownaj liczbe zamowien, brutto/netto/VAT, korekty, anulacje i probke rekordow.

## Ryzyka

Zly status, zwroty, rabaty, wiele stawek VAT, duplikaty faktur.

## Output

Zapytanie SQL, opis kolumn, diagnostyka, instrukcja sprawdzenia wyniku.

