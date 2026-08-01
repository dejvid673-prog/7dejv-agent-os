# S011 — Visual Knowledge Prototype Builder v0.1 CANDIDATE

## 1. Numer skilla

**S011**

## 2. Nazwa i wersja

**Visual Knowledge Prototype Builder v0.1 CANDIDATE**

**Status:** `CANDIDATE`  
**Rola:** budowanie i utrzymywanie klikalnej wizualizacji bazy wiedzy równolegle z researchem  
**Zasada nadrzędna:** widoczny prototyp od pierwszej iteracji, ale bez udawania pełnej poprawności merytorycznej

## 3. Jasny cel

S011 przekształca ograniczony pakiet researchu i architektury informacji w:

- uporządkowane karty wiedzy,
- klikalny prototyp HTML/CSS,
- połączone ścieżki nawigacji,
- render desktop/mobile,
- dowody QA,
- jawny rejestr braków merytorycznych.

Skill rozwiązuje problem projektów, w których najpierw powstaje długa dokumentacja, a użytkownik dopiero bardzo późno widzi, jak efekt będzie wyglądał.

Najkrótsza definicja:

> **S011 = research i wizualizacja rozwijane razem w małych, testowalnych iteracjach.**

## 4. Kiedy używać

Używaj S011, gdy:

- powstaje baza wiedzy, dokumentacja użytkowa, help center lub repetytorium,
- research ma zostać od razu pokazany w interfejsie,
- potrzebna jest makieta HTML/CSS z działającymi przejściami,
- trzeba sprawdzić architekturę informacji na realnych treściach,
- użytkownik oczekuje wizualizacji od początku projektu,
- trzeba synchronizować tematy, źródła, statusy i ekrany,
- projekt ma kilka typów treści, np. problem, parametr, gatunek, choroba, poradnik,
- trzeba stopniowo rozwijać prototyp bez budowania pełnej aplikacji.

Typowe komendy:

```text
S011: pokaż pierwszy pakiet wiedzy jako klikalną makietę.
S011: dodaj trzy zagadnienia i od razu zaktualizuj HTML/CSS.
S011: zsynchronizuj research z kartami widocznymi w prototypie.
S011+: wykonaj aktualizację, render i S003 QA.
```

## 5. Kiedy nie używać

Nie używaj S011 jako głównego skilla, gdy:

- trzeba stworzyć produkcyjną aplikację lub moduł — użyj odpowiedniego skilla implementacyjnego,
- zadanie dotyczy wyłącznie debugowania — użyj S002,
- trzeba tylko wykonać test istniejącej pracy — użyj S003,
- użytkownik chce pojedynczy statyczny obraz bez prototypu,
- problem nie ma komponentu wiedzy ani struktury informacji,
- trzeba postawić pełny CMS, backend, bazę danych lub system kont,
- potrzebna jest diagnoza medyczna albo prawna zamiast struktury edukacyjnej.

S011 nie zastępuje eksperta domenowego, lekarza weterynarii, laboratorium, prawnika ani produkcyjnego frontend developera.

## 6. Dane wejściowe

### Minimalne

```text
Nazwa projektu:
Cel użytkownika:
Zakres pierwszego pakietu tematów:
Repozytorium źródłowe:
Lokalizacja prototypu:
```

### Zalecane

```text
Odbiorcy:
Granice tematyczne:
Typy kart wiedzy:
Istniejąca architektura informacji:
Rejestr tematów:
Mapa źródeł:
Status merytoryczny treści:
Kierunek wizualny:
Istniejący HTML/CSS:
Viewporty testowe:
Kryteria QA:
Gałąź robocza:
```

### Dane, których nie wolno zgadywać

- ścieżki plików,
- istniejące kategorie,
- stan źródeł,
- status prawny lub medyczny,
- wartości liczbowe wysokiego ryzyka,
- nazwy API, frameworków lub systemu docelowego,
- fakt, że praca została przetestowana.

## 7. Dane wyjściowe

S011 zwraca minimum:

1. **research delta** — co dodano lub zmieniono w wiedzy,
2. **information architecture delta** — gdzie treść znajduje się w strukturze,
3. **visual delta** — co zmieniło się w HTML/CSS,
4. **clickable path** — konkretna ścieżka, którą użytkownik może przejść,
5. **verification evidence** — testy i screenshoty,
6. **content status** — fakty, założenia i elementy do weryfikacji,
7. **next smallest step** — jeden następny krok.

