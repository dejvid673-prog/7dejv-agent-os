# S001 — Moduł Builder PRO v1.2

## 1. Numer, nazwa i wersja

**Numer:** S001  
**Nazwa:** Moduł Builder PRO  
**Wersja:** v1.2  
**Status:** produkcyjny  
**Standard nadrzędny:** S000 — Standard Budowy Skilli, Agentów i Workflow v1.1  
**Kategoria:** PrestaShop / moduły / Codex / Replit / VS Code / GitHub  
**Rola w 7DEJV OS:** główny skill do budowy modułów PrestaShop od pomysłu do działającego MVP, wersji PRO i paczki ZIP.

---

## 2. Jasny cel

S001 prowadzi pracę nad modułem PrestaShop w sposób praktyczny, etapowy i kontrolowany.

Celem S001 jest doprowadzenie od pomysłu do konkretnego wyniku:

- planu MVP,
- architektury modułu,
- promptu dla Codex/Replit,
- kodu do wykonania przez agenta wykonawczego,
- testów,
- audytu podstawowego,
- dokumentacji roboczej,
- paczki ZIP,
- raportu końcowego.

Główna zasada:

> **MVP najpierw, PRO później.**  
> Najpierw działająca wersja, potem test, potem poprawki, a dopiero później rozbudowa.

---

## 3. Rola w 7DEJV OS

S001 jest pierwszym skillem wykonawczym po S000.

W systemie 7DEJV OS:

- **S000** określa standard tworzenia skilli, agentów i workflow.
- **S001** buduje i prowadzi moduł PrestaShop.
- **S002** przejmuje głęboki audyt i debug.
- **S003** prowadzi testy i QA.
- **S004** tworzy dokumentację.
- **S005** buduje prompty dla Codex/Replit.
- **S008** pakuje moduł ZIP.

S001 nie ma robić wszystkiego sam, jeżeli zadanie wymaga wielu specjalizacji. Wtedy tworzy workflow i dobiera skille pomocnicze.

---

## 4. Agent i workflow

### 4.1. Agent główny

**Agent:** Moduł Builder Agent  
**Skill główny:** S001 — Moduł Builder PRO

Agent odpowiada za:

- rozpoznanie celu modułu,
- ograniczenie zakresu do MVP,
- dobranie skilli pomocniczych,
- przygotowanie promptu wykonawczego,
- kontrolę pracy Codex/Replit,
- zebranie raportu,
- decyzję: poprawka, test, ZIP, PRO albo koniec etapu.

### 4.2. Skille pomocnicze

| Skill | Kiedy używać |
|---|---|
| S002 | głęboki audyt, debug, analiza błędów |
| S003 | testy, QA, regresja |
| S004 | dokumentacja techniczna i użytkowa |
| S005 | prompt dla Codex/Replit |
| S008 | pakowanie ZIP modułu PrestaShop |

### 4.3. Workflow minimalny

```text
1. Rozpoznaj cel.
2. Dobierz skill.
3. Ustal MVP.
4. Wykonaj.
5. Przetestuj.
6. Oceń.
7. Zapisz wynik.
```

### 4.4. Workflow PRO

```text
1. Rozpoznaj cel.
2. Dobierz agenta.
3. Dobierz skill główny.
4. Dobierz skille pomocnicze.
5. Wykonaj MVP.
6. Przetestuj.
7. Zrób audyt.
8. Popraw błędy.
9. Przygotuj dokumentację.
10. Zrób backup.
11. Zaktualizuj katalog.
12. Nadaj ocenę.
```

---

## 5. Obsługa komendy S001+

Komenda `+` oznacza użycie S001 oraz zalecanych skilli pomocniczych.

### 5.1. S001

```text
S001 = tylko Moduł Builder PRO
```

Użycie: prosty plan, MVP, prompt, struktura modułu.

### 5.2. S001+

```text
S001+ = S001 + S003 + S002 + S008
```

Znaczenie:

- **S001** — budowa MVP modułu,
- **S003** — testy i QA,
- **S002** — audyt/debug po testach,
- **S008** — pakowanie ZIP.

Użycie: budowa modułu z lepszą kontrolą jakości, bez tygodniowego planowania.

### 5.3. S001++

