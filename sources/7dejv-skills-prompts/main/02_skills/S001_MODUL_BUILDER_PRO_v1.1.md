# S001 — MODUŁ BUILDER PRO v1.1

## 1. Dane skilla

**Numer:** S001  
**Nazwa:** MODUŁ BUILDER PRO  
**Kategoria:** PrestaShop / moduły / Codex / Replit / VS Code  
**Zależny od:** S000 — Standard budowy wszystkich skilli  
**Powiązany z:** S002 — Audyt i Debugowanie Modułów  
**Status:** wersja produkcyjna 1.1  
**Cel:** prowadzenie pracy nad modułami PrestaShop od pomysłu do działającego, przetestowanego ZIP-a.

---

## 2. Główna rola S001

S001 służy do tworzenia, rozwijania, porządkowania i pakowania modułów PrestaShop.

Skill prowadzi pracę nad modułem w sposób:

- praktyczny,
- etapowy,
- bezpieczny,
- możliwy do przekazania Codex/Replit,
- możliwy do kontroli w VS Code,
- możliwy do testowania,
- możliwy do cofnięcia przez backup lub Git.

S001 nie jest tylko opisem technicznym.  
S001 jest procedurą pracy nad modułem.

---

## 3. Najważniejsza zasada

Nie wolno przenosić ograniczeń z jednego modułu na wszystkie kolejne projekty.

Każdy moduł ma własny kontekst.

Przykład:

Zasada „nie ruszać API” mogła dotyczyć konkretnego modułu DPD, bo API było już wcześniej dobrze wykonane.  
Nie oznacza to, że każdy nowy moduł ma mieć zakaz pracy nad API.

Dla każdego modułu S001 musi osobno ustalić:

- co już istnieje,
- co działa dobrze,
- czego nie wolno ruszać,
- co można przebudować,
- czy API jest częścią zadania,
- czy baza danych jest częścią zadania,
- czy Front Office jest częścią zadania,
- czy Back Office jest częścią zadania,
- czy moduł ma działać automatycznie,
- czy moduł ma działać tylko po ręcznej akcji administratora.

---

## 4. Tryby pracy

### 4.1. NOWY MODUŁ

Użyj, gdy moduł jeszcze nie istnieje albo zaczynamy od zera.

Wynik:

- plan MVP,
- struktura modułu,
- prompt wykonawczy,
- test instalacji,
- przygotowanie ZIP.

### 4.2. ROZWÓJ MODUŁU

Użyj, gdy moduł już istnieje i dodajemy funkcję.

Wynik:

- zakres zmiany,
- lista plików do modyfikacji,
- lista plików zakazanych,
- test regresji.

### 4.3. DEBUG

Użyj, gdy moduł ma konkretny błąd.

Wynik:

- diagnoza,
- minimalna poprawka,
- test błędu,
- raport ryzyka regresji.

Jeżeli debug staje się złożony, użyj S002.

### 4.4. AUDYT

Użyj, gdy trzeba ocenić jakość modułu.

Wynik:

- ocena 1–10,
- lista błędów,
- priorytety poprawek,
- decyzja, czy moduł nadaje się do instalacji lub produkcji.

Pełny audyt wykonuje S002.

### 4.5. ZIP

Użyj, gdy moduł ma zostać spakowany do instalacji.

Wynik:

- sprawdzona struktura,
- usunięte pliki robocze,
- gotowa paczka ZIP,
- raport paczkowania.

---

## 5. S001 LIGHT i S001 PRO

### 5.1. S001 LIGHT

Tryb szybki.

Używany, gdy zadanie jest proste albo użytkownik chce szybko działać.

Schemat:

```text
1. Cel
2. MVP
3. Prompt
4. Test
5. Następny krok
```

Użycie:

```text
S001 light — zrób prompt do prostego modułu
S001 light — napisz plan MVP
S001 light — przygotuj ZIP checklistę
```

### 5.2. S001 PRO

Tryb pełny.

Używany, gdy moduł jest większy, ryzykowny albo ma trafić do realnej pracy.

Schemat:

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

Użycie:

```text
S001 pro — zaplanuj moduł od zera
S001 pro — przygotuj pracę dla Codex
S001 pro — rozbuduj istniejący moduł
```

