# S000 — STANDARD BUDOWY SKILLI 7DEJV OS
## v1.0 FINAL

**Numer skilla:** S000  
**Nazwa:** Standard Budowy Skilli 7DEJV OS  
**Wersja:** v1.0 FINAL  
**Typ:** skill nadrzędny / skill do pisania skilli  
**Status:** stabilny standard bazowy  
**Ocena jakości:** 9.75/10  

---

## 1. Definicja S000

**S000** to nadrzędny standard tworzenia, poprawiania, oceniania, testowania, wersjonowania i katalogowania wszystkich skilli w systemie **7DEJV OS**.

Najkrócej:

```text
S000 = skill do pisania skilli
```

Dokładniej:

```text
S000 = wzorzec konstrukcji, jakości, kontroli i utrzymania wszystkich kolejnych skilli.
```

S000 nie służy do bezpośredniego wykonywania zadań końcowych typu:

- napisanie modułu,
- debugowanie błędu,
- stworzenie grafiki,
- przygotowanie opisu produktu,
- napisanie dokumentacji.

S000 służy do tworzenia i kontrolowania skilli, które później wykonują takie zadania.

---

## 2. Cel S000

Celem S000 jest zapewnienie, że każdy skill w bazie 7DEJV OS:

- ma jasny cel,
- ma określony zakres,
- ma granice użycia,
- działa etapami,
- daje konkretny wynik,
- nie jest tylko teorią,
- nie wymusza zbędnych danych,
- nadaje się do pracy z ChatGPT, Codex, Replit, GitHub, VS Code, Dockerem i Laragonem,
- może być testowany,
- może być oceniany,
- może być rozwijany wersjami,
- może być zapisany jako plik `.md`,
- może być wywołany krótką komendą, np. `S001`, `S002+`, `S000 audyt S001`.

---

## 3. Główna zasada S000

**Skill ma pomagać działać, nie blokować pracę.**

Każdy skill ma być narzędziem roboczym, nie tylko długą instrukcją.

Obowiązuje zasada:

```text
MVP najpierw, PRO później.
```

Czyli:

1. najpierw powstaje wersja działająca,
2. potem jest test,
3. potem poprawki,
4. dopiero potem rozbudowa PRO.

Skill nie może powodować sytuacji, w której długo planujemy, ale nie powstaje żaden konkretny wynik.

---

## 4. Rola S000 w katalogu skilli

| Numer | Rola |
|---|---|
| **S000** | standard budowy wszystkich skilli |
| **S001** | budowa modułów / projektów od zera |
| **S002** | audyt, debugowanie i naprawa |
| **S003** | testy / QA / checklisty |
| **S004** | dokumentacja / instrukcje / raporty |
| **S005+** | kolejne skille specjalistyczne |

S000 stoi nad resztą. Każdy nowy skill powinien być zgodny ze standardem S000.

---

## 5. Kiedy używać S000

Używaj S000, gdy:

- tworzysz nowy skill,
- poprawiasz istniejący skill,
- oceniasz skill,
- robisz katalog skilli,
- ustalasz numerację,
- sprawdzasz jakość skilla,
- przygotowujesz skill do backupu,
- tworzysz wersję `.md`,
- chcesz podciągnąć skill do 9/10 albo 10/10,
- chcesz przygotować prompt dla Codex/Replit na podstawie skilla.

---

## 6. Kiedy NIE używać S000 jako głównego skilla

Nie używaj S000 jako głównego skilla, gdy zadanie dotyczy bezpośrednio:

- napisania modułu,
- naprawy błędu,
- stworzenia grafiki,
- napisania opisu produktu,
- wygenerowania kodu,
- wykonania szybkiej jednorazowej czynności.

Wtedy użyj konkretnego skilla, np.:

```text
S001 — budowa modułu
S002 — audyt/debug
S009 — grafiki produktowe
S010 — opisy produktów
```

