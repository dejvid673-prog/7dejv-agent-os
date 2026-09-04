# Source Of Truth

`7dejv-agent-os` is the canonical source of truth for shared 7DEJV:

- agents;
- skills;
- workflows;
- prompts;
- registries and policies;
- agent-artifact inventory and audit evidence.

## Online first

1. GitHub state is authoritative for 7DEJV repositories.
2. Local clones are working copies only until their state is committed and visible on GitHub.
3. Inventory and routing start from the current online repository list.
4. `registry/repositories.json` is the machine-readable repository inventory; human-readable indexes must agree with it.

## Canonical vs reference

Canonical active definitions live in first-class directories such as `agents/`, `skills/`, `workflows/`, `prompts/`, `registry/` and `policies/`.

`sources/**` is an immutable migration/reference archive. It preserves provenance and historical evidence. Content under `sources/**` must not be treated as an active instruction source and must not be deleted merely because an identical canonical copy exists.

Product repositories may keep local usage documentation, compatibility stubs and product-specific instructions. They are not the source of truth for shared 7DEJV agents, skills or workflows.

## Canonical vs runtime-active

Canonical storage and runtime activation are separate states.

A shared artifact being canonical in this repository does **not** make Codex automatically discover or apply it while working in another repository. Before reporting an artifact as installed, active or enforced in a target runtime, verify the actual supported activation path, for example:

- applicable `AGENTS.md` / `AGENTS.override.md` guidance in the target instruction hierarchy;
- a discoverable Codex skill under a supported `.agents/skills` or user/admin/system skill location;
- an installed plugin that distributes the skill or MCP dependency;
- active MCP/config/managed-policy configuration in that runtime;
- another explicitly documented and tested installation mechanism.

The canonical artifact remains maintained here. Runtime copies/installations must retain provenance and must not silently diverge from the canonical contract. If a sync/install mechanism is introduced, its version/evidence rules must be documented and tested before it is treated as reliable.

See `docs/decisions/openai-platform-alignment-2026-09-04.md` for the current OpenAI/Codex platform boundary.

## Artifact status

- `canonical` — active reference version.
- `reference` — historical/supporting material, not active instructions.
- `duplicate` — redundant active artifact whose canonical replacement and cleanup evidence are known.
- `unclear` — conflict or incomplete evidence requires a decision.
- `deprecated` — intentionally retained compatibility artifact with a documented replacement.

These catalog statuses do not by themselves prove target-runtime installation or readiness.

## Migration and cleanup

A deletion or promotion requires:

1. identified canonical target;
2. verified source/provenance;
3. comparison of purpose and content/contract;
4. migration or cleanup decision in `docs/decisions/`;
5. updated registry/inventory where applicable.

Identical content in `sources/**` and a canonical directory is expected provenance preservation, not an automatic duplicate.

## Evidence rule

Documentation claims do not establish runtime readiness. Positive readiness must be backed by tests, CI, runtime logs or another explicit evidence artifact.
