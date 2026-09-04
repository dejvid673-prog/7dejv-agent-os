---
name: 7dejv-codex-runtime-bootstrap
description: Audit, install, sync or repair the user-level 7DEJV Codex runtime from canonical repository assets. Use when configuring Codex guidance, skills, subagents, profile/MCP settings or runtime readiness; do not use for ordinary application-code changes.
---

# 7DEJV Codex Runtime Bootstrap

## Purpose

Turn the canonical runtime assets in `7dejv-agent-os/runtime/codex` into a verified local Codex setup without silently overwriting personal configuration.

## Inputs

Required:

- canonical `7dejv-agent-os` repository/ref;
- target Codex home or the platform default;
- whether the task is audit-only, dry-run planning or an explicitly approved apply operation.

Optional:

- install all canonical skills instead of the small baseline set;
- explicit approval to replace conflicting runtime copies after backup.

## Procedure

1. Verify the exact repository/ref and read `runtime/codex/README.md`.
2. Inspect current runtime state with `python scripts/audit_codex_runtime.py` when local filesystem/command access is available.
3. Run `pwsh ./scripts/install_codex_runtime.ps1` without `-Apply` first.
4. Review every `HOLD`/`BLOCKED`, especially an existing global `AGENTS.md`, profile, custom agent or installed-skill conflict.
5. Do not overwrite a conflicting runtime artifact unless the user explicitly approves replacement; use `-Force` only after reviewing the specific conflict.
6. Apply with `pwsh ./scripts/install_codex_runtime.ps1 -Apply` only after the plan is acceptable.
7. Restart/reload the relevant Codex client.
8. Run the runtime audit again and verify `codex --profile 7dejv` starts successfully.
9. Verify MCP state with `/mcp` and run representative smoke tasks for skill triggering, documentation research, review and test delegation.
10. Report evidence and final state without treating installation alone as runtime verification.

## Baseline acceptance criteria

A baseline runtime is `TESTED` only when:

- `codex --version` succeeds;
- `~/.codex/AGENTS.md` contains the intended 7DEJV global guidance;
- `~/.codex/7dejv.config.toml` parses and uses the intended approval/sandbox boundary;
- baseline skills are installed and match the canonical checkout;
- `docs_researcher`, `reviewer` and `test_runner` runtime adapters parse correctly;
- OpenAI Developer Docs MCP is configured and its runtime status is inspected;
- one representative smoke task demonstrates correct capability routing without an unnecessary write or permission escalation.

`CONFIGURED` is not `TESTED`; `TESTED` is not `VERIFIED` across every repository.

## Safety boundaries

- Dry-run first.
- Never write secrets to Codex config, skill files, logs or reports.
- Never overwrite the user's primary `~/.codex/config.toml` from this skill.
- Never default to `--yolo` or unrestricted permissions.
- Never install every canonical skill globally merely because it exists; use the baseline unless broad discovery is explicitly desired.
- Runtime copies are not the source of truth; future synchronization starts from the canonical repository.

## Output

Return:

- target Codex home and skills home;
- planned/applied artifacts;
- conflicts and backup locations;
- audit results;
- smoke-test evidence;
- final status `PASS`, `HOLD` or `BLOCKED` plus the next required action.