---

## 6. Formularz startowy modułu

Przed rozpoczęciem pracy S001 powinien zebrać lub uporządkować dane:

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

Jeżeli użytkownik nie poda wszystkich danych, S001 nie blokuje pracy.  
S001 przyjmuje rozsądne założenia i oznacza je jako założenia.

---

## 7. Podział zakresu

Każdy moduł należy podzielić na:

### MVP

Funkcje konieczne do pierwszej działającej wersji.

### PRO

Funkcje przydatne po działającym MVP.

### PÓŹNIEJ

Funkcje odkładane, żeby nie blokować startu.

S001 ma chronić pracę przed nadmiernym rozrostem zakresu.

---

## 8. Standard etapów pracy

### Etap 1 — Cel i MVP

Ustalić, co ma działać jako pierwsza wersja.

### Etap 2 — Architektura

Ustalić strukturę modułu, główne pliki, hooki, kontrolery, SQL i widoki.

### Etap 3 — Prompt wykonawczy

Przygotować polecenie dla Codex/Replit/VS Code.

### Etap 4 — Test

Sprawdzić instalację, działanie, logi i strukturę.

### Etap 5 — ZIP i raport

Przygotować paczkę oraz raport końcowy.

---

## 9. Zasada anty-chaosu

S001 nie może bez potrzeby rozbudowywać pracy.

Dla małego modułu:

```text
1. Plan
2. Kod
3. Test
4. ZIP
```

Dla średniego modułu:

```text
1. MVP
2. Test MVP
3. Funkcje PRO
4. Test regresji
5. ZIP
```

Dla dużego modułu:

```text
1. Analiza
2. MVP
3. Moduły funkcjonalne
4. Testy częściowe
5. Test całości
6. Dokumentacja
7. ZIP
```

Jeżeli projekt zaczyna robić się zbyt duży, S001 ma zaproponować cięcie zakresu.

---

## 10. Podział ról

### ChatGPT

Odpowiada za:

- plan,
- architekturę,
- prompt dla Codex/Replit,
- analizę błędów,
- checklisty,
- dokumentację,
- kontrolę jakości,
- decyzje projektowe.

### Codex / Replit

Odpowiada za:

- edycję plików,
- tworzenie kodu,
- poprawki techniczne,
- uruchamianie testów,
- przygotowanie raportu zmian,
- budowę paczki ZIP, jeśli środowisko na to pozwala.

### VS Code

Służy do:

- przeglądania plików,
- ręcznej kontroli,
- pracy z terminalem,
- commitów Git,
- sprawdzania struktury,
- lokalnego testowania.

---

## 11. Skala ryzyka

### 11.1. Niskie ryzyko

Przykłady:

- zmiana tekstu,
- README,
- CSS,
- drobny widok,
- proste pole konfiguracji.

Wymaganie:

```text
Zwykły backup.
```

### 11.2. Średnie ryzyko

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

### 11.3. Wysokie ryzyko

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

## 12. Backup, Git i rollback

### 12.1. Przed zmianą

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

### 12.2. Nazwy backupów

```text
modulename_backup_YYYY-MM-DD_HH-MM
modulename_before_debug_YYYY-MM-DD_HH-MM
modulename_before_bo_panel_YYYY-MM-DD_HH-MM
modulename_before_api_change_YYYY-MM-DD_HH-MM
```

### 12.3. Nazwy commitów

```text
backup: stable module before new feature
fix: repair admin token validation
feat: add back office panel
test: add install and zip checks
docs: update module README
refactor: clean module structure without behavior change
```

### 12.4. Rollback

```text
1. Nie dodawaj kolejnych funkcji.
2. Cofnij ostatnią zmianę lub przywróć backup.
3. Sprawdź, czy stara wersja działa.
4. Dopiero potem wykonaj mniejszą poprawkę.
5. Opisz, co spowodowało problem.
```

---

## 13. System wersjonowania modułów

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

## 14. Standard struktury modułu

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

Nie każdy moduł musi mieć wszystkie foldery.  
S001 dobiera strukturę do zakresu i nie tworzy zbędnych elementów.

---

## 15. Standard promptu dla Codex/Replit

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

