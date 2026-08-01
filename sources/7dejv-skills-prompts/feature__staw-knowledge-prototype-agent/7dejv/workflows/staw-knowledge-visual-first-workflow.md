# STAW Knowledge Visual-First Workflow

## Status

`CANDIDATE v0.1`

## Cel

Workflow prowadzi rozwój Repetytorium Wiedzy STAW EXPERT tak, aby od początku powstawały równolegle:

- uporządkowane zagadnienia,
- ocenione źródła,
- modele kart wiedzy,
- klikalna makieta HTML/CSS,
- rendery i screenshoty,
- raporty QA oraz handoff.

Workflow nie czeka z wizualizacją do końca researchu. Każda mała iteracja powinna kończyć się widocznym rezultatem.

## Agent główny

`7dejv-staw-knowledge-prototype-agent`

## Skill główny

`S011 — Visual Knowledge Prototype Builder`

## Skille i procedury pomocnicze

Dobieraj maksymalnie trzy aktywne skille w jednym przebiegu.

### Research i struktura

- `ux-researcher-designer`
- `knowledge-ops`
- `content-strategy`
- `product-research` albo `deep-research`

### Wizualizacja

- `frontend-design`
- `ui-design-system`
- `senior-frontend`
- procedura `cs-frontend-engineer`

### QA

- `playwright-cli` albo `playwright-pro`
- `a11y-audit`
- `full-page-screenshot`
- `S003 Testy i QA PRO`
- `S002 Audyt i Debug PRO` wyłącznie przy błędzie

### Domena

- `7dejv-pond-product-expert` jako konsultant terminologii, pytań użytkownika i realiów stawowych,
- bez przenoszenia funkcji sprzedażowej, CTA i niepotwierdzonych parametrów.

## Repozytoria

### Źródło agentów i workflow

```text
7dejv-skills-prompts
```

### Źródło prawdy projektu i miejsce pracy

```text
7dejv-staw-expert/12_repetytorium-wiedzy/
```

### Późniejsza implementacja

```text
7dejv-prestashop
```

Nie zapisuj kodu produkcyjnego modułu PrestaShop podczas tego workflow.

## Model dwóch zsynchronizowanych strumieni

### Strumień A — wiedza

```text
problem użytkownika
→ pytania
→ źródła
→ fakty i ograniczenia
→ typ karty
→ powiązania
→ status merytoryczny
```

### Strumień B — wizualizacja

```text
ścieżka użytkownika
→ ekran wejściowy
→ karta kategorii
→ karta wiedzy
→ linki powiązane
→ HTML/CSS
→ render
→ screenshot
→ QA
```

### Reguła synchronizacji

Strumienie nie mogą pozostawać rozdzielone dłużej niż jeden mały przebieg.

Jeżeli zmiana w strumieniu A wpływa na to, co widzi użytkownik, strumień B musi zostać zaktualizowany w tej samej iteracji.

Jeżeli zmiana wizualna dodaje nowe twierdzenie, strumień A musi posiadać dla niego status i źródło albo oznaczenie `DO WERYFIKACJI`.

## Wymagany punkt startowy

Przed wykonaniem pracy agent odczytuje:

1. mapę repozytoriów i decyzje nadrzędne,
2. globalne zasady STAW EXPERT,
3. dokumentację `12_repetytorium-wiedzy/`,
4. aktualny rejestr tematów,
5. aktualną mapę źródeł,
6. aktualną makietę HTML/CSS,
7. aktualne raporty QA,
8. ostatni handoff i otwarty draft PR.

Agent zapisuje:

```text
Current knowledge state:
Current visual state:
Current QA state:
Open blockers:
Chosen iteration:
```

## P0 — mapa projektu i baseline wizualny

### Cel

Zrozumieć projekt i natychmiast pokazać jego najważniejszy kierunek.

### Działania

1. Potwierdź zakres i wyłączenia.
2. Potwierdź odbiorców.
3. Potwierdź główne typy kart.
4. Sprawdź istniejącą makietę.
5. Jeżeli makieta nie istnieje, utwórz minimalny baseline:
   - `index.html`,
   - wspólny CSS,
   - jedna podstrona,
   - jedna karta wiedzy,
   - działające przejścia.
6. Wykonaj pierwszy render.
7. Pokaż użytkownikowi screenshot lub ZIP HTML/CSS.

### Bramka P0

