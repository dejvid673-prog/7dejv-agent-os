# OpenAI platform alignment — 2026-09-04

Status: `canonical decision record`

## Purpose

Record the current OpenAI/Codex platform facts that materially affect 7DEJV architecture and make the adoption boundary explicit. This document does not claim runtime readiness of any integration.

## Source contract

Authoritative sources for platform-dependent behavior are current official OpenAI documentation and product documentation checked on 2026-09-04. Repository artifacts remain authoritative for 7DEJV-specific decisions and product code.

Primary official indexes reviewed:

- https://developers.openai.com/llms.txt
- https://developers.openai.com/plugins/llms.txt
- https://developers.openai.com/workspace-agents/llms.txt
- https://developers.openai.com/commerce/llms.txt
- https://developers.openai.com/codex/llms.txt
- https://developers.openai.com/cookbook/llms.txt
- https://learn.chatgpt.com/use-cases/llms.txt

Relevant official guidance includes Codex AGENTS, skills, MCP, Hooks, Rules, sandbox/approvals, subagents, worktrees, Codex SDK, App Server, `codex exec`, plugins, WebMCP/site tools, Workspace Agents, Agentic Commerce, evals and current OpenAI developer examples.

## Canonical storage is not runtime activation

`7dejv-agent-os` is the canonical governance/catalog source for shared 7DEJV artifacts. That does **not** mean Codex automatically discovers or applies those artifacts while working in another repository.

A shared artifact is runtime-active only when its activation path is verified for the target environment, for example:

- repository guidance is present in the applicable `AGENTS.md` / `AGENTS.override.md` hierarchy;
- a Codex skill is installed/discoverable from a supported location such as `$REPO_ROOT/.agents/skills` or `$HOME/.agents/skills`;
- a plugin containing the skill/MCP dependency is installed where that distribution model is used;
- MCP/config/managed policy is configured in the actual Codex runtime;
- another explicitly documented supported installation mechanism is verified.

Do not report a canonical skill, rule, workflow or MCP dependency as `active`, `installed` or `enforced` merely because its source exists in this repository.

## Codex execution architecture

Do not build a custom generic agent harness while the native Codex harness already satisfies the execution need.

Use the narrowest official integration surface that fits:

- `codex exec` — scripts, CI, pre-merge checks and bounded non-interactive jobs;
- Codex SDK — application/pipeline code that starts, resumes and programmatically controls Codex work;
- Codex App Server — a custom client/product that needs conversation lifecycle, event streaming, approvals and interactive agent state;
- Codex local/cloud clients — normal interactive development workflows.

The 7DEJV application layer should own business context, domain UI, source-of-truth records, operational boundaries and approval surfaces. Codex should own the agent loop rather than duplicating it in a custom manager.

## AGENTS, skills, workflows and deterministic code

Use the following responsibility split:

- `AGENTS.md` — small, durable repository guidance and mandatory routing rules;
- skills — focused reusable procedures for recognizable user goals;
- MCP — live external context and controlled external actions;
- CLI/scripts — deterministic, repeated local mechanics that are easier to validate as code;
- workflows — orchestration/decision structure that may invoke skills, MCP and deterministic tools;
- subagents — bounded delegation for exploration, review, testing or specialist analysis;
- Git worktrees — preferred isolation for parallel changes to the same repository.

A skill description is routing metadata. It must state when the skill should and should not trigger and what output it produces. Add scripts only when deterministic mechanics are genuinely more reliable than instructions plus existing tools.

Before creating a new agent, skill, workflow, script or MCP tool, search canonical registries and target-repository implementations for an existing equivalent.

## MCP and WebMCP boundary

Use classic MCP when a capability must exist independently of an open browser page or needs server-side access to an external system. This remains the default architecture for the PrestaShop integration.

Use WebMCP/site tools when the capability belongs to a currently open web application/session and can reuse that application's existing authentication, authorization and UI context. A future 7DEJV Dashboard may expose page-context actions this way instead of creating a separate MCP server for every UI-only action.

Website tools do not replace server-side authorization, validation or confirmation for consequential actions.

For a private/local MCP server that later needs hosted ChatGPT/OpenAI access, evaluate OpenAI's Secure MCP Tunnel before exposing a public endpoint or introducing a broad generic tunnel.

## Plugin boundary

Plugins are a distribution unit for reusable skills, MCP dependencies and optional UI. Start with the smallest working shape:

1. instructions/skill if existing tools are enough;
2. MCP only when live external capabilities are required;
3. optional UI only when it improves the user workflow;
4. package as a plugin when reusable distribution is actually needed.