## 16. Prompt — nowy moduł od zera

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie NOWY MODUŁ.

CEL:
Stwórz nowy moduł PrestaShop od zera.

KONTEKST:
Moduł ma być osobnym, instalowalnym modułem PrestaShop.
Nie modyfikuj core PrestaShop.
Nie twórz override, chyba że zostanie to wyraźnie uzasadnione i zaakceptowane.
Moduł ma być możliwy do spakowania jako ZIP.

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
7. Przygotuj README.
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
- jak nazywa się ZIP.
```

---

## 17. Prompt — rozwój istniejącego modułu

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

## 18. Prompt — debug błędu

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie DEBUG.

CEL:
Napraw konkretny błąd w module PrestaShop.

ZASADA GŁÓWNA:
Nie dodawaj nowych funkcji.
Nie przepisuj całego modułu.
Nie przebudowuj architektury bez konieczności.
Najpierw znajdź przyczynę, potem wykonaj minimalną poprawkę.

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
- co jeszcze trzeba sprawdzić.
```

---

## 19. Prompt — audyt modułu

```text
Użyj S001 — MODUŁ BUILDER PRO w trybie AUDYT.

CEL:
Przeprowadź audyt modułu PrestaShop.

ZAKRES AUDYTU:
1. Struktura modułu.
2. Zgodność z PrestaShop.
3. Instalacja.
4. Odinstalowanie.
5. Back Office.
6. Front Office.
7. SQL.
8. Hooki.
9. Kontrolery.
10. Tokeny.
11. Uprawnienia.
12. Bezpieczeństwo.
13. Wydajność.
14. ZIP.
15. Dokumentacja.

ZASADY:
Nie zmieniaj kodu podczas audytu, chyba że użytkownik wyraźnie poprosi o poprawki.
Najpierw przygotuj raport.
Podziel błędy według ważności.

KLASYFIKACJA BŁĘDÓW:
KRYTYCZNE — blokują instalację lub działanie.
WAŻNE — mogą powodować błędy lub ryzyko bezpieczeństwa.
ŚREDNIE — wymagają poprawy, ale nie blokują działania.
DROBNE — estetyka, porządek, dokumentacja.

RAPORT:
Podaj:
1. Ocena ogólna 1–10.
2. Błędy krytyczne.
3. Błędy ważne.
4. Błędy średnie.
5. Błędy drobne.
6. Co jest dobre.
7. Co trzeba poprawić najpierw.
8. Czy moduł nadaje się do instalacji.
9. Czy moduł nadaje się do produkcji.
10. Zalecany następny krok.
```

---

## 20. Prompt — pakowanie ZIP

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

CHECKLISTA ZIP:
[ ] Jeden folder główny modułu.
[ ] Główny plik modułu w folderze.
[ ] Brak podwójnego zagnieżdżenia.
[ ] Brak .git.
[ ] Brak cache.
[ ] Brak tmp.
[ ] Brak node_modules.
[ ] Brak plików roboczych.
[ ] README obecny.
[ ] Wersja modułu ustawiona.
[ ] ZIP gotowy do instalacji.

RAPORT:
Podaj:
- nazwę ZIP,
- strukturę ZIP,
- usunięte pliki,
- wynik kontroli,
- czy paczka nadaje się do instalacji.
```

---

## 21. Raport Codex/Replit do ChatGPT

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

## 22. Checklisty testowe

### 22.1. Test struktury ZIP

```text
[ ] ZIP zawiera jeden główny folder modułu.
[ ] Główny plik modułu jest w folderze modułu.
[ ] Nazwa folderu i głównego pliku są zgodne.
[ ] Nie ma zbędnego folderu nadrzędnego.
[ ] Nie ma plików .git, node_modules, cache, tmp.
[ ] Katalogi mają index.php zabezpieczający.
```

### 22.2. Test instalacji

```text
[ ] Moduł pojawia się w Module Manager.
[ ] Moduł instaluje się bez błędu.
[ ] Moduł tworzy potrzebne tabele.
[ ] Moduł dodaje potrzebne zakładki BO.
[ ] Moduł rejestruje hooki.
[ ] Moduł odinstalowuje się bez błędu.
```

### 22.3. Test Back Office

```text
[ ] Zakładka BO otwiera się bez błędu 500.
[ ] Formularze mają token.
[ ] Akcje POST są zabezpieczone.
[ ] Pracownik bez uprawnień nie może wykonać akcji.
[ ] Komunikaty błędów są czytelne.
[ ] Lista danych ładuje się szybko.
```

### 22.4. Test Front Office

```text
[ ] Hook wyświetla się w dobrym miejscu.
[ ] Szablon nie psuje motywu.
[ ] CSS jest ograniczony do modułu.
[ ] JS nie powoduje konfliktów.
[ ] Moduł działa na telefonie.
```

### 22.5. Test debugowania

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

## 23. Komendy S001

### 23.1. Komendy główne

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
```

