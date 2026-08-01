# Agents — instrukcje ról roboczych

Ten folder zawiera instrukcje dla wyspecjalizowanych agentów używanych w pracy 7DEJV AI Command Center.

## Cel folderu

Agenci mają pomagać Codexowi działać konsekwentnie, bez zgadywania roli przy każdym zadaniu.

Każdy agent opisuje:

- kiedy go używać,
- czego ma pilnować,
- jaki ma zakres odpowiedzialności,
- jak ma raportować wynik,
- czego nie powinien robić.

## Lista agentów

| Plik | Rola |
|---|---|
| `AGENTS_codex_coordinator.md` | koordynator pracy Codex |
| `AGENTS_prestashop.md` | specjalista PrestaShop |
| `AGENTS_orderpanelmvp.md` | specjalista modułu listy zamówień |
| `AGENTS_dpdshipmvp.md` | specjalista modułu DPD |
| `AGENTS_auditor.md` | audytor jakości i błędów |
| `AGENTS_docs_reporter.md` | dokumentalista i raportujący |
| `AGENTS_security_guard.md` | strażnik bezpieczeństwa projektu |

## Zasada użycia

Jeżeli zadanie dotyczy modułu, Codex powinien dobrać minimum:

1. koordynatora,
2. specjalistę modułu,
3. audytora,
4. dokumentalistę.

Jeżeli zadanie dotyczy konfiguracji, danych lub integracji, należy dodać strażnika bezpieczeństwa.