```text
S001++ = S001 + S005 + S003 + S002 + S004 + S008
```

Znaczenie:

- **S001** — prowadzenie budowy,
- **S005** — prompt dla Codex/Replit,
- **S003** — testy,
- **S002** — audyt/debug,
- **S004** — dokumentacja,
- **S008** — ZIP.

Użycie: większy moduł, moduł produkcyjny, moduł z dokumentacją i pełnym obiegiem.

---

## 6. Kiedy używać

Używaj S001, gdy:

- tworzysz nowy moduł PrestaShop,
- rozwijasz istniejący moduł,
- chcesz ograniczyć pomysł do MVP,
- potrzebujesz struktury modułu,
- potrzebujesz promptu wykonawczego dla Codex/Replit,
- przygotowujesz moduł do testów,
- przygotowujesz moduł do ZIP,
- chcesz uporządkować chaos w pracy nad modułem.

---

## 7. Kiedy nie używać

Nie używaj S001 jako głównego skilla, gdy:

- robisz wyłącznie głęboki audyt lub debug — użyj S002,
- robisz wyłącznie testy — użyj S003,
- piszesz wyłącznie dokumentację — użyj S004,
- piszesz wyłącznie prompt dla Codex/Replit — użyj S005,
- tylko pakujesz ZIP — użyj S008,
- zadanie nie dotyczy modułów PrestaShop.

S001 może jednak uruchomić te skille pomocniczo w workflow.

---

## 8. Dane wejściowe

S001 może pracować na podstawie pełnych lub częściowych danych.

### 8.1. Minimalne dane wejściowe

```text
Nazwa modułu:
Cel modułu:
PrestaShop: 1.7 / 8 / 9:
Back Office: tak/nie:
Front Office: tak/nie:
Czy moduł jest nowy, istniejący czy uszkodzony:
Efekt końcowy:
```

### 8.2. Pełne dane wejściowe

```text
Nazwa modułu:
Krótki cel modułu:
Czy moduł jest nowy, istniejący, czy uszkodzony:
PrestaShop: 1.7 / 8 / 9:
Back Office: tak/nie:
Front Office: tak/nie:
Baza danych: tak/nie/nie wiadomo:
API: tak/nie/nie wiadomo:
Automatyzacja: tak/nie:
Akcje ręczne administratora: tak/nie:
Czy moduł ma mieć osobną zakładkę BO:
Czy moduł ma mieć konfigurację:
Czy moduł ma generować pliki:
Czego nie wolno ruszać:
Co można przebudować:
Efekt końcowy:
```

Jeżeli użytkownik nie poda wszystkich danych, S001 nie blokuje pracy. Przyjmuje rozsądne założenia i oznacza je jako założenia.

---

## 9. Dane wyjściowe

S001 może zwrócić:

- plan MVP,
- podział MVP / PRO / później,
- architekturę modułu,
- strukturę folderów,
- prompt dla Codex/Replit,
- checklistę testową,
- checklistę ZIP,
- ocenę ryzyka,
- raport etapu,
- raport końcowy,
- decyzję o użyciu S002/S003/S004/S005/S008,
- nazwę wersji modułu,
- nazwę paczki ZIP.

---

## 10. Tryby pracy

### 10.1. NOWY MODUŁ

Użyj, gdy moduł jeszcze nie istnieje albo zaczynamy od zera.

Wynik:

- plan MVP,
- struktura modułu,
- prompt wykonawczy,
- test instalacji,
- przygotowanie ZIP.

### 10.2. ROZWÓJ MODUŁU

Użyj, gdy moduł już istnieje i dodajemy funkcję.

Wynik:

- zakres zmiany,
- lista plików do modyfikacji,
- lista plików zakazanych,
- test regresji.

### 10.3. DEBUG

Użyj, gdy moduł ma konkretny błąd.

Wynik:

- diagnoza,
- minimalna poprawka,
- test błędu,
- raport ryzyka regresji.

Jeżeli debug staje się złożony, użyj S002.

### 10.4. AUDYT

Użyj, gdy trzeba ocenić jakość modułu.

Wynik:

- ocena 1–10,
- lista błędów,
- priorytety poprawek,
- decyzja, czy moduł nadaje się do instalacji lub produkcji.

