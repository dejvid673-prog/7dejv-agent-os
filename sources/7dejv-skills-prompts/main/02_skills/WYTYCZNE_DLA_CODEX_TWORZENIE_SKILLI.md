# WYTYCZNE DLA CODEX — TWORZENIE SKILLI 7DEJV

Data utworzenia: 2026-06-13
Status: `v0.1 — instrukcja główna do testu`

## Cel pliku

Ten dokument jest główną instrukcją dla Codex, gdy ma przygotowywać nowe skille dla systemu 7DEJV.

Codex ma na podstawie tego pliku tworzyć skille w sposób uporządkowany, bezpieczny i zgodny z aktualną mapą repozytoriów.

## Najważniejsza zasada

Codex nie ma tworzyć skilli chaotycznie.

Każdy skill musi mieć:

- jasny cel,
- kategorię,
- status,
- wersję,
- zakres działania,
- ograniczenia,
- dane wejściowe,
- oczekiwany wynik,
- procedurę działania,
- zasady kontroli jakości,
- kryteria testu,
- decyzję, kiedy skill jest gotowy.

## Repozytorium docelowe

Wszystkie skille trafiają do repo:

```text
7dejv-skills-prompts
```

Nie zapisywać skilli jako głównego źródła w:

- `7dejv-ai-command-center`,
- `7dejv-prestashop`,
- `7dejv-staw-expert`,
- `7dejv-dawid`.

W innych repo mogą być tylko linki, wzmianki albo informacje, że skill znajduje się w `7dejv-skills-prompts`.

## Aktualna struktura skilli

Skille zapisywać w katalogu:

```text
02_skills/
```

Dostępne kategorie:

```text
02_skills/graphics/
02_skills/prestashop/
02_skills/research/
02_skills/product-description/
02_skills/quality-control/
```

Jeżeli skill nie pasuje do żadnej kategorii, Codex nie tworzy nowej kategorii automatycznie. Najpierw ma wpisać w raporcie: `WYMAGA DECYZJI — nowa kategoria`.

## Nazewnictwo plików

Nazwa pliku skilla ma być krótka, techniczna i bez polskich znaków.

Format:

```text
7dejv-nazwa-skilla.md
```

Przykłady:

```text
7dejv-repo-auditor.md
7dejv-codex-safety-gate.md
7dejv-prestashop-error-cataloger.md
7dejv-staw-expert-market-researcher.md
7dejv-competitor-product-database-builder.md
7dejv-skill-auditor.md
```

Nie używać nazw typu:

```text
nowy skill.md
skill poprawiony.md
final final.md
wersja ostatnia.md
```

## Statusy skilli

Każdy skill musi mieć jeden status:

- `v0.1 — roboczy`
- `v0.1 — do testu`
- `v0.2 — po pierwszym teście`
- `v1.0 — zatwierdzony roboczo`
- `do poprawy`
- `do scalenia`
- `do archiwizacji`
- `wstrzymany — wymaga decyzji`

Nowy skill domyślnie ma status:

```text
v0.1 — do testu
```

Nie wolno oznaczać nowego skilla jako `v1.0`, dopóki nie przejdzie testu.

## Czego Codex nie może robić podczas tworzenia skilli

Codex nie może:

- usuwać plików,
- przenosić plików bez decyzji,
- zmieniać kodu modułów PrestaShop,
- uruchamiać nieznanych skryptów,
- instalować paczek,
- zapisywać tokenów, haseł, kluczy API ani danych klientów,
- tworzyć wielu skilli naraz bez listy i priorytetów,
- nadpisywać istniejącego skilla bez audytu,
- uznawać skilla za finalny bez testu,
- mieszać w jednym skillu kilku niezależnych celów.

## Czego Codex ma pilnować

Codex ma pilnować:

1. zgodności z mapą repozytoriów,
2. rozdzielenia PrestaShop, STAW EXPERT, promptów i command center,
3. bezpieczeństwa danych,
4. czytelnej struktury pliku,
5. minimalnego zakresu skilla,
6. testowalności,
7. możliwości późniejszego audytu,
8. braku duplikatów.

## Obowiązkowe pliki do przeczytania przed tworzeniem skilli

Codex musi najpierw przeczytać:

```text
README.md
TODO.md
REPO_STATUS.md
CHANGELOG.md
DECISIONS.md
02_skills/README.md
02_skills/propozycje-skilli-do-zbudowania.md
05_templates/skill-card-template.md
07_quality-control/standard-testowania-promptow-i-skilli.md
```

Jeżeli któregoś pliku nie ma, Codex ma wpisać to w raporcie i nie zgadywać jego treści.

## Obowiązkowa struktura skilla

Każdy skill ma mieć dokładnie tę strukturę bazową:

```markdown
# 7dejv-nazwa-skilla

## Kategoria

## Status

## Cel skilla

## Kiedy używać

## Czego skill nie robi

## Dane wejściowe

## Wynik

## Procedura działania

## Format wyniku

## Zasady bezpieczeństwa

## Kryteria jakości

## Minimalny test

## Decyzja po teście

## Uwagi
```

Można dodać dodatkowe sekcje, ale nie wolno usuwać tych podstawowych.

## Opis sekcji

### `Kategoria`

Wpisać jedną z kategorii:

- `graphics`
- `prestashop`
- `research`
- `product-description`
- `quality-control`

### `Status`

Dla nowego skilla:

```text
v0.1 — do testu
```

### `Cel skilla`

Jednoznacznie opisać, jaki problem rozwiązuje skill.

Zły przykład:

```text
Pomaga w pracy.
```

Dobry przykład:

```text
Audytuje repozytorium bez wprowadzania zmian i wskazuje braki w README, TODO, REPO_STATUS, CHANGELOG oraz DECISIONS.
```

### `Kiedy używać`

Opisać konkretne sytuacje.

### `Czego skill nie robi`

To jest obowiązkowa sekcja. Ma chronić przed rozszerzaniem zakresu.

### `Dane wejściowe`

Wypisać, czego skill potrzebuje, np. nazwa repo, treść błędu, opis produktu, brief grafiki.

### `Wynik`

Opisać, co dokładnie ma powstać.

### `Procedura działania`

Lista kroków. Minimum 5 punktów.

### `Format wyniku`

Podać konkretny format Markdown, tabelę albo listę.

### `Zasady bezpieczeństwa`

Wymienić ograniczenia, np. brak danych wrażliwych, brak kodowania, brak usuwania.

### `Kryteria jakości`

Jak ocenić, czy skill zrobił dobrą robotę.

### `Minimalny test`

Opisać pierwszy test skilla.

### `Decyzja po teście`

Jedna z opcji:

- `używać dalej`,
- `poprawić`,
- `scalić`,
- `archiwizować`,
- `wstrzymać`.

## Kategorie i przykładowe zastosowania

### `quality-control`

Skille do kontroli jakości, audytu, bezpieczeństwa i organizacji.

Przykłady:

- `7dejv-repo-auditor`,
- `7dejv-codex-safety-gate`,
- `7dejv-skill-auditor`,
- `7dejv-sensitive-data-checker`.

### `prestashop`

Skille do analizy i audytu PrestaShop.

Przykłady:

- `7dejv-prestashop-error-cataloger`,
- `7dejv-prestashop-test-checklist-builder`.

Ważne: implementacja modułów jest obecnie wstrzymana. Skille PrestaShop mają wspierać audyt, dokumentację i testy, a nie pchanie kodu.

### `research`

Skille do badań rynku, konkurencji, laboratoriów i źródeł.

Przykłady:

- `7dejv-staw-expert-market-researcher`,
- `7dejv-competitor-product-database-builder`,
- `7dejv-juniewicz-company-researcher`.

### `product-description`

Skille do opisów produktów, marketplace, SEO i języka sprzedażowego.

Przykłady:

- `7dejv-marketplace-description-builder`,
- `7dejv-seo-problem-article-builder`,
- `7dejv-product-claim-safety-checker`.

### `graphics`

Skille do grafik, etykiet, plandek i kontroli tekstu.

Przykłady:

- `7dejv-label-qa-auditor`,
- `7dejv-graphics-sheet-splitter`.

## Priorytet budowy skilli

Codex ma budować skille w kolejności ustalonej w:

```text
02_skills/propozycje-skilli-do-zbudowania.md
```

Aktualna rekomendowana kolejność:

