# n8n Node Map

## Workflow nadrzędny

```text
Manual Trigger / Schedule / Webhook
→ Set: utwórz product_id i input_version
→ Data Store/PostgreSQL: pobierz stan
→ IF: sprawdź idempotencję
→ Execute Sub-workflow: bieżący etap
→ Code/JSON Schema Validator: waliduj kontrakt
→ Switch: PASS / HOLD / BLOCKED / ERROR / WAITING_APPROVAL
→ Data Store/PostgreSQL: zapisz stan i raport
→ Execute Sub-workflow: następny etap albo STOP
```

## Sub-workflow agenta

```text
Execute Workflow Trigger
→ Set: przygotuj minimalne wejście
→ HTTP Request / LLM Agent / lokalne API
→ Code: normalizacja odpowiedzi
→ JSON Schema validation
→ Set: status, ryzyka, braki i next_stage
→ Return from Sub-workflow
```

## Narzędzia

- GPT Researcher: `HTTP Request` do lokalnego API.
- Browser Use: osobny serwis, wyłącznie odczyt i ekstrakcja.
- Własne profile 7DEJV: prompt systemowy + Structured Output Parser.
- ChemCrow: opcjonalny serwis laboratoryjny.
- Google Sheets/PostgreSQL: rejestr produktów i etapów.
- Google Drive: raporty i materiały wejściowe.
- Wait/Form/Webhook: decyzje człowieka.
- Error Trigger: centralny workflow błędów.

## Minimalne tabele

- `products`: product_id, nazwa robocza, stage, status, input_version.
- `executions`: execution_id, product_id, stage, start, end, wynik, retry_count.
- `evidence`: product_id, etap, źródło, klasa, treść, hash.
- `approvals`: product_id, etap, decyzja, reviewer, timestamp, notes.
- `artifacts`: product_id, typ, ścieżka, wersja, status.