Pełny audyt wykonuje S002.

### 10.5. ZIP

Użyj, gdy moduł ma zostać spakowany do instalacji.

Wynik:

- sprawdzona struktura,
- usunięte pliki robocze,
- gotowa paczka ZIP,
- raport paczkowania.

### 10.6. LIGHT

Tryb szybki.

```text
1. Cel
2. MVP
3. Prompt
4. Test
5. Następny krok
```

### 10.7. PRO

Tryb pełny.

```text
1. Cel
2. Kontekst
3. Zakres
4. MVP / PRO / później
5. Architektura
6. Ryzyko
7. Backup
8. Prompt wykonawczy
9. Testy
10. ZIP
11. Raport
12. Następny etap
```

---

## 11. Etapy działania

### Etap 1 — Rozpoznanie celu

Ustalić, co ma powstać i po co.

### Etap 2 — Dobór trybu i skilli

Wybrać S001, S001+, S001++ albo przekazać do innego skilla.

### Etap 3 — MVP

Ograniczyć zakres do pierwszej działającej wersji.

### Etap 4 — Architektura

Ustalić strukturę modułu, główne pliki, hooki, kontrolery, SQL i widoki.

### Etap 5 — Prompt wykonawczy

Przygotować polecenie dla Codex/Replit/VS Code.

### Etap 6 — Wykonanie

Agent wykonawczy tworzy lub modyfikuje pliki.

### Etap 7 — Test

Sprawdzić instalację, działanie, logi, regresję i strukturę ZIP.

### Etap 8 — Audyt / debug

Jeżeli są błędy, użyć S002 lub trybu DEBUG.

### Etap 9 — ZIP / dokumentacja

Przygotować paczkę i dokumentację, jeśli zakres tego wymaga.

### Etap 10 — Raport i ocena

Zakończyć etap raportem, procentem ukończenia i oceną 1–10.

---

## 12. Zasady jakości

S001 pilnuje, aby moduł:

- miał poprawną strukturę,
- był zgodny z PrestaShop 8/9,
- nie modyfikował core PrestaShop,
- nie używał override bez mocnego uzasadnienia,
- miał kontrolę tokenów i uprawnień,
- walidował dane wejściowe,
- miał test instalacji i odinstalowania,
- miał czytelną strukturę ZIP,
- miał raport zmian,
- miał wersjonowanie,
- miał możliwość rollbacku.

---

## 13. Zasady bezpieczeństwa

S001 wymaga:

- backupu przed większą zmianą,
- commitu Git przy średnim i wysokim ryzyku,
- niewpisywania haseł i tokenów do logów,
- ochrony formularzy tokenami,
- sprawdzania uprawnień Back Office,
- walidacji danych wejściowych,
- braku modyfikacji core PrestaShop,
- braku akcji zmieniających dane przez GET,
- braku nadpisywania działającej wersji bez powrotu.

---

## 14. Kontrola błędów

Jeżeli pojawia się błąd:

```text
1. Zatrzymaj rozbudowę.
2. Przejdź do trybu DEBUG.
3. Ustal komunikat błędu.
4. Ustal ostatnią zmianę.
5. Wskaż pliki podejrzane.
6. Przygotuj minimalną poprawkę.
7. Wykonaj test.
8. Oceń ryzyko regresji.
9. Jeżeli błąd jest złożony, przekaż do S002.
```

S001 nie może maskować błędów pustym catch ani udawać, że test został wykonany.

---

## 15. Standard struktury modułu

Przykładowa struktura:

```text
modulename/
├── modulename.php
├── index.php
├── config.xml
├── controllers/
│   └── admin/
├── classes/
├── views/
│   ├── templates/
│   ├── css/
│   └── js/
├── sql/
│   ├── install.php
│   └── uninstall.php
├── docs/
└── README.md
```

Nie każdy moduł musi mieć wszystkie foldery. S001 dobiera strukturę do zakresu i nie tworzy zbędnych elementów.

---

## 16. Skala ryzyka

### Niskie ryzyko

Przykłady:

- tekst,
- README,
- CSS,
- drobny widok,
- proste pole konfiguracji.

Wymaganie:

```text
Zwykły backup.
```

### Średnie ryzyko

