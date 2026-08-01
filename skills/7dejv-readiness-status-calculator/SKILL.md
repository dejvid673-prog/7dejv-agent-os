---
name: 7dejv-readiness-status-calculator
description: Calculate 7DEJV repository readiness statuses from machine-readable evidence rather than manual claims. Use after CI, audits, runtime tests or release preparation.
---

# 7DEJV Readiness Status Calculator

## Inputs
- repository registries,
- CI and audit results,
- benchmark evidence,
- runtime and deployment evidence,
- readiness rule set.

## Procedure
1. Evaluate every readiness condition independently.
2. Require explicit evidence paths or CI results.
3. Apply dependency rules between statuses.
4. Downgrade stale or unsupported claims.
5. Produce current status, missing evidence and next required actions.

## Output
Return readiness statuses, evidence, blockers, calculated timestamp and status `PASS` or `HOLD`.

## Errors and stop conditions
Return `HOLD` when evidence is absent, stale or contradictory. Never infer runtime readiness from design artifacts.

## Limits
Do not set `PRODUCTION_READY` unless runtime, security, rollback and end-to-end requirements all pass.

## Examples
Passing static CI can establish `STATIC_VALIDATED`, but cannot establish `LOCAL_RUNTIME_TESTED`.

## Tests and acceptance criteria
Every positive readiness status must cite at least one existing evidence artifact and satisfy all prerequisite statuses.
