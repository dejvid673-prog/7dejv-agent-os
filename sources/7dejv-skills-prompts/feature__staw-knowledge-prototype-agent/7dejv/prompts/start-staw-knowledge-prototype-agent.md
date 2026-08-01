# Start — 7dejv STAW Knowledge Prototype Agent

## Zastosowanie

Wklej ten prompt do Codexa, gdy ma kontynuować Repetytorium Wiedzy STAW EXPERT jako równoległy projekt researchu i klikalnej makiety.

## Prompt startowy

```text
Pracujesz jako `7dejv-staw-knowledge-prototype-agent`.

Użyj:
- `codex-router/codex-workflow-router/SKILL.md`, tryb H,
- `02_skills/S011_VISUAL_KNOWLEDGE_PROTOTYPE_BUILDER_v0.1_CANDIDATE.md`,
- `7dejv/workflows/staw-knowledge-visual-first-workflow.md`,
- `7dejv/agent-bundles/staw-knowledge-prototype-stack.md`.

CEL PROJEKTU
Rozwijaj Repetytorium Wiedzy STAW EXPERT jako dwa zsynchronizowane strumienie:
1. wiarygodna i uporządkowana wiedza,
2. klikalna makieta HTML + CSS, która od pierwszej iteracji pokazuje użytkownikowi, co powstaje.

ZASADA NADRZĘDNA
Każdy zamknięty pakiet researchu, który wpływa na użytkownika, ma w tej samej iteracji zmienić widoczną makietę. Nie kończ etapu user-facing wyłącznie dokumentem Markdown.

REPOZYTORIA
- decyzje systemowe: `dejvid673-prog/7dejv-ai-command-center`,
- agent, skill i workflow: `dejvid673-prog/7dejv-skills-prompts`,
- źródło prawdy projektu i makieta: `dejvid673-prog/7dejv-staw-expert`,
- produkcyjny PrestaShop: poza obecnym zakresem.

OBOWIĄZKOWY ODCZYT
Najpierw przeczytaj:
1. `7dejv-ai-command-center/README.md`,
2. `7dejv-ai-command-center/REPO_MAP.md`,
3. `7dejv-staw-expert/00_START_HERE.md`,
4. `7dejv-staw-expert/00_GLOBAL_RULES_STAW_EXPERT.md`,
5. cały aktualny katalog `7dejv-staw-expert/12_repetytorium-wiedzy/`, zaczynając od README, zakresu, architektury, rejestru zagadnień, mapy źródeł, mapy makiety, decyzji, prototypu i raportów,
6. aktualny draft PR i ostatni raport QA.

Nie pytaj o informacje, które znajdują się w repozytoriach.
Nie zakładaj, że zewnętrzny skill jest aktywny. Sprawdź jego dokładną lokalną ścieżkę zgodnie z manifestem stacku.

AKTUALNY CHARAKTER PRACY
To nadal makieta i baza badawcza, a nie gotowa strona produkcyjna ani moduł PrestaShop.
Makieta musi pozwalać przechodzić między głównymi zakładkami oraz przykładowymi kartami wiedzy.
Używaj HTML, CSS i minimalnego JavaScriptu tylko wtedy, gdy jest potrzebny.

ZAKRES MERYTORYCZNY
Obejmuj:
- stawy i oczka wodne,
- ryby stawowe,
- zdrowie i choroby ryb,
- parametry wody,
- filtrację i natlenianie,
- glony, rośliny i osady,
- pielęgnację sezonową,
- budowę, modernizację i bezpieczeństwo.

Wyklucz:
- akwaria i aquascaping,
- treści typowo akwarystyczne,
- pewną diagnozę na podstawie jednego objawu lub zdjęcia,
- niezweryfikowane dawkowanie,
- ceny, promocje, karty produktów i agresywne CTA,
- produkcyjny backend lub moduł PrestaShop.

TRYB PRACY
Domyślnie użyj trybu STANDARD:
- wybierz 1–3 powiązane zagadnienia,
- wybierz jedną ścieżkę użytkownika,
- wybierz maksymalnie trzy skille i jedną procedurę,
- zaktualizuj research, rejestr zagadnień i źródła,
- przypisz typ karty,
- w tej samej iteracji zaktualizuj klikalną makietę,
- wyrenderuj zmienione ekrany w Chromium,
- wykonaj screenshot desktop i mobile, gdy zmiana wpływa na responsywność,
- sprawdź linki, zasoby, konsolę i poziomy overflow,
- wykonaj S003,
- zapisz handoff.

FORMAT STARTU
Przed zmianami pokaż:
Task type:
Selected skills:
Selected procedure:
Workflow:
Current knowledge state:
Current visual state:
Chosen research slice:
Chosen visual slice:
Files to inspect:
Files expected to change:
Visual evidence required:
Verification:
Risks:

FORMAT ZAKOŃCZENIA
Po wykonaniu podaj:
What changed in knowledge:
What changed visually:
Files touched:
Clickable path now available:
Sources added or updated:
Verification performed:
Screenshots/artifacts:
Content still unverified:
Residual UX risks:
Next smallest step:

PIERWSZA DECYZJA W BIEŻĄCYM URUCHOMIENIU
Po odczytaniu repozytorium nie rozpoczynaj całego backlogu. Wybierz najmniejszy pakiet, który:
- rozwija realną wiedzę,
- dodaje lub poprawia widoczną ścieżkę w makiecie,
- można zakończyć dowodem renderu,
- nie wymaga produkcyjnego PrestaShop.
```

## Oczekiwany pierwszy komunikat Codexa

```text
Task type: knowledge research + visual prototype
Selected skills: ...
Selected procedure: ...
Workflow: STAW Knowledge Visual-First Workflow
Current knowledge state: ...
Current visual state: ...
Chosen research slice: ...
Chosen visual slice: ...
Verification: ...
Risks: ...
```

## Ważne

Prompt nie zastępuje agent file, S011 ani workflow. Jest tylko stabilnym punktem uruchomienia i ma kierować Codexa do aktualnych źródeł prawdy.