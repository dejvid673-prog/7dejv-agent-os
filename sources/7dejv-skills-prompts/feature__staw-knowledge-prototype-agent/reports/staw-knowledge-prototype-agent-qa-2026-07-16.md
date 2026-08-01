# QA — STAW Knowledge Prototype Agent Stack

Data: 2026-07-16

## Materiał

Sprawdzono:

- `7dejv/agents/7dejv-staw-knowledge-prototype-agent.md`,
- `02_skills/S011_VISUAL_KNOWLEDGE_PROTOTYPE_BUILDER_v0.1_CANDIDATE.md`,
- `7dejv/workflows/staw-knowledge-visual-first-workflow.md`,
- `7dejv/agent-bundles/staw-knowledge-prototype-stack.md`,
- `7dejv/prompts/start-staw-knowledge-prototype-agent.md`,
- zmiany w routerze i indeksach.

## Cel testu

Sprawdzić, czy przygotowany zestaw:

1. rozumie zakres Repetytorium Wiedzy STAW EXPERT,
2. prowadzi research i wizualizację równolegle,
3. wymaga widocznego HTML/CSS od pierwszej iteracji,
4. nie miesza repozytoriów,
5. nie rozpoczyna produkcyjnego PrestaShop,
6. rozdziela treści potwierdzone i robocze,
7. ma jasny workflow, QA i handoff,
8. jest możliwy do uruchomienia przez Codexa.

## S003 — test MVP

| Pytanie | Wynik | Dowód |
|---|---|---|
| Czy wynik istnieje? | PASS | agent, skill, workflow, manifest i launcher zapisane na gałęzi |
| Czy odpowiada na cel? | PASS | visual-first contract oraz dwa zsynchronizowane strumienie są obowiązkowe |
| Czy da się go użyć? | PASS | istnieje osobny prompt startowy i routing w `codex-workflow-router` |
| Czy istnieje błąd blokujący? | NIE | brak wykrytej sprzeczności blokującej uruchomienie CANDIDATE |

## S000 — kontrola skilla S011

S011 posiada wymagane sekcje:

- numer,
- nazwa i wersja,
- jasny cel,
- kiedy używać,
- kiedy nie używać,
- dane wejściowe,
- dane wyjściowe,
- tryby pracy,
- etapy działania,
- zasady jakości,
- zasady bezpieczeństwa,
- kontrola błędów,
- format wyniku,
- test końcowy,
- ocena,
- historia zmian.

Wynik strukturalny: `PASS`.

## Kontrola projektu STAW EXPERT

| Wymaganie | Wynik |
|---|---|
| źródło prawdy projektu w `7dejv-staw-expert` | PASS |
| agent i skille w `7dejv-skills-prompts` | PASS |
| implementacja PrestaShop poza bieżącym zakresem | PASS |
| makieta HTML/CSS wymagana od początku | PASS |
| klikalne przejścia zamiast samych screenshotów | PASS |
| miniatury zamiast emotikon | PASS |
| brak akwarystyki | PASS |
| brak diagnozy z jednego objawu | PASS |
| brak automatycznego produktu i CTA | PASS |
| źródła i statusy treści wymagane | PASS |
| render desktop/mobile i screenshoty | PASS jako wymaganie; wykonanie zależy od iteracji |

## Kontrola routingu

Router otrzymał tryb H:

```text
Knowledge base, research and visual prototype
```

Tryb kieruje do:

- agenta STAW,
- workflow visual-first,
- S011,
- małych pakietów 1–3 tematów,
- renderowania i browser QA,
- zakazu produkcyjnej implementacji bez handoffu.

Wynik: `PASS`.

## Kontrola dostępności skilli

### Potwierdzone lokalnie

- router,
- `cs-frontend-engineer`,
- `7dejv-pond-product-expert`,
- S000,
- S002,
- S003,
- nowe S011, agent i workflow.

### Zewnętrzni kandydaci

