---
name: skills-normalization-skill
description: Normalize inventoried agents, skills and workflows into a canonical source-of-truth structure with provenance-aware duplicate handling. Use after inventory and before promotion, migration or cleanup.
---

# Skills Normalization Skill

## Inputs

Required:

- evidence-backed inventory;
- current canonical structure and policies;
- candidate source/reference artifacts.

Optional:

- prior normalization decisions;
- overlap or contract audit findings.

## Procedure

1. Verify inventory provenance and canonical boundaries.
2. Group artifacts by purpose and contract, not name alone.
3. Compare content, scope, inputs/outputs and dependencies.
4. Classify candidates as `canonical`, `reference`, `duplicate`, `unclear` or `deprecated`.
5. For any proposed duplicate cleanup, identify the canonical replacement and verify that no independent archival/provenance role exists.
6. For conflicts, request a consolidation decision instead of creating another variant.
7. Produce the smallest reversible migration/cleanup plan with registry/documentation updates and validation requirements.

## Output

Return:

- canonicalization map;
- per-artifact classification and evidence;
- proposed promotions/migrations/deletions;
- conflicts requiring review;
- affected registries/docs;
- validation requirements;
- status `PASS`, `HOLD` or `BLOCKED`.

## Limits and stop conditions

- Never classify artifacts as duplicates from similar names alone.
- Never delete `sources/**` solely because a canonical copy exists.
- Stop destructive cleanup when replacement, provenance, ownership or rollback evidence is incomplete.
- Return `HOLD` for ambiguous equivalence/scope/provenance.
- Return `BLOCKED` if cleanup could remove the only known copy, destroy provenance or overwrite conflicting work.
