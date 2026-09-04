# 7DEJV Codex Runtime Kit

Status: `DESIGNED`

This directory turns canonical 7DEJV guidance into a repeatable local Codex runtime without making the runtime itself the source of truth.

## Goal

A full 7DEJV Codex workstation should have four verified layers:

1. **Guidance** — a small global `AGENTS.md` plus repository-local `AGENTS.md` files.
2. **Reusable capabilities** — selected canonical skills installed under `$HOME/.agents/skills`.
3. **Runtime/tooling** — a safe Codex profile, subagents and bounded MCP servers.
4. **Evidence** — deterministic runtime audit plus repository CI validating the kit itself.

Canonical artifacts remain in `7dejv-agent-os`. Installed files under the user's home directory are runtime copies and must never become the source of truth.

## Official Codex locations used

- user guidance: `$CODEX_HOME/AGENTS.md` (normally `~/.codex/AGENTS.md`);
- user skills: `$HOME/.agents/skills/<skill>/SKILL.md`;
- user custom agents: `$CODEX_HOME/agents/*.toml`;
- profile config: `$CODEX_HOME/7dejv.config.toml`, selected with `codex --profile 7dejv`;
- project guidance/config remains repository-local and takes precedence where Codex defines closer/local instruction precedence.

## Included runtime assets

```text
runtime/codex/
├── README.md
├── global/
│   └── AGENTS.md
├── config/
│   └── 7dejv.config.toml
└── agents/
    ├── docs-researcher.toml
    ├── reviewer.toml
    └── test-runner.toml
```

Supporting deterministic scripts:

```text
scripts/install_codex_runtime.ps1
scripts/audit_codex_runtime.py
scripts/validate_codex_runtime_assets.py
```

## Baseline runtime capability set

The default installer deliberately does **not** install every domain skill globally. It installs a small cross-repository baseline:

- `repository-inventory-skill`;
- `7dejv-repository-quality-audit-skill`;
- `7dejv-secret-scanner`;
- `7dejv-external-dependency-auditor`;
- `7dejv-prompt-injection-defense`;
- `7dejv-eval-generator`;
- `7dejv-eval-grader`;
- `7dejv-readiness-status-calculator`;
- `7dejv-skill-linter`;
- `7dejv-skill-factory`.

Project/domain skills should normally be installed at repository scope or explicitly requested. Use `-AllCanonicalSkills` only when broad global discovery is intentional.

## Safe installation model

The installer is dry-run by default.

```powershell
pwsh ./scripts/install_codex_runtime.ps1
```

Apply only after reviewing the plan:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply
```

The installer:

- never edits `~/.codex/config.toml`;
- installs a separate `7dejv.config.toml` profile;
- never stores credentials or API keys;
- does not overwrite conflicting runtime files unless `-Force` is explicitly supplied;
- creates timestamped backups before forced replacement;
- reports `PASS`, `HOLD`, `BLOCKED` or `DRY_RUN` with concrete paths/actions.

After installation, restart the Codex client and run:

```powershell
python ./scripts/audit_codex_runtime.py
codex --profile 7dejv
```

Inside Codex, verify MCP state with `/mcp` and use a small smoke task that should trigger one baseline skill.

## Runtime profile philosophy

`7dejv.config.toml` is intentionally conservative:

- `approval_policy = "on-request"`;
- `sandbox_mode = "workspace-write"`;
- live web search for current documentation/research;
- multi-agent support enabled with bounded concurrency;
- OpenAI Developer Docs MCP configured as a non-required read-only research dependency;
- no hard-coded model slug, so the current Codex/client default remains authoritative unless the user explicitly selects a model.

Do not use `--yolo` as the default 7DEJV operating mode. Full-access sessions may be used only as explicit, task-scoped exceptions after reviewing the blast radius.

## Custom subagents

The kit adds only roles that provide clear reusable value beyond Codex's built-in `default`, `worker` and `explorer` agents:

- `docs_researcher` — read-only version-sensitive documentation verification;
- `reviewer` — read-only correctness/security/test review;
- `test_runner` — executes validation commands and reports evidence without editing source code.

These runtime TOML files are execution adapters. Canonical domain agent contracts remain under `agents/` and should not be duplicated here without a documented runtime need.

## Readiness states

- `DESIGNED` — assets exist in the canonical repository and pass static validation.
- `CONFIGURED` — installer applied the assets to an actual Codex home.
- `CONNECTED` — Codex starts with the profile and required MCP/tool surfaces initialize.
- `TESTED` — runtime audit and smoke tasks succeed.
- `VERIFIED` — representative real project tasks demonstrate correct routing, permissions and evidence behavior.

`DESIGNED != CONFIGURED != TESTED != VERIFIED`.

## Sources

This runtime layout follows current OpenAI Codex documentation checked on 2026-09-04, including AGENTS, Skills, Config, MCP, Subagents, Hooks, sandbox/approval and customization guidance. Version-sensitive behavior must be rechecked against current official documentation before future changes.