Do not build a plugin merely to package a repository-local experiment.

## Tool design contract

For MCP/plugin tools:

- design from user goals, not by mirroring internal API endpoints;
- separate read and write operations when permissions/safety differ;
- use explicit stable identifiers and bounded inputs;
- state auth requirements, side effects and failure behavior;
- return minimum structured data needed to continue and verify the task;
- do not expose secrets, raw diagnostics or unnecessary personal data;
- use correct read/destructive/open-world annotations, but never treat annotations as authorization;
- server-side auth/authz/validation remain mandatory.

Maintain a small golden prompt/eval set containing direct, indirect, negative and edge-case prompts for important tools and skills. Metadata changes should be evaluated rather than treated as cosmetic documentation edits.

## Verification and run evidence

Preferred execution lifecycle:

`SOURCE/INVENTORY -> PLAN -> APPROVAL (when needed) -> ACTION -> EXPECTED RESULT -> VERIFICATION -> EVIDENCE -> STATUS`

For repeatable or long-running work, preserve a run record/notebook containing at least:

- intent/goal;
- source references;
- plan;
- commands/actions performed;
- relevant outputs;
- interpretation;
- decisions/approvals;
- failures and dead ends that materially affected the result;
- verification evidence;
- final status and next action.

An agent statement that work is complete is not evidence. A successful process exit code alone is not enough when correctness depends on resulting behavior or output content.

## Current external documentation rule

When implementing or changing behavior that depends on a current external API, platform or SDK, verify the relevant current official documentation during the task. Historical repository examples and agent memory are supporting context, not authority for version-sensitive external behavior.

If documentation and a canonical 7DEJV artifact conflict, record the conflict before changing the canonical artifact. Do not silently reinterpret an old local decision as a new global rule.

## PrestaShop decision scope

The 2026-08-25 canonical `prestashop-operations-agent` decision selected the native PrestaShop Classic Webservice and read-only production operation for that agent. Treat that as a valid historical/project decision for that agent, not as proof that every future PrestaShop integration must use Classic Webservice.

The separate `7dejv-mcp` project currently requires a fresh API-choice audit for its four READ tools. Admin API versus Classic Webservice must be decided from the target PrestaShop version, available endpoints, authentication model, installed modules, permissions and runtime evidence. No silent fallback between authentication/API mechanisms.

Until that audit is accepted, do not use the older Webservice choice to mark the new MCP API adapter as `DESIGNED` or `VERIFIED`.

## Workspace Agents

Workspace Agents are a separate execution surface. They can be triggered from backend systems/automations when a published workspace agent and API channel are configured.

Use them when a ChatGPT-native workspace workflow is the desired destination. Do not treat Workspace Agents as the canonical storage layer for 7DEJV repo artifacts, and do not use them as a drop-in replacement for machine-to-machine workflows that require a synchronously retrievable structured result unless the current API contract supports that requirement.

Use idempotency for retried external triggers and stable conversation continuity only when the workflow benefits from it.

## Commerce implications

Agentic Commerce/Product Feeds are a future commerce channel, not part of the PrestaShop MCP scope.

For future product-master design, preserve:

- stable parent product identifiers;
- unique purchasable variant identifiers;
- variant-specific price, availability, URL, media and description where they differ;
- explicit seller/policy links and channel attribution;
- validation and source ownership for catalog fields.

Do not implement an OpenAI product feed or Agentic Checkout until access, business value, product eligibility and compliance are separately reviewed. Pond/water-treatment chemical products require product-by-product eligibility review; do not assume the whole catalog is eligible.

## Adoption policy

This decision updates architecture/routing guidance only. It does not automatically promote new agents or skills.

Before adding a canonical artifact because an OpenAI example contains an analogous workflow:

1. search the existing registry;
2. compare scope and contract;
3. prefer extending a suitable canonical artifact over creating a near-duplicate;
4. add a new artifact only when the gap is real and reusable;
5. update registry/schema/evidence as required;
6. run repository validators and CI before promotion.

## Status

- OpenAI platform alignment: `DESIGNED` / documented against current official sources.
- Runtime installation/sync mechanism for canonical 7DEJV assets: `UNKNOWN` until separately designed and tested.
- PrestaShop MCP API adapter selection: `UNKNOWN` pending the MCP architecture audit.
- WebMCP use in 7DEJV Dashboard: candidate, not implemented.
- Agentic Commerce integration: future candidate, not implemented.
