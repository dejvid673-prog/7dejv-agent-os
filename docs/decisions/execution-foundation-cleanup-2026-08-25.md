# Execution Foundation Cleanup — 2026-08-25

## Decision

Move `7dejv-agent-os` from a documentation-heavy migration repository toward an enforceable canonical control plane without broad refactoring or uncontrolled artifact creation.

## Changes

1. Harden root `AGENTS.md` with instruction precedence, trust boundaries, multi-agent ownership, cleanup rules, security and evidence requirements.
2. Define `sources/**` as immutable reference data, never an active instruction source.
3. Refresh repository inventory from current GitHub state: 16 repositories.
4. Add `registry/repositories.json` as the machine-readable repository inventory.
5. Add JSON schemas for repository registry and multi-agent task contracts.
6. Add executable `scripts/validate_repository.py` using only the Python standard library.
7. Add `.github/workflows/repository-quality.yml` to compile and execute the validator.
8. Add the `tasks/` ownership/handoff protocol.
9. Update README and script documentation to reflect the executable operating model.

## Duplicate cleanup decision

No canonical artifact was deleted in this change solely because an identical copy exists under `sources/**`.

Reason: those copies preserve provenance and historical migration evidence. Under the established architecture they are intentional reference copies, not competing active definitions.

No unambiguous competing canonical duplicate was proven during this cleanup. Therefore destructive deletion would violate the repository's own cleanup rules.

Conflicting versions such as previously identified workflow/router variants remain subject to a dedicated semantic comparison before consolidation.

## Evidence and validation

- Current online repository inventory contains 16 repositories under `dejvid673-prog`.
- The executable validator and CI workflow were added in this branch.
- Local clone-based execution could not be performed from the tool runtime because outbound DNS access to GitHub was unavailable.
- CI result must therefore be reviewed before merge; successful workflow execution is the required execution evidence for this change.

## Follow-up

After the foundation CI passes:

1. normalize/promote canonical quality and security workflows from `sources/**`;
2. add deterministic fixtures/tests before broadening scanner rules;
3. compare and consolidate conflicting router/workflow variants;
4. complete contracts for the first quality/security agents before promoting domain agents;
5. automate generation or verification of human-readable indexes from registries.
