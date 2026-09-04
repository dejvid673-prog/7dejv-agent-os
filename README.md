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

**Canonical storage is not the same as runtime activation.** A skill, policy or workflow stored here is not automatically discovered or enforced by Codex in another repository. Target runtimes must use a supported, verified activation path (`AGENTS.md` hierarchy, `.agents/skills`, plugin, MCP/config/managed policy, or another explicitly documented mechanism). See `SOURCE_OF_TRUTH.md` and `docs/decisions/openai-platform-alignment-2026-09-04.md`.

## Operating model

1. GitHub is authoritative; inspect online state before acting.
2. Reuse existing canonical artifacts before creating new ones.
3. `sources/**` is immutable reference evidence, never an active instruction surface.
4. Shared artifacts are promoted only after provenance and contract review.
5. Completion requires evidence; documentation alone does not establish runtime readiness.
6. Non-trivial changes use a branch and pass the repository quality gate.
7. For current external APIs/SDKs/platforms, verify current official documentation during the task rather than relying on historical examples or agent memory.

See `AGENTS.md` for instruction precedence, security, cleanup and multi-agent rules.
See `SOURCE_OF_TRUTH.md` for canonical/reference/runtime boundaries.

## Structure

- `agents/` — canonical contracted agent definitions.
- `skills/` — canonical native-skill source artifacts (`SKILL.md` + provenance where applicable); target-runtime discovery must be separately verified.
- `workflows/` — canonical global work procedures and gates.
- `prompts/` — reusable canonical prompt assets.
- `registry/` — machine-readable repositories, agents, skills, workflows and prompts.
- `schemas/` — formal contracts for registries/tasks and future machine-readable artifacts.
- `tasks/` — multi-agent task ownership and handoff protocol.
- `scripts/` — executable deterministic validation/audit helpers.
- `runtime/codex/` — canonical installation/profile/subagent adapters plus expert-pack routing for turning this repository into an actual local Codex runtime; see `runtime/codex/README.md`.
- `.github/workflows/` — CI quality gates.
- `inventory/` — human-readable inventory views.
- `docs/inventory/` — audit/inventory evidence.
- `docs/decisions/` — architecture, promotion and cleanup decisions.
- `sources/` — immutable historical/migration archive; reference only.

## Canonical catalogs

Machine-readable routing starts from:

- `registry/repositories.json` — repository inventory snapshot;
- `registry/agents.json` — active contracted agents;
- `registry/skills.json` — canonical skills;
- `registry/workflows.json` — active global workflows/gates;
- `registry/prompts.json` — active canonical prompts.

An artifact under a canonical directory is not allowed to silently bypass its registry where CI enforcement exists.

## Codex runtime bootstrap

The repository contains a safe user-runtime bootstrap path. Dry-run first:

```powershell
pwsh ./scripts/install_codex_runtime.ps1
```

After review, apply:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply
python ./scripts/audit_codex_runtime.py
codex --profile 7dejv
```

The installer does not overwrite the primary `~/.codex/config.toml`; it installs a separate profile, a small global baseline skill set and bounded custom subagents. Conflicting existing runtime files return `HOLD` unless replacement is explicitly requested with `-Force`, with backup first.

### Expert packs

Broad capability is provided through **project-scoped expert packs**, not by globally installing every domain skill. Current families:

- `engineering`;
- `security-quality`;
- `data-analysis`;
- `research-rnd`;
- `product-commerce`;
- `ui-product-design`;
- `ops-integrations`;
- `generalist` as a project-scoped fallback.

The canonical `7dejv-expert-router` selects the smallest useful pack/tool surface for mixed-domain work.

Dry-run one project pack:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -ProjectRoot G:\path\to\repo -Pack engineering
```

Apply after review:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply -ProjectRoot G:\path\to\repo -Pack engineering
python ./scripts/audit_codex_runtime.py --project-root G:\path\to\repo --pack engineering
```

## Current validation

Run:

```bash
python scripts/validate_repository.py
python scripts/validate_catalogs.py
python scripts/validate_skill_registry.py
python scripts/validate_schema_documents.py
python scripts/validate_codex_runtime_assets.py
```

GitHub Actions compiles and executes all validators on pull requests and pushes to `main`. The checks cover repository inventory consistency, canonical skill identity/frontmatter, agent/workflow/prompt registry uniqueness and path coverage, required paths, JSON Schema document integrity, Codex runtime/profile/subagent/expert-pack contracts, PowerShell installer syntax, and a small set of high-confidence secret patterns.

## Current migration status

- Canonical skill, agent, workflow and prompt counts are defined by the machine-readable registries; do not copy stale counts into downstream repositories.
- Imported candidates remain `HOLD` until their contracts, global/local scope and overlap are resolved.
- Historical/reference copies under `sources/**` are retained deliberately.
- Conflicting router/reference variants remain reference-only until referenced capabilities can be resolved against canonical registries.

The current priority is executable governance, registry completeness, conflict consolidation, correct runtime activation and evidence-backed promotion—not increasing artifact count for its own sake.