S000 może wtedy działać pomocniczo jako kontrola jakości.

---

## 7. Numeracja skilli

Każdy skill musi mieć stały numer:

```text
S000
S001
S002
S003
...
```

### Zasady numeracji

1. Numer raz nadany zostaje.
2. Nie zmieniamy numeru przy poprawkach.
3. Poprawki oznaczamy wersją.
4. Nie tworzymy nazw typu `FINAL`, `NOWY`, `OSTATECZNY`.

Poprawnie:

```text
S001 — MODUŁ BUILDER PRO — v0.1
S001 — MODUŁ BUILDER PRO — v0.2
S001 — MODUŁ BUILDER PRO — v1.0
```

Błędnie:

```text
S001_FINAL
S001_NOWY
S001_OSTATECZNY_2
```

---

## 8. Format nazwy skilla

Każdy skill ma mieć format:

```text
SXXX — NAZWA SKILLA — vX.X
```

Przykłady:

```text
S000 — STANDARD BUDOWY SKILLI — v1.0
S001 — MODUŁ BUILDER PRO — v1.0
S002 — AUDYT I DEBUG PRO — v1.0
S003 — TESTY I QA PRO — v1.0
```

---

## 9. Wersjonowanie skilli

Każdy skill musi mieć wersję.

| Wersja | Znaczenie |
|---|---|
| **v0.1** | pierwszy szkic |
| **v0.2–v0.9** | wersje robocze |
| **v1.0 RC** | kandydat do wersji stabilnej |
| **v1.0** | pierwsza wersja stabilna |
| **v1.1** | mała poprawka |
| **v1.5** | większe ulepszenie |
| **v2.0** | duża przebudowa |

Nie nazywamy wersji roboczej finalną, jeśli nie przeszła testów jakości.

---

## 10. Obowiązkowa struktura każdego skilla

Każdy skill tworzony według S000 powinien mieć tę strukturę:

```text
# SXXX — NAZWA SKILLA — vX.X

## 1. Cel skilla
## 2. Rola skilla w systemie 7DEJV OS
## 3. Kiedy używać
## 4. Kiedy nie używać
## 5. Dane wejściowe wymagane
## 6. Dane opcjonalne
## 7. Dane wyjściowe
## 8. Tryby pracy
## 9. Etapy działania
## 10. Zasady jakości
## 11. Zasady bezpieczeństwa
## 12. Kontrola błędów
## 13. Format wyniku
## 14. Prompt dla Codex/Replit/wykonawcy AI
## 15. Test końcowy
## 16. Skala oceny
## 17. Historia zmian
```

Nie każdy skill musi być długi, ale każdy musi mieć te obszary logicznie ujęte.

---

## 11. Minimalna wersja nowego skilla

Jeżeli tworzymy nowy skill od zera, zaczynamy od wersji minimalnej:

```text
# SXXX — NAZWA SKILLA — v0.1

## 1. Cel
## 2. Kiedy używać
## 3. Kiedy nie używać
## 4. Dane wejściowe
## 5. Dane wyjściowe
## 6. Etapy pracy
## 7. Format wyniku
## 8. Test końcowy
## 9. Ocena jakości
```

Dopiero potem rozbudowujemy go do wersji PRO.

---

## 12. Dane wejściowe i wyjściowe

Każdy skill musi rozróżniać trzy grupy danych.

### Dane wejściowe wymagane

Czyli minimum potrzebne do pracy.

```text
- cel zadania,
- oczekiwany wynik,
- zakres pracy.
```

### Dane opcjonalne

Pomagają, ale nie blokują pracy.

```text
- pliki,
- screeny,
- kod,
- logi,
- repozytorium,
- wcześniejsze błędy,
- preferencje użytkownika.
```

### Dane wyjściowe

Czyli co skill ma zwrócić.

```text
- gotowy prompt,
- raport,
- kod,
- checklistę,
- dokumentację,
- plan pracy,
- poprawioną wersję,
- instrukcję,
- listę testów,
- paczkę ZIP.
```

