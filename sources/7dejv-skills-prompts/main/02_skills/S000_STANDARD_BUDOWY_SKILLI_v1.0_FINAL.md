# S000 — Standard Budowy Skilli v1.0 FINAL

## 1. Numer skilla

**S000**

---

## 2. Nazwa i wersja

**Standard Budowy Skilli v1.0 FINAL**

**Status:** FINAL  
**Rola:** standard nadrzędny dla wszystkich skilli 7DEJV OS  
**Zasada nadrzędna:** MVP najpierw, PRO później  
**Katalog docelowy:** `02_skills/`

---

## 3. Jasny cel

S000 określa, jak tworzyć, oceniać, poprawiać, numerować, testować i katalogować wszystkie skille w bazie 7DEJV OS.

S000 ma zapewnić, że każdy skill jest:

- praktyczny,
- zrozumiały,
- możliwy do użycia od razu,
- zgodny z numeracją SXXX,
- odporny na chaos,
- możliwy do testowania,
- możliwy do poprawiania,
- możliwy do zapisania jako `.md`,
- zgodny z zasadą: **MVP najpierw, PRO później**.

Najkrótsza definicja:

> **S000 = standard jakości i konstrukcji wszystkich skilli.**

---

## 4. Kiedy używać

Używaj S000, gdy:

- tworzysz nowy skill,
- poprawiasz istniejący skill,
- oceniasz skill,
- porządkujesz katalog skilli,
- decydujesz, czy skill jest DRAFT / CANDIDATE / FINAL,
- sprawdzasz, czy skill ma komplet sekcji,
- przygotowujesz skill do GitHub,
- chcesz uniknąć zbyt długiego planowania,
- chcesz podnieść skill do poziomu 9–10/10.

Typowe komendy:

```txt
S000: sprawdź ten skill.
S000: zbuduj nowy skill zgodnie ze standardem.
S000: popraw skill do wersji CANDIDATE.
S000+: popraw skill + użyj S003 do QA.
```

---

## 5. Kiedy nie używać

Nie używaj S000 jako głównego skilla, gdy:

- trzeba napisać moduł PrestaShop — użyj S001,
- trzeba debugować błąd — użyj S002,
- trzeba wykonać QA wyniku — użyj S003,
- trzeba napisać dokumentację — użyj S004,
- trzeba przygotować prompt dla Codex/Replit — użyj S005,
- trzeba zarządzać repo GitHub — użyj S006,
- trzeba spakować ZIP — użyj S008,
- użytkownik potrzebuje szybkiej odpowiedzi, a nie budowy skilla.

S000 jest standardem, a nie kombajnem do każdej pracy.

---

## 6. Dane wejściowe

S000 może przyjąć:

- nazwę skilla,
- numer SXXX,
- opis celu,
- istniejący tekst skilla,
- listę wymagań użytkownika,
- wynik poprzedniej wersji,
- raport S003,
- listę błędów,
- decyzję, czy skill ma być DRAFT / CANDIDATE / FINAL.

Minimalne dane wejściowe:

```txt
Numer skilla:
Nazwa skilla:
Do czego ma służyć:
Kiedy ma być używany:
```

Jeżeli użytkownik poda tylko numer, np. `S003`, należy odczytać go jako polecenie pracy nad wskazanym skillem w kontekście katalogu 7DEJV OS.

---

## 7. Dane wyjściowe

S000 zwraca:

- kompletną strukturę skilla,
- ocenę 1–10,
- status: DRAFT / CHECKPOINT / CANDIDATE / FINAL,
- listę braków,
- listę poprawek,
- etap prac w procentach,
- decyzję, czy tworzyć plik `.md`,
- nazwę pliku,
- następny krok.

---

## 8. Obowiązkowa struktura każdego skilla

Każdy główny skill musi mieć:

1. numer SXXX,
2. nazwę i wersję,
3. jasny cel,
4. kiedy używać,
5. kiedy nie używać,
6. dane wejściowe,
7. dane wyjściowe,
8. tryby pracy,
9. etapy działania,
10. zasady jakości,
11. zasady bezpieczeństwa,
12. kontrolę błędów,
13. format wyniku,
14. test końcowy,
15. ocenę 1–10,
16. historię zmian.

Brak jednej z tych sekcji nie musi blokować wersji DRAFT, ale blokuje wersję FINAL.

---

## 9. Tryby pracy

