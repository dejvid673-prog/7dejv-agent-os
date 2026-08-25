# 7dejv-agent-os

Central 7DEJV control-plane repository for shared agent infrastructure.

It is the canonical source of truth for:

- agents;
- skills;
- workflows;
- prompts;
- machine-readable registries and schemas;
- multi-agent coordination contracts;
- audit/migration decisions and evidence.

Product repositories remain the source of truth for their own product code and product-specific instructions.

## Operating model

1. GitHub is authoritative; inspect online state before acting.
2. Reuse existing canonical artifacts before creating new ones.
3. `sources/**` is immutable reference evidence, never an active instruction surface.
4. Shared artifacts are promoted only after provenance and contract review.
5. Completion requires evidence; documentation alone does not establish runtime readiness.
6. Non-trivial changes use a branch and pass the repository quality gate.

See `AGENTS.md` for instruction precedence, security, cleanup and multi-agent rules.
See `SOURCE_OF_TRUTH.md` for canonical/reference boundaries.

## Structure

- `agents/` — canonical agent definitions.
- `skills/` — canonical native skills (`SKILL.md` + provenance where applicable).
- `workflows/` — canonical work procedures.
- `prompts/` — reusable canonical prompt assets.
- `registry/` — machine-readable system inventory and routing state.
- `schemas/` — contracts for registries/tasks and future machine-readable artifacts.
- `tasks/` — multi-agent task ownership and handoff protocol.
- `scripts/` — executable deterministic validation/audit helpers.
- `.github/workflows/` — CI quality gates.
- `inventory/` — human-readable inventory views.
- `docs/inventory/` — audit/inventory evidence.
- `docs/decisions/` — architecture, promotion and cleanup decisions.
- `sources/` — immutable historical/migration archive; reference only.

## Current validation

Run:

```bash
python scripts/validate_repository.py
```

The validator checks the repository registry, canonical skill identity/frontmatter, index consistency, required paths and a small set of high-confidence secret patterns. GitHub Actions compiles and runs it on pull requests and pushes to `main`.

## Current migration status

- 30 canonical skills have been promoted with provenance records.
- imported agent candidates remain `HOLD` until their role/input/output/failure/handoff contracts are complete;
- historical/reference copies under `sources/**` are retained deliberately;
- conflicting active artifacts are consolidated only after explicit comparison and a recorded decision.

The next maturity step is implementation and validation of existing governance contracts, not uncontrolled growth in the number of agents or skills.