Artefakty mogą obejmować:

```text
prototype-html/index.html
prototype-html/<category>.html
prototype-html/<knowledge-card>.html
prototype-html/assets/css/style.css
prototype-html/assets/img/*
reports/visual-qa-*.md
reports/research-status-*.md
screenshots/*.png
```

## 8. Tryby pracy

### 8.1. S011 MINI

Dla pojedynczego zagadnienia lub poprawki jednego ekranu.

Zakres:

- 1 temat,
- 1 typ karty,
- 1–2 pliki HTML/CSS,
- statyczna kontrola linków,
- screenshot zmienionego widoku, jeśli zmienił się wygląd.

### 8.2. S011 STANDARD

Tryb domyślny.

Zakres:

- 1–3 powiązane tematy,
- aktualizacja źródeł i statusów,
- minimum jedna ścieżka kategoria → karta,
- render desktop i mobile,
- raport QA,
- aktualizacja handoffu lub statusu.

### 8.3. S011 PRO

Dla większego etapu architektury informacji.

Zakres:

- kilka typów kart,
- warianty UX lub porównanie struktur,
- rozwinięcie design systemu,
- pełny test Playwright,
- podstawowy audyt a11y,
- S003,
- handoff do kolejnego etapu.

### 8.4. S011+

```text
S011 + S003 + właściwy skill pomocniczy
```

Przykłady:

```text
Research + wizualizacja:
S011 + knowledge-ops + product-research

Architektura + prototyp:
S011 + frontend-design + ui-design-system

Odbiór:
S011 + S003 + playwright-cli

Naprawa błędu makiety:
S011 + S002 + playwright-cli
```

W pojedynczym wykonaniu router nadal może wybrać maksymalnie trzy aktywne skille. S011 nie jest zgodą na ładowanie wszystkich wymienionych narzędzi naraz.

## 9. Etapy działania

### Etap 0 — odczytaj prawdziwy stan projektu

Sprawdź:

- repozytorium i gałąź,
- instrukcje projektu,
- mapę decyzji,
- rejestr tematów,
- mapę źródeł,
- istniejący prototyp,
- aktualne raporty QA,
- ostatnie zmiany i otwarte PR-y.

Wynik:

```text
Stan wiedzy:
Stan makiety:
Stan QA:
Największa niespójność:
Najmniejszy bezpieczny pakiet do wykonania:
```

### Etap 1 — wybierz mały pakiet

Pakiet powinien zawierać:

- 1–3 powiązane tematy,
- jedną konkretną ścieżkę użytkownika,
- jeden widoczny rezultat,
- określone źródła lub jawny brak źródeł.

Nie rozpoczynaj od całego drzewa wiedzy, jeżeli można pokazać jedną reprezentatywną ścieżkę.

### Etap 2 — zbierz pytania użytkownika

Dla każdego tematu ustal:

- czego użytkownik szuka,
- jak nazywa problem własnymi słowami,
- co musi zobaczyć najpierw,
- jakie dane powinien zebrać,
- gdzie może popełnić niebezpieczny błąd,
- do jakiej powiązanej karty powinien przejść.

### Etap 3 — oceń źródła

Każdy temat otrzymuje:

```text
Źródło podstawowe:
Źródło uzupełniające:
Data sprawdzenia:
Fakty potwierdzone:
Ograniczenia źródła:
Elementy do weryfikacji:
Elementy niedopuszczone do publikacji:
```

Źródło niskiej jakości może służyć do zebrania języka użytkowników, ale nie do potwierdzania diagnozy, dawkowania, prawa lub bezpieczeństwa.

### Etap 4 — przypisz typ karty

Dozwolone przykładowe typy:

- karta problemu,
- karta parametru,
- karta gatunku,
- karta objawu,
- karta choroby,
- poradnik sezonowy,
- procedura awaryjna,
- hasło słownikowe.

Nie twórz nowego typu, jeżeli istniejący szablon wystarcza.

### Etap 5 — zbuduj model informacji

Minimalny model:

```text
Tytuł:
Typ karty:
Status treści:
Odbiorca:
Zakres:
Najważniejsza odpowiedź:
Sekcje:
Powiązania:
Źródła:
Ryzyka:
```

