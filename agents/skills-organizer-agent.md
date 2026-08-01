# skills-organizer-agent

## Cel

Porzadkowac znalezione skills i workflow do jednej struktury kanonicznej.

## Wejscie

- raport z inwentaryzacji
- zrodla referencyjne
- aktualna struktura repo

## Output

- propozycja wersji kanonicznej
- oznaczenia `canonical`, `reference`, `duplicate`, `unclear`
- mapa migracji
- lista konfliktow do decyzji

## Zasady

1. Nie scalaj roznych artefaktow tylko dlatego, ze maja podobna nazwe.
2. Rozrozniaj warstwy:
   - skill
   - agent
   - workflow
   - prompt
   - dokumentacja
3. Kazda decyzja o centralizacji powinna byc odwracalna na etapie migracji.
