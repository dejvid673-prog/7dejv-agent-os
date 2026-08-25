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

- `agents/` — canonical contracted agent definitions.
- `skills/` — canonical native skills (`SKILL.md` + provenance where applicable).
- `workflows/` — canonical global work procedures and gates.
- `prompts/` — reusable canonical prompt assets.
- `registry/` — machine-readable repositories, agents, skills, workflows and prompts.
- `schemas/` — formal contracts for registries/tasks and future machine-readable artifacts.
- `tasks/` — multi-agent task ownership and handoff protocol.
- `scripts/` — executable deterministic validation/audit helpers.
- `.github/workflows/` — CI quality gates.
- `inventory/` — human-readable inventory views.
- `docs/inventory/` — audit/inventory evidence.
- `docs/decisions/` — architecture, promotion and cleanup decisions.
- `sources/` — immutable historical/migration archive; reference only.

## Canonical catalogs

Machine-readable routing starts from:

- `registry/repositories.json` — 16 repositories in the 2026-08-25 snapshot;
- `registry/agents.json` — 5 active contracted agents;
- `registry/skills.json` — 32 canonical skills;
- `registry/workflows.json` — 5 active global workflows/gates;
- `registry/prompts.json` — 2 active canonical prompts.

An artifact under a canonical directory is not allowed to silently bypass its registry where CI enforcement exists.

## Current validation

Run:

```bash
python scripts/validate_repository.py
python scripts/validate_catalogs.py
python scripts/validate_skill_registry.py
python scripts/validate_schema_documents.py
```

GitHub Actions compiles and executes all validators on pull requests and pushes to `main`. The checks cover repository inventory consistency, canonical skill identity/frontmatter, agent/workflow/prompt registry uniqueness and path coverage, required paths, JSON Schema document integrity, and a small set of high-confidence secret patterns.

## Current migration status

- 32 canonical skills are registered: 30 promoted with migration provenance plus 2 pre-existing bootstrap skills (`repository-inventory-skill` and `skills-normalization-skill`), now normalized to the canonical contract style.
- 5 canonical agents are active: inventory, organizer, repository-quality auditor, security auditor and documentation-consistency auditor.
- 5 canonical global workflows are active: inventory, normalization, repository quality gate, agent-definition review and security release gate.
- 2 canonical prompts are registered and bounded by the same trust/cleanup rules.
- remaining imported agent/workflow candidates stay `HOLD` until their contracts, global/local scope and overlap are resolved.
- historical/reference copies under `sources/**` are retained deliberately.
- the two historical `codex-workflow-router` variants remain reference-only: the feature variant adds a local STAW/Repetytorium mode to the global router, and neither variant may be promoted until all referenced capabilities can be resolved against canonical registries.

The current priority is executable governance, registry completeness, conflict consolidation and evidence-backed promotion—not increasing artifact count for its own sake.