```text
[ ] Projekt ma znane źródła prawdy.
[ ] Istnieje widoczny prototyp.
[ ] Użytkownik może przejść przynajmniej jedną ścieżkę.
[ ] Prototyp jest jawnie oznaczony jako roboczy.
```

Bez baseline wizualnego nie przechodź do wielotygodniowego researchu.

## P1 — wybór pakietu iteracji

### Cel

Ograniczyć pracę do fragmentu, który można zbadać, pokazać i sprawdzić.

### Domyślny rozmiar

- 1–3 powiązane zagadnienia,
- jeden główny typ karty,
- jedna ścieżka użytkownika,
- maksymalnie kilka ekranów.

### Przykład

```text
Pakiet: Ryby przy powierzchni
Karta problemu: ryby chwytają powietrze
Karta parametru: tlen rozpuszczony
Kontekst sezonowy: upał i świt
Ścieżka: strona główna → problemy → karta problemu → karta tlenu
```

### Bramka P1

```text
[ ] Pakiet ma jasny zakres.
[ ] Wiadomo, co zostanie pokazane wizualnie.
[ ] Wiadomo, jakie źródła są potrzebne.
[ ] Wiadomo, czego nie wolno publikować.
```

## P2 — research i ocena źródeł

### Cel

Zebrać wystarczającą wiedzę do bezpiecznego modelu karty, nie do napisania całej encyklopedii.

### Działania

1. Zapisz pytania użytkownika.
2. Wyszukaj źródła podstawowe.
3. Dodaj źródło uzupełniające, gdy temat jest złożony lub wysokiego ryzyka.
4. Zapisz datę sprawdzenia.
5. Wyodrębnij fakty.
6. Zapisz ograniczenia źródła.
7. Oznacz elementy do weryfikacji.
8. Oznacz elementy niedopuszczone do publikacji.
9. Zaktualizuj rejestr zagadnień i mapę źródeł.

### Hierarchia źródeł

1. prawo i źródła urzędowe,
2. publikacje naukowe i podręczniki specjalistyczne,
3. uczelnie i uznane ośrodki extension,
4. dokumentacja techniczna i SDS,
5. źródła branżowe,
6. fora i relacje użytkowników wyłącznie jako źródło języka, problemów i hipotez.

### Bramka P2

```text
[ ] Każdy fakt ma źródło lub status roboczy.
[ ] Nie ma diagnozy z jednego objawu.
[ ] Nie ma dawkowania bez źródła.
[ ] Informacja prawna ma datę albo status DO WERYFIKACJI.
[ ] Brakujące źródła są jawne.
```

Jeżeli bramka nie przechodzi, pozostaw bezpieczny szkielet karty i nie zatrzymuj całego projektu.

## P3 — model informacji

### Cel

Przełożyć research na strukturę czytelną dla użytkownika.

### Działania

1. Wybierz typ karty.
2. Zdefiniuj najważniejszą odpowiedź.
3. Ustal kolejność sekcji.
4. Dodaj status treści.
5. Dodaj powiązane materiały.
6. Dodaj synonimy i popularne sformułowania użytkowników.
7. Ustal poziom pilności, jeżeli dotyczy.
8. Ustal ostrzeżenia i granice odpowiedzialności.

### Minimalny model

```text
ID:
Tytuł:
Typ karty:
Status:
Odbiorca:
Problem lub pytanie:
Jednominutowe podsumowanie:
Sekcje:
Powiązania:
Synonimy:
Źródła:
Ryzyka:
```

### Bramka P3

```text
[ ] Karta ma jeden jasny cel.
[ ] Informacje są ułożone według potrzeb użytkownika.
[ ] Istnieje miejsce wejścia do karty.
[ ] Istnieje co najmniej jedno sensowne powiązanie.
[ ] Status merytoryczny jest znany.
```

## P4 — natychmiastowa aktualizacja makiety

### Cel

Pokazać wiedzę w działającym interfejsie jeszcze w tej samej iteracji.

### Działania

1. Zaktualizuj kategorię lub ekran wejściowy.
2. Dodaj kartę wiedzy albo jej bezpieczny szkielet.
3. Dodaj breadcrumbs.
4. Dodaj powiązane karty.
5. Dodaj widoczny status treści.
6. Zastosuj wspólne tokeny i komponenty CSS.
7. Użyj miniatury obrazkowej albo neutralnego placeholdera — nie emotikonu.
8. Zachowaj lokalne, działające ścieżki.
9. Nie dodawaj backendu, jeśli statyczny prototyp wystarcza.

