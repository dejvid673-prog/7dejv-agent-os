# 7DEJV Codex Runtime Kit

Status: `DESIGNED`

This directory turns canonical 7DEJV guidance into a repeatable local Codex runtime without making the runtime itself the source of truth.

## Goal

A full 7DEJV Codex workstation should have five verified layers:

1. **Guidance** — a small global `AGENTS.md` plus repository-local `AGENTS.md` files.
2. **Reusable capabilities** — a small global baseline plus project-scoped expert skill packs.
3. **Runtime/tooling** — a safe Codex profile, subagents and bounded MCP servers.
4. **Routing** — an expert router that selects the smallest relevant skill pack/tool surface instead of enabling everything.
5. **Evidence** — deterministic runtime audit plus repository CI validating the kit itself.

Canonical artifacts remain in `7dejv-agent-os`. Installed files under the user's home directory and project `.agents/skills` directories are runtime copies and must never become the source of truth.

## Official Codex locations used

- user guidance: `$CODEX_HOME/AGENTS.md` (normally `~/.codex/AGENTS.md`);
- user skills: `$HOME/.agents/skills/<skill>/SKILL.md`;
- repository skills: `$REPO/.agents/skills/<skill>/SKILL.md`;
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
├── packs/
│   └── skill-packs.json
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

## Global baseline

The default installer deliberately does **not** install every domain skill globally. It installs a cross-repository baseline:

- `repository-inventory-skill`;
- `7dejv-repository-quality-audit-skill`;
- `7dejv-secret-scanner`;
- `7dejv-external-dependency-auditor`;
- `7dejv-prompt-injection-defense`;
- `7dejv-eval-generator`;
- `7dejv-eval-grader`;
- `7dejv-readiness-status-calculator`;
- `7dejv-skill-linter`;
- `7dejv-skill-factory`;
- `7dejv-expert-router`.

`7dejv-expert-router` chooses the smallest specialist pack/tool surface for mixed or ambiguous work. Project/domain skills should normally remain repository-scoped.

## Expert packs

`runtime/codex/packs/skill-packs.json` defines validated project-scoped packs:

| Pack | Intended use |
|---|---|
| `engineering` | software engineering, repository work, contracts and implementation quality |
| `security-quality` | security, dependencies, prompt-injection resistance and release QA |
| `data-analysis` | structured data, contracts, schemas, validation and analytical work |
| `research-rnd` | evidence-first research, R&D briefs and test planning |
| `product-commerce` | product master, naming, copy, offer analysis and multichannel release QA |
| `ui-product-design` | UI/product-design delivery, visual validation and implementation quality |
| `ops-integrations` | APIs, external systems, integration contracts, secrets and operational readiness |
| `generalist` | balanced mixed-domain pack; project-scoped fallback when no smaller pack is adequate |

Packs contain only canonical skills from `registry/skills.json`. They can also record preferred external capabilities such as GitHub, Supabase, Figma or OpenAI Developers, but those names are routing preferences rather than proof that a plugin/service is installed or connected.

## Safe installation model

The installer is dry-run by default.

```powershell
pwsh ./scripts/install_codex_runtime.ps1
```

Apply the global baseline only after reviewing the plan:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply
```

Activate a specialist pack for one repository:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -ProjectRoot G:\path\to\repo -Pack engineering
```

Apply it after reviewing the dry-run:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply -ProjectRoot G:\path\to\repo -Pack engineering
```

Cross-domain repositories may receive more than one pack:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply -ProjectRoot G:\path\to\repo -Pack engineering,ops-integrations
```

Use `generalist` only when a smaller pack is not adequate. Use `-AllCanonicalSkills` only when broad **global** discovery is explicitly intended.

The installer:

- never edits `~/.codex/config.toml`;
- installs a separate `7dejv.config.toml` profile;
- never stores credentials or API keys;
- keeps expert packs project-scoped by requiring `-ProjectRoot`;
- does not overwrite conflicting runtime files unless `-Force` is explicitly supplied;
- creates timestamped backups before forced replacement;
- reports `PASS`, `HOLD`, `BLOCKED` or `DRY_RUN` with concrete paths/actions.

After installation, restart the Codex client and run:

```powershell
python ./scripts/audit_codex_runtime.py
codex --profile 7dejv
```

Verify one project pack explicitly:

```powershell
python ./scripts/audit_codex_runtime.py --project-root G:\path\to\repo --pack engineering
```

Inside Codex, verify MCP state with `/mcp` and use small representative tasks that should trigger the expert router, a pack skill and one specialist subagent.

## Runtime profile philosophy

`7dejv.config.toml` is intentionally conservative:

- `approval_policy = "on-request"`;
- `sandbox_mode = "workspace-write"`;
- live web search for current documentation/research;
- multi-agent support enabled with bounded concurrency;
- OpenAI Developer Docs MCP configured as a non-required read-only research dependency;
- no hard-coded model slug, so the current Codex/client default remains authoritative unless the user explicitly selects a model.

Do not use `--yolo` as the default 7DEJV operating mode. Full-access sessions may be used only as explicit, task-scoped exceptions after reviewing the blast radius.

## Tool and plugin routing

Prefer the narrowest existing surface instead of duplicating integrations:

- GitHub → repositories, PRs, issues and CI;
- OpenAI Developers / official docs MCP → current OpenAI/Codex/API behavior;
- Supabase → Supabase/PostgreSQL project work;
- Figma + Product Design → UI/design system/mock-to-implementation work;
- Google Drive → Drive-native source documents and packs;
- Creative Production → requested marketing/product visual production;
- classic MCP → capabilities that must exist independently of an open web page/session, such as the planned PrestaShop integration;
- deterministic CLI/code → filtering, joins, validation, schema checks, idempotent transformations and repeatable mechanics.

Do not add a second wrapper/MCP for a capability that an already connected tool handles adequately unless a real contract or security gap is documented.

## Custom subagents

The kit adds only roles that provide clear reusable value beyond Codex's built-in `default`, `worker` and `explorer` agents:

- `docs_researcher` — read-only version-sensitive documentation verification;
- `reviewer` — read-only correctness/security/test review;
- `test_runner` — executes validation commands and reports evidence without editing source code.

These runtime TOML files are execution adapters. Canonical domain agent contracts remain under `agents/` and should not be duplicated here without a documented runtime need.

## Readiness states

- `DESIGNED` — assets exist in the canonical repository and pass static validation.
- `CONFIGURED` — installer applied the assets to an actual Codex home/project.
- `CONNECTED` — Codex starts with the profile and required MCP/tool surfaces initialize.
- `TESTED` — runtime audit and smoke tasks succeed.
- `VERIFIED` — representative real project tasks demonstrate correct routing, permissions and evidence behavior.

`DESIGNED != CONFIGURED != TESTED != VERIFIED`.

## Sources

This runtime layout follows current OpenAI Codex documentation checked on 2026-09-04, including AGENTS, Skills, Config, MCP, Subagents, Hooks, sandbox/approval and customization guidance. Version-sensitive behavior must be rechecked against current official documentation before future changes.
