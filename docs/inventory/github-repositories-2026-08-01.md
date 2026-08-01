# GitHub Repositories Inventory

Data sprawdzenia: 2026-08-01

Zakres: konto `dejvid673-prog` na GitHub.

## Wynik

Nie znaleziono brakujacych repo do skopiowania lokalnie. Lista repo online pokrywa sie z lista lokalnych klonow w `G:\repo 7dejv.os\inne`.

## Tabela repo

| repo | online | lokalnie | domyslna galaz | sygnal z katalogu glownego | rola robocza |
| --- | --- | --- | --- | --- | --- |
| `7dejv-agent-os` | tak | tak | `main` | `README.md` | nowa baza centralna |
| `7dejv-skills-prompts` | tak | tak | `main` | `02_skills`, `03_agents`, `04_workflows`, `codex-router`, `skills` | glowne zrodlo migracji dla skills i workflow |
| `7dejv-ai-command-center` | tak | tak | `main` | `AGENTS.md`, `agents`, `skills`, `docs`, `prompts`, `REPO_MAP.md` | zrodlo migracji dla governance i procedur |
| `airtable-agent` | tak | tak | `main` | `README.md` | wyspecjalizowany agent domenowy, do osobnej oceny migracji |
| `7dejv.os` | tak | tak | `main` | `stages`, `mockup`, `AUDIT_REPORT.md` | repo produktowe z lokalnymi artefaktami do ekstrakcji |
| `7dejv-staw-expert` | tak | tak | `main` | `08_product-os`, `11_raporty-ai`, `research` | repo domenowe z workflow i materialem referencyjnym |
| `7dejv-prestashop` | tak | tak | `main` | `01_modules`, `03_tests`, `docs`, `docker-compose.yml` | repo techniczne i produktowe |
| `repetytorium` | tak | tak | `main` | `README.md` | niski sygnal, wymaga dalszego przegladu |
| `n8n_7d` | tak | tak | `main` | `README.md` | pomocnicze repo integracyjne, niski sygnal |
| `bufor-github` | tak | tak | `main` | `repos.json`, `summaries`, `clone_repos.sh` | repo pomocnicze do indeksow i mirroringu |
| `Agent-repo` | tak | tak | `main` | `README.md` | niski sygnal, prawdopodobnie pomocnicze |
| `7dejv-dawid` | tak | tak | `main` | `.github`, `README.md` | niski sygnal, wymaga dalszego przegladu |
| `n8n` | tak | tak | brak | repo puste | brak wartosci migracyjnej na ten etap |

## Dowody

- Lista repo online zostala zweryfikowana przez `gh repo list dejvid673-prog`.
- Zawartosc katalogow glownych zostala zweryfikowana przez `gh api repos/<repo>/contents`.
- `n8n` zostal potwierdzony jako repo puste przez odpowiedz API GitHub.

## Wniosek

Etap kopiowania brakujacych repo jest zakonczony wynikiem `0 brakujacych`. Dalsza praca powinna przejsc do klasyfikacji i migracji artefaktow z repo o najwyzszym sygnale.
