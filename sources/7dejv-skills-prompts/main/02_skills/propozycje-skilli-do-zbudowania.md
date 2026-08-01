# Propozycje skilli do zbudowania — 7DEJV

Data: 2026-06-12

## Cel

Przygotować listę skilli, które mogą przydać się w kolejnych pracach 7DEJV: GitHub, PrestaShop, STAW EXPERT, grafiki, badania, produkty i kontrola jakości.

## Priorytet A — skille najpilniejsze

### 1. `7dejv-repo-auditor`

Cel: audyt repozytorium bez wprowadzania zmian.

Zastosowanie:

- sprawdzenie struktury repo,
- wykrycie niepasujących plików,
- wykrycie braków w README/TODO/DECISIONS/CHANGELOG,
- raport przed migracją.

Status: do zbudowania.

### 2. `7dejv-github-sync-guard`

Cel: bezpieczna kontrola lokalnego repo po zmianach na GitHub.

Zastosowanie:

- sprawdzenie `git status`,
- sprawdzenie `remote origin`,
- instrukcja `fetch/pull`,
- ostrzeżenie przed ponownym klonowaniem i duplikatami.

Status: do zbudowania.

### 3. `7dejv-codex-safety-gate`

Cel: wymuszenie trybu: najpierw audyt i raport, potem zmiany.

Zastosowanie:

- praca z Codex,
- repozytoria techniczne,
- moduły PrestaShop,
- ryzykowne migracje.

Status: do zbudowania.

### 4. `7dejv-prestashop-error-cataloger`

Cel: katalogowanie błędów PrestaShop z podziałem na Symfony, PHP, MySQL, Back Office, moduły i API.

Zastosowanie:

- błędy HTTP 500,
- błędy modułów,
- błędy tokenów,
- błędy DPD API,
- błędy instalacji.

Status: do zbudowania.

### 5. `7dejv-prestashop-test-checklist-builder`

Cel: tworzenie checklist testów dla modułów i Back Office.

Zastosowanie:

- test instalacji modułu,
- test odinstalowania,
- test widoku zamówienia,
- test uprawnień,
- test logów,
- test braku danych wrażliwych.

Status: do zbudowania.

## Priorytet B — STAW EXPERT

### 6. `7dejv-staw-expert-market-researcher`

Cel: prowadzenie badań rynku oczek wodnych i stawów.

Zastosowanie:

- baza problemów klientów,
- produkty konkurencji,
- firmy i marki,
- ceny,
- opinie,
- sezonowość.

Status: do zbudowania.

### 7. `7dejv-competitor-product-database-builder`

Cel: budowa tabeli produktów konkurencji.

Zastosowanie:

- marka,
- produkt,
- problem klienta,
- cena,
- pojemność,
- skład,
- obietnica marketingowa,
- źródło.

Status: do zbudowania.

### 8. `7dejv-juniewicz-company-researcher`

Cel: osobna analiza firmy z Juniewicz.

Zastosowanie:

- produkty,
- pozycja rynkowa,
- mikroorganizmy,
- porównanie z konkurencją,
- wnioski dla STAW EXPERT.

Status: do zbudowania.

### 9. `7dejv-lab-verification-brief-builder`

Cel: przygotowanie briefu dla laboratorium.

Zastosowanie:

- pytania do laboratorium,
- wymagane badania,
- dawkowanie,
- bezpieczeństwo dla ryb,
- etykieta,
- deklaracje marketingowe.

Status: do zbudowania.

### 10. `7dejv-product-claim-safety-checker`

Cel: kontrola, czy opis produktu nie obiecuje zbyt dużo bez potwierdzenia.

Zastosowanie:

- opisy sprzedażowe,
- etykiety,
- Allegro/Erli,
- deklaracje działania,
- ostrzeżenia.

Status: do zbudowania.

## Priorytet C — grafiki i opisy

### 11. `7dejv-label-qa-auditor`

Cel: kontrola etykiety produktu.

Zastosowanie:

- czytelność,
- kompletność danych,
- dawkowanie,
- ostrzeżenia,
- spójność przodu i tyłu etykiety.

Status: do zbudowania.

### 12. `7dejv-graphics-sheet-splitter`

Cel: pilnowanie zasady dzielenia dużych grafik na arkusze.

Zastosowanie:

- plandeki,
- dokumentacje techniczne,
- grafiki z tabelami,
- etykiety z dużą ilością tekstu.

Status: do zbudowania.

### 13. `7dejv-marketplace-description-builder`

Cel: tworzenie opisów głównych, skróconych, Allegro i Erli na podstawie jednego kryterium problemu klienta.

Zastosowanie:

- opisy produktów,
- marketplace,
- sklep,
- SEO.

Status: do zbudowania.

### 14. `7dejv-seo-problem-article-builder`

Cel: tworzenie artykułów SEO opartych o problem klienta.

Zastosowanie:

- zielona woda,
- glony nitkowate,
- start po zimie,
- KH/pH,
- muł,
- tlen.

Status: do zbudowania.

## Priorytet D — organizacja pracy

### 15. `7dejv-daily-start-assistant`

Cel: przygotowanie startu dnia na podstawie statusów repo.

Zastosowanie:

- co jest aktywne,
- co jest wstrzymane,
- które repo otworzyć,
- co robić jako pierwsze.

Status: do zbudowania.

### 16. `7dejv-decision-logger`

Cel: zamiana ważnych ustaleń z rozmowy na wpis do `DECISIONS.md`.

Zastosowanie:

- repozytoria,
- moduły,
- produkty,
- skille,
- grafiki,
- badania.

Status: do zbudowania.

### 17. `7dejv-prompt-card-builder`

Cel: zamiana luźnego promptu w kartę promptu zgodną z szablonem repo.

Zastosowanie:

- kategoria,
- wersja,
- status,
- cel,
- dane wejściowe,
- wynik,
- treść promptu.

Status: do zbudowania.

### 18. `7dejv-skill-auditor`

Cel: audyt istniejącego skilla i decyzja: zostawić, poprawić, scalić, zarchiwizować.

Zastosowanie:

- duplikaty skilli,
- skille graficzne,
- skille PrestaShop,
- skille badawcze.

Status: do zbudowania.

## Priorytet E — bezpieczeństwo i higiena pracy AI

### 19. `7dejv-sensitive-data-checker`

Cel: sprawdzanie, czy w materiale nie ma haseł, tokenów, danych klientów, danych zamówień lub prywatnych logów.

Zastosowanie:

- repozytoria,
- raporty błędów,
- konfiguracje,
- prompty dla Codex.

Status: do zbudowania.

### 20. `7dejv-ai-tool-risk-checker`

Cel: ocena, czy nowe narzędzie, paczka, aplikacja albo integracja AI jest bezpieczna przed użyciem.

Zastosowanie:

- narzędzia do Codex,
- aplikacje z internetu,
- rozszerzenia,
- paczki npm/Python,
- integracje GitHub.

Status: do zbudowania.

## Rekomendowana kolejność budowy

1. `7dejv-repo-auditor`
2. `7dejv-codex-safety-gate`
3. `7dejv-prestashop-error-cataloger`
4. `7dejv-staw-expert-market-researcher`
5. `7dejv-competitor-product-database-builder`
6. `7dejv-prompt-card-builder`
7. `7dejv-skill-auditor`

## Zasada

Nie budować wszystkich skilli naraz. Najpierw tworzyć te, które realnie obsłużą najbliższą pracę.
