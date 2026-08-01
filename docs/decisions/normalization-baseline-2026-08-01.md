# Normalization Baseline - 2026-08-01

## Decyzja

1. `sources/` jest archiwum `reference`, nie katalogiem aktywnych definicji.
2. Nie promowano automatycznie zadnego pliku z archiwum do `agents/`, `skills/`, `workflows/` ani `prompts/`.
3. Wlasne definicje istniejace w katalogach glownych pozostaja jedynymi elementami `canonical` na tym etapie.
4. Brak identycznych SHA w archiwum, wiec nie oznaczono zadnego pliku jako `duplicate`.
5. Definicje o niejasnej roli pozostaja poza katalogiem pierwszej klasy i wymagaja przegladu tresci.

## Kryteria promocji

- jednoznaczna rola, wejscie i wyjscie;
- brak konfliktu funkcjonalnego z wersja kanoniczna;
- dowod pochodzenia i konkretna wersja zrodla;
- reczna decyzja `canonical` lub zatwierdzony raport normalizacji.

## Nastepny etap

Przegladac katalog pierwszej klasy grupami: najpierw quality/security, potem PrestaShop i e-commerce, nastepnie STAW EXPERT oraz Airtable. Kazda promocja ma byc osobnym, odwracalnym commitem.