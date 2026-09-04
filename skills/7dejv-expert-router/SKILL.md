---
name: 7dejv-expert-router
description: Route a mixed or ambiguous 7DEJV task to the smallest relevant expert skill pack and preferred tool surface. Use when the task spans multiple domains or when it is unclear which specialist skills, MCP, plugin, CLI or subagent should be used. Do not use when a more specific skill already clearly matches.
---

# 7DEJV Expert Router

## Goal

Choose the smallest expert configuration that can complete the task safely and with good routing quality. Do not activate every available capability by default.

## Inputs

- user goal;
- target repository/project if known;
- current runtime capabilities;
- applicable repository `AGENTS.md`;
- available skill-pack manifest under `runtime/codex/packs/skill-packs.json` when present.

## Routing procedure

1. Classify the task into one or more domains:
   - `engineering`;
   - `security-quality`;
   - `data-analysis`;
   - `research-rnd`;
   - `product-commerce`;
   - `ui-product-design`;
   - `ops-integrations`.
2. Prefer one primary pack. Add a second pack only when the task genuinely crosses domains.
3. If the task is broad and no smaller pack is adequate, use `generalist` at project scope.
4. Prefer an already-installed specific skill over installing a broader pack.
5. Prefer native/built-in tools or existing connected plugins before creating a new MCP/tool wrapper.
6. Use classic MCP for external capabilities that must work independently of an open page/session; use site/WebMCP-style capabilities for actions belonging to the current web application/session when supported.
7. Use deterministic CLI/code for repeatable mechanics such as validation, filtering, joins, schema checks and idempotent transformations.
8. Delegate bounded work to specialist subagents when it reduces context or improves independent review; keep one implementation owner.

## Activation behavior

When a required pack is not active in the target repository, do not pretend it is installed. Return or execute the canonical project-scoped activation path when authorized:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -ProjectRoot <repo-path> -Pack <pack-name>
```

Run dry-run first. Apply only after conflicts are reviewed:

```powershell
pwsh ./scripts/install_codex_runtime.ps1 -Apply -ProjectRoot <repo-path> -Pack <pack-name>
```

Do not use `-Force` unless the conflicting destination was explicitly reviewed and backup behavior is understood.

## Preferred external capability mapping

- code/repositories/PR/CI → GitHub;
- current OpenAI/Codex/API behavior → OpenAI Developers / official docs MCP;
- database/PostgreSQL/Supabase projects → Supabase;
- UI/design-system/mock implementation → Figma + Product Design;
- documents/source packs → Google Drive when the source actually lives there;
- marketing/product visuals → Creative Production when visual generation is part of the requested workflow.

Availability must be verified at runtime. A capability listed here is a routing preference, not proof that it is installed or connected.

## Output

Return:

- primary domain/pack;
- optional secondary pack and why it is needed;
- selected skills/tools/subagents;
- capabilities intentionally not enabled;
- required approval or activation step;
- expected validation/evidence path.

## Guardrails

- Do not install every canonical skill globally just to maximize apparent capability.
- Do not create a new agent, skill, MCP or plugin wrapper before searching for an existing equivalent.
- Do not treat plugin presence, canonical storage or documentation as proof of runtime activation.
- Consequential writes remain approval-sensitive and must be protected by the target system's own auth/authz/policy, not only by routing metadata.