Jeżeli nie wiadomo, co skill ma zwrócić, skill jest niedopracowany.

---

## 13. Tryby pracy skilla

Każdy większy skill powinien mieć tryby pracy.

| Tryb | Kiedy używać | Schemat |
|---|---|---|
| **Szybki** | proste zadania | Cel → szybka decyzja → wynik |
| **Standard** | domyślna praca | Cel → dane → plan → wykonanie → test → wynik |
| **PRO** | ważne projekty | Analiza → warianty → plan → wykonanie → audyt → poprawki → test → raport |
| **Naprawczy** | poprawa istniejącego materiału | Ocena → błędy → poprawki → nowa wersja → test → ocena końcowa |
| **Codex/Replit** | zadanie dla wykonawcy AI | Kontekst → zakres → pliki → zakazy → testy → oczekiwany wynik |

---

## 14. Etapy działania każdego skilla

Minimalny schemat działania:

```text
ETAP 1 — Rozpoznanie celu
ETAP 2 — Ustalenie zakresu
ETAP 3 — Zebranie danych
ETAP 4 — Wykonanie
ETAP 5 — Kontrola jakości
ETAP 6 — Test końcowy
ETAP 7 — Raport i następny krok
```

Skill ma prowadzić do wyniku, a nie tylko analizować.

---

## 15. Zasada „nie pytać bez potrzeby”

W pracy nad skillami obowiązuje zasada:

```text
Jeżeli można sensownie pracować na dostępnych danych, kontynuuj.
```

Nie blokuj pracy pytaniami, jeśli można przyjąć rozsądne założenia.

Jeżeli brakuje danych krytycznych:

1. nazwij brak,
2. przyjmij jawne założenie albo zadaj jedno krótkie pytanie,
3. nie rozbijaj pracy na zbędne konsultacje.

---

## 16. Zasada nieprzenoszenia ograniczeń historycznych

Nie wolno przenosić ograniczeń z jednego projektu jako zasad globalnych.

Przykład:

```text
Nie ruszać API.
```

To mogło być prawidłowe dla konkretnego modułu DPD, bo API było już dobrze zrobione.  
Ale dla nowego modułu od zera taka zasada może być błędna.

Każdy skill musi rozróżniać:

| Typ zasady | Znaczenie |
|---|---|
| **Globalna** | obowiązuje zawsze |
| **Projektowa** | obowiązuje tylko w danym projekcie |
| **Etapowa** | obowiązuje tylko na danym etapie |
| **Historyczna** | pochodzi ze starego przypadku i wymaga ponownej oceny |

---

## 17. Zasady jakości

Każdy skill musi spełniać minimum:

1. Ma jasny cel.
2. Ma określony zakres.
3. Ma granice.
4. Nie wymusza zbędnych danych.
5. Działa etapami.
6. Daje konkretny wynik.
7. Ma test końcowy.
8. Ma ocenę jakości.
9. Jest praktyczny.
10. Nie jest tylko teorią.
11. Nie miesza zadań.
12. Nie kopiuje zasad historycznych jako globalnych.
13. Nadaje się do ponownego użycia.
14. Może być rozwijany wersjami.
15. Ma sensowny stosunek długości do celu.

---

## 18. Zasady bezpieczeństwa

Każdy skill musi mieć zasady bezpieczeństwa dopasowane do swojej dziedziny.

### Dla kodu / PrestaShop

```text
- nie modyfikować core bez wyraźnej decyzji,
- nie usuwać danych bez backupu,
- nie logować haseł, tokenów ani danych wrażliwych,
- nie wykonywać automatycznych akcji bez zgody,
- nie rozszerzać zakresu bez potrzeby,
- pilnować instalowalności ZIP,
- wskazywać ryzyka techniczne.
```

### Dla dokumentacji