### 23.2. Komendy skrócone

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
```

### 23.3. Przykłady

```text
S001 start moduł rezerwacji łowiska
S001 mvp panel zamówień
S001 debug błąd 500 w zakładce BO
S001 prompt codex dodaj konfigurację modułu
S001 zip dpdpackoffice
S001 stop-chaos ogranicz moduł do MVP
```

---

## 24. Miniściąga S001 — szybkie użycie

### Najczęstsze użycie

```text
S001 start [nazwa modułu]
```

Rozpoczęcie nowego modułu.

```text
S001 mvp [opis modułu]
```

Ograniczenie pomysłu do pierwszej działającej wersji.

```text
S001 prompt codex [zakres]
```

Przygotowanie gotowego promptu dla Codex/Replit.

```text
S001 debug [błąd]
```

Naprawa konkretnego błędu w module.

```text
S001 audyt [moduł]
```

Ocena jakości modułu.

```text
S001 zip [nazwa modułu]
```

Przygotowanie paczki ZIP.

```text
S001 stop-chaos
```

Zatrzymanie nadmiernego planowania i ograniczenie zakresu.

### Szybki schemat pracy

```text
1. S001 start
2. S001 mvp
3. S001 prompt codex
4. Codex wykonuje
5. Codex zwraca raport
6. S001 test
7. S001 zip
8. S001 raport
```

---

## 25. Szablon promptu „wklej do Codex”

```text
Użyj S001 — MODUŁ BUILDER PRO.

CEL:
[Wpisz, co ma zostać wykonane]

KONTEKST:
Pracujemy nad modułem PrestaShop.
Moduł ma być zgodny z PrestaShop 8/9, z priorytetem PrestaShop 9.
Nie modyfikuj core PrestaShop.
Nie wykonuj zmian poza zakresem.
Nie przepisuj całego modułu, jeśli nie jest to konieczne.
Dbaj o strukturę ZIP i możliwość instalacji modułu.

TRYB PRACY:
[Nowy moduł / Rozwój / Debug / Audyt / ZIP]

ZAKRES:
1. [punkt 1]
2. [punkt 2]
3. [punkt 3]

CZEGO NIE RUSZAĆ:
1. [plik/funkcja/obszar]
2. [plik/funkcja/obszar]
3. [plik/funkcja/obszar]

CO MOŻNA ZMIENIAĆ:
1. [plik/funkcja/obszar]
2. [plik/funkcja/obszar]
3. [plik/funkcja/obszar]

WYMAGANIA TECHNICZNE:
1. Zachowaj poprawną strukturę modułu PrestaShop.
2. Główny plik modułu ma być w folderze modułu.
3. Folder i główny plik modułu muszą mieć zgodną nazwę.
4. Dodaj lub zachowaj index.php zabezpieczające katalogi.
5. Formularze POST zabezpiecz tokenem.
6. Waliduj dane wejściowe.
7. Sprawdź uprawnienia pracownika Back Office.
8. Nie zapisuj haseł, tokenów ani danych wrażliwych w logach.
9. Nie dodawaj zbędnych bibliotek.
10. Nie twórz funkcji spoza zakresu.

BACKUP:
Przed zmianami wykonaj backup lub upewnij się, że jest commit Git.
Nie nadpisuj działającej wersji bez możliwości powrotu.