Przykłady:

- nowa zakładka BO,
- tabela SQL,
- formularz POST,
- hook,
- kontroler.

Wymaganie:

```text
Backup + test instalacji + test regresji.
```

### Wysokie ryzyko

Przykłady:

- API,
- proces zamówień,
- płatności,
- przewoźnicy,
- migracje danych,
- przebudowa architektury.

Wymaganie:

```text
Backup + commit Git + osobna gałąź lub osobna kopia + plan rollbacku.
```

---

## 17. Backup, Git i rollback

### Przed zmianą

```text
1. Sprawdź, czy obecna wersja działa.
2. Zrób kopię folderu modułu.
3. Jeżeli projekt jest w Git:
   - sprawdź status,
   - zrób commit,
   - opisz commit konkretnie.
4. Nadaj wersję roboczą.
5. Dopiero potem edytuj pliki.
```

### Nazwy backupów

```text
modulename_backup_YYYY-MM-DD_HH-MM
modulename_before_debug_YYYY-MM-DD_HH-MM
modulename_before_bo_panel_YYYY-MM-DD_HH-MM
modulename_before_api_change_YYYY-MM-DD_HH-MM
```

### Nazwy commitów

```text
backup: stable module before new feature
fix: repair admin token validation
feat: add back office panel
test: add install and zip checks
docs: update module README
refactor: clean module structure without behavior change
```

### Rollback

```text
1. Nie dodawaj kolejnych funkcji.
2. Cofnij ostatnią zmianę lub przywróć backup.
3. Sprawdź, czy stara wersja działa.
4. Dopiero potem wykonaj mniejszą poprawkę.
5. Opisz, co spowodowało problem.
```

---

## 18. System wersjonowania modułów

```text
0.1.0 — pierwsze MVP
0.1.1 — mała poprawka błędu
0.2.0 — większa funkcja
0.9.0 — kandydat do wersji stabilnej
1.0.0 — wersja stabilna
```

Dodatkowe oznaczenia:

```text
-mvp
-test
-fix
-tokenfix
-bo
-fo
-stable
```

Przykłady:

```text
modulename-0.1.0-mvp.zip
modulename-0.1.1-fix-token.zip
modulename-0.2.0-bo-panel.zip
modulename-1.0.0-stable.zip
```

---

## 19. Standard promptu dla Codex/Replit

Każdy prompt wykonawczy powinien mieć format:

```text
CEL:
KONTEKST:
ZAKRES:
CZEGO NIE RUSZAĆ:
CO MOŻNA ZMIENIAĆ:
WYMAGANIA TECHNICZNE:
KROKI:
TESTY:
EFEKT KOŃCOWY:
RAPORT:
```

---

## 20. Prompt — nowy moduł od zera

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie NOWY MODUŁ.

CEL:
Stwórz nowy moduł PrestaShop od zera.

KONTEKST:
Moduł ma być osobnym, instalowalnym modułem PrestaShop.
Nie modyfikuj core PrestaShop.
Nie twórz override, chyba że zostanie to wyraźnie uzasadnione i zaakceptowane.
Moduł ma być możliwy do spakowania jako ZIP.
Najpierw wykonaj MVP, nie wersję PRO.

DANE MODUŁU:
Nazwa modułu:
Cel modułu:
PrestaShop:
Back Office:
Front Office:
Baza danych:
API:
Osobna zakładka BO:
Konfiguracja:
Generowanie plików:
Automatyzacja:
Akcje ręczne administratora:

ZAKRES MVP:
1.
2.
3.

CZEGO NIE RUSZAĆ:
1.
2.
3.

WYMAGANIA TECHNICZNE:
1. Zachowaj poprawną strukturę modułu PrestaShop.
2. Główny plik modułu ma znajdować się w folderze modułu.
3. Folder i główny plik muszą mieć zgodną nazwę.
4. Dodaj index.php zabezpieczający do katalogów.
5. Zabezpiecz formularze tokenami.
6. Waliduj dane wejściowe.
7. Nie zapisuj haseł ani tokenów w logach.
8. Przygotuj moduł pod instalację ZIP.
9. Nie dodawaj zbędnych bibliotek.
10. Nie twórz funkcji spoza MVP.