```text
- nie dopisywać faktów bez danych,
- oddzielać fakty od założeń,
- zachować ostrzeżenia,
- nie mieszać wersji.
```

### Dla grafik

```text
- nie fałszować danych produktu,
- nie zmieniać marki bez polecenia,
- pilnować czytelności tekstu,
- pilnować marginesów i formatu.
```

S000 nie wpisuje wszystkich zasad projektowych na stałe.  
S000 wymaga, żeby konkretny skill miał własne zasady bezpieczeństwa.

---

## 19. Kontrola błędów

Skill ma wykrywać:

```text
- brak celu,
- zbyt szeroki zakres,
- brak danych krytycznych,
- sprzeczne wymagania,
- brak wyniku końcowego,
- brak testów,
- za dużo teorii,
- za mało działania,
- brak granic,
- błędne ograniczenia historyczne,
- brak wersji,
- brak oceny jakości.
```

Jeżeli skill wykryje problem, ma:

1. nazwać problem,
2. określić ryzyko,
3. zaproponować poprawkę,
4. kontynuować pracę, jeżeli to możliwe.

---

## 20. Format wyniku po użyciu skilla

Każda odpowiedź po użyciu skilla powinna kończyć się blokiem kontrolnym:

```text
## Etap prac
SXXX: X%

## Ocena mojej pracy
X/10

## Co poprawić w następnym kroku
1. ...
2. ...
3. ...
```

---

## 21. Komendy S000

| Komenda | Znaczenie |
|---|---|
| **S000** | użyj standardu S000 do aktualnej pracy |
| **S000 nowy skill** | rozpocznij tworzenie nowego skilla |
| **S000 audyt SXXX** | oceń wskazany skill |
| **S000 popraw SXXX** | popraw wskazany skill |
| **S000 katalog** | pokaż / zaktualizuj katalog skilli |
| **S000 backup SXXX** | przygotuj skill do zapisu jako `.md` |
| **S000 mini** | użyj skróconej wersji standardu |
| **S000 test SXXX** | wykonaj test jakości |
| **S000+** | użyj S000 + audyt + test + backup + katalog |

---

## 22. Komenda z plusem

Znak `+` oznacza:

```text
Użyj wskazanego skilla oraz jego zalecanych skilli pomocniczych.
```

| Komenda | Znaczenie |
|---|---|
| **S001+** | S001 + S002 + S003 + S008 |
| **S002+** | S002 + S003 + S004 |
| **S003+** | S003 + S004 |
| **S009+** | S009 + S010 |

Dla modułów PrestaShop:

```text
S001+ = budowa modułu + audyt/debug + testy + pakowanie ZIP
```

Zasada:

```text
+ nie może oznaczać tygodniowego planowania.
```

Ma oznaczać lepszą kontrolę jakości.

---

## 23. Proces tworzenia nowego skilla

Gdy użytkownik mówi `S000 nowy skill` albo `Stwórz nowy skill`, stosuj procedurę:

```text
1. Sprawdź, czy skill jest potrzebny.
2. Nadaj numer.
3. Nadaj nazwę.
4. Ustal cel.
5. Ustal rolę w 7DEJV OS.
6. Ustal, kiedy używać.
7. Ustal, kiedy nie używać.
8. Ustal dane wejściowe.
9. Ustal dane wyjściowe.
10. Ustal tryby pracy.
11. Ustal etapy działania.
12. Dodaj zasady jakości.
13. Dodaj zasady bezpieczeństwa.
14. Dodaj kontrolę błędów.
15. Dodaj format wyniku.
16. Dodaj prompt dla Codex/Replit, jeśli potrzebny.
17. Dodaj test końcowy.
18. Nadaj ocenę.
19. Dodaj historię zmian.
20. Wskaż kolejny krok.
```

---

## 24. Proces poprawiania istniejącego skilla

Gdy użytkownik mówi `Popraw S001`, `Podciągnij S002 do 10/10`, `Zrób audyt i popraw`, stosuj procedurę:

