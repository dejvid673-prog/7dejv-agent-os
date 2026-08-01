# Zakładka Agents — jak używać

## Do czego służy

Zakładka `Agents` jest miejscem związanym z pracą agentów AI/GitHub/Codex, jeżeli funkcja jest dostępna w danym repozytorium.

W projekcie 7DEJV agentów traktujemy jako role robocze, które pomagają prowadzić zadania techniczne.

## Co trzymamy w repo

Instrukcje agentów są w folderze:

```text
agents/
```

Przykłady:

- `AGENTS_codex_coordinator.md`,
- `AGENTS_prestashop.md`,
- `AGENTS_orderpanelmvp.md`,
- `AGENTS_dpdshipmvp.md`,
- `AGENTS_auditor.md`,
- `AGENTS_docs_reporter.md`,
- `AGENTS_security_guard.md`.

## Kiedy używać agentów

Używać agentów, gdy zadanie wymaga konkretnej roli:

- koordynator — przy większej pracy,
- audytor — po każdym etapie,
- PrestaShop — przy modułach,
- DPD — przy `dpdshipmvp`,
- UX Back Office — przy widokach,
- security — przy konfiguracji i API.

## Jak kierować Codex

Codex powinien przed zadaniem dobrać agentów.

Przykład:

```text
Zadanie dotyczy dpdshipmvp.
Użyj:
- AGENTS_codex_coordinator.md
- AGENTS_dpdshipmvp.md
- AGENTS_auditor.md
- AGENTS_security_guard.md
- AGENTS_docs_reporter.md
```

## Dobra praktyka

Nie używać wszystkich agentów do każdego zadania. Dobierać role do celu.