- `frontend-design`,
- `ux-researcher-designer`,
- `ui-design-system`,
- `knowledge-ops`,
- `playwright-cli`,
- wzorce `brainstorming` i `writing-plans`.

Ich istnienie w repozytoriach źródłowych zostało potwierdzone podczas researchu, ale dokładna aktywna lokalizacja w środowisku Codexa nie została potwierdzona. Manifest zawiera obowiązkowy `availability gate`.

Wynik: `WARNING`, nie `FAIL`.

Lokalny zestaw wystarcza do rozpoczęcia pracy bez instalowania wszystkich kandydatów zewnętrznych.

## Wykryte ryzyka

### [P2] Duża objętość dokumentów

Agent, skill i workflow są szczegółowe i częściowo powtarzają kluczowe zasady.

Skutek:

- większy koszt kontekstu,
- ryzyko nadmiernej ceremonii przy drobnej poprawce.

Zabezpieczenie:

- tryb MINI,
- router ograniczający aktywne skille,
- launcher kierujący do źródeł zamiast kopiowania pełnego projektu,
- przyszły test, czy agent file można skrócić po dwóch cyklach.

### [P2] Brak praktycznego testu nowego agenta

Zestaw został sprawdzony strukturalnie, lecz nie wykonał jeszcze pełnej nowej iteracji projektu.

Decyzja:

- status pozostaje `CANDIDATE`,
- nie oznaczać jako `FINAL`.

### [P2] Zewnętrzne skille nie są automatycznie aktywne

Nazwy z repozytoriów źródłowych nie mogą być traktowane jak lokalnie zainstalowane skille.

Zabezpieczenie:

- manifest stacku,
- availability gate,
- lokalne odpowiedniki wystarczające do MVP.

### [P3] Ryzyko rozrostu pierwszej iteracji

Agent zna cały projekt, ale może próbować ruszyć zbyt wiele tematów.

Zabezpieczenie:

- pakiet 1–3 tematów,
- jedna ścieżka użytkownika,
- jeden widoczny rezultat,
- następny najmniejszy krok.

## Plan dwóch testów przed FINAL

### Cykl testowy 1 — problem pielęgnacyjny

```text
Pakiet: zielona woda + zakwit fitoplanktonu + lampa UV
Ścieżka: home → problemy → zielona woda → woda/filtracja
Wymagane: źródła, karta problemu, aktualizacja kategorii, desktop/mobile, screenshoty, S003
```

Cel testu:

- sprawdzić research niskiego ryzyka,
- sprawdzić synchronizację kilku działów,
- sprawdzić, czy agent nie zmienia makiety zbyt szeroko.

### Cykl testowy 2 — gatunek i parametr

```text
Pakiet: jesiotr syberyjski + tlen + żywienie denne
Ścieżka: home → ryby → jesiotr → tlen/filtracja/sezon
Wymagane: minimum dwa źródła gatunkowe, jawne braki, rozwinięcie karty, render i QA
```

Cel testu:

- sprawdzić wartości liczbowe i kontekst źródeł,
- sprawdzić powiązanie karty gatunku z parametrami,
- sprawdzić blokowanie niepotwierdzonych danych.

## Decyzja QA

```text
Decyzja: WARNING
Ocena: 8.8/10
Czy można używać dalej: TAK, jako CANDIDATE
Czy można oznaczyć FINAL: NIE
Największy brak: brak dwóch pełnych testów praktycznych
Pierwszy krok poprawy: uruchomić cykl testowy 1 na aktualnym Repetytorium Wiedzy
```

## Stan

- agent: `CANDIDATE v0.1`,
- S011: `CANDIDATE 8.7/10`,
- workflow: `CANDIDATE v0.1`,
- routing: gotowy do testu,
- launcher Codex: gotowy,
- PR: do utworzenia jako draft,
- merge do `main`: niedozwolony przed przeglądem i testem praktycznym.