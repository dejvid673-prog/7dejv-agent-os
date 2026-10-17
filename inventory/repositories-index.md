# Repositories Index

Snapshot: 2026-09-04
Owner: `dejvid673-prog`
Source: current GitHub repository inventory.
Machine-readable source: `registry/repositories.json`.

## Current repositories

There are 19 repositories in scope at this snapshot.

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

### reference-low-signal

- `Agent-repo`
- `7dejv-dawid`
- `bufor-github`
- `WATAHA`

### empty

- `n8n`
- `n8n_7d`

## Classification notes added in this snapshot

- `7dejv-mcp` is an active domain/project repository and its own source of truth for the 7DEJV MCP implementation.
- `Explorer--najciekawsze` is an active domain repository used as the 7DEJV technology radar; its findings are candidates/evidence, not global governing instructions.
- `WATAHA` currently contains insufficient repository evidence beyond a minimal README, so it remains `review` / `reference-low-signal` until its intended role is documented.

## Routing rules

1. Shared agents, skills, workflows, prompts and their governance belong in `7dejv-agent-os`.
2. Migration-source repositories are evidence/input until their shared artifacts are promoted or explicitly rejected.
3. Product/domain repositories own product-specific code and local instructions only.
4. Reference-low-signal repositories require explicit review before reuse.
5. Empty repositories must not be assumed to provide capabilities.
6. Classification is not a deletion decision. Repository retirement requires a separate audit and explicit approval.
7. Canonical registration does not prove runtime installation/discovery; runtime activation must be separately verified.
