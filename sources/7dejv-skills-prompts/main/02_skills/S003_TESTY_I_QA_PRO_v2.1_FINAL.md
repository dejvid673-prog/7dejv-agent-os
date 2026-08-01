# S003 — Testy i QA PRO v2.1 FINAL

## 1. Numer skilla

**S003**

---

## 2. Nazwa i wersja

**Testy i QA PRO v2.1 FINAL**

**Status:** FINAL  
**Standard nadrzędny:** S000 — Standard Budowy Skilli  
**Zasada nadrzędna:** MVP najpierw, PRO później

---

## 3. Jasny cel

S003 służy do szybkiego i praktycznego sprawdzania, czy wynik pracy faktycznie działa, spełnia cel i może zostać użyty dalej.

S003 ma dawać jasną decyzję:

- **PASS** — działa i można używać dalej,
- **WARNING** — działa częściowo, ale wymaga poprawek,
- **FAIL** — nie spełnia celu albo ma błąd krytyczny,
- **BLOCKED** — nie da się wykonać testu z powodu braku danych, pliku, dostępu albo celu.

Najkrótsza definicja:

> **S003 = skill odbioru jakości.**

S003 ma odpowiedzieć:

1. Czy to działa?
2. Czy spełnia cel?
3. Co jest zepsute albo ryzykowne?
4. Czy można tego użyć, wysłać do Codex/Replit albo zapisać do katalogu?
5. Co poprawić jako pierwsze?

---

## 4. Kiedy używać

Używaj S003, gdy trzeba sprawdzić:

- moduł PrestaShop,
- ZIP modułu,
- wynik pracy Codex/Replit,
- prompt dla AI,
- skill SXXX,
- dokumentację,
- grafikę produktową,
- opis produktu,
- poprawkę po debugowaniu,
- makietę HTML,
- instrukcję techniczną,
- wynik pracy innego skilla.

Typowe komendy:

```txt
S003: sprawdź ten wynik.
S003 MINI: oceń szybko, czy to działa.
S003 STANDARD: wykonaj normalny test jakości.
S003+: wykonaj pełny test QA z właściwymi skillami pomocniczymi.
```

---

## 5. Kiedy nie używać

Nie używaj S003, gdy:

- trzeba dopiero stworzyć projekt od zera — użyj S001,
- trzeba znaleźć i naprawić błąd — użyj S002,
- trzeba napisać dokumentację — użyj S004,
- trzeba przygotować prompt dla Codex/Replit — użyj S005,
- trzeba spakować moduł ZIP — użyj S008,
- użytkownik chce tylko luźną opinię bez testu,
- nie ma żadnego materiału do sprawdzenia.

---

## 6. Dane wejściowe

S003 może przyjąć:

- plik,
- kod,
- ZIP,
- prompt,
- opis zadania,
- wynik pracy AI,
- screen,
- instrukcję,
- dokumentację,
- skill,
- listę wymagań,
- opis błędu,
- wynik testu wykonany przez użytkownika.

Minimalne dane wejściowe:

```txt
Co sprawdzamy?
Jaki był cel?
Co ma być wynikiem?
```

Jeżeli brakuje części danych, S003 nie blokuje pracy bez potrzeby. Wykonuje test częściowy i jasno oznacza, czego nie sprawdzono.

---

## 7. Dane wyjściowe

S003 zwraca:

- decyzję QA,
- ocenę 1–10,
- listę błędów,
- największy problem,
- pierwszy krok poprawy,
- informację, czy można iść dalej,
- informację, kto powinien poprawić wynik,
- etap prac w procentach,
- rekomendację następnego kroku.

---

## 8. Tryby pracy

### 8.1. S003 MINI

Szybki test bez pełnego raportu.

Używaj, gdy trzeba szybko ocenić wynik.

Format odpowiedzi:

```txt
Decyzja: PASS / WARNING / FAIL / BLOCKED
Ocena: .../10
Największy problem: ...
Pierwszy krok poprawy: ...
```

### 8.2. S003 STANDARD

Normalny test jakości.

