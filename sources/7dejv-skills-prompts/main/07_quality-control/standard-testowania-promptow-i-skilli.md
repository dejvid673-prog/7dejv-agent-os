# Standard testowania promptów i skilli — 7DEJV

## Cel

Ustalić prosty standard, który mówi, kiedy prompt albo skill jest gotowy do użycia, a kiedy jest tylko wersją roboczą.

## Statusy

### `roboczy`

Materiał istnieje, ale nie był jeszcze użyty w realnym zadaniu.

### `do testu`

Materiał jest gotowy do pierwszego testu, ale nie wolno traktować go jako finalnego.

### `przetestowany`

Materiał przeszedł test i dał wynik użyteczny.

### `do poprawy`

Materiał działa częściowo, ale ma błędy, braki albo powoduje zbyt chaotyczny wynik.

### `archiwalny`

Materiał jest stary, zastąpiony albo ryzykowny.

## Minimalny test promptu

1. Sprawdź, czy cel jest jasny.
2. Sprawdź, czy prompt nie miesza kilku niezależnych zadań.
3. Uruchom prompt na przykładowych danych.
4. Oceń wynik.
5. Wypisz błędy.
6. Popraw prompt.
7. Uruchom ponownie.
8. Zapisz wersję i datę testu.

## Minimalny test skilla

1. Sprawdź cel skilla.
2. Sprawdź dane wejściowe.
3. Wykonaj test 1 — typowy przypadek.
4. Wykonaj test 2 — trudniejszy przypadek.
5. Wykonaj test 3 — przypadek z brakującymi danymi.
6. Oceń, czy skill zachowuje się stabilnie.
7. Popraw instrukcję.
8. Zapisz wersję.

## Kryteria jakości

Materiał jest dobry, jeżeli:

- daje powtarzalny wynik,
- ma jasny zakres,
- nie wymaga zgadywania,
- nie tworzy nadmiaru niepotrzebnych danych,
- ma czytelny format wyjściowy,
- nie miesza repozytoriów i odpowiedzialności,
- da się go użyć po czasie bez tłumaczenia od zera.

## Kryteria odrzucenia

Materiał trzeba poprawić albo zarchiwizować, jeżeli:

- generuje chaos,
- tworzy zbyt długie wyniki bez struktury,
- wymusza zbyt wiele danych wejściowych,
- prowadzi do działań niezgodnych z ustaleniami,
- miesza kod, dokumentację, badania i prompty w jednym miejscu,
- powoduje ryzyko pracy bez audytu.

## Zasada końcowa

Prompt lub skill bez testu nie jest narzędziem produkcyjnym. Jest tylko wersją roboczą.
