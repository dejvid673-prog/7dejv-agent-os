---
name: repository-inventory-skill
description: Wyszukuje w repozytoriach artefakty agentowe i przygotowuje raport inwentaryzacyjny z dowodami.
---

# repository-inventory-skill

## Kiedy uzywac

Uzyj, gdy trzeba:

- znalezc skills, agents, workflows i prompty
- porownac wiele repo pod katem artefaktow agentowych
- przygotowac raport do migracji

## Wejscie

- lista repo do analizy
- frazy wyszukiwania
- foldery wykluczone

## Kroki

1. Znajdz kandydatow po nazwach katalogow i plikow.
2. Zawęz liste po tresci tylko do relewantnych plikow.
3. Zbierz krotki dowod tekstowy.
4. Nadaj typ i poziom pewnosci.
5. Zapisz wynik do raportu tabelarycznego.

## Wyjscie

- tabela inwentaryzacyjna
- lista katalogow projektowych
- wstepny podzial na aktywne, dokumentacyjne i pomocnicze