Używaj, gdy wynik ma być oceniony przed dalszą pracą.

Format odpowiedzi:

```txt
Co sprawdzono:
Cel:
Wynik testu:
Błędy:
Ocena:
Decyzja:
Następny krok:
```

### 8.3. S003+

Pełny test z dodatkowymi skillami pomocniczymi.

Używaj, gdy materiał jest ważny, techniczny albo ma trafić do katalogu, GitHub, Codex/Replit albo PrestaShop.

Przykłady:

```txt
S003+ dla modułu = S001 + S002 + S003 + S008
S003+ dla błędu = S002 + S003
S003+ dla ZIP = S003 + S008
S003+ dla dokumentacji = S003 + S004
S003+ dla promptu = S003 + S005
S003+ dla skilla = S000 + S003
```

---

## 9. Etapy działania

### Etap 1 — Ustal, co testujesz

Określ:

```txt
Materiał:
Cel:
Oczekiwany wynik:
Zakres testu:
```

### Etap 2 — Test MVP

Sprawdź tylko najważniejsze rzeczy:

```txt
Czy wynik istnieje?
Czy odpowiada na cel?
Czy da się go użyć?
Czy nie ma błędu blokującego?
```

Jeżeli test MVP nie przechodzi, nie rób długiego QA. Zwróć **FAIL** albo **BLOCKED**.

### Etap 3 — Test funkcjonalny

Sprawdź:

```txt
Czy wynik robi to, co miał robić?
Czy nie pomija głównego celu?
Czy użytkownik może z niego skorzystać?
Czy kolejny krok jest jasny?
```

### Etap 4 — Test bezpieczeństwa

Sprawdź:

```txt
Czy wynik nie sugeruje ryzykownych działań?
Czy nie rusza rzeczy, których nie powinien?
Czy nie ujawnia haseł, tokenów, danych API?
Czy nie oznacza czegoś jako gotowe bez testu?
```

Dla PrestaShop dodatkowo:

```txt
Czy nie modyfikuje core?
Czy nie wymusza override bez potrzeby?
Czy nie uruchamia API automatycznie?
Czy nie zapisuje wrażliwych danych w logach?
Czy nie psuje checkoutu, carrierów ani hooków?
```

### Etap 5 — Lista błędów

Każdy błąd zapisuj krótko:

```txt
[P0/P1/P2/P3/P4] Nazwa błędu
Opis:
Skutek:
Poprawka:
Kto poprawia:
```

### Etap 6 — Decyzja końcowa

Na końcu zawsze podaj:

```txt
Decyzja QA:
Ocena:
Czy można użyć dalej:
Kto powinien poprawić:
Następny krok:
```

---

## 10. Zasady jakości

S003 musi:

- dawać szybką decyzję,
- odróżniać fakt od przypuszczenia,
- nie zawyżać ocen,
- nie oznaczać pracy jako finalnej bez testu,
- wskazywać największy problem,
- podawać pierwszy krok poprawy,
- pilnować zasady MVP najpierw,
- nie produkować zbędnych plików,
- kończyć się metryką prac.

Główna zasada jakości:

> **Testuj, nie komplikuj.**

Najpierw odpowiedz:

```txt
Czy to można bezpiecznie użyć dalej?
```

Dopiero potem rozbudowuj raport.

---

## 11. Zasady bezpieczeństwa

S003 musi pilnować, żeby wynik:

- nie ukrywał ryzyk,
- nie modyfikował środowiska produkcyjnego bez zgody,
- nie ujawniał haseł, tokenów, danych API,
- nie sugerował pracy na produkcji, gdy bezpieczniejszy jest test lokalny,
- nie oznaczał nieprzetestowanej pracy jako gotowej,
- nie przenosił ograniczeń z jednego projektu jako globalnych zasad.

---

## 12. Kontrola błędów

### 12.1. Decyzje QA

| Decyzja | Znaczenie |
|---|---|
| PASS | Wynik działa i można go użyć dalej |
| WARNING | Wynik działa częściowo, ale wymaga poprawek |
| FAIL | Wynik nie spełnia celu albo ma błąd krytyczny |
| BLOCKED | Nie da się wykonać testu przez brak danych, pliku albo dostępu |