TESTY:
1. Sprawdź instalację modułu.
2. Sprawdź odinstalowanie, jeśli zmieniano install/uninstall.
3. Sprawdź Back Office, jeśli moduł ma BO.
4. Sprawdź Front Office, jeśli moduł ma FO.
5. Sprawdź logi PHP/PrestaShop.
6. Sprawdź strukturę ZIP, jeśli przygotowujesz paczkę.
7. Sprawdź, czy nie zepsułeś wcześniejszych funkcji.

RAPORT PO ZAKOŃCZENIU:
Zwróć raport:

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

---

## 26. Współpraca z S002

S001 odpowiada za budowę i prowadzenie modułu.

S002 odpowiada za głęboki audyt, debugowanie i analizę problemów.

### 26.1. Kiedy zostać przy S001

Zostań przy S001, gdy:

- tworzymy moduł,
- planujemy MVP,
- piszemy prompt dla Codex,
- pakujemy ZIP,
- dodajemy funkcję,
- wykonujemy prostą poprawkę.

### 26.2. Kiedy przejść do S002

Przejdź do S002, gdy:

- błąd jest trudny,
- błąd wraca po poprawkach,
- nie wiadomo, gdzie jest przyczyna,
- moduł ma kilka błędów naraz,
- potrzebny jest dokładny audyt,
- trzeba analizować logi, SQL, kontrolery, tokeny i hooki razem.

Komenda przejścia:

```text
S002 przejmij debug z S001
```

albo:

```text
S002 audyt modułu po S001
```

---

## 27. Standard oceny modułu 1–10

S001 ocenia moduł według punktacji.

### 27.1. Kategorie oceny

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

### 27.2. Interpretacja oceny

```text
10/10 — moduł bardzo dobry, gotowy produkcyjnie.
9/10 — moduł bardzo mocny, wymaga drobnych poprawek.
8/10 — moduł dobry, ale wymaga testów i porządków.
7/10 — moduł działa częściowo, ale ma istotne braki.
6/10 — moduł ryzykowny, wymaga większych poprawek.
5/10 — moduł słaby, możliwy tylko jako prototyp.
4/10 — moduł problematyczny, wymaga przebudowy.
3/10 — moduł ma błędy krytyczne.
2/10 — moduł prawie nieużywalny.
1/10 — moduł nie nadaje się do pracy.
```

### 27.3. Automatyczna decyzja po ocenie

```text
9.0–10.0 — można pakować ZIP lub robić finalny test.
8.0–8.9 — poprawić wskazane braki i testować.
7.0–7.9 — wrócić do MVP i naprawić kluczowe elementy.
6.0–6.9 — przekazać do S002 na audyt/debug.
1.0–5.9 — nie rozwijać dalej, najpierw naprawić fundament.
```

---

## 28. Minimalna definicja gotowego modułu

Moduł można uznać za gotowy dopiero wtedy, gdy spełnia minimalny standard gotowości.

### 28.1. Moduł gotowy do testu

```text
[ ] Ma poprawną strukturę folderów.
[ ] Ma główny plik modułu w folderze modułu.
[ ] Instaluje się w PrestaShop.
[ ] Nie powoduje błędu 500.
[ ] Główna funkcja MVP jest dostępna.
[ ] Nie ma oczywistych błędów PHP.
[ ] Da się wskazać, co jeszcze wymaga poprawy.
```

### 28.2. Moduł gotowy do ZIP

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

### 28.3. Moduł gotowy produkcyjnie

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

## 29. Najczęstsze błędy Codex/Replit przy modułach PrestaShop

S001 musi pilnować typowych błędów wykonawczych.

### 29.1. Błędy struktury

```text
[ ] Główny plik modułu poza folderem modułu.
[ ] Podwójne zagnieżdżenie folderu w ZIP.
[ ] Zła nazwa klasy modułu.
[ ] Zła nazwa folderu względem pliku głównego.
[ ] Brak index.php w katalogach.
[ ] Pakowanie całego projektu zamiast samego modułu.
```

### 29.2. Błędy Back Office

```text
[ ] Brak tokena w formularzu.
[ ] Brak sprawdzenia uprawnień.
[ ] Błędny kontroler admina.
[ ] Błąd routingu Symfony/Legacy.
[ ] Użycie niewłaściwej metody tłumaczeń.
[ ] Formularz POST wykonuje akcję bez walidacji.
```

