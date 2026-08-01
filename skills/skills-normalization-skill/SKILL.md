---
name: skills-normalization-skill
description: Normalizuje i porzadkuje skills, agents i workflows do jednej struktury source-of-truth.
---

# skills-normalization-skill

## Kiedy uzywac

Uzyj, gdy trzeba:

- uporzadkowac duplikaty
- wyznaczyc wersje kanoniczne
- przygotowac migracje do repo centralnego

## Wejscie

- raport inwentaryzacyjny
- kandydaci na wersje kanoniczne
- obecna struktura repo centralnego

## Kroki

1. Grupuj artefakty po funkcji i zrodle, nie po samej nazwie.
2. Oddziel `canonical`, `reference`, `duplicate`, `unclear`.
3. Zaproponuj docelowa sciezke w repo centralnym.
4. Wypisz konflikty i braki metadanych.
5. Przygotuj liste do migracji albo cleanup.

## Wyjscie

- mapa normalizacji
- propozycja migracji
- lista konfliktow wymagajacych decyzji