```text
1. Oceń obecną wersję.
2. Wskaż główny problem.
3. Podziel błędy na krytyczne, średnie i kosmetyczne.
4. Określ, co zostaje.
5. Określ, co usunąć lub skrócić.
6. Określ, co dodać.
7. Napisz poprawioną wersję.
8. Porównaj przed / po.
9. Wykonaj test końcowy.
10. Nadaj ocenę po poprawkach.
11. Wskaż następny krok.
```

---

## 25. Proces audytu skilla

Audyt skilla musi mieć format:

```text
# AUDYT SKILLA SXXX

## 1. Ocena ogólna
x/10

## 2. Mocne strony
- ...

## 3. Słabe strony
- ...

## 4. Błędy krytyczne
- ...

## 5. Błędy średnie
- ...

## 6. Błędy kosmetyczne
- ...

## 7. Czy skill nadaje się do pracy?
TAK / NIE / CZĘŚCIOWO

## 8. Co poprawić najpierw
1. ...
2. ...
3. ...

## 9. Ocena po sugerowanych poprawkach
x/10
```

---

## 26. Prompt dla Codex / Replit / wykonawcy AI

Jeżeli skill ma być przekazany wykonawcy AI, użyj szablonu:

```text
# ZADANIE DLA WYKONAWCY AI

## Cel
[Opisz dokładnie, co ma zostać wykonane.]

## Kontekst
[Opisz projekt, technologię, obecny stan i ważne ograniczenia.]

## Zakres pracy
Wykonaj:
1. ...
2. ...
3. ...

## Czego nie robić
Nie wykonuj:
1. ...
2. ...
3. ...

## Wymagania jakościowe
- ...
- ...
- ...

## Test końcowy
Po wykonaniu sprawdź:
1. ...
2. ...
3. ...

## Wynik końcowy
Na końcu podaj:
- listę zmienionych plików,
- opis zmian,
- testy,
- ryzyka,
- instrukcję uruchomienia,
- gotową paczkę, jeżeli dotyczy.
```

---

## 27. Test końcowy każdego skilla

Każdy skill przed uznaniem za gotowy musi przejść test:

| Test | Wynik |
|---|---|
| Czy ma jasny cel? | PASS / FAIL |
| Czy ma jasny zakres? | PASS / FAIL |
| Czy wiadomo, kiedy go używać? | PASS / FAIL |
| Czy wiadomo, kiedy go nie używać? | PASS / FAIL |
| Czy ma dane wejściowe? | PASS / FAIL |
| Czy ma dane wyjściowe? | PASS / FAIL |
| Czy działa etapami? | PASS / FAIL |
| Czy ma zasady jakości? | PASS / FAIL |
| Czy ma zasady bezpieczeństwa? | PASS / FAIL |
| Czy ma kontrolę błędów? | PASS / FAIL |
| Czy kończy się konkretnym wynikiem? | PASS / FAIL |
| Czy ma ocenę jakości? | PASS / FAIL |
| Czy nie jest tylko teorią? | PASS / FAIL |
| Czy nie jest za długi względem celu? | PASS / FAIL |
| Czy nie kopiuje zasad historycznych jako globalnych? | PASS / FAIL |

---

## 28. Skala oceny skilla

| Ocena | Znaczenie |
|---|---|
| **1–3** | słaby, wymaga przebudowy |
| **4–5** | działa częściowo, ale jest chaotyczny |
| **6–7** | użyteczny, ale wymaga poprawek |
| **8** | dobry do pracy |
| **9** | bardzo dobry |
| **9.5** | prawie wzorcowy |
| **10** | standard referencyjny |

Główne skille powinny dojść minimum do `9/10`. Najważniejsze skille systemowe powinny dojść do `9.5–10/10`.

---

## 29. S000 MINI

