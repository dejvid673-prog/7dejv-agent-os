# Canonical Catalog Hardening — 2026-08-25

## Decision

Remove remaining format/validation exceptions from canonical artifact catalogs and close the gap for prompts and registry schemas.

## Changes

1. Normalize the two pre-existing bootstrap workflows to explicit `Status: canonical`, evidence-backed `PASS/HOLD/BLOCKED` procedures.
2. Remove their legacy exception from `scripts/validate_catalogs.py`.
3. Normalize the two pre-existing bootstrap skills (`repository-inventory-skill`, `skills-normalization-skill`) with explicit inputs, procedure, output, limits and stop conditions.
4. Normalize the two canonical prompts and add `registry/prompts.json`.
5. Extend catalog validation to require every canonical prompt to be registered and explicitly marked canonical.
6. Add JSON Schema contracts for agent, skill, workflow and prompt registries.
7. Add `scripts/validate_schema_documents.py` and execute it in GitHub Actions.

## Duplicate/cleanup rule

This hardening intentionally removes validation exceptions and hidden catalog state rather than deleting provenance. No artifact under `sources/**` is deleted. No active artifact is deleted without a proven canonical replacement and absence of an independent archival role.

## Acceptance criteria

- repository validator passes;
- agent/workflow/prompt catalog validator passes with no exceptions;
- skill registry validator passes for all 32 canonical skills;
- all JSON Schema documents parse and expose the expected draft, `$id`, title and root object type;
- GitHub Actions workflow completes successfully before merge.