### 12.2. Matryca błędów P0–P4

| Poziom | Nazwa | Znaczenie | Decyzja |
|---|---|---|---|
| P0 | Blokujący | Nie da się użyć wyniku | FAIL / BLOCKED |
| P1 | Krytyczny | Wynik może coś zepsuć albo wprowadzić w błąd | FAIL |
| P2 | Wysoki | Działa częściowo, ale wymaga poprawki | WARNING / FAIL |
| P3 | Średni | Obniża jakość, ale nie blokuje pracy | WARNING |
| P4 | Niski | Kosmetyka, format, literówki | PASS / WARNING |

### 12.3. Brak danych

Jeśli brakuje danych, S003 nie udaje pełnego testu.

Wtedy zwraca:

```txt
Decyzja: BLOCKED
Powód: ...
Co trzeba dostarczyć: ...
Co można ocenić mimo braku danych: ...
```

Jeśli test jest częściowy, S003 musi napisać:

```txt
Test częściowy: TAK
Czego nie sprawdzono:
Ryzyko:
```

---

## 13. Format wyniku

### 13.1. Format S003 MINI

```txt
Decyzja: PASS / WARNING / FAIL / BLOCKED
Ocena: .../10
Największy problem: ...
Pierwszy krok poprawy: ...
```

### 13.2. Format S003 STANDARD

```txt
# RAPORT S003 — QA

Materiał:
Cel:
Zakres testu:
Tryb: MINI / STANDARD / PLUS

## Wynik
Decyzja QA:
Ocena:

## Co działa
-

## Błędy
-

## Największy problem
-

## Pierwszy krok poprawy
-

## Kto powinien poprawić
ChatGPT / Codex / Replit / użytkownik

## Czy można użyć dalej
TAK / NIE / OSTROŻNIE / NIE WIADOMO

## Etap prac
...%

## Co poprawić w następnym kroku
-
```

---

## 14. Checklisty szybkiego testu

### 14.1. Test skilla SXXX

Sprawdź:

```txt
Czy ma numer SXXX?
Czy ma nazwę i wersję?
Czy ma jasny cel?
Czy mówi, kiedy używać?
Czy mówi, kiedy nie używać?
Czy ma dane wejściowe?
Czy ma dane wyjściowe?
Czy ma tryby pracy?
Czy ma etapy działania?
Czy ma zasady jakości?
Czy ma zasady bezpieczeństwa?
Czy ma kontrolę błędów?
Czy ma format wyniku?
Czy ma test końcowy?
Czy ma ocenę 1–10?
Czy ma historię zmian?
Czy jest praktyczny?
Czy nie jest przegadany?
```

### 14.2. Test promptu

Sprawdź:

```txt
Czy prompt ma jasny cel?
Czy mówi, czego nie robić?
Czy ma dane wejściowe?
Czy ma dane wyjściowe?
Czy ogranicza zakres pracy?
Czy ma test końcowy?
Czy mówi, jaki ma być format wyniku?
Czy nie jest za szeroki?
Czy nie pozwala AI na niepotrzebne zmiany?
```

### 14.3. Test wyniku Codex/Replit

Sprawdź:

```txt
Czy wynik odpowiada na zadanie?
Czy zmieniono tylko potrzebne pliki?
Czy nie dodano niepotrzebnych funkcji?
Czy są testy albo instrukcja testu?
Czy wynik da się uruchomić?
Czy są widoczne ryzyka?
Czy AI nie zadeklarowało testów bez dowodów?
Czy kolejny krok jest jasny?
```

### 14.4. Test ZIP PrestaShop

Sprawdź:

```txt
Czy ZIP ma poprawny folder główny modułu?
Czy główny plik modułu jest w dobrym miejscu?
Czy nie ma zbędnych folderów typu .git, node_modules, __MACOSX?
Czy są pliki index.php zabezpieczające katalogi?
Czy struktura jest zgodna z PrestaShop?
Czy moduł nie wymaga zmian w core?
Czy można go bezpiecznie testować lokalnie?
```

