# Prompt dla Codex — `dpdshipmvp` mock-first

Data utworzenia: 2026-06-06
Cel: przygotować `dpdshipmvp` bez zgadywania prawdziwego API DPD.

---

## Prompt do wklejenia w Codex

```text
Pracuj w repozytorium 7dejv-ai-command-center.

Tryb pracy: DPD MOCK-FIRST.

Nie zgaduj endpointów DPD.
Nie wpisuj fałszywych URL API.
Nie implementuj prawdziwej komunikacji z DPD, jeśli nie ma oficjalnej dokumentacji API w repo.
Nie zapisuj sekretów.
Nie twórz realnych etykiet.

Najpierw przeczytaj:
1. .ai/CONTEXT.md
2. .ai/GOTCHAS.md
3. .ai/PRESTASHOP_MODULE_FACTORY.md
4. docs/modules/dpdshipmvp/wymagania.md
5. docs/modules/dpdshipmvp/api-dpd-notatki.md, jeśli istnieje
6. skills/skill-dpd-api-adapter.md
7. skills/skill-prestashop-order-hooks.md
8. skills/skill-prestashop-symfony-config-form.md
9. templates/spec-konfiguracji-dpd.md
10. templates/checklista-dpdshipmvp-order-hooks.md
11. templates/checklista-bezpieczenstwa-modulu.md

Zadanie:
Przygotuj plan mock-first dla modułu dpdshipmvp.

Raport ma zawierać:
1. które elementy można przygotować bez prawdziwego API,
2. interfejs adaptera DPD,
3. listę mocków,
4. scenariusze mocków,
5. strukturę klas,
6. przepływ panel -> kontroler -> serwis -> adapter,
7. zasady logowania,
8. zasady obsługi błędów,
9. czego nie wolno implementować bez dokumentacji DPD,
10. pytania do dokumentacji DPD,
11. decyzję, czy można budować szkielet mock-first.

Nie twórz jeszcze kodu.
Najpierw raport.
```
