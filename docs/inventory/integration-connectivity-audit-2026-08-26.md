# PrestaShop + ERLI connectivity audit — 2026-08-26

Status: `evidence`

## Scope

Verify current evidence for the two agent integrations being prepared for 7DEJV:

- production PrestaShop native Webservice as a read-only source;
- ERLI Shop API as a marketplace target, with write capability planned but not yet exercised in this audit.

No credentials or secrets are stored in this document.

## PrestaShop — LIVE connectivity

Result: `PASS / READ-ONLY CONNECTIVITY VERIFIED`

Evidence observed during the integration session:

- authenticated request to the production `/api/` Webservice index returned the PrestaShop resource catalogue;
- `GET=true` and write methods disabled were visible for relevant resources including products, categories, combinations, images, orders, order details, order states, carriers and stock availability;
- therefore authentication and native Webservice routing are functioning for the configured key.

### Security finding

The current Webservice key exposes GET access to more resources than the product/marketplace agent initially requires, including customer- and administration-adjacent resources. This is not a write risk because POST/PUT/PATCH/DELETE are disabled, but it violates least-privilege intent.

Action: after initial integration validation, reduce GET permissions to the exact resource allowlist needed by the agent.

## PrestaShop — CODE/CI

Result: `PASS`

Repository: `dejvid673-prog/7dejv-prestashop`

Commit: `aabc46b5ce539df1dcd07587906ed1237cb0489c`

GitHub Actions run: `32914568147` — `success`.

Ten Python unit tests passed, including five tests dedicated to the native Webservice client:

1. Basic authentication encodes `API_KEY:` correctly.
2. API index request is GET-only and requests JSON.
3. Product reader uses `/api/products/{id}`.
4. Invalid product id is rejected before network access.
5. The Webservice client exposes no generic write methods.

The existing mapper/audit/Admin-API compatibility tests also remain green.

## ERLI — LIVE connectivity

Result: `PASS / READ CONNECTIVITY VERIFIED`

Evidence observed during the integration session:

- authenticated request to `GET /svc/shop-api/delivery/priceLists` returned HTTP `200`;
- response body contained a valid JSON list of the seller account's delivery price lists;
- therefore the API key, Bearer authentication and ERLI Shop API routing are functioning.

## ERLI — WRITE readiness

Result: `HOLD`

The successful GET proves connectivity and authorization for the tested read endpoint. It does **not** prove safe offer publishing.

Before changing this status to PASS:

1. implement a bounded ERLI runtime client outside the LLM with schema validation;
2. select one explicit test product;
3. read source data from PrestaShop;
4. build and review the ERLI payload/diff;
5. execute one authorized `POST /products/{externalId}` or minimal `PATCH`;
6. treat HTTP `202` only as accepted/pending, not final success;
7. re-read/observe ERLI processing result and synchronization errors;
8. record before/source data, payload class, target externalId and final verification evidence;
9. do not override frozen/manual ERLI fields automatically.

## Secret handling finding

During manual troubleshooting, API key values appeared in screenshots. Any key whose full value was exposed in a screenshot must be revoked and replaced. No secret value is recorded in GitHub.

## Final status

| Integration | Live read | Code/contract tests | Write readiness |
|---|---|---|---|
| PrestaShop Webservice | PASS | PASS — 10/10 CI | N/A by policy (read-only) |
| ERLI Shop API | PASS | Agent contract exists; bounded runtime client still required | HOLD |

Overall: `CONNECTIVITY VERIFIED`. Do not label ERLI offer publishing `DONE` until a single controlled write passes post-write verification.