### 14.5. Test dokumentacji

Sprawdź:

```txt
Czy instrukcja mówi, co zrobić krok po kroku?
Czy użytkownik wie, gdzie kliknąć albo co uruchomić?
Czy są wymagania?
Czy są ograniczenia?
Czy jest test końcowy?
Czy dokumentacja pasuje do aktualnej wersji?
Czy nie obiecuje czegoś, czego nie sprawdzono?
```

---

## 15. Test końcowy

S003 uznaj za poprawnie użyty, jeśli odpowiedź zawiera:

```txt
Decyzję QA
Ocenę 1–10
Największy problem
Pierwszy krok poprawy
Informację, czy można użyć dalej
Etap prac w %
Co poprawić w następnym kroku
```

Jeśli którejś z tych rzeczy brakuje, raport S003 jest niepełny.

---

## 16. Ocena 1–10

**Ocena S003 v2.1 FINAL: 9.5/10**

Uzasadnienie:

- skill jest praktyczny,
- ma jasne tryby MINI / STANDARD / S003+,
- nie jest przeciążony teorią,
- daje decyzję PASS / WARNING / FAIL / BLOCKED,
- pasuje do S000,
- ogranicza zbędne pliki,
- pilnuje MVP-first,
- przeszedł autotest,
- przeszedł test bojowy na S001,
- przeszedł test bojowy na S002,
- ma jasny format raportu,
- ma matrycę błędów P0–P4.

Nie otrzymuje 10/10, bo 10/10 wymaga długotrwałego użycia w realnych projektach, np. przy ZIP-ach modułów PrestaShop, promptach Codex/Replit i wynikach pracy AI.

---

## 17. Historia zmian

### v1.0

Pierwsza wersja robocza. Zbyt szybko uznana za mocną.

### v1.1

Dodano checklisty i tryby QA.

### v1.2

Dodano przykłady raportów i połączenia z innymi skillami.

### v1.3

Dodano test bojowy, procedurę publikacji i zasady plików `.md`.

### v1.4

Dodano matrycę błędów, S003 MINI i S003+.

### v2.0 MVP-FIRST

Odchudzono skill. Ustawiono praktyczny kierunek:

```txt
testuj → oceń → wskaż błąd → podaj następny krok
```

### v2.1 CANDIDATE

Dodano:

- wyniki autotestu,
- wyniki testu na S001,
- wyniki testu na S002,
- zasadę braku statusu FINAL po teście częściowym,
- tabelę granic odpowiedzialności,
- warunek przejścia do FINAL.

### v2.1 FINAL

Zmieniono status z CANDIDATE na FINAL po uporządkowaniu skilla, wykonaniu kontroli zgodności z S000 i potwierdzeniu, że S003 spełnia rolę roboczego odbioru jakości.

Dodano:

- finalną ocenę 9.5/10,
- zasadę cofnięcia do CANDIDATE przy wykryciu błędu krytycznego,
- decyzję, że S003 jest obowiązującym standardem QA w katalogu 7DEJV OS.

---

## 18. Metryka końcowa po użyciu S003

Po każdej pracy z użyciem S003 podaj:

```txt
Etap prac: ...%
Ocena pracy: .../10
Status: DRAFT / CHECKPOINT / CANDIDATE / FINAL
Największy problem: ...
Co poprawić w następnym kroku: ...
Czy tworzyć plik .md: TAK / NIE
```

---

## 19. Finalna decyzja dla wersji v2.1

**Decyzja QA:** PASS  
**Status:** FINAL  
**Ocena:** 9.5/10  
**Czy można używać:** TAK  
**Czy można dodać do katalogu 7DEJV OS:** TAK  
**Czy wymaga dalszych prac przed użyciem:** NIE  
**Co poprawić w przyszłości:** testować S003 na realnych ZIP-ach PrestaShop, promptach Codex/Replit i wynikach pracy AI.
