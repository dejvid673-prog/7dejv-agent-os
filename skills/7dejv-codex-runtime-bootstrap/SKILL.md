---
name: 7dejv-codex-runtime-bootstrap
description: Audit, install, sync or repair the user-level 7DEJV Codex runtime and project-scoped expert packs from canonical repository assets. Use when configuring Codex guidance, skills, subagents, profile/MCP settings or runtime readiness; do not use for ordinary application-code changes.
---

# 7DEJV Codex Runtime Bootstrap

## Purpose

Turn the canonical runtime assets in `7dejv-agent-os/runtime/codex` into a verified local Codex setup without silently overwriting personal configuration, and activate only the specialist skills needed by the current project.

## Inputs

Required:

- canonical `7dejv-agent-os` repository/ref;
- target Codex home or the platform default;
- whether the task is audit-only, dry-run planning or an explicitly approved apply operation.

Optional:

- target project root;
- one or more expert packs from `runtime/codex/packs/skill-packs.json`;
- install all canonical skills instead of the small baseline set;
- explicit approval to replace conflicting runtime copies after backup.

## Procedure

1. Verify the exact repository/ref and read `runtime/codex/README.md`.
2. Inspect current runtime state with `python scripts/audit_codex_runtime.py` when local filesystem/command access is available.
3. Run `pwsh ./scripts/install_codex_runtime.ps1` without `-Apply` first.
4. Review every `HOLD`/`BLOCKED`, especially an existing global `AGENTS.md`, profile, custom agent or installed-skill conflict.
5. Do not overwrite a conflicting runtime artifact unless the user explicitly approves replacement; use `-Force` only after reviewing the specific conflict.
6. Apply the small global baseline with `pwsh ./scripts/install_codex_runtime.ps1 -Apply` only after the plan is acceptable.
7. For a project needing specialist capabilities, select the smallest relevant expert pack using `7dejv-expert-router` and dry-run it with:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -ProjectRoot <repo-path> -Pack <pack-name>
```

8. Apply a reviewed project pack with:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply -ProjectRoot <repo-path> -Pack <pack-name>
```

9. Restart/reload the relevant Codex client.
10. Run the runtime audit again; when packs were activated, verify them explicitly with `--project-root` and `--pack`.
11. Verify `codex --profile 7dejv` starts successfully.
12. Verify MCP state with `/mcp` and run representative smoke tasks for expert routing, skill triggering, documentation research, review and test delegation.
13. Report evidence and final state without treating installation alone as runtime verification.

## Expert-pack routing

Prefer one primary pack and add a second only when the repository genuinely crosses domains:

- `engineering` — software/repository work;
- `security-quality` — security and release quality;
- `data-analysis` — structured data and validation;
- `research-rnd` — evidence-first research/R&D;
- `product-commerce` — products/offers/multichannel commerce;
- `ui-product-design` — UI/product design delivery;
- `ops-integrations` — APIs/external systems/operations;
- `generalist` — project-scoped fallback when no smaller pack is adequate.

Do not use expert packs as a substitute for repository-local `AGENTS.md` or actual connected tools/MCP.

## Baseline acceptance criteria

A baseline runtime is `TESTED` only when:

- `codex --version` succeeds;
- `~/.codex/AGENTS.md` contains the intended 7DEJV global guidance;
- `~/.codex/7dejv.config.toml` parses and uses the intended approval/sandbox boundary;
- baseline skills, including `7dejv-expert-router`, are installed and match the canonical checkout;
- `docs_researcher`, `reviewer` and `test_runner` runtime adapters parse correctly;
- OpenAI Developer Docs MCP is configured and its runtime status is inspected;
- one representative smoke task demonstrates correct capability routing without an unnecessary write or permission escalation.

A project pack is `TESTED` only when its requested skills are present under the project's `.agents/skills`, match the canonical checkout and at least one representative project task routes correctly.

`CONFIGURED` is not `TESTED`; `TESTED` is not `VERIFIED` across every repository.

## Safety boundaries

- Dry-run first.
- Never write secrets to Codex config, skill files, logs or reports.
- Never overwrite the user's primary `~/.codex/config.toml` from this skill.
- Never default to `--yolo` or unrestricted permissions.
- Never install every canonical skill globally merely because it exists; use the baseline plus project-scoped expert packs.
- `-Pack` requires a concrete project root; do not turn domain packs into hidden global state.
- Runtime copies are not the source of truth; future synchronization starts from the canonical repository.

## Output

Return:

- target Codex home and global skills home;
- target project root and project skills home when applicable;
- selected expert packs and why they were selected;
- planned/applied artifacts;
- conflicts and backup locations;
- audit results;
- smoke-test evidence;
- final status `PASS`, `HOLD` or `BLOCKED` plus the next required action.
