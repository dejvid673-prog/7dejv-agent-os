# Commerce Platform Connection Bootstrap

Status: `canonical`

Purpose: safely connect 7DEJV agents to PrestaShop 9 and ERLI without granting write permissions before real read-only evidence exists.

## Non-negotiable rules

- secrets never enter GitHub, prompts, reports or screenshots;
- first connection is always `READ_ONLY`;
- one platform is verified at a time;
- connectivity is not readiness: endpoint payloads and permissions must also be verified;
- no write endpoint is called during bootstrap;
- production credentials stay in local/runtime secret storage only.

## Stage A — PrestaShop 9

### A1. Create dedicated API client

Create a dedicated Admin API client for 7DEJV. Start with minimum scopes needed for read-only validation, initially:

- `api_client_read`;
- `product_read` only if product-read verification is part of the first test.

Add other read scopes only when an actual workflow requires them. Never start with all scopes.

### A2. Runtime secrets

Configure locally/runtime only:

- `PRESTASHOP_BASE_URL`;
- `PRESTASHOP_CLIENT_ID`;
- `PRESTASHOP_CLIENT_SECRET`;
- explicit requested scope list.

### A3. Connectivity verification

1. POST to `/admin-api/access_token` using `client_credentials` and explicit scopes.
2. Confirm an access token is returned without logging the token.
3. GET `/admin-api/api-client/infos` using the Bearer token.
4. Record only client id/name, enabled state, lifetime and granted scopes.
5. Compare actual scopes with the expected allowlist.

### A4. Product read verification

Only after A3 passes:

1. choose one known non-sensitive product id;
2. call the verified product endpoint;
3. store no customer/order data;
4. normalize the response into ProductDTO;
5. run deterministic product audit;
6. mark PrestaShop product integration `READ_ONLY_VERIFIED` only after the real payload maps correctly.

## Stage B — ERLI

### B1. Obtain API key

Use the seller panel integration section for the official Shop API key. Store it only as runtime secret `ERLI_API_KEY`.

### B2. Runtime configuration

- `ERLI_API_BASE_URL=https://erli.pl/svc/shop-api`;
- `ERLI_API_KEY`;
- truthful `User-Agent` for the 7DEJV integration;
- timeout and bounded retry budget.

### B3. Connectivity verification

1. Perform a minimal authenticated GET against a verified read endpoint, initially `/inbox`.
2. Send `Authorization: Bearer <key>`, `Accept: application/json` and the integration User-Agent.
3. Do not mark messages as read during bootstrap.
4. Record HTTP status and payload shape only; redact customer/order personal data from evidence.
5. Handle HTTP 429 without busy-looping.

### B4. Contract verification

After connectivity passes:

- verify inbox event shape;
- identify product and order read endpoints required by the first workflow;
- document pagination/cursor behavior;
- define PrestaShop↔ERLI field ownership before any synchronization write is enabled.

## Stage C — Cross-platform mapping

Before any write capability:

1. define canonical owner per field (PrestaShop, ERLI-only, manually managed, derived);
2. map product identifiers and variants deterministically;
3. map order states and shipment states;
4. define frozen/manual ERLI fields that must never be overwritten automatically;
5. define safe discrepancy classes vs approval-required discrepancy classes.

## Stage D — Write readiness gate

Write mode remains disabled until all are true:

- read-only connectivity PASS for both platforms;
- real payload contracts documented;
- identity mapping verified;
- deterministic validation exists;
- field ownership exists;
- before/after snapshot mechanism exists;
- post-write re-read verification exists;
- audit log exists;
- exact write allowlist approved.

If any condition is missing, status is `HOLD`, not `READY`.
