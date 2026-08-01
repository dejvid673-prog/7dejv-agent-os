# AGENTS.md — nadrzędna instrukcja repozytorium 7DEJV

## 1. Rola repozytorium

To repozytorium jest repozytorium sterującym 7DEJV OS. Przechowuje zasady globalne, etapy migracji, audyty, dokumentację, konfigurację pracy Codexa i rejestr narzędzi.

Źródłem prawdy dla skilli, agentów i workflow pozostaje repozytorium `7dejv-skills-prompts`. Katalog `.agents/skills` w tym repozytorium jest kontrolowaną kopią wykonawczą wybranych skilli, a nie trzecią niezależną biblioteką.

## 2. Obowiązkowa kolejność pracy

Przed każdą zmianą Codex musi:

1. potwierdzić katalog roboczy i repozytorium,
2. odczytać ten plik `AGENTS.md`,
3. sprawdzić `git status --short`, bieżącą gałąź i `git remote -v`,
4. odczytać dokument etapu migracji oraz właściwy audyt,
5. uruchomić kontrolę startową repozytorium,
6. uruchomić `codex-workflow-router`,
7. wskazać wybrany skill, workflow, zakres plików, ryzyka i testy,
8. dopiero po zaliczeniu kontroli startowej rozpocząć modyfikację.

Jeżeli kontrola startowa nie została wykonana albo zakończyła się błędem, Codex ma odmówić zapisu i podać przyczynę blokady.

## 3. Format rozpoczęcia większego zadania

Codex ma przed zmianą zapisać:

```text
Etap migracji:
Typ zadania:
Repozytorium:
Kontrola startowa:
Wybrany router:
Wybrany skill:
Wybrany workflow lub agent:
Zakres plików:
Plan:
Testy:
Ryzyka:
Warunki odmowy:
```

Nie wolno zgadywać ścieżek, API, klas, hooków, tabel, statusów ani istnienia narzędzi. Najpierw należy sprawdzić rzeczywiste pliki.

## 4. Zasady MIG-003

Aktualny etap to `MIG-003`: selekcja narzędzi, uporządkowanie struktury i przygotowanie bezpiecznej migracji.

W MIG-003 wolno:

- audytować i klasyfikować narzędzia,
- poprawiać strukturę i dokumentację,
- wdrażać kontrolę startową, router, hooks i walidator,
- kopiować zweryfikowane skille do kanonicznej kopii wykonawczej,
- wykonywać testy i porównania plików.

W MIG-003 nie wolno:

- usuwać zatwierdzonych kandydatów na duplikaty,
- usuwać całych pakietów archiwalnych,
- usuwać aktywnych kopii z `C:\Users\Gez\.codex\skills`,
- usuwać innych repozytoriów Git,
- usuwać plików z niezapisanymi zmianami,
- usuwać `pond-rd-lab` ani `prestashop-module-builder`,
- uznawać podobnych nazw za identyczną zawartość bez porównania SHA-256.

Fizyczne usuwanie duplikatów należy wyłącznie do `MIG-004`.

## 5. Podstawowy zestaw skilli

Pierwszeństwo audytu i wdrożenia mają:

1. `codex-workflow-router`,
2. `7dejv-pond-rd-lab`,
3. `7dejv-product-graphics-builder-pro`,
4. `7dejv-brand-identity-builder`,
5. `7dejv-graphic-auditor`.

`prestashop-module-builder` jest chroniony przed usunięciem, nawet jeśli nie należy do pierwszej piątki wdrażanej w MIG-003.

Skill można oznaczyć jako aktywny tylko wtedy, gdy posiada poprawny `SKILL.md`, zgodny `name`, jednoznaczny `description`, poprawne referencje oraz przechodzi wymagane testy.

Plik Markdown opisujący rolę, personę lub procedurę nie jest natywnym skillem ani agentem Codexa. Profile Markdown pozostają dokumentacją, dopóki wybrana rola nie zostanie świadomie przekształcona do `.codex/agents/*.toml` i zweryfikowana.

## 6. Klasyfikacja narzędzi

Każde rozpoznane narzędzie lub dokument otrzymuje jeden status:

- `PRODUCTION` — gotowe i zweryfikowane,
- `SPECIALIZED` — poprawne, ale przeznaczone do określonej klasy zadań,
- `LAB` — eksperymentalne,
- `HOLD` — tymczasowo wstrzymane,
- `LEGACY` — historyczne i nieaktywne,
- `CONVERSION CANDIDATE` — wartościowy dokument wymagający przebudowy,
- `REJECTED` — błędne, puste, niebezpieczne albo podszywające się pod narzędzie.

Status `REJECTED` w MIG-003 nie oznacza zgody na fizyczne usunięcie.

## 7. Obowiązkowa kontrola skilla

Przed wdrożeniem skilla sprawdzić:

- obecność i poprawność `SKILL.md`,
- zgodność `name` z nazwą katalogu,
- jednoznaczność `description`,
- warunki użycia i zakończenia,
- wszystkie referencje do plików i narzędzi,
- brak sekretów, danych klientów i podejrzanych instrukcji,
- poprawność Python, JSON, YAML i TOML,
- zakres dozwolonych operacji,
- testy wymagane przed uznaniem za aktywny.

Nie wolno oznaczyć skilla jako `PRODUCTION` bez dowodu testów.

## 8. Minimalny zakres zmian

Codex ma:

- pracować etapami,
- ograniczać zmianę do zatwierdzonego zakresu,
- nie wykonywać szerokiego refaktoru bez uzasadnienia,
- nie zmieniać działających elementów poza zakresem,
- nie dodawać ciężkich zależności bez potrzeby,
- zatrzymać pracę przy konflikcie instrukcji, utracie danych albo braku dostępu do wymaganego źródła prawdy.

## 9. Bezpieczeństwo

Zakazane jest zapisywanie w repozytorium:

- haseł,
- tokenów,
- kluczy API,
- danych klientów,
- sekretów środowiskowych,
- produkcyjnych eksportów zawierających dane poufne.

Nie wykonywać automatycznie operacji destrukcyjnych, takich jak `git reset --hard`, `git clean -fd`, wymuszony push, masowe usuwanie albo nadpisanie historii.

## 10. Zakończenie każdego etapu

Każdy etap musi zakończyć się:

1. testami adekwatnymi do zmiany,
2. audytem wyniku i bezpieczeństwa,
3. `git status --short`,
4. `git diff`,
5. `git diff --check`,
6. raportem zawierającym zmienione pliki, testy wykonane i niewykonane, wyniki, ryzyka oraz stan kryteriów akceptacji,
7. lokalnym commitem zabezpieczającym.

Commit nie może być traktowany jako dowód poprawności bez wyników testów.

## 11. Format raportu końcowego

```text
Etap:
Status:
Zmodyfikowane pliki:
Wybrane narzędzia:
Testy wykonane:
Testy niewykonane:
Wyniki:
Git diff:
Ryzyka i ograniczenia:
Kryteria akceptacji:
Commit lokalny:
Następny krok:
```

Codex nie może deklarować pełnego zakończenia MIG-003, dopóki test czystej sesji nie potwierdzi, że sam odczytuje instrukcje, uruchamia router, wybiera właściwy skill, wykonuje testy i odmawia modyfikacji po niezaliczonej kontroli startowej.