### Visual-first gate

Etap P4 jest obowiązkowy, gdy zmienia się:

- kategoria,
- nawigacja,
- typ karty,
- kolejność informacji,
- ostrzeżenie,
- sposób prezentacji statusu,
- ścieżka użytkownika.

### Bramka P4

```text
[ ] Użytkownik może kliknąć nową lub zmienioną ścieżkę.
[ ] Ekran nie zawiera pustych atrap bez uzasadnienia.
[ ] Treści robocze są oznaczone.
[ ] Nie dodano elementów sprzedażowych.
[ ] Nie dodano treści akwarystycznych.
```

## P5 — browser QA i dowód wizualny

### Cel

Sprawdzić rzeczywisty interfejs, a nie tylko kod.

### Działania

1. Uruchom lokalny serwer albo otwórz statyczny prototyp.
2. Sprawdź lokalne linki.
3. Uruchom Chromium przez Playwright CLI lub istniejący workflow.
4. Sprawdź błędy konsoli.
5. Sprawdź nieudane zasoby i błędy HTTP.
6. Sprawdź liczbę `h1` i obecność `main`.
7. Sprawdź poziomy overflow.
8. Wykonaj screenshot desktop.
9. Wykonaj screenshot mobile, jeżeli zmiana wpływa na responsywność.
10. W razie błędu użyj S002 i wykonaj minimalną poprawkę.
11. Ponów test.

### Bramka P5

```text
[ ] Linki lokalne: PASS
[ ] Zasoby lokalne: PASS
[ ] Render desktop: PASS lub jawny WARNING
[ ] Render mobile: PASS lub NOT REQUIRED z uzasadnieniem
[ ] Błędy konsoli: 0 albo opisane
[ ] Screenshoty: zapisane
```

Nie oznaczaj jako `PASS`, jeżeli test nie został wykonany.

## P6 — przegląd użytkownika

### Cel

Umożliwić właścicielowi projektu ocenę kierunku, zanim agent pogłębi złą strukturę.

### Agent pokazuje

- klikalny ZIP HTML/CSS albo miejsce w repo,
- screenshot desktop,
- screenshot mobile przy zmianach responsywnych,
- krótkie wyjaśnienie, co jest działające,
- listę elementów roboczych,
- maksymalnie jedną najważniejszą decyzję do oceny.

### Pytania przeglądowe

- Czy główna ścieżka jest zrozumiała?
- Czy użytkownik wie, od czego zacząć?
- Czy karta pokazuje najważniejszą informację wystarczająco wcześnie?
- Czy status roboczy jest widoczny, ale nie przeszkadza?
- Czy wygląd pasuje do eksperckiego centrum wiedzy?

### Zasada

Agent nie zatrzymuje całej pracy z powodu braku odpowiedzi, jeżeli może bezpiecznie kontynuować kolejny niezależny pakiet. Nie podejmuje jednak nieodwracalnej decyzji projektowej wbrew istniejącym ustaleniom.

## P7 — S003 i synchronizacja stanu

### Cel

Sprawdzić, czy wiedza, dokumentacja i makieta pozostają zgodne.

### S003 sprawdza

- kompletność zakresu iteracji,
- zgodność rejestru z kartami,
- zgodność źródeł ze statusem treści,
- działanie przejść,
- brak regresji,
- jawność placeholderów,
- zgodność z wyłączeniami projektu,
- dowody renderu.

### Synchronizowane pliki

```text
03_rejestr-zagadnien.md
04_mapa-zrodel.md i uzupełnienia
05_mapa-makiety.md
DECISIONS.md — tylko przy nowej decyzji
prototype-html/*
reports/*
```

### Bramka P7

```text
[ ] Statusy tematów są spójne.
[ ] Źródła są przypisane.
[ ] Makieta nie pokazuje więcej pewności niż dokumentacja.
[ ] QA ma dowody.
[ ] Nowa decyzja jest zapisana tylko raz w źródle prawdy.
```

## P8 — commit, draft PR i handoff

### Cel

Pozostawić projekt w stanie możliwym do wznowienia bez odtwarzania kontekstu.

### Działania

1. Użyj opisowego commita.
2. Nie zapisuj małych eksperymentów jako wielu niepotrzebnych plików.
3. Przy większej zmianie użyj osobnej gałęzi.
4. Utrzymuj draft PR do czasu przeglądu.
5. Zapisz handoff.