```text
S000 MINI — STANDARD BUDOWY SKILLI 7DEJV OS

1. Każdy skill musi mieć numer: S000, S001, S002...
2. Każdy skill musi mieć nazwę: SXXX — NAZWA SKILLA — vX.X.
3. Każdy skill musi mieć jasny cel.
4. Każdy skill musi mieć określoną rolę w 7DEJV OS.
5. Każdy skill musi mówić, kiedy go używać.
6. Każdy skill musi mówić, kiedy go NIE używać.
7. Każdy skill musi oddzielać dane wejściowe od danych wyjściowych.
8. Dane wejściowe dzielimy na wymagane i opcjonalne.
9. Dane wyjściowe muszą być konkretne.
10. Każdy większy skill powinien mieć tryby pracy.
11. Każdy skill działa etapami: cel → zakres → dane → wykonanie → kontrola → test → wynik.
12. Każdy skill musi mieć zasady jakości.
13. Każdy skill musi mieć zasady bezpieczeństwa właściwe dla swojej dziedziny.
14. Każdy skill musi mieć kontrolę błędów.
15. Każdy skill musi kończyć się konkretnym wynikiem.
16. Każdy skill musi mieć test końcowy PASS / FAIL.
17. Każdy skill musi mieć ocenę jakości 1–10.
18. Każdy skill musi mieć historię zmian.
19. Każdy skill powinien mieć wersję plikową .md.
20. Główna zasada: MVP najpierw, PRO później.
21. Zakaz: nie przenoś ograniczeń z jednego projektu jako zasad globalnych.
22. Zasada pracy: jeżeli można działać na dostępnych danych, nie blokuj pracy pytaniami.
23. Po każdej pracy nad skillem podaj etap prac, ocenę pracy i co poprawić dalej.
24. Komenda z plusem oznacza użycie skilla oraz zalecanych skilli pomocniczych.
25. Skill jest gotowy dopiero wtedy, gdy pomaga realnie działać, a nie tylko dobrze wygląda.
```

---

## 30. Backup skilli

Każdy ważny skill zapisujemy jako plik `.md`.

### Format nazwy pliku

```text
SXXX_nazwa_skilla_vX.X.md
```

Przykłady:

```text
S000_standard_budowy_skilli_v1.0.md
S001_modul_builder_pro_v0.1.md
S002_audyt_debug_pro_v0.1.md
```

### Proponowana struktura folderów

```text
7dejv-os/
└── skills/
    ├── S000_standard_budowy_skilli/
    │   ├── S000_standard_budowy_skilli_v0.1.md
    │   ├── S000_standard_budowy_skilli_v0.2.md
    │   ├── S000_standard_budowy_skilli_v0.3.md
    │   ├── S000_standard_budowy_skilli_v0.4.md
    │   ├── S000_standard_budowy_skilli_v0.5.md
    │   └── S000_standard_budowy_skilli_v1.0.md
    │
    ├── S001_modul_builder_pro/
    │   └── S001_modul_builder_pro_v0.1.md
    │
    └── S002_audyt_debug_pro/
        └── S002_audyt_debug_pro_v0.1.md
```

---

## 31. Katalog pierwszych skilli

| Numer | Nazwa robocza | Rola | Priorytet | Status |
|---|---|---|---|---|
| **S000** | Standard Budowy Skilli | skill do pisania skilli | Krytyczny | v1.0 |
| **S001** | Moduł Builder PRO | budowa modułów/projektów od zera | Krytyczny | do poprawy |
| **S002** | Audyt i Debug PRO | analiza, naprawa błędów, debug | Krytyczny | do poprawy |
| **S003** | Testy i QA PRO | checklisty, testy, weryfikacja | Wysoki | planowany |
| **S004** | Dokumentacja PRO | instrukcje, README, raporty | Wysoki | planowany |
| **S005** | Prompt dla Codex/Replit PRO | zadania dla wykonawcy AI | Wysoki | planowany |
| **S006** | GitHub Repo Manager | repozytoria, wersje, commity | Średni | planowany |
| **S007** | PrestaShop BO UI Builder | panele Back Office | Wysoki | planowany |
| **S008** | PrestaShop ZIP Packager | ZIP, struktura, instalacja | Wysoki | planowany |
| **S009** | Product Graphics Builder | grafiki produktowe i marketplace | Średni | planowany |
| **S010** | Product Description Builder | opisy produktów, Allegro, Erli, sklep | Średni | planowany |

---

## 32. Test praktyczny S000

S000 przed przejściem do wersji stabilnej został sprawdzony na realnym skillu:

```text
S001 — MODUŁ BUILDER PRO
```

### Wynik testu

S000 pomógł ustalić dla S001:

- cel,
- rolę,
- granice,
- dane wejściowe,
- dane wyjściowe,
- zasadę MVP najpierw,
- zasadę anty-przeplanowanie,
- zakaz przenoszenia ograniczeń historycznych,
- logiczne połączenie `S001+`.

### Najważniejsza wykryta poprawka dla S001

S001 nie może globalnie kopiować zasady:

```text
Nie ruszać API.
```

Poprawna zasada:

```text
Ograniczenia API ustalaj dla konkretnego projektu.
Nie przenoś ograniczeń historycznych jako globalnych.
```

### Werdykt testu

```text
PASS
```

S000 zdał test praktyczny na S001.

---

## 33. Ocena S000 v1.0 FINAL

| Obszar | Ocena |
|---|---:|
| Cel | 10/10 |
| Struktura | 9.8/10 |
| Praktyczność | 9.7/10 |
| Komendy | 9.6/10 |
| Proces tworzenia skilla | 9.7/10 |
| Proces poprawy skilla | 9.6/10 |
| Audyt | 9.5/10 |
| S000 MINI | 9.5/10 |
| Backup | 9.5/10 |
| Test praktyczny | 9.8/10 |
| Testowalność | 9.7/10 |
| Prostota | 9.1/10 |
| Gotowość do użycia | 9.8/10 |

**Ocena ogólna:** `9.75/10`

---

## 34. Historia zmian S000

```text
v0.1:
- utworzono pierwszą wersję roboczą,
- ustalono, że S000 jest standardem budowy wszystkich skilli.

v0.2:
- doprecyzowano, że S000 jest skillem do pisania skilli,
- dodano zasadę MVP → PRO,
- dodano rozróżnienie zasad globalnych, projektowych i historycznych.

v0.3:
- dodano szablon nowego skilla,
- dodano szablon audytu,
- dodano szablon poprawy,
- dodano katalog S000–S010,
- dodano S000 MINI.

v0.4:
- dodano system komend S000,
- dodano proces tworzenia nowego skilla krok po kroku,
- dodano proces poprawiania istniejącego skilla,
- dodano backup,
- dodano test logiczny na przykładzie S001.

v0.5:
- scalono wcześniejsze sekcje w jeden czysty dokument,
- usunięto część powtórzeń,
- dodano standard końcówki odpowiedzi z etapem, oceną i następnymi poprawkami,
- uporządkowano komendy, procesy, testy i backup.

v1.0 RC:
- przygotowano kandydatkę do wersji stabilnej,
- dodano formalny test praktyczny na S001,
- dopracowano S000 MINI,
- dopracowano katalog skilli.

v1.0 FINAL:
- przygotowano czystą wersję finalną,
- usunięto robocze komentarze,
- utrzymano strukturę gotową do zapisu jako .md,
- zatwierdzono S000 jako stabilny standard bazowy.
```

---

## 35. Decyzja końcowa

```text
S000 — STANDARD BUDOWY SKILLI 7DEJV OS — v1.0 FINAL
```

zostaje przyjęty jako **stabilny standard bazowy** do tworzenia, oceniania i poprawiania kolejnych skilli.

Następny logiczny skill do pracy:

```text
S001 — MODUŁ BUILDER PRO
```