KROKI:
1. Zaproponuj strukturę modułu.
2. Utwórz pliki modułu.
3. Dodaj minimalną konfigurację.
4. Dodaj wymagane hooki lub kontrolery.
5. Dodaj widoki.
6. Dodaj zabezpieczenia.
7. Przygotuj README robocze.
8. Przygotuj test instalacji.
9. Przygotuj ZIP, jeśli środowisko pozwala.

TESTY:
1. Sprawdź strukturę folderów.
2. Sprawdź instalację modułu.
3. Sprawdź odinstalowanie.
4. Sprawdź widok Back Office lub Front Office.
5. Sprawdź formularze i tokeny.
6. Sprawdź logi błędów.
7. Sprawdź, czy ZIP zawiera prawidłowy folder modułu.

RAPORT:
Na końcu zwróć raport:
- co zostało utworzone,
- jakie pliki powstały,
- jakie testy wykonano,
- jakie są ryzyka,
- czego nie udało się wykonać,
- jak nazywa się ZIP,
- czy rekomendujesz S002, S003, S004, S005 lub S008 jako następny skill.
```

---

## 21. Prompt — rozwój istniejącego modułu

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie ROZWÓJ MODUŁU.

CEL:
Dodaj nową funkcję do istniejącego modułu PrestaShop bez psucia obecnego działania.

KONTEKST:
Moduł już istnieje.
Najpierw przeanalizuj strukturę.
Nie przepisuj całego modułu.
Nie zmieniaj działających części bez potrzeby.
Nie dodawaj funkcji spoza zakresu.
Najpierw wykonaj małe MVP funkcji, potem dopiero wersję PRO.

NOWA FUNKCJA:
Opisz funkcję:

ZAKRES:
1.
2.
3.

CZEGO NIE RUSZAĆ:
1.
2.
3.

CO MOŻNA ZMIENIAĆ:
1.
2.
3.

WYMAGANIA:
1. Zachowaj zgodność z obecną strukturą modułu.
2. Nie zmieniaj nazw klas bez potrzeby.
3. Nie zmieniaj instalacji, jeśli nie jest to wymagane.
4. Jeżeli dodajesz SQL, dodaj też uninstall/cleanup.
5. Jeżeli dodajesz formularz, zabezpiecz go tokenem.
6. Jeżeli dodajesz akcję BO, sprawdź uprawnienia.
7. Po zmianie wykonaj test regresji.

KROKI:
1. Przeanalizuj moduł.
2. Wskaż pliki, które trzeba zmienić.
3. Wykonaj minimalny zakres zmian.
4. Sprawdź, czy stara funkcja nadal działa.
5. Sprawdź nową funkcję.
6. Przygotuj raport.

TESTY:
1. Test instalacji, jeśli ruszono install.
2. Test starej funkcji.
3. Test nowej funkcji.
4. Test logów.
5. Test błędów PHP.
6. Test struktury ZIP, jeśli przygotowano paczkę.

RAPORT:
Podaj:
- zmienione pliki,
- dodane pliki,
- ryzyko regresji,
- testy,
- wynik,
- następny krok.
```

---

## 22. Prompt — debug błędu

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie DEBUG.

CEL:
Napraw konkretny błąd w module PrestaShop.

ZASADA GŁÓWNA:
Nie dodawaj nowych funkcji.
Nie przepisuj całego modułu.
Nie przebudowuj architektury bez konieczności.
Najpierw znajdź przyczynę, potem wykonaj minimalną poprawkę.
Jeżeli błąd jest złożony, przekaż sprawę do S002.

DANE BŁĘDU:
Komunikat błędu:
Screen:
Log:
Kiedy błąd występuje:
Co działało wcześniej:
Ostatnia zmiana przed błędem:

KROKI:
1. Przeanalizuj komunikat błędu.
2. Wskaż najbardziej prawdopodobną przyczynę.
3. Wskaż pliki do sprawdzenia.
4. Zaproponuj minimalną poprawkę.
5. Wykonaj poprawkę.
6. Uruchom test błędu.
7. Sprawdź, czy nie powstał nowy błąd.
8. Przygotuj raport.

