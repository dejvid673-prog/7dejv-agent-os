# Workflow weryfikacji preparatow — STAW EXPERT

## Cel

Ten workflow okresla, jak zamieniac pomysl preparatu z researchu w kandydata produktu.

## Etapy

1. Wpisac preparat do katalogu roboczego.
2. Nadac status GREEN / YELLOW / RED.
3. Oddzielic fakty od zalozen.
4. Oznaczyc wszystkie liczby jako robocze, dopoki nie ma zrodel.
5. Sprawdzic fundament naukowy.
6. Sprawdzic dokumentacje produktu.
7. Sprawdzic jezyk deklaracji.
8. Przygotowac etykiete robocza.
9. Policzyc cene i logistyke.
10. Zamknac release gate.

## Zasady przejscia

| Z obecnego statusu | Do nowego statusu | Warunek |
|---|---|---|
| RED | YELLOW | specjalista uzna, ze temat mozna badac dalej |
| YELLOW | GREEN | sa zrodla, bezpieczny jezyk i dokumentacja |
| GREEN | produkt roboczy | wypelniony brief, etykieta, cena i release gate |

## Blokady

- Produkt ma opis wysokiego ryzyka.
- Produkt wymaga dokumentow, ktorych nie ma.
- Etykieta obiecuje wiecej niz zrodla.
- Liczby pochodza tylko z materialu roboczego.
- Brak planu pakowania i wysylki.

## Pierwszy test

Najpierw testowac na `Pond Volume & Dose Tool`, pozniej na produkcie KH/alkalicznosc. Produkty RED nie ida do testu sprzedazowego.
