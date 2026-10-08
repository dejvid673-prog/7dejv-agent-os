# Repositories Index

Snapshot: 2026-10-08
Owner: `dejvid673-prog`
Source: current GitHub repository inventory.
Machine-readable source: `registry/repositories.json`.

## Current repositories

There are **21** repositories in scope at this snapshot. Classification describes routing and review priority; it does not prove deployment or recent development.

### canonical-control-plane

- `7dejv-agent-os`

### primary-migration-source

- `7dejv-ai-command-center`
- `7dejv-skills-prompts`
- `7dejv-staw-expert`
- `7dejv.os`
- `airtable-agent`

### product-or-domain-repository

- `7dejv-mcp`
- `7dejv-prestashop`
- `7dejv-prestashop-resources`
- `allegro`
- `ideas`
- `mcp`
- `repetytorium`
- `WATAHA`

### reference-low-signal

- `7dejv_os` — status: `review`
- `7dejv-dawid` — status: `review`
- `Agent-repo` — status: `review`
- `bufor-github` — status: `review`
- `Explorer--najciekawsze` — status: `review`

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

## Audit notes (2026-10-08)

- Registry entries were reconciled with the authenticated GitHub account's 21 accessible repositories.
- `n8n`, `n8n_7d` and `7dejv_os` have only placeholder documentation; do not infer operational readiness.
- `7dejv-mcp` documents architecture while `mcp` includes the executable integration foundation; do not classify them as duplicate without a technical comparison.
- `WATAHA` contains a domain PrestaShop agent with read-only policy; this is not a replacement for the canonical global agent registry.
- `Explorer--najciekawsze` is a technology research radar, not an application runtime.
- Repository deletion, archival, merges, or promotions require separate review and approval.