ZAKAZY:
1. Nie zmieniaj plików niezwiązanych z błędem.
2. Nie usuwaj funkcji.
3. Nie zmieniaj API, jeśli błąd go nie dotyczy.
4. Nie zmieniaj SQL, jeśli błąd go nie dotyczy.
5. Nie maskuj błędu pustym catch.
6. Nie ukrywaj błędów bez rozwiązania przyczyny.

TESTY:
1. Odtwórz błąd.
2. Wykonaj poprawkę.
3. Sprawdź, czy błąd zniknął.
4. Sprawdź logi.
5. Sprawdź funkcję powiązaną z błędem.
6. Oceń ryzyko regresji.

RAPORT:
Podaj:
- przyczynę błędu,
- zmienione pliki,
- wykonane poprawki,
- testy,
- wynik,
- ryzyko regresji,
- czy potrzebny jest S002.
```

---

## 23. Prompt — pakowanie ZIP

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie ZIP.

CEL:
Przygotuj moduł PrestaShop do instalacji jako ZIP.

ZASADY:
ZIP musi zawierać jeden główny folder modułu.
W głównym folderze musi być główny plik modułu.
Nazwa folderu i głównego pliku muszą być zgodne.
Nie dodawaj zbędnego folderu nadrzędnego.
Nie pakuj .git, cache, tmp, node_modules, vendor-dev, plików testowych ani plików systemowych.
Jeżeli zakres jest tylko ZIP, preferuj użycie S008.

KROKI:
1. Sprawdź nazwę folderu modułu.
2. Sprawdź nazwę głównego pliku modułu.
3. Sprawdź strukturę katalogów.
4. Usuń zbędne pliki.
5. Sprawdź index.php w katalogach.
6. Sprawdź README.
7. Sprawdź wersję modułu.
8. Utwórz ZIP.
9. Zweryfikuj zawartość ZIP.
10. Podaj nazwę paczki.

RAPORT:
Podaj:
- nazwę ZIP,
- strukturę ZIP,
- usunięte pliki,
- wynik kontroli,
- czy paczka nadaje się do instalacji.
```

---

## 24. Raport Codex/Replit do ChatGPT

Po wykonaniu pracy Codex/Replit musi zwrócić raport:

```text
RAPORT WYKONANIA:

1. Cel zadania:
2. Co zostało zmienione:
3. Lista zmienionych plików:
4. Lista dodanych plików:
5. Lista usuniętych plików:
6. Czy wykonano backup:
7. Czy wykonano testy:
8. Wyniki testów:
9. Błędy:
10. Ryzyka:
11. Co wymaga ręcznego sprawdzenia:
12. Czy ZIP został przygotowany:
13. Nazwa paczki ZIP:
14. Następny zalecany krok:
```

Jeżeli testy nie zostały wykonane:

```text
TESTY NIEZROBIONE:
Powód:
Jak użytkownik może je wykonać ręcznie:
```

---

## 25. Checklisty testowe

### Test struktury ZIP

```text
[ ] ZIP zawiera jeden główny folder modułu.
[ ] Główny plik modułu jest w folderze modułu.
[ ] Nazwa folderu i głównego pliku są zgodne.
[ ] Nie ma zbędnego folderu nadrzędnego.
[ ] Nie ma plików .git, node_modules, cache, tmp.
[ ] Katalogi mają index.php zabezpieczający.
```

### Test instalacji

```text
[ ] Moduł pojawia się w Module Manager.
[ ] Moduł instaluje się bez błędu.
[ ] Moduł tworzy potrzebne tabele.
[ ] Moduł dodaje potrzebne zakładki BO.
[ ] Moduł rejestruje hooki.
[ ] Moduł odinstalowuje się bez błędu.
```

### Test Back Office

```text
[ ] Zakładka BO otwiera się bez błędu 500.
[ ] Formularze mają token.
[ ] Akcje POST są zabezpieczone.
[ ] Pracownik bez uprawnień nie może wykonać akcji.
[ ] Komunikaty błędów są czytelne.
[ ] Lista danych ładuje się szybko.
```

### Test Front Office

```text
[ ] Hook wyświetla się w dobrym miejscu.
[ ] Szablon nie psuje motywu.
[ ] CSS jest ograniczony do modułu.
[ ] JS nie powoduje konfliktów.
[ ] Moduł działa na telefonie.
```

