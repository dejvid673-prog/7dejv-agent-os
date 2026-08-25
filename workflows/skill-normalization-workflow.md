# Skill Normalization Workflow

Status: `canonical`

## Purpose

Consolidate inventoried shared agent-system artifacts into the canonical 7DEJV structure while preserving provenance and preventing unsafe duplicate cleanup.

## Sequence

```text
INVENTORY
→ VERIFY_PROVENANCE
→ GROUP_BY_PURPOSE
→ COMPARE_CONTRACTS
→ CLASSIFY
→ PLAN_PROMOTION_OR_CLEANUP
→ VALIDATE
→ PASS / HOLD / BLOCKED
```

## Procedure

1. Consume an evidence-backed inventory for explicit repositories/refs.
2. Verify provenance and current canonical boundaries.
3. Group candidates by purpose and contract, not by name alone.
4. Compare content, role, inputs/outputs, dependencies and scope.
5. Classify each artifact `canonical`, `reference`, `duplicate`, `unclear` or `deprecated`.
6. Promote only unambiguous artifacts with provenance and required contracts.
7. Delete only proven redundant active artifacts whose canonical replacement is established and whose archival role is absent.
8. Update registries/documentation and execute required validation gates.

## Status rules

- `PASS`: classifications and intended changes are evidenced, canonical registries agree and required validation passes.
- `HOLD`: equivalence, provenance, ownership, local/global scope or dependencies remain ambiguous.
- `BLOCKED`: proposed cleanup would remove the only known copy, destroy provenance, overwrite conflicting work or violate security/integrity rules.

## Evidence

A normalization result must identify source and canonical paths, refs/SHAs where available, classification rationale, actual changes, validation evidence and unresolved conflicts. Identical copies under `sources/**` are intentional provenance unless a separate decision proves otherwise.