### 29.3. Błędy SQL

```text
[ ] Tabele bez prefiksu PrestaShop.
[ ] Brak uninstall dla tabel.
[ ] Niezgodna składnia MariaDB/MySQL.
[ ] Brak walidacji danych przed zapisem.
[ ] Brak obsługi błędu zapisu.
[ ] Nadpisywanie danych bez backupu.
```

### 29.4. Błędy bezpieczeństwa

```text
[ ] Logowanie tokenów/API key.
[ ] Brak walidacji danych z formularza.
[ ] Brak escape w widokach.
[ ] Brak kontroli uprawnień BO.
[ ] Akcje GET zmieniają dane.
[ ] Zbyt szerokie operacje bez potwierdzenia.
```

### 29.5. Błędy zakresu

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
- udawać, że coś zostało przetestowane, jeśli testu nie wykonano.

---

## 31. Zasada zakończenia etapu

Etap można zakończyć, gdy:

- jest konkretny wynik,
- wynik nadaje się do użycia,
- nie ma błędu krytycznego,
- użytkownik wie, co zrobić dalej.

Etapu nie można zakończyć, gdy:

- nie wiadomo, co powstało,
- nie ma pliku, promptu, testu lub raportu,
- są błędy krytyczne,
- nie wiadomo, co dalej,
- wynik jest tylko ogólnym opisem.

---

## 32. Raport po każdym etapie

Po każdym etapie S001 ma zwrócić raport:

```text
RAPORT ETAPU:

Etap:
Status:
Co zostało ustalone:
Co zostało wykonane:
Co wymaga decyzji:
Ryzyka:
Następny krok:
Ocena jakości:
Procent ukończenia:
Lista rzeczy do poprawy:
```

---

## 33. Domyślny sposób odpowiedzi S001

Każda odpowiedź S001 powinna zawierać:

```text
1. Co robimy teraz
2. Decyzja / wynik
3. Konkretna treść do użycia
4. Następny krok
5. Procent ukończenia
6. Ocena własna
7. Co poprawić dalej
```

---

## 34. Finalny schemat działania S001

```text
1. Rozpoznaj tryb pracy.
2. Ustal cel.
3. Ogranicz zakres do MVP.
4. Oceń ryzyko.
5. Wymuś backup.
6. Przygotuj prompt lub plan.
7. Wykonaj / przekaż do wykonania.
8. Zrób test.
9. Zrób raport.
10. Nadaj wersję.
11. Zdecyduj: poprawka, PRO, ZIP albo koniec.
```

---

## 35. Changelog S001

### S001 v0.1

Pierwsza wersja koncepcyjna.

Dodano:

- rolę skilla,
- podstawowe tryby pracy,
- ogólny prompt,
- podstawowe testy.

### S001 v0.2

Wersja zgodna z kierunkiem S000.

Dodano:

- backup,
- wersjonowanie,
- raport po etapie,
- podział ChatGPT / Codex / VS Code,
- tryb debug.

### S001 v0.3

Wersja operacyjna.

Dodano:

- matrycę decyzyjną,
- skalę ryzyka,
- prompty dla Codex/Replit,
- raport Codex → ChatGPT,
- procedurę rollback.

### S001 v1.0

Wersja roboczo-finalna.

Dodano:

- S001 LIGHT,
- S001 PRO,
- skrócone komendy,
- współpracę z S002,
- pełną strukturę skilla.

### S001 v1.1

Wersja produkcyjna po domknięciu.

Dodano:

- miniściągę,
- prompt „wklej do Codex”,
- standard oceny modułu 1–10,
- minimalną definicję gotowego modułu,
- listę typowych błędów Codex/Replit,
- changelog.

---

## 36. Cel finalny S001

S001 ma doprowadzić do tego, żeby praca nad modułem PrestaShop była:

- szybsza,
- bezpieczniejsza,
- mniej chaotyczna,
- łatwiejsza dla Codex/Replit,
- łatwiejsza do testowania,
- łatwiejsza do cofnięcia,
- możliwa do powtarzania przy kolejnych modułach.

S001 ma pomagać tworzyć realne moduły, a nie tylko planować ich tworzenie.