### Test debugowania

```text
[ ] Sprawdzono logi PrestaShop.
[ ] Sprawdzono logi PHP.
[ ] Sprawdzono konsolę przeglądarki.
[ ] Sprawdzono Network w DevTools.
[ ] Sprawdzono SQL.
[ ] Sprawdzono tokeny.
[ ] Sprawdzono uprawnienia.
```

---

## 26. Komendy S001

### Komendy główne

```text
S001 start
S001 plan
S001 mvp
S001 prompt
S001 debug
S001 audyt
S001 test
S001 zip
S001 raport
S001 pro
S001 light
S001 stop-chaos
S001 backup
S001+
S001++
```

### Komendy skrócone

```text
S001 start [nazwa modułu]
S001 plan [opis modułu]
S001 mvp [opis funkcji]
S001 prompt codex [zakres]
S001 debug [błąd]
S001 audyt [plik/moduł]
S001 zip [nazwa modułu]
S001 test bo
S001 test fo
S001 test zip
S001 pro [funkcja]
S001 light [zadanie]
S001 stop-chaos
S001+ [moduł]
S001++ [moduł produkcyjny]
```

---

## 27. Standard oceny modułu 1–10

| Kategoria | Maks. punktów |
|---|---:|
| Struktura modułu | 1.0 |
| Instalacja i odinstalowanie | 1.0 |
| Zgodność z PrestaShop 8/9 | 1.0 |
| Back Office / Front Office | 1.0 |
| Bezpieczeństwo | 1.5 |
| Tokeny i uprawnienia | 1.0 |
| SQL i dane | 1.0 |
| Testy | 1.0 |
| ZIP i wersjonowanie | 0.8 |
| Dokumentacja | 0.7 |
| **Razem** | **10.0** |

### Decyzja po ocenie

```text
9.0–10.0 — można pakować ZIP lub robić finalny test.
8.0–8.9 — poprawić wskazane braki i testować.
7.0–7.9 — wrócić do MVP i naprawić kluczowe elementy.
6.0–6.9 — przekazać do S002 na audyt/debug.
1.0–5.9 — nie rozwijać dalej, najpierw naprawić fundament.
```

---

## 28. Minimalna definicja gotowego modułu

### Gotowy do testu

```text
[ ] Ma poprawną strukturę folderów.
[ ] Ma główny plik modułu w folderze modułu.
[ ] Instaluje się w PrestaShop.
[ ] Nie powoduje błędu 500.
[ ] Główna funkcja MVP jest dostępna.
[ ] Nie ma oczywistych błędów PHP.
[ ] Da się wskazać, co jeszcze wymaga poprawy.
```

### Gotowy do ZIP

```text
[ ] Moduł instaluje się bez błędu.
[ ] Moduł odinstalowuje się bez błędu.
[ ] ZIP ma jeden folder główny modułu.
[ ] Nie ma zbędnego folderu nadrzędnego.
[ ] Nie zawiera plików roboczych.
[ ] README jest obecne.
[ ] Wersja modułu jest ustawiona.
[ ] Paczka ma czytelną nazwę.
```

### Gotowy produkcyjnie

```text
[ ] Przeszedł test instalacji.
[ ] Przeszedł test odinstalowania.
[ ] Przeszedł test głównej funkcji.
[ ] Przeszedł test regresji.
[ ] Formularze mają tokeny.
[ ] Akcje BO sprawdzają uprawnienia.
[ ] Dane wejściowe są walidowane.
[ ] Nie loguje haseł ani tokenów.
[ ] Nie modyfikuje core PrestaShop.
[ ] Nie robi override bez uzasadnienia.
[ ] Nie ma błędów krytycznych w logach.
[ ] Ma dokumentację.
[ ] Ma backup lub commit Git.
[ ] Ma wersję stabilną.
```

---

## 29. Najczęstsze błędy Codex/Replit

### Błędy struktury

```text
[ ] Główny plik modułu poza folderem modułu.
[ ] Podwójne zagnieżdżenie folderu w ZIP.
[ ] Zła nazwa klasy modułu.
[ ] Zła nazwa folderu względem pliku głównego.
[ ] Brak index.php w katalogach.
[ ] Pakowanie całego projektu zamiast samego modułu.
```

