# Repository status — STAW EXPERT Product Pipeline

## Stan potwierdzony przez repozytorium i CI

- 27 skilli z `SKILL.md`,
- 18 profili agentów z kontraktami maszynowymi,
- 13 kanonicznych workflow,
- 1 główny JSON Schema procesu produktowego,
- 6 zapisanych raportów audytowych,
- maszynowy rejestr etapów i przejść,
- kontrakty wejścia, wyjścia, uprawnień, retry i warunków STOP agentów,
- automatyczna kontrola skilli, evals, kontraktów, routingu, bezpieczeństwa, runtime artifacts i governance,
- automatycznie generowane rejestry agentów, skilli, workflow, schematów, audytów i gotowości,
- automatyczna analiza duplikatów odpowiedzialności i właścicieli etapów,
- lokalny szkielet Docker Compose dla n8n i PostgreSQL,
- nieaktywny plik workflow n8n przeznaczony do importu,
- transakcyjna migracja PostgreSQL,
- szablon `.env.example` bez zapisanych sekretów,
- końcowy audyt spójności dokumentacji i zależności runtime zakończony,
- tag `n8n:latest` usunięty; runtime wymaga jawnej wersji `N8N_VERSION`.

## Statusy gotowości

- `DESIGN_READY`: tak,
- `STATIC_VALIDATED`: tak,
- `EVAL_SCHEMA_READY`: tak,
- `CONTRACT_SCHEMA_READY`: tak,
- `STATIC_ROUTING_VALIDATED`: tak,
- `SECURITY_CI_READY`: tak,
- `AGENT_CONTRACTS_READY`: tak,
- `REPOSITORY_GOVERNANCE_READY`: tak,
- `SKILL_PACK_READY_FOR_REVIEW`: tak,
- `RUNTIME_ARTIFACTS_READY`: tak,
- `N8N_WORKFLOW_FILE_READY`: tak,
- `POSTGRES_MIGRATION_READY`: tak,
- `RUNTIME_STATIC_VALIDATION`: PASS,
- `STATIC_MERGE_GATE`: PASS,
- `N8N_IMPORT_TESTED`: nie,
- `POSTGRES_MIGRATION_EXECUTED`: nie,
- `LOCAL_RUNTIME_TESTED`: nie,
- `END_TO_END_TESTED`: nie,
- `SECURITY_RUNTIME_TESTED`: nie,
- `PRODUCTION_READY`: nie.

## Ograniczenia aktualnego statusu

`PASS` w GitHub Actions potwierdza poprawność statyczną repozytorium i przygotowanie artefaktów runtime. Nie potwierdza poprawnego importu workflow do działającego n8n, wykonania migracji na rzeczywistej bazie, działania agentów ani integracji w środowisku lokalnym lub produkcyjnym.

Workflow n8n jest bezpiecznym, nieaktywnym szkieletem. Nie wywołuje modeli ani usług zewnętrznych i kończy pracę statusem `STATIC_RUNTIME_SKELETON_ONLY`.

Zewnętrzne zależności GPT Researcher, Browser Use i ChemCrow pozostają w statusie `HOLD`, dopóki nie zostaną przypięte konkretne wersje lub commity i zakończony przegląd licencji.

## Pozostałe prace runtime

1. Skonfigurować lokalny plik `.env` poza Git.
2. Uruchomić stos Docker Compose.
3. Wykonać migrację PostgreSQL i zapisać dowód jej poprawnego wykonania.
4. Zaimportować workflow do n8n i potwierdzić zgodność importu.
5. Rozbudować szkielet o jeden bezpieczny pionowy przebieg MVP zakończony `HUMAN_APPROVAL_REQUIRED`.
6. Uruchomić rzeczywiste benchmarki baseline i with-skill.
7. Uruchomić testy prompt injection i uprawnień w runtime.
8. Wykonać lokalny test end-to-end.
9. Przygotować rollback i zatwierdzić pilot.

Repozytorium nie może deklarować gotowości lokalnego runtime ani produkcyjnej, dopóki powyższe dowody nie zostaną utworzone i zapisane.