1. `7dejv-repo-auditor`
2. `7dejv-codex-safety-gate`
3. `7dejv-prestashop-error-cataloger`
4. `7dejv-staw-expert-market-researcher`
5. `7dejv-competitor-product-database-builder`
6. `7dejv-prompt-card-builder`
7. `7dejv-skill-auditor`

Jeżeli pierwsze trzy już istnieją, Codex nie ma ich tworzyć ponownie. Ma je audytować albo przejść do kolejnych.

## Kontrola duplikatów

Przed utworzeniem nowego skilla Codex musi sprawdzić, czy podobny skill już istnieje.

Szukaj po:

- nazwie,
- celu,
- kategorii,
- słowach: `auditor`, `checker`, `builder`, `cataloger`, `researcher`, `workflow`, `safety`.

Jeżeli podobny skill istnieje, Codex ma w raporcie napisać:

```text
PODOBNY SKILL ISTNIEJE — wymaga decyzji: rozbudować istniejący, scalić czy utworzyć nowy.
```

## Tryb pracy Codex

Codex ma pracować etapami:

1. Przeczytaj dokumenty startowe.
2. Sprawdź listę proponowanych skilli.
3. Sprawdź, czy skill już istnieje.
4. Wybierz maksymalnie 1–3 skille do utworzenia w jednym przebiegu.
5. Przygotuj plan.
6. Utwórz pliki skilli.
7. Zaktualizuj `TODO.md`, `REPO_STATUS.md` i `CHANGELOG.md`.
8. Wypisz raport końcowy.

## Limit jednego przebiegu

W jednym przebiegu Codex może utworzyć maksymalnie 3 nowe skille.

Jeżeli lista jest dłuższa, ma przygotować kolejność i zatrzymać się po 3.

## Aktualizacja plików po utworzeniu skilli

Po utworzeniu skilla Codex powinien zaktualizować:

```text
TODO.md
REPO_STATUS.md
CHANGELOG.md
```

Nie aktualizować innych plików bez potrzeby.

## Raport końcowy Codex

Po pracy Codex ma podać raport:

```markdown
# Raport tworzenia skilli

## Co przeczytano

## Jakie skille już istniały

## Jakie skille utworzono

## Jakie pliki zmieniono

## Jakie pliki wymagają testu

## Ryzyka

## Następny krok
```

## Minimalny prompt dla Codex

Użyj tego promptu, gdy chcesz, żeby Codex przygotował kolejne skille:

```text
Pracuj w repozytorium `7dejv-skills-prompts`.

Najpierw przeczytaj:
- README.md
- TODO.md
- REPO_STATUS.md
- CHANGELOG.md
- DECISIONS.md
- 02_skills/WYTYCZNE_DLA_CODEX_TWORZENIE_SKILLI.md
- 02_skills/propozycje-skilli-do-zbudowania.md
- 05_templates/skill-card-template.md
- 07_quality-control/standard-testowania-promptow-i-skilli.md

Twoje zadanie:
Przygotuj kolejne skille z listy priorytetowej.

Zasady:
- nie twórz więcej niż 3 skilli w jednym przebiegu,
- nie usuwaj plików,
- nie zmieniaj kodu,
- nie ruszaj repo PrestaShop,
- nie twórz duplikatów,
- każdy skill zapisz jako osobny plik `.md`,
- każdy skill musi mieć kategorię, status, cel, zakres, ograniczenia, dane wejściowe, wynik, procedurę, format wyniku, zasady bezpieczeństwa, test i decyzję po teście,
- po pracy zaktualizuj TODO.md, REPO_STATUS.md i CHANGELOG.md,
- zakończ raportem.

Jeżeli podobny skill już istnieje, nie twórz nowego. Zgłoś konflikt w raporcie.
```

## Najważniejsze ostrzeżenie

Skill ma pomagać powtarzalnie wykonywać zadanie.

Jeżeli instrukcja jest jednorazowym promptem, a nie powtarzalną procedurą, Codex ma zaproponować zapisanie jej w `01_prompts/`, a nie w `02_skills/`.

## Decyzja końcowa

Ten plik jest nadrzędną instrukcją tworzenia skilli w 7DEJV.

Jeżeli Codex ma wątpliwość, ma zatrzymać się i napisać:

```text
WYMAGA DECYZJI UŻYTKOWNIKA
```
