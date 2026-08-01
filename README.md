# 7dejv-agent-os

Centralne repozytorium 7DEJV dla:

- agents
- skills
- workflows
- prompts
- inventory

To repo ma byc kanonicznym source of truth dla artefaktow agentowych. Stare repo pozostaja na etapie migracji jako zrodla referencyjne, dopoki nie zostanie zakonczone porownanie i cleanup.

## Tryb pracy

Priorytetem jest GitHub jako zrodlo prawdy:

1. Najpierw sprawdzaj repo online.
2. Lokalne klony traktuj pomocniczo do porownan, backupu i szybszej pracy.
3. Decyzje porzadkowe zapisuj tutaj, nawet jesli material zrodlowy pochodzi z innych repo.

## Struktura

- `agents/` - definicje agentow w Markdown
- `skills/` - natywne skille i procedury z `SKILL.md`
- `workflows/` - przeplywy pracy i procedury migracyjne
- `prompts/` - prompty robocze i szablony analizy
- `docs/inventory/` - raporty inwentaryzacyjne
- `docs/decisions/` - decyzje porzadkowe i migracyjne
- `scripts/` - pomocnicze skrypty do audytu i migracji
- `inventory/` - dane robocze, mapy i indeksy

## Zasady

1. Nowe artefakty agentowe trafiaja tutaj, a nie do rozproszonych repo.
2. Kazdy artefakt powinien miec status:
   - `canonical`
   - `reference`
   - `duplicate`
   - `unclear`
3. Przed usunieciem duplikatow najpierw musi istniec:
   - wersja kanoniczna,
   - dowod zrodla,
   - mapa migracji,
   - osobna decyzja cleanup.
4. Repo produktowe moga zawierac jedynie lokalne stuby, dokumentacje uzycia albo wskazanie do wersji kanonicznej.

## Start

Na poczatku aktywne sa dwa glowne byty robocze:

- `agents/skills-inventory-agent.md`
- `agents/skills-organizer-agent.md`

oraz dwa odpowiadajace im skille:

- `skills/repository-inventory-skill/`
- `skills/skills-normalization-skill/`

## Status

Ten repozytorium jest przygotowane jako baza centralna. Migracja z dotychczasowych repo nie zostala jeszcze zakonczona.
