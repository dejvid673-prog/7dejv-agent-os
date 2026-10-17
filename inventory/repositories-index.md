# Repositories Index

Snapshot: 2026-10-08
Owner: `dejvid673-prog`
Source: current GitHub repository inventory.
Machine-readable source: `registry/repositories.json`.

## Current repositories

There are 21 repositories in scope at this snapshot. Registry status is not a claim of deployed runtime.

### canonical-control-plane

- `7dejv-agent-os`

### primary-migration-source

- `7dejv-skills-prompts`
- `7dejv-ai-command-center`
- `7dejv.os`
- `7dejv-staw-expert`
- `airtable-agent`

### product-or-domain-repository

- `7dejv-mcp`
- `7dejv-prestashop`
- `7dejv-prestashop-resources`
- `allegro`
- `Explorer--najciekawsze`
- `repetytorium`
- `ideas`
- `mcp`

### reference-low-signal

- `Agent-repo` — status: `review`
- `7dejv-dawid` — status: `review`
- `bufor-github` — status: `review`
- `WATAHA` — status: `review`
- `7dejv_os` — status: `review`

### empty

- `n8n` — status: `empty`
- `n8n_7d` — status: `empty`

## Routing rules

1. Shared agents, skills, workflows, prompts and their governance belong in `7dejv-agent-os`.
2. Migration-source repositories are evidence/input until their shared artifacts are promoted or explicitly rejected.
3. Product/domain repositories own product-specific code and local instructions only.
4. Reference-low-signal repositories require explicit review before reuse.
5. Empty repositories must not be assumed to provide capabilities.
6. Classification is not a deletion decision. Repository retirement requires a separate audit and explicit approval.
7. Canonical registration does not prove runtime installation/discovery; runtime activation must be separately verified.

## 2026-10-08 synchronization notes

- Compared registry names, visibility and default branches against the connected GitHub account: 21/21 repositories.
- `n8n`, `n8n_7d`, and `7dejv_os` contain only placeholder documentation, not proven automation/runtime capabilities.
- `7dejv-mcp` is an architectural source while `mcp` holds application code: similarity of names alone does not establish duplication.
- Do not archive, delete, migrate, or activate repositories automatically based on this inventory.