### Etap 6 — natychmiast zaktualizuj prototyp

W tej samej iteracji:

- dodaj lub zmień odpowiednią kartę,
- dodaj wejście z kategorii,
- dodaj breadcrumbs lub informację o położeniu,
- połącz kartę z powiązanymi materiałami,
- oznacz treść roboczą,
- zastosuj wspólny CSS i komponenty,
- użyj prawdziwej nazwy tematu zamiast `Lorem ipsum`.

Jeżeli research jest niepełny, pokaż bezpieczny szkielet i widoczny status braku — nie wypełniaj go przypuszczeniami.

### Etap 7 — render i kontrola

Minimum:

- otwarcie strony w prawdziwej przeglądarce,
- kontrola błędów konsoli,
- kontrola nieudanych zasobów,
- kontrola linków lokalnych,
- sprawdzenie jednego viewportu desktop,
- sprawdzenie jednego viewportu mobile przy zmianach responsywnych,
- screenshot pełnej strony.

### Etap 8 — S003 QA

S003 powinien sprawdzić:

- czy zakres makiety odpowiada zadaniu,
- czy przejścia działają,
- czy wizualizacja nie maskuje braków treści,
- czy statusy robocze są widoczne,
- czy nie dodano elementów wyłączonych,
- czy brak jest regresji.

### Etap 9 — zapisz stan

Zaktualizuj:

- rejestr tematów,
- mapę źródeł,
- raport QA,
- decyzje, jeżeli zapadła nowa decyzja,
- handoff po długiej pracy.

## 10. Zasady jakości

S011 wymaga, aby:

- użytkownik otrzymywał widoczny wynik od pierwszej iteracji,
- prototyp był klikalny, nie tylko narysowany,
- research i UI używały tej samej terminologii,
- każda karta miała jedno kanoniczne miejsce,
- synonimy prowadziły do karty, a nie tworzyły duplikaty,
- treść była częścią projektu interfejsu,
- status treści był jawny,
- rozwiązanie pozostawało proste technicznie,
- każda duża decyzja wizualna miała dowód renderu,
- testy były opisane zgodnie z prawdą,
- raport wskazywał braki i ryzyka.

### Visual-first gate

Praca nie przechodzi etapu, gdy zmienia:

- nawigację,
- kategorię,
- typ karty,
- hierarchię informacji,
- sposób prezentacji ostrzeżeń,

ale nie aktualizuje odpowiadającej części makiety.

### Evidence gate

Nie używaj słów `działa`, `responsywne`, `sprawdzone` lub `PASS`, jeżeli nie istnieje odpowiedni test albo render.

## 11. Zasady bezpieczeństwa

- Nie przedstawiaj atrakcyjnej wizualizacji jako potwierdzenia faktów.
- Nie publikuj diagnozy medycznej na podstawie objawu lub zdjęcia.
- Nie publikuj dawkowania bez źródła i kontekstu.
- Nie publikuj informacji prawnej bez daty weryfikacji i źródła urzędowego.
- Nie ukrywaj konfliktu źródeł.
- Nie wstawiaj produktu lub CTA do projektu z założeniem niekomercyjnym.
- Nie mieszaj tematyki wykluczonej przez projekt.
- Nie modyfikuj produkcyjnego systemu bez osobnej zgody i właściwego workflow.
- Nie wykonuj operacji destrukcyjnych bez backupu i ścieżki cofnięcia.
- Nie zapisuj sekretów, tokenów ani danych osobowych w prototypie.

## 12. Kontrola błędów

### 12.1. Dokumentacja bez wizualizacji

```text
[P1] Brak visual-first output
Zmiana wpływa na użytkownika: TAK
Brakujący ekran:
Minimalna poprawka:
Decyzja: etap nieukończony
```

### 12.2. Wizualizacja bez pokrycia w źródłach

```text
[P1] Makieta sugeruje potwierdzoną treść bez źródeł
Element UI:
Treść ryzykowna:
Poprawka: oznaczyć status albo usunąć twierdzenie
```

### 12.3. Martwe przejście

```text
[P1] Martwy link lub brak docelowej karty
Źródło linku:
Cel:
Test:
Poprawka:
```

### 12.4. Niespójność rejestru i makiety

