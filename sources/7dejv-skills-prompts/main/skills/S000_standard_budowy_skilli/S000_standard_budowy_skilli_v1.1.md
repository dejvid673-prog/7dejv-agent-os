# S000 — STANDARD BUDOWY SKILLI 7DEJV OS
## v1.1 — AGENT + WORKFLOW READY

**Numer skilla:** S000  
**Nazwa:** Standard Budowy Skilli 7DEJV OS  
**Wersja:** v1.1  
**Typ:** skill nadrzędny / skill do pisania skilli / standard pracy agentów i workflow  
**Status:** stabilny standard bazowy rozszerzony o agentów i workflow  
**Ocena jakości:** 9.85/10

---

## 1. Definicja

S000 to nadrzędny standard tworzenia, poprawiania, oceniania, testowania, wersjonowania i katalogowania wszystkich skilli w systemie 7DEJV OS.

Od wersji v1.1 S000 jest także standardem pracy dla człowieka, ChatGPT, Codex, Replit, wykonawcy AI, dedykowanego agenta oraz workflow złożonego z wielu etapów i wielu skilli.

```text
S000 = skill do pisania skilli + standard pracy agentów i workflow
```

---

## 2. Główna zasada

Skill, agent i workflow mają pomagać działać, nie blokować pracę.

```text
MVP najpierw, PRO później.
```

Agent lub workflow ma najpierw doprowadzić do pierwszego konkretnego wyniku, a dopiero później uruchamiać audyt, rozbudowę, optymalizację i wersję PRO.

---

## 3. Definicje: agent, skill, workflow

```text
Agent = kto pracuje
Skill = jak pracuje
Workflow = w jakiej kolejności pracuje
```

**Agent** to jednostka robocza, która ma określoną rolę i może używać jednego albo wielu skilli. Agentem może być człowiek, ChatGPT, Codex/Replit, dedykowany agent AI lub automatyczny proces.

**Skill** to procedura robocza określająca, jak wykonać dany typ zadania.

**Workflow** to kolejność działań, w której agent używa jednego lub wielu skilli.

---

## 4. Kiedy używać S000

Używaj S000, gdy:

- tworzysz nowy skill,
- poprawiasz istniejący skill,
- oceniasz skill,
- tworzysz agenta,
- przypisujesz skille do agenta,
- projektujesz workflow,
- sprawdzasz, czy agent dobrze dobiera skill,
- sprawdzasz, czy workflow nie jest przeładowany,
- katalogujesz skille,
- przygotowujesz skill do backupu,
- przygotowujesz prompt dla Codex/Replit na podstawie skilla.

---

## 5. Obowiązkowa struktura każdego skilla

Każdy skill tworzony według S000 powinien mieć:

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
## 15. Agent i workflow
## 16. Test końcowy
## 17. Skala oceny
## 18. Historia zmian
```

Od wersji S000 v1.1 sekcja **Agent i workflow** jest zalecana dla każdego ważnego skilla.

---

## 6. Tryby pracy

| Tryb | Kiedy używać |
|---|---|
| Szybki | proste zadania |
| Standard | domyślna praca |
| PRO | ważne projekty |
| Naprawczy | poprawa istniejącego materiału |
| Codex/Replit | zadanie dla wykonawcy AI |
| Agent | praca przez agenta |
| Workflow | wiele skilli po kolei |

---

## 7. Etapy działania

```text
ETAP 1 — Rozpoznanie celu
ETAP 2 — Ustalenie zakresu
ETAP 3 — Dobór skilla albo zestawu skilli
ETAP 4 — Ustalenie workflow
ETAP 5 — Zebranie danych
ETAP 6 — Wykonanie
ETAP 7 — Kontrola jakości
ETAP 8 — Test końcowy
ETAP 9 — Raport i następny krok
```

---

## 8. Agent i workflow

### Agent może mieć wiele skilli

Przykład:

```text
Agent PrestaShop PRO:
- S001 — Moduł Builder PRO
- S002 — Audyt i Debug PRO
- S003 — Testy i QA PRO
- S004 — Dokumentacja PRO
- S008 — PrestaShop ZIP Packager
```

### Agent musi dobrać skill do celu

| Cel użytkownika | Pierwszy skill |
|---|---|
| Nowy moduł od zera | S001 |
| Błąd w istniejącym module | S002 |
| Test działania | S003 |
| Dokumentacja | S004 |
| Prompt dla Codex/Replit | S005 |
| Pakowanie ZIP | S008 |
| Grafiki produktu | S009 |
| Opis produktu | S010 |

### Agent nie może mieszać ról

Agent nie powinien:

- używać S001 do debugowania gotowego modułu,
- używać S002 do budowy projektu od zera,
- używać S008 przed testami,
- używać S004 zamiast realnej kontroli jakości.

Jeżeli zadanie wymaga wielu skilli, agent tworzy workflow.

### Agent powinien wyjaśnić większy workflow

```text
Wybrany agent: ...
Wybrane skille: ...
Workflow: ...
Efekt końcowy: ...
```

---

## 9. Workflow

### Minimalny workflow

```text
1. Rozpoznaj cel.
2. Dobierz skill.
3. Ustal minimalny zakres MVP.
4. Wykonaj.
5. Przetestuj.
6. Oceń.
7. Zapisz wynik.
```

### Workflow PRO

```text
1. Rozpoznaj cel.
2. Dobierz agenta.
3. Dobierz skill główny.
4. Dobierz skille pomocnicze.
5. Ustal MVP.
6. Wykonaj MVP.
7. Przetestuj.
8. Wykonaj audyt.
9. Popraw błędy.
10. Przygotuj dokumentację.
11. Zrób backup.
12. Zaktualizuj katalog.
13. Nadaj ocenę.
```

### Workflow dla komendy +

```text
S001+ = S001 + S002 + S003 + S008
```

Prawidłowa kolejność:

```text
1. S001 — zbuduj MVP
2. S003 — wykonaj testy
3. S002 — napraw błędy, jeśli wystąpiły
4. S008 — spakuj ZIP
```

Komenda `+` nie może oznaczać tygodniowego planowania. Ma oznaczać lepszą kontrolę jakości.

---

## 10. Bramki jakości workflow

| Bramka | Warunek przejścia |
|---|---|
| Po MVP | Czy powstał konkretny wynik? |
| Po teście | Czy test jest PASS? |
| Po audycie | Czy nie ma błędów krytycznych? |
| Przed backupem | Czy plik ma poprawną nazwę i wersję? |
| Przed katalogiem | Czy status i ocena są aktualne? |

---

## 11. Zasada nieprzenoszenia ograniczeń historycznych

Nie wolno przenosić ograniczeń z jednego projektu jako zasad globalnych.

Przykład:

```text
Nie ruszać API.
```

To mogło być prawidłowe dla konkretnego modułu DPD, ale dla nowego modułu od zera może być błędne.

Każdy skill, agent i workflow musi rozróżniać zasady globalne, projektowe, etapowe i historyczne.

---

## 12. Kontrola błędów

Skill, agent i workflow mają wykrywać:

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
- brak oceny jakości,
- źle dobrany skill,
- źle dobrany agent,
- zbyt długi workflow,
- workflow bez bramek jakości.
```

