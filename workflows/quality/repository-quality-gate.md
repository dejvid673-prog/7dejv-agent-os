# Repository Quality Gate

Status: `canonical`

Provenance: adapted from `sources/7dejv-skills-prompts/main/04_workflows/quality/repository-quality-gate.md` (source blob `f5c19b640303a885bb71161f0563ae941d85344b`).

## Purpose

Block merge and readiness claims when required repository-quality evidence is missing or contradictory.

## Sequence

```text
INVENTORY
→ STRUCTURE_CHECK
→ DOCUMENTATION_COMPARE
→ AGENT_AUDIT
→ SKILL_AUDIT
→ WORKFLOW_AUDIT
→ SCHEMA_AUDIT
→ TEST_EVIDENCE_CHECK
→ SECURITY_CHECK
→ READINESS_CALCULATION
→ PASS / HOLD / BLOCKED
```

## Decision rules

### `BLOCKED`

- active critical/high security issue;
- active secret or private key;
- destructive action without the required approval gate;
- material integrity issue such as intentionally misleading readiness evidence.

### `HOLD`

- required tests were not executed or their evidence is unavailable;
- documentation disagrees with repository state;
- required contracts, registries or artifacts are incomplete;
- runtime readiness is claimed without runtime evidence;
- configured repository-quality threshold is not met.

### `PASS`

- no blocking critical/high findings remain;
- all checks required for the claimed readiness level have execution evidence;
- documentation agrees with current repository state;
- required contracts validate;
- configured quality threshold is met.

## Evidence

A quality-gate result must cite:

- repository/ref or commit SHA;
- checks actually executed;
- CI/test/audit evidence identifiers;
- blockers and unresolved findings;
- calculated status and timestamp.

A test definition is not test evidence. A design document is not runtime evidence.
