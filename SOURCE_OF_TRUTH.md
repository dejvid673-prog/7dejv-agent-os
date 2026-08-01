# Source Of Truth

Repozytorium `7dejv-agent-os` jest kanonicznym zrodlem prawdy dla:

- `agents`
- `skills`
- `workflows`
- `prompts`
- inwentaryzacji artefaktow agentowych

## Online First

1. GitHub jest nadrzednym zrodlem prawdy dla repo 7DEJV.
2. Lokalne kopie nie zmieniaja klasyfikacji repo bez potwierdzenia stanu online.
3. Inwentaryzacja i routing zaczynaja sie od listy repo online.

## Zasady

1. Wersja kanoniczna artefaktu agentowego ma mieszkac tutaj.
2. Stare repo moga pozostac jako zrodla migracji, referencje albo stuby zgodnosci.
3. Duplikaty nie sa usuwane automatycznie. Najpierw trzeba je oznaczyc i porownac.
4. Kazda migracja powinna zostawic slad w:
   - `docs/inventory/`
   - `docs/decisions/`
   - `inventory/`

## Kategorie statusu

- `canonical` - jedyna wersja referencyjna
- `reference` - material pomocniczy lub historyczny
- `duplicate` - duplikat wersji kanonicznej
- `unclear` - wymaga decyzji

## Biezace zrodla migracji

- `G:\repo 7dejv.os\inne\7dejv-skills-prompts`
- `G:\repo 7dejv.os\inne\7dejv-ai-command-center`
- `G:\repo 7dejv.os\inne\7dejv.os`
- `G:\repo 7dejv.os\inne\7dejv-staw-expert`
- `G:\airtable-agent`