---

## 13. Format wyniku po użyciu skilla

```text
## Użyty agent
...

## Użyte skille
...

## Workflow
...

## Etap prac
SXXX: X%

## Ocena mojej pracy
X/10

## Co poprawić w następnym kroku
1. ...
2. ...
3. ...
```

Jeżeli agent/workflow nie był potrzebny:

```text
Użyty agent: brak — praca bezpośrednia
Workflow: prosty / jednoetapowy
```

---

## 14. Komendy S000

| Komenda | Znaczenie |
|---|---|
| S000 | użyj standardu S000 |
| S000 nowy skill | rozpocznij tworzenie nowego skilla |
| S000 audyt SXXX | oceń wskazany skill |
| S000 popraw SXXX | popraw wskazany skill |
| S000 agent | zaprojektuj agenta używającego skilli |
| S000 workflow | zaprojektuj workflow dla zadania |
| S000 katalog | pokaż / zaktualizuj katalog skilli |
| S000 backup SXXX | przygotuj skill do zapisu jako .md |
| S000 mini | użyj skróconej wersji standardu |
| S000 test SXXX | wykonaj test jakości |
| S000+ | użyj S000 + audyt + test + backup + katalog |

---

## 15. Test końcowy każdego skilla

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
| Czy nadaje się do pracy z agentem? | PASS / FAIL |
| Czy nadaje się do workflow? | PASS / FAIL |
| Czy nie jest tylko teorią? | PASS / FAIL |
| Czy nie jest za długi względem celu? | PASS / FAIL |
| Czy nie kopiuje zasad historycznych jako globalnych? | PASS / FAIL |

---

## 16. S000 MINI

```text
S000 MINI — STANDARD BUDOWY SKILLI 7DEJV OS

1. Każdy skill musi mieć numer.
2. Każdy skill musi mieć nazwę i wersję.
3. Każdy skill musi mieć jasny cel.
4. Każdy skill musi mieć określoną rolę.
5. Każdy skill musi mówić, kiedy go używać.
6. Każdy skill musi mówić, kiedy go NIE używać.
7. Każdy skill działa etapami.
8. Każdy skill musi mieć zasady jakości.
9. Każdy skill musi mieć zasady bezpieczeństwa.
10. Każdy skill musi mieć kontrolę błędów.
11. Każdy skill musi mieć test końcowy.
12. Każdy skill musi mieć ocenę jakości.
13. Każdy ważny skill powinien mieć sekcję Agent i workflow.
14. Skill powinien być możliwy do użycia przez człowieka, AI albo agenta.
15. Workflow powinien mieć kolejność działań i bramki jakości.
16. MVP najpierw, PRO później.
17. Nie przenoś ograniczeń historycznych jako zasad globalnych.
18. Po pracy podaj etap, ocenę i następny krok.
19. Skill jest gotowy dopiero wtedy, gdy pomaga realnie działać.
```

---

## 17. Historia zmian

```text
v1.0:
- zatwierdzono S000 jako stabilny standard bazowy do tworzenia, oceniania i poprawiania skilli.

v1.1:
- dodano pełne przystosowanie do pracy z agentem,
- dodano definicję agenta, skilla i workflow,
- dodano tryb Agent,
- dodano tryb Workflow,
- dodano zasady doboru skilla przez agenta,
- dodano workflow dla komendy +,
- dodano bramki jakości workflow,
- dodano sekcję Agent i workflow jako zalecaną dla ważnych skilli,
- zaktualizowano test końcowy,
- podniesiono ocenę S000 do 9.85/10.
```

---

## 18. Decyzja końcowa

```text
S000 — STANDARD BUDOWY SKILLI 7DEJV OS — v1.1
```

zostaje przyjęty jako standard budowy:

- skilli,
- agentów używających skilli,
- workflow złożonych z wielu skilli.
