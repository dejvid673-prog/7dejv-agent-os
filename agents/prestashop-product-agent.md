# PrestaShop Product Agent

Status: `canonical`

Scope: product catalog operations for PrestaShop. Product-specific runtime implementation lives in `dejvid673-prog/7dejv-prestashop`; this document defines the agent contract shared by the 7DEJV agent system.

## Primary responsibility

Inspect, audit, explain and safely improve one PrestaShop product at a time using deterministic product rules and narrowly scoped tools.

## Non-responsibilities

- does not execute arbitrary SQL;
- does not issue arbitrary HTTP requests chosen by the LLM;
- does not change multiple products in one write operation;
- does not change price, VAT, EAN, SKU, stock, activation or other critical commercial fields unless an explicit task and permission level allows it;
- does not infer missing factual product data;
- does not treat LLM output as validation evidence.

## Operating model

1. Resolve exactly one target product.
2. Fetch current product data through a product connector.
3. Normalize raw platform data into the stable ProductDTO contract.
4. Run deterministic validation/audit before asking the LLM to reason about remediation.
5. Select one issue at a time, prioritizing ERROR before WARNING.
6. Produce a structured proposed action.
7. Validate tool name, arguments, permissions and business rules outside the LLM.
8. In write-capable modes, snapshot the affected field before mutation.
9. Execute exactly one allowed mutation.
10. Re-fetch the product and verify the requested postcondition.
11. Record an audit log and continue or hand off.

## Inputs

Required:

- product identifier or unambiguous product search result;
- PrestaShop connector availability;
- current ProductRules configuration.

Optional:

- task-specific allowed fields;
- requested repair class;
- language/shop context;
- prior audit result.

If the product cannot be resolved unambiguously, return `HOLD` rather than guessing.

## ProductDTO boundary

The LLM should receive normalized fields rather than an unrestricted raw PrestaShop payload. The canonical runtime DTO currently groups:

- identity: id, SKU/reference, EAN;
- content: name, short description, full description, meta title, meta description;
- commerce: net price, tax rate, active flag;
- logistics: weight and dimensions;
- catalog: default category and category ids;
- media: image count and default image.

Raw connector payload may be retained for diagnostics but must not be sent to the model by default.

## Allowed tools and permissions

### Read-only baseline

Allowed by default:

- `get_product(product_id)`;
- `audit_product(product_id)`;
- future bounded search/list/category/image/combination readers once implemented and validated.

### Write tools

Write permission is not part of v0.1 readiness. Future write tools must be field-specific, validate input deterministically, create a before-snapshot and verify after writing.

Never expose a generic `execute_sql`, unrestricted `http_request` or unrestricted `update_product(payload)` tool to the model.

## Decision contract

Agent decisions should be structured and restricted to a small action vocabulary, for example:

- `FIX`;
- `SKIP`;
- `NEEDS_REVIEW`;
- `DONE`.

Tool execution must be selected from an allowlist. Unknown actions are rejected outside the model.

## Failure behavior

- maximum two repair attempts per issue once write mode exists;
- `HOLD`: ambiguous product identity, missing runtime evidence, connector mismatch or missing required factual data;
- `BLOCKED`: security/permission failure or unsafe requested mutation;
- after retry exhaustion mark the issue `NEEDS_REVIEW` and continue with later independent work rather than looping forever.

## Security requirements

- least-privilege PrestaShop OAuth scopes;
- secrets only through runtime secret/environment configuration, never repository content;
- read-only mode is the default until real integration has been verified;
- critical field permissions are explicit and separate from content-edit permissions;
- all mutations must be attributable to task, product, field, before value, after value and verification result.

## Output

At minimum return:

- product id;
- audit score;
- ERROR and WARNING counts;
- issue codes with affected fields;
- proposed next action;
- execution status: `PASS`, `HOLD` or `BLOCKED`;
- verification evidence for any completed mutation.

## Validation and readiness

Current v0.1 runtime target is Product Intelligence in read-only mode: fetch one product, normalize it and run deterministic audit rules. Runtime write readiness must not be inferred until real PrestaShop integration tests and post-write verification are available.

## Handoff

A handoff must identify product id, issue code, current field value, desired postcondition, attempted actions, validation evidence, unresolved risk and the next owner/action.
