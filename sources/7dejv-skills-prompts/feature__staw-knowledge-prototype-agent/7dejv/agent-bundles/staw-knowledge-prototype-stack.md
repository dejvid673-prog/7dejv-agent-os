# STAW Knowledge Prototype — agent stack manifest

## Cel

Ten manifest rozdziela elementy:

- potwierdzone lokalnie w `7dejv-skills-prompts`,
- utworzone dla projektu,
- zewnętrzne wzorce i kandydatów wymagających potwierdzenia ścieżki lub instalacji.

Agent nie może traktować nazwy wymienionej w dokumentacji jako dowodu, że skill jest lokalnie zainstalowany i aktywny.

## A. Elementy potwierdzone lokalnie

| Element | Typ | Ścieżka | Rola |
|---|---|---|---|
| `codex-workflow-router` | router | `codex-router/codex-workflow-router/SKILL.md` | wybór maksymalnie 1–3 skilli i jednej procedury |
| `cs-frontend-engineer` | procedura | `agent-procedures/engineering/cs-frontend-engineer.md` | frontend, rendering, WCAG, performance i screenshoty |
| `7dejv-pond-product-expert` | procedura domenowa | `7dejv/agents/7dejv-pond-product-expert.md` | pytania klientów i język domeny stawowej; bez wymyślania parametrów |
| `S000` | standard | `02_skills/S000_STANDARD_BUDOWY_SKILLI_v1.0_FINAL.md` | standard budowy i oceny skilli |
| `S002` | skill | `02_skills/S002_AUDYT_I_DEBUG_PRO_v1.0_FINAL.md` | diagnoza i minimalne poprawki błędów |
| `S003` | skill | `02_skills/S003_TESTY_I_QA_PRO_v2.1_FINAL.md` | QA makiety, plików i działania |

## B. Elementy utworzone dla projektu

| Element | Typ | Ścieżka | Status |
|---|---|---|---|
| `7dejv-staw-knowledge-prototype-agent` | agent procedure | `7dejv/agents/7dejv-staw-knowledge-prototype-agent.md` | CANDIDATE v0.1 |
| `S011 Visual Knowledge Prototype Builder` | skill | `02_skills/S011_VISUAL_KNOWLEDGE_PROTOTYPE_BUILDER_v0.1_CANDIDATE.md` | CANDIDATE 8.7/10 |
| `STAW Knowledge Visual-First Workflow` | workflow | `7dejv/workflows/staw-knowledge-visual-first-workflow.md` | CANDIDATE v0.1 |

## C. Zewnętrzne wzorce potwierdzone w repozytoriach źródłowych

Poniższe elementy zostały odnalezione w zewnętrznych repozytoriach, ale przed użyciem jako lokalnego skilla trzeba potwierdzić ich dokładną ścieżkę w bieżącym środowisku Codexa albo wykonać kontrolowaną adaptację.

| Element | Źródło | Zastosowanie | Status lokalny |
|---|---|---|---|
| `frontend-design` | `anthropics/skills` | kierunek wizualny, responsywność, dostępność, krytyka screenshotów | do potwierdzenia |
| `ux-researcher-designer` | `alirezarezvani/claude-skills` | pytania użytkowników, journey map, usability i synteza | do potwierdzenia |
| `ui-design-system` | `alirezarezvani/claude-skills` | tokeny, komponenty, responsywność i WCAG | do potwierdzenia |
| `knowledge-ops` | `alirezarezvani/claude-skills` | higiena bazy wiedzy, ownership, linkowanie, staleness i runbooki | do potwierdzenia |
| `product-research` / research toolkit | `alirezarezvani/claude-skills` | strukturalny research produktu i użytkownika | do potwierdzenia |
| `playwright-cli` | `microsoft/playwright-cli` | browser automation, screenshoty, mobile emulation i sesje | do zainstalowania lub wywołania przez istniejący workflow |
| `brainstorming` | `obra/superpowers` | analiza kontekstu i porównanie wariantów przed implementacją | wzorzec procesu |
| `writing-plans` | `obra/superpowers` | dokładne plany z plikami, testami i małymi krokami | wzorzec procesu |

## D. Availability gate

Przed użyciem skilla lub narzędzia agent wykonuje:

```text
1. Znajdź dokładną ścieżkę lokalną.
2. Otwórz plik instrukcji lub dokumentację.
3. Sprawdź zgodność z bieżącym zadaniem.
4. Sprawdź, czy nie dubluje S011 albo istniejącej procedury.
5. Sprawdź licencję i zasady adaptacji, jeżeli plik ma być kopiowany.
6. Dopiero wtedy oznacz element jako ACTIVE.
```

Jeżeli elementu nie odnaleziono:

- nie twierdź, że został użyty,
- użyj lokalnego odpowiednika,
- zapisz status `NOT FOUND` albo `EXTERNAL CANDIDATE`,
- nie blokuj prostego wykonania HTML/CSS, jeśli lokalne narzędzia wystarczają.

## E. Domyślne zestawy wykonawcze

### Pierwszy przebieg projektu

```text
Agent: 7dejv-staw-knowledge-prototype-agent
Skill: S011
Procedura: cs-frontend-engineer
QA: S003
```

To wystarcza do utworzenia prostego, klikalnego baseline HTML/CSS i jego sprawdzenia.

### Research pakietu

```text
Agent: 7dejv-staw-knowledge-prototype-agent
Skill główny: S011
Skill pomocniczy: knowledge-ops — tylko po potwierdzeniu dostępności
Procedura domenowa: 7dejv-pond-product-expert
```

### Rozwinięcie design systemu

```text
Agent: 7dejv-staw-knowledge-prototype-agent
Skill główny: S011
Skill pomocniczy: frontend-design albo ui-design-system — po potwierdzeniu
Procedura: cs-frontend-engineer
```

### Browser QA

```text
Skill główny: S003
Narzędzie: istniejący workflow Playwright w repo projektu albo playwright-cli
Skill naprawczy: S002 tylko przy błędzie
```

## F. Zasada minimalizmu

Nie instaluj i nie aktywuj całej biblioteki agentów.

Dla pojedynczej iteracji wybierz:

- jeden agent główny,
- jeden skill główny,
- maksymalnie dwa skille pomocnicze,
- jedną procedurę wykonawczą,
- jeden workflow.

## G. Decyzja

Najbliższym istniejącym agentem zewnętrznym jest UX Researcher połączony z UI Design System, natomiast najbliższą procedurą lokalną jest `cs-frontend-engineer`. Żaden z nich samodzielnie nie obejmuje:

- specyfiki STAW EXPERT,
- bezpiecznej treści zdrowotnej,
- rejestru źródeł,
- synchronizacji wiedzy z makietą,
- obowiązkowej wizualizacji od pierwszego przebiegu.

Dlatego agent lokalny jest adaptacją celowaną, a nie kopią jednego zewnętrznego agenta.