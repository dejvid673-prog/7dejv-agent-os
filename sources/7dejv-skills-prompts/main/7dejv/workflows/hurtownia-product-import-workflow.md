# Hurtownia product import workflow

## Kiedy uzywac

Dla importu produktow z hurtowni do PrestaShop, BaseLinker lub Allegro.

## Wejscie

Feed/XML/CSV/API, mapowanie kategorii, stany, ceny, VAT, zdjecia, SKU/EAN.

## Skille

`zero-hallucination-coder`, `sql-database-assistant`, `database-schema-designer`, `process-mapper`, `performance-profiler`.

## Procedury agentow

`cs-backend-engineer`, `cs-bizops-orchestrator`.

## Kroki

1. Sprawdz format danych i pola wymagane.
2. Zmapuj SKU, EAN, kategorie, VAT, ceny i stany.
3. Zaprojektuj import najpierw jako dry-run.
4. Dodaj walidacje duplikatow i brakow.
5. Dopiero po akceptacji wykonuj zapis.

## Weryfikacja

Porownaj liczbe rekordow, probke produktow, ceny, VAT, stany, zdjecia.

## Ryzyka

Nadpisanie cen, duplikaty SKU, bledny VAT, brak rollbacku.

## Output

Plan importu, mapowanie pol, dry-run report, checklist produkcyjna.

