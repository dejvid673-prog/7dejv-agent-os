# External tools registry — STAW EXPERT Product Pipeline

Zewnętrzne repozytoria nie są kopiowane do `7dejv-skills-prompts`. Pozostają osobnymi zależnościami i wymagają audytu licencji, bezpieczeństwa oraz konfiguracji.

| Projekt | Repozytorium | Rola | Status |
|---|---|---|---|
| GPT Researcher | `assafelovic/gpt-researcher` | badania internetowe i lokalne, raporty ze źródłami | `RECOMMENDED` |
| Browser Use | `browser-use/browser-use` | kontrolowana obsługa przeglądarki i ekstrakcja danych | `SPECIALIZED` |
| ChemCrow | `ur-whitelab/chemcrow-public` | pomocnicze narzędzia chemiczne i wyszukiwanie danych | `LAB` |
| CrewAI | `crewAIInc/crewAI` | dodatkowa orkiestracja zespołów agentów | `HOLD` |

## Zasady

- n8n pozostaje głównym orkiestratorem procesu,
- każde narzędzie zewnętrzne działa jako osobna usługa lub kontener,
- nie instalować ciężkich zależności bezpośrednio w głównym kontenerze n8n,
- nie przekazywać sekretów w promptach ani repozytorium,
- Browser Use nie może kupować, publikować ani omijać zabezpieczeń,
- ChemCrow nie zatwierdza receptury ani dawkowania,
- GPT Researcher musi zachować źródła każdej istotnej tezy,
- CrewAI wdrażać dopiero, gdy n8n nie wystarcza do danego podprocesu.

## Plan integracji

```text
n8n
├── HTTP → GPT Researcher
├── HTTP/API → Browser Use
├── HTTP → własne profile agentów 7DEJV
├── HUMAN/LAB approval
└── opcjonalnie HTTP → ChemCrow
```
