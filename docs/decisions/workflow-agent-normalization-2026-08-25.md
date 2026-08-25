# Workflow and Agent Normalization — 2026-08-25

## Decision

Promote only global quality/security workflows and a minimal set of fully contracted quality/security agents. Keep product-local or registry-dependent historical variants in `sources/**` until their dependencies and scope are resolved.

## Canonical workflows promoted

- `workflows/quality/repository-quality-gate.md`
  - source blob: `f5c19b640303a885bb71161f0563ae941d85344b`
- `workflows/quality/agent-definition-review.md`
  - source blob: `ec7f9b6ec451a1a706cd665a0c05518593d02399`
- `workflows/security/security-release-gate.md`
  - source blob: `199cd87f556cbd0bfa2d1d1b213023fb5e51153f`

The promoted versions preserve intent while using the canonical `PASS/HOLD/BLOCKED` status model and current evidence rules.

## Workflow held as reference

`contract-validation-gate.md` remains reference-only because its contract assumes a concrete stage registry, business-rule validation and routing model. Promoting it globally would incorrectly turn a product/pipeline-specific assumption into a universal 7DEJV rule.

## Canonical agents promoted

- `7dejv-repository-quality-auditor`
- `7dejv-agent-security-auditor`
- `7dejv-documentation-consistency-agent`

Each candidate was rewritten as a full contract with primary/non-responsibilities, inputs, procedure, least-privilege tool scope, output, failure/stop behavior, handoff and validation references. Original source blobs are recorded in each agent file.

Existing `skills-inventory-agent` and `skills-organizer-agent` were normalized to the same contract standard rather than leaving two incompatible agent-definition formats active.

## Machine-readable catalogs

Added:

- `registry/agents.json`
- `registry/skills.json`
- `registry/workflows.json`

CI validators enforce registered paths, uniqueness and canonical directory coverage. This is intended to prevent silent active artifacts and duplicate names from reappearing.

## Router conflict

Two historical `codex-workflow-router` variants were compared:

- base/main source blob: `28dd1531b2e37ea7b01bd6adb4f5229c46d49b2b`
- feature/STAW source blob: `3f1cd94e55bd98c78f401380aee01715ae274e24`

The feature version is substantially the base router plus a knowledge-base/visual-prototype mode tied to STAW/Repetytorium artifacts. That addition is product/domain-local and must not silently become a global routing rule.

Decision: do not promote either router yet and do not create a third merged variant. The base/main version is the better future global candidate, but promotion remains `HOLD` until its referenced skills/procedures can be resolved against canonical registries. The STAW-specific mode should ultimately live in a local domain workflow/router if still needed.

## Duplicate cleanup

No provenance/reference copy under `sources/**` is deleted. No competing active canonical artifact with proven semantic equivalence was found in this phase. The correct cleanup action is therefore consolidation/registration, not destructive deletion.

## Validation gate

Merge requires successful GitHub Actions execution of repository, agent/workflow catalog and skill-registry validators. A green workflow is execution evidence; this decision document alone is not.