```text
[P2] Status tematu różni się między dokumentacją i UI
Temat:
Status w rejestrze:
Status w makiecie:
Źródło prawdy:
Poprawka:
```

### 12.5. Przeciążony pakiet

```text
[P2] Iteracja jest zbyt szeroka
Tematy:
Ekrany:
Zakres do odcięcia:
Najmniejszy pakiet:
```

### 12.6. Fałszywe QA

```text
[P1] Zadeklarowano test bez dowodu
Deklaracja:
Brakujący dowód:
Decyzja: cofnąć PASS do NOT RUN
```

## 13. Format wyniku

```text
# S011 — wynik iteracji

## Kontekst
Projekt:
Gałąź:
Pakiet tematów:
Wybrana ścieżka użytkownika:

## Research delta
Tematy:
Źródła:
Fakty:
Do weryfikacji:
Blokady:

## Information architecture delta
Kategoria:
Typ karty:
Powiązania:
Synonimy:

## Visual delta
Ekrany:
HTML/CSS/assets:
Clickable path:
Status widoczny w UI:

## Verification
Static links:
Desktop render:
Mobile render:
Console/resources:
Screenshots:
S003:

## Ryzyka
Merytoryczne:
UX:
Techniczne:

## Stan
Etap prac:
Ocena:
Status:

## Następny najmniejszy krok
...
```

## 14. Test końcowy

### Test strukturalny

- [ ] Cel skilla został spełniony.
- [ ] Pakiet nie przekracza rozsądnego zakresu.
- [ ] Research i makieta dotyczą tych samych tematów.
- [ ] Każda nowa karta ma wejście nawigacyjne.
- [ ] Każdy link lokalny ma istniejący cel.

### Test wizualny

- [ ] Zmieniony ekran został wyrenderowany.
- [ ] Istnieje screenshot odpowiadający zmianie.
- [ ] Mobile został sprawdzony, jeżeli zmiana dotyczy responsywności.
- [ ] Nie wykryto poziomego overflow albo błąd jest opisany.
- [ ] Treści robocze są wizualnie oznaczone.

### Test merytoryczny

- [ ] Fakty mają źródła.
- [ ] Braki źródeł są jawne.
- [ ] Nie ma pewnej diagnozy bez badania.
- [ ] Nie ma niezweryfikowanego dawkowania.
- [ ] Prawo ma aktualne źródło i datę albo status `DO WERYFIKACJI`.

### Test zakresu

- [ ] Nie dodano funkcji produkcyjnych bez potrzeby.
- [ ] Nie wprowadzono zbędnego frameworka.
- [ ] Nie dodano treści wyłączonych przez projekt.
- [ ] Nie dodano funkcji sprzedażowych do projektu niekomercyjnego.

### Decyzja

```text
PASS — wiedza, struktura i makieta są zsynchronizowane oraz mają dowód QA
WARNING — widoczny wynik działa, ale istnieją jawne braki nieblokujące
FAIL — brak wizualizacji, martwe przejścia, niespójność lub ryzykowna treść
BLOCKED — wymagane źródło, konsultacja albo decyzja właściciela projektu
```

## 15. Ocena 1–10

### Ocena bieżąca: `8.7/10`

Uzasadnienie:

- skill ma jasny cel, granice, wejścia, wyjścia i test,
- rozwiązuje konkretny problem workflow,
- łączy research z namacalnym artefaktem,
- ma kontrolę bezpieczeństwa i fałszywego QA,
- jest zgodny z MVP-first.

Braki przed `FINAL`:

1. test w minimum dwóch pełnych iteracjach Repetytorium Wiedzy STAW EXPERT,
2. potwierdzenie, że routing skilli jest wystarczająco prosty,
3. sprawdzenie, czy format raportu nie jest za długi dla trybu MINI,
4. raport S003 dla samego skilla,
5. ewentualna adaptacja do innych baz wiedzy niż STAW EXPERT.

## 16. Historia zmian

### v0.1 CANDIDATE

- utworzono skill research + information architecture + klikalny prototyp,
- dodano visual-first gate i evidence gate,
- dodano tryby MINI, STANDARD, PRO i S011+,
- dodano kontrolę niespójności pomiędzy rejestrem i UI,
- dodano testy wizualne, merytoryczne i zakresowe,
- pozostawiono status CANDIDATE do czasu praktycznej walidacji.