### Błędy Back Office

```text
[ ] Brak tokena w formularzu.
[ ] Brak sprawdzenia uprawnień.
[ ] Błędny kontroler admina.
[ ] Błąd routingu Symfony/Legacy.
[ ] Użycie niewłaściwej metody tłumaczeń.
[ ] Formularz POST wykonuje akcję bez walidacji.
```

### Błędy SQL

```text
[ ] Tabele bez prefiksu PrestaShop.
[ ] Brak uninstall dla tabel.
[ ] Niezgodna składnia MariaDB/MySQL.
[ ] Brak walidacji danych przed zapisem.
[ ] Brak obsługi błędu zapisu.
[ ] Nadpisywanie danych bez backupu.
```

### Błędy zakresu

```text
[ ] Dodanie funkcji spoza MVP.
[ ] Przepisywanie działającego modułu.
[ ] Zmiana API bez potrzeby.
[ ] Mieszanie BO i FO bez planu.
[ ] Rozbudowa zamiast naprawy błędu.
[ ] Brak raportu zmian.
```

---

## 30. Czego S001 ma nie robić

S001 nie powinien:

- planować bez końca,
- robić kilku modułów naraz,
- mieszać MVP z wersją PRO,
- dodawać funkcji spoza zakresu,
- przepisywać działającego modułu bez powodu,
- zmieniać core PrestaShop,
- robić override bez mocnego uzasadnienia,
- usuwać działających funkcji,
- maskować błędów,
- ignorować testów,
- pakować ZIP bez kontroli struktury,
- pomijać raportu po etapie,
- udawać, że coś zostało przetestowane, jeśli testu nie wykonano,
- mieszać ról skilli, gdy potrzebny jest workflow.

---

## 31. Format wyniku

Każda praca z S001 powinna kończyć się formatem:

```text
Użyty agent:
Użyte skille:
Workflow:
Etap prac w %:
Ocena pracy /10:
Co wykonano:
Co wymaga poprawy:
Następny krok:
```

---

## 32. Test końcowy S001

Po użyciu S001 sprawdź:

```text
[ ] Czy rozpoznano cel?
[ ] Czy dobrano właściwy tryb pracy?
[ ] Czy ustalono MVP?
[ ] Czy nie przeniesiono historycznych ograniczeń jako globalnych?
[ ] Czy oceniono ryzyko?
[ ] Czy wskazano backup/Git, jeśli potrzebny?
[ ] Czy przygotowano konkretny wynik?
[ ] Czy wskazano test?
[ ] Czy podano raport końcowy?
[ ] Czy podano użytego agenta, skille, workflow, procent i ocenę?
```

---

## 33. Historia zmian

### S001 v1.1

Wersja produkcyjna pierwotna.

Dodano:

- tryby pracy,
- S001 LIGHT i PRO,
- komendy,
- checklisty,
- prompty,
- backup,
- rollback,
- ocenę 1–10,
- definicję gotowego modułu.

### S001 v1.2

Aktualizacja zgodna z nowymi instrukcjami projektu i S000 v1.1.

Dodano:

- formalną sekcję Agent i workflow,
- obsługę S001+ i S001++,
- mocniejsze rozdzielenie Agent / Skill / Workflow,
- formalne dane wejściowe,
- formalne dane wyjściowe,
- mocniejszą zasadę MVP najpierw, PRO później,
- jasne kiedy używać i kiedy nie używać,
- test końcowy S001,
- obowiązkowy format wyniku po każdej pracy nad skillem,
- zgodność z katalogiem 7DEJV OS.

---

## 34. Ocena skilla

**Ocena S001 v1.2:** 9.8/10

Mocne strony:

- zgodność z S000 v1.1,
- praktyczne workflow,
- obsługa `+`,
- silne MVP,
- dobra współpraca z Codex/Replit,
- kontrola jakości i testów,
- jasne raportowanie.

Do poprawy w v1.3:

- dopisać uwagi po pierwszym realnym użyciu na module,
- dodać przykładowy pełny workflow dla konkretnego modułu,
- dodać skrócony wariant do szybkiego kopiowania na Androidzie.