### Format handoffu

```text
Project:
Branch:
PR:
Iteration package:
Knowledge added:
Sources added:
Screens changed:
Clickable path:
QA evidence:
Screenshots:
Decisions made:
Content blocked:
Residual risks:
Next smallest step:
Files to open first:
```

### Bramka P8

```text
[ ] Stan repozytorium jest opisany.
[ ] Zmienione pliki są wymienione.
[ ] Braki są jawne.
[ ] Następny krok jest pojedynczy i konkretny.
[ ] Nie scalono wersji roboczej jako produkcyjnej.
```

## Pętla iteracyjna

Po P8 agent wraca do P1:

```text
P1 pakiet
→ P2 źródła
→ P3 model
→ P4 wizualizacja
→ P5 render
→ P6 przegląd
→ P7 QA
→ P8 handoff
→ następny pakiet
```

Domyślnie nie wraca do pełnego P0, chyba że:

- zmienił się cel projektu,
- zmieniły się granice repozytoriów,
- makieta została zastąpiona,
- użytkownik zmienił grupę docelową,
- pojawiła się sprzeczna decyzja nadrzędna.

## Priorytety STAW EXPERT

### P0 bezpieczeństwa

- ryby przy powierzchni,
- nagłe śnięcia,
- problemy po burzy, upale lub dodaniu substancji,
- tlen, TAN, azotyny,
- choroby wysokiego ryzyka,
- bioasekuracja i czerwone flagi.

### P1 fundamentu

- zielona woda,
- glony nitkowate,
- pH i KH,
- karta jesiotra,
- filtracja biologiczna,
- awaryjne natlenianie,
- sezonowe poradniki.

Priorytet nie oznacza automatycznej publikacji. Temat wysokiego ryzyka może otrzymać wizualny szkielet i blokadę merytoryczną.

## Zakazy

- brak pełnego serwisu produkcyjnego w tym workflow,
- brak implementacji PrestaShop bez przekazania,
- brak akwarystyki,
- brak diagnozy po zdjęciu,
- brak preparatu jako automatycznej odpowiedzi,
- brak cen, promocji i agresywnego CTA,
- brak `Lorem ipsum` w miejscach, gdzie istnieje realna treść robocza,
- brak nieuzasadnionego frameworka,
- brak fałszywego `PASS`,
- brak zamknięcia etapu user-facing bez widocznego artefaktu.

## Definition of Done — iteracja STANDARD

```text
[ ] 1–3 tematy zostały wybrane i opisane.
[ ] Źródła lub braki źródeł zostały zapisane.
[ ] Powstał model informacji.
[ ] Zaktualizowano klikalny HTML/CSS.
[ ] Działa ścieżka kategoria → karta → powiązanie.
[ ] Treść robocza ma widoczny status.
[ ] Wykonano render desktop.
[ ] Wykonano render mobile, gdy wymagany.
[ ] Linki i zasoby przeszły test.
[ ] Screenshoty zostały zapisane.
[ ] Rejestr, źródła i makieta są zsynchronizowane.
[ ] Raport wskazuje ryzyka i następny krok.
```

## Przykładowe uruchomienie

```text
Użyj 7dejv-staw-knowledge-prototype-agent.
Workflow: staw-knowledge-visual-first-workflow.
Tryb: STANDARD.
Pakiet: zielona woda + zakwit fitoplanktonu + lampa UV.
Najpierw przeczytaj aktualny stan Repetytorium Wiedzy.
Zbierz wiarygodne źródła, zaktualizuj rejestr i mapę źródeł.
Następnie w tej samej iteracji dodaj klikalną kartę problemu i powiązanie do działu filtracji.
Wyrenderuj desktop i mobile, wykonaj screenshoty oraz S003.
Nie twórz modułu PrestaShop i nie dodawaj produktów.
```

## Historia zmian

### v0.1 CANDIDATE

- zdefiniowano dwa zsynchronizowane strumienie pracy,
- dodano obowiązkowy baseline wizualny w P0,
- dodano pętlę research → model → HTML/CSS → render → użytkownik → QA,
- dodano bramki dla źródeł, wizualizacji i dowodów,
- dodano granice STAW EXPERT oraz zasady chorób,
- pozostawiono workflow jako CANDIDATE do czasu dwóch pełnych cykli praktycznych.