### 9.1. S000 MINI

Szybka ocena skilla.

Format:

```txt
Status:
Ocena:
Największy brak:
Pierwsza poprawka:
Czy robić plik .md: TAK/NIE
```

### 9.2. S000 STANDARD

Normalna budowa lub poprawa skilla.

Zakres:

- sprawdzenie struktury,
- uzupełnienie braków,
- uproszczenie treści,
- ocena 1–10,
- decyzja o statusie,
- rekomendacja następnego kroku.

### 9.3. S000+

Pełna poprawa skilla z kontrolą QA.

S000+ oznacza:

```txt
S000 + S003 + właściwy skill pomocniczy
```

Przykłady:

```txt
Skill techniczny = S000 + S003 + S002
Skill do modułów = S000 + S001 + S003
Skill do dokumentacji = S000 + S004 + S003
Skill do promptów = S000 + S005 + S003
```

---

## 10. Etapy działania

### Etap 1 — Ustal rolę skilla

Najpierw odpowiedz:

```txt
Do czego ten skill ma służyć?
Jakiego problemu ma nieść rozwiązanie?
Czy to ma być osobny skill, czy część istniejącego?
```

Jeśli skill nie ma jasnej roli, nie przechodź do wersji FINAL.

### Etap 2 — Ustal granice

Każdy skill musi mówić:

```txt
Co robi?
Czego nie robi?
Z czym się łączy?
Kiedy przekazuje pracę innemu skillowi?
```

### Etap 3 — Zbuduj MVP

Najpierw zrób wersję działającą.

MVP skilla musi mieć:

- cel,
- kiedy używać,
- dane wejściowe,
- dane wyjściowe,
- tryby pracy,
- format wyniku,
- ocenę.

Dopiero potem dodawaj szczegóły PRO.

### Etap 4 — Dodaj sekcje PRO

Po MVP dopisz:

- kontrolę błędów,
- zasady bezpieczeństwa,
- checklisty,
- przykłady użycia,
- połączenia z innymi skillami,
- test końcowy,
- historię zmian.

### Etap 5 — Wykonaj QA

Przed finalizacją użyj S003.

Minimalny test:

```txt
S003: sprawdź skill pod kątem S000, praktyczności i kompletności.
```

### Etap 6 — Zapisz lub nie zapisuj pliku

Nie twórz pliku `.md` po każdej małej poprawce.

Plik twórz, gdy:

- skill jest CANDIDATE,
- skill jest FINAL,
- potrzebny jest ważny checkpoint,
- użytkownik wyraźnie chce backup,
- plik ma trafić do GitHub.

---

## 11. Zasady jakości

S000 wymaga, aby każdy skill:

- pomagał działać, a nie blokował teorią,
- miał praktyczny format wyniku,
- miał jasny zakres,
- nie udawał testu, jeśli test nie został wykonany,
- nie zawyżał oceny,
- nie tworzył zbędnych plików,
- nie mieszał ról innych skilli,
- miał informację, co poprawić dalej,
- był możliwy do użycia przez użytkownika i AI wykonawcze.

Najważniejsza zasada:

> **Skill ma działać w pracy, nie tylko wyglądać dobrze jako dokument.**

---

## 12. Zasady bezpieczeństwa

S000 wymaga, aby skille:

- nie sugerowały ryzykownych działań bez ostrzeżenia,
- nie przenosiły ograniczeń historycznych jako globalnych zasad,
- nie oznaczały nieprzetestowanej pracy jako FINAL,
- nie ukrywały braków,
- nie obiecywały wykonania rzeczy, których nie wykonano,
- nie mieszały produkcji z testami lokalnymi,
- nie zachęcały do zmian nieodwracalnych bez backupu,
- nie ujawniały haseł, tokenów ani danych API.

Ważna zasada 7DEJV OS:

> Ograniczenia wynikają z aktualnego celu i kontekstu, a nie z historii innego modułu.

---

## 13. Kontrola błędów

### 13.1. Braki strukturalne

Jeżeli skill nie ma obowiązkowej sekcji, oznacz błąd:

```txt
[P2] Brak sekcji wymaganej przez S000
Sekcja:
Skutek:
Poprawka:
```

### 13.2. Za szeroki zakres

Jeżeli skill próbuje robić zbyt wiele:

```txt
[P2] Skill ma zbyt szeroki zakres
Co trzeba odciąć:
Do którego skilla przekazać:
```

### 13.3. Brak testu

Jeśli skill nie ma testu końcowego:

```txt
[P1] Brak testu końcowego
Decyzja: nie może być FINAL
```

### 13.4. Fałszywy FINAL

Jeżeli skill jest oznaczony jako FINAL bez spełnienia S000:

```txt
[P1] Fałszywy status FINAL
Decyzja: cofnąć do CANDIDATE albo DRAFT
```

---

## 14. Format wyniku

### 14.1. Format budowy skilla

```txt
# SXXX — Nazwa skilla vX.X

## 1. Numer skilla
## 2. Nazwa i wersja
## 3. Jasny cel
## 4. Kiedy używać
## 5. Kiedy nie używać
## 6. Dane wejściowe
## 7. Dane wyjściowe
## 8. Tryby pracy
## 9. Etapy działania
## 10. Zasady jakości
## 11. Zasady bezpieczeństwa
## 12. Kontrola błędów
## 13. Format wyniku
## 14. Test końcowy
## 15. Ocena 1–10
## 16. Historia zmian
```

### 14.2. Format metryki po pracy

Po każdej pracy nad skillem podaj:

```txt
Etap prac: ...%
Ocena pracy: .../10
Status: DRAFT / CHECKPOINT / CANDIDATE / FINAL
Największy problem: ...
Co poprawić w następnym kroku: ...
Czy tworzyć plik .md: TAK/NIE
```

---

## 15. Test końcowy

Skill zbudowany według S000 przechodzi test końcowy, jeśli odpowiedź na poniższe pytania brzmi TAK:

1. Czy skill ma numer SXXX?
2. Czy ma nazwę i wersję?
3. Czy ma jasny cel?
4. Czy wiadomo, kiedy go używać?
5. Czy wiadomo, kiedy go nie używać?
6. Czy ma dane wejściowe?
7. Czy ma dane wyjściowe?
8. Czy ma tryby pracy?
9. Czy ma etapy działania?
10. Czy ma zasady jakości?
11. Czy ma zasady bezpieczeństwa?
12. Czy ma kontrolę błędów?
13. Czy ma format wyniku?
14. Czy ma test końcowy?
15. Czy ma ocenę 1–10?
16. Czy ma historię zmian?
17. Czy nie jest przegadany?
18. Czy nie robi pracy innego skilla bez potrzeby?
19. Czy można go użyć praktycznie?
20. Czy wiadomo, jaki jest następny krok?

Wynik:

```txt
20/20 = FINAL możliwy
17–19/20 = CANDIDATE
13–16/20 = CHECKPOINT
0–12/20 = DRAFT
```

---

## 16. Ocena 1–10

**Ocena S000 v1.0 FINAL: 9.6/10**

Uzasadnienie:

- zawiera pełny standard budowy skilli,
- zabezpiecza przed chaosem,
- wymusza MVP-first,
- blokuje fałszywe finalizacje,
- definiuje format `.md`,
- wymusza metrykę po pracy,
- dobrze współpracuje z S002 i S003,
- nadaje się jako fundament katalogu 7DEJV OS.

Nie otrzymuje 10/10, bo standard będzie jeszcze wzmacniany po realnym użyciu na kolejnych skillach S004–S010.

---

## 17. Historia zmian

### v0.1

Ustalenie, że S000 jest standardem nadrzędnym dla wszystkich skilli.

### v0.5

Dodanie obowiązkowej struktury 16 sekcji.

### v0.8

Dodanie zasad statusów DRAFT / CHECKPOINT / CANDIDATE / FINAL i ograniczenia zbędnych plików `.md`.

### v1.0 FINAL

Finalizacja standardu.

Dodano:

- tryby S000 MINI / STANDARD / S000+,
- obowiązkowy format skilla,
- test końcowy 20 pytań,
- metrykę po pracy,
- zasady bezpieczeństwa,
- kontrolę błędów,
- zasadę MVP-first,
- ocenę 9.6/10.

---

## 18. Finalna decyzja dla wersji v1.0

**Decyzja QA:** PASS  
**Status:** FINAL  
**Ocena:** 9.6/10  
**Czy można używać:** TAK  
**Czy można dodać do katalogu 7DEJV OS:** TAK  
**Czy wymaga dalszych prac przed użyciem:** NIE  
**Co poprawić w przyszłości:** przetestować i doprecyzować standard po finalizacji S004–S010.
