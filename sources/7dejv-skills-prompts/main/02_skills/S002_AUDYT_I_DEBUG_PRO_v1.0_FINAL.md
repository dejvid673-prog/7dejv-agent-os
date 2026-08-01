# S002 — Audyt i Debug PRO v1.0 FINAL

## 1. Numer skilla

**S002**

---

## 2. Nazwa i wersja

**Audyt i Debug PRO v1.0 FINAL**

**Status:** FINAL  
**Standard nadrzędny:** S000 — Standard Budowy Skilli  
**Powiązania:** S001, S003, S004, S005, S008  
**Zasada nadrzędna:** najpierw minimalna diagnoza i minimalna poprawka, dopiero później przebudowa.

---

## 3. Jasny cel

S002 służy do audytu, diagnozowania i naprawiania błędów w sposób kontrolowany, minimalny i bezpieczny.

S002 ma odpowiedzieć:

1. Co jest zepsute?
2. Dlaczego jest zepsute?
3. Jaka jest najmniejsza bezpieczna poprawka?
4. Czego nie wolno ruszać?
5. Jak sprawdzić, czy poprawka zadziałała?
6. Czy po poprawce trzeba uruchomić S003?

Najkrótsza definicja:

> **S002 = skill diagnozy i minimalnej naprawy błędu.**

S002 nie ma robić wielkiej przebudowy, jeśli problem da się naprawić mniejszym zakresem.

---

## 4. Kiedy używać

Używaj S002, gdy:

- coś nie działa,
- pojawia się błąd techniczny,
- wynik AI jest podejrzany,
- moduł PrestaShop ma problem,
- ZIP ma złą strukturę,
- prompt działa źle albo za szeroko,
- Codex/Replit wykonał zmianę, ale efekt jest niejasny,
- trzeba znaleźć przyczynę błędu,
- trzeba ustalić minimalną poprawkę,
- trzeba przygotować raport dla Codex/Replit,
- trzeba wykonać test regresji po naprawie.

Typowe komendy:

```txt
S002: znajdź przyczynę błędu.
S002: wykonaj audyt tego wyniku.
S002: przygotuj minimalną poprawkę.
S002+: audyt + debug + test regresji + przekazanie do S003.
```

---

## 5. Kiedy nie używać

Nie używaj S002, gdy:

- moduł ma dopiero powstać od zera — użyj S001,
- trzeba tylko odebrać jakość wyniku — użyj S003,
- trzeba napisać dokumentację — użyj S004,
- trzeba napisać prompt dla Codex/Replit od zera — użyj S005,
- trzeba tylko spakować ZIP — użyj S008,
- użytkownik chce luźną opinię bez debugowania,
- brakuje jakiegokolwiek materiału do analizy.

---

## 6. Dane wejściowe

S002 może przyjąć:

- opis błędu,
- komunikat błędu,
- screen,
- log,
- plik,
- kod,
- ZIP,
- strukturę katalogów,
- wynik Codex/Replit,
- prompt,
- README,
- raport testu,
- informację, co działało wcześniej,
- informację, czego nie wolno ruszać.

Minimalne dane wejściowe:

```txt
Co nie działa?
Jaki był oczekiwany efekt?
Co zostało ostatnio zmienione?
Czego nie wolno ruszać?
```

Jeżeli dane są niepełne, S002 wykonuje diagnozę częściową i jasno oznacza ryzyka.

---

## 7. Dane wyjściowe

S002 zwraca:

- diagnozę błędu,
- prawdopodobną przyczynę,
- poziom ryzyka,
- listę rzeczy, których nie wolno ruszać,
- minimalną poprawkę,
- listę plików do zmiany,
- listę plików zakazanych,
- test po poprawce,
- test regresji,
- decyzję, czy uruchomić S003,
- ocenę 1–10,
- etap prac w procentach,
- następny krok.

---

## 8. Tryby pracy

### 8.1. S002 MINI

Szybka diagnoza bez pełnego raportu.

Format:

```txt
Najbardziej prawdopodobna przyczyna:
Minimalna poprawka:
Czego nie ruszać:
Pierwszy test po poprawce:
Czy uruchomić S003: TAK/NIE
```

### 8.2. S002 STANDARD

Normalny audyt i debug.

Format:

```txt
Materiał:
Błąd:
Cel:
Diagnoza:
Przyczyna:
Minimalna poprawka:
Pliki do zmiany:
Nie ruszać:
Test po poprawce:
Test regresji:
Decyzja:
```

### 8.3. S002+

Pełny tryb dla ważnych lub ryzykownych błędów.

S002+ oznacza:

```txt
S002 + S003 + właściwy skill pomocniczy
```

Przykłady:

```txt
Błąd modułu PrestaShop = S002 + S003 + S008
Błąd ZIP = S002 + S003 + S008
Błąd promptu = S002 + S003 + S005
Błąd dokumentacji = S002 + S003 + S004
Błąd skilla = S000 + S002 + S003
```

---

## 9. Etapy działania

### Etap 1 — Zatrzymaj rozrost pracy

Nie zaczynaj od przebudowy.

Najpierw ustal:

```txt
Co dokładnie nie działa?
Czy problem jest jeden, czy jest ich kilka?
Co działa poprawnie i ma zostać nienaruszone?
Jaki jest minimalny zakres analizy?
```

### Etap 2 — Ustal kontekst

Zbierz:

```txt
Cel pierwotny:
Aktualny błąd:
Ostatnia zmiana:
Środowisko:
Pliki podejrzane:
Pliki zakazane:
Dane wrażliwe:
```

### Etap 3 — Klasyfikuj błąd

Użyj poziomów:

| Poziom | Nazwa | Znaczenie |
|---|---|---|
| P0 | Blokujący | Nie da się użyć wyniku |
| P1 | Krytyczny | Może coś zepsuć albo naruszyć bezpieczeństwo |
| P2 | Wysoki | Działa częściowo, ale wymaga poprawki |
| P3 | Średni | Obniża jakość, ale nie blokuje pracy |
| P4 | Niski | Kosmetyka, format, literówki |

### Etap 4 — Wskaż przyczynę

Nie pisz ogólnie „może być problem”.

Podaj:

```txt
Najbardziej prawdopodobna przyczyna:
Dlaczego:
Dowód / przesłanka:
Czego jeszcze nie wiadomo:
```

### Etap 5 — Zaproponuj minimalną poprawkę

Najpierw najmniejsza bezpieczna zmiana.

Format:

```txt
Minimalna poprawka:
Pliki do zmiany:
Pliki bez zmian:
Ryzyko poprawki:
Rollback:
```

### Etap 6 — Test po poprawce

Każda poprawka musi mieć test.

Format:

```txt
Test 1 — czy błąd zniknął:
Test 2 — czy główna funkcja działa:
Test 3 — czy nie ma nowego błędu:
```

### Etap 7 — Test regresji

Sprawdź, czy poprawka nie zepsuła wcześniejszego działania.

Format:

```txt
Co działało przed poprawką:
Co trzeba sprawdzić ponownie:
Jak rozpoznać regresję:
```

### Etap 8 — Przekaż do S003

Po ważnej poprawce S002 nie powinien sam oznaczać pracy jako finalnej.

Użyj:

```txt
S003: sprawdź poprawkę po S002 i wykonaj test regresji.
```

---

## 10. Zasady jakości

S002 musi:

- diagnozować konkretny błąd,
- szukać minimalnej poprawki,
- nie przebudowywać całego projektu bez potrzeby,
- podawać listę „nie ruszać”,
- oddzielać fakty od przypuszczeń,
- wskazywać poziom ryzyka,
- kończyć się testem po poprawce,
- kończyć się decyzją, czy uruchomić S003,
- nie zawyżać oceny,
- nie uznawać poprawki za finalną bez QA.

Główna zasada jakości:

> **Naprawiaj najmniejszy bezpieczny zakres.**

---

## 11. Zasady bezpieczeństwa

S002 musi pilnować, żeby:

- nie modyfikować produkcji bez zgody,
- nie usuwać danych bez backupu,
- nie logować haseł, tokenów ani danych API,
- nie modyfikować core PrestaShop bez wyraźnej decyzji,
- nie robić override bez potrzeby,
- nie ruszać checkoutu, płatności, carrierów ani API, jeśli nie są częścią aktualnego zakresu,
- nie przenosić ograniczeń historycznych jako zasad globalnych,
- nie wykonywać zmian nieodwracalnych bez planu rollbacku.

Ważne:

> Zasada „nie ruszać API” może dotyczyć jednego konkretnego modułu, np. DPD, ale nie jest globalną zasadą dla każdego projektu.

---

## 12. Kontrola błędów

### 12.1. Brak danych

Jeśli brakuje danych, S002 zwraca:

```txt
Diagnoza: częściowa
Czego brakuje:
Co można ocenić:
Ryzyko:
Następny krok:
```

### 12.2. Brak pliku / brak kodu

Jeśli użytkownik pyta o konkretny błąd, ale nie ma kodu/logu:

```txt
Nie można wykonać pełnego debugowania.
Możliwa jest tylko diagnoza kierunkowa.
Do pełnej diagnozy potrzebne:
- komunikat błędu,
- plik / fragment kodu,
- opis ostatniej zmiany,
- oczekiwany efekt.
```

### 12.3. Błąd krytyczny

Jeśli błąd jest P0/P1:

```txt
Zatrzymaj dalsze dodawanie funkcji.
Wykonaj backup.
Napraw minimalny zakres.
Uruchom test regresji.
Przekaż do S003.
```

---

## 13. Format wyniku

### 13.1. Raport S002 STANDARD

```txt
# RAPORT S002 — AUDYT I DEBUG

Materiał:
Cel:
Błąd:
Tryb: MINI / STANDARD / PLUS

## Diagnoza
Najbardziej prawdopodobna przyczyna:
Dowód / przesłanka:
Czego nie wiadomo:

## Ryzyko
Poziom błędu: P0/P1/P2/P3/P4
Skutek:

## Minimalna poprawka
Co zmienić:
Pliki do zmiany:
Pliki bez zmian:
Czego nie ruszać:

## Test po poprawce
-

## Test regresji
-

## Decyzja
Czy poprawiać teraz: TAK/NIE
Czy uruchomić S003: TAK/NIE
Kto powinien poprawić: ChatGPT / Codex / Replit / użytkownik

## Etap prac
...%

## Ocena pracy
.../10

## Co poprawić w następnym kroku
-
```

---

## 14. Test końcowy

S002 uznaj za poprawnie użyty, jeśli raport zawiera:

```txt
Diagnozę błędu
Najbardziej prawdopodobną przyczynę
Poziom błędu P0–P4
Minimalną poprawkę
Listę czego nie ruszać
Test po poprawce
Test regresji
Decyzję, czy uruchomić S003
Etap prac w %
Ocenę pracy /10
Co poprawić w następnym kroku
```

Jeśli brakuje testu po poprawce albo listy „nie ruszać”, raport S002 jest niepełny.

---

## 15. Ocena 1–10

**Ocena S002 v1.0 FINAL: 9.4/10**

Uzasadnienie:

- ma jasną rolę,
- dobrze oddziela debug od budowania i QA,
- wymusza minimalną poprawkę,
- wymusza listę „nie ruszać”,
- wymusza test po poprawce,
- wymusza test regresji,
- przekazuje finalne QA do S003,
- pasuje do S000,
- pasuje do pracy z Codex/Replit i PrestaShop.

Nie otrzymuje 10/10, bo wymaga dalszego testowania na realnych błędach modułów PrestaShop i wynikach Codex/Replit.

---

## 16. Historia zmian

### v0.1

Założenie roli S002 jako skilla audytu i debugowania.

### v0.5

Doprecyzowanie współpracy z S001 i S003.

### v0.8

Dodanie minimalnej poprawki, listy „nie ruszać” i testu regresji.

### v1.0 FINAL

Finalizacja skilla zgodnie z S000.

Dodano:

- tryby MINI / STANDARD / S002+,
- klasyfikację błędów P0–P4,
- pełny format raportu debugowania,
- obowiązkową listę „czego nie ruszać”,
- obowiązkowy test po poprawce,
- obowiązkowy test regresji,
- przekazanie do S003 po istotnej poprawce,
- finalną ocenę 9.4/10.

---

## 17. Metryka końcowa po użyciu S002

Po każdej pracy z użyciem S002 podaj:

```txt
Etap prac: ...%
Ocena pracy: .../10
Status: DIAGNOZA / POPRAWKA / TEST / PRZEKAZANE DO S003
Największy problem: ...
Co poprawić w następnym kroku: ...
Czy uruchomić S003: TAK/NIE
```

---

## 18. Finalna decyzja dla wersji v1.0

**Decyzja QA:** PASS  
**Status:** FINAL  
**Ocena:** 9.4/10  
**Czy można używać:** TAK  
**Czy można dodać do katalogu 7DEJV OS:** TAK  
**Czy wymaga dalszych prac przed użyciem:** NIE  
**Co poprawić w przyszłości:** przetestować na realnych błędach PrestaShop, ZIP-ach, promptach Codex/Replit i wynikach pracy AI.
