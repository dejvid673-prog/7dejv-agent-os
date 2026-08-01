---
name: 7dejv-repo-index-generator
description: Generate canonical machine-readable catalogs of 7DEJV agents, skills, workflows, schemas and audits from the actual repository tree. Use after structural changes and before documentation or readiness checks.
---

# 7DEJV Repository Index Generator

## Inputs
- repository root,
- catalog output directory,
- optional prior registries.

## Procedure
1. Discover agent Markdown files, skill folders, workflows, schemas and audit reports.
2. Extract names, paths, versions and declared statuses where available.
3. Reject duplicate canonical names.
4. Generate deterministic sorted JSON registries.
5. Report additions, removals and unresolved metadata.

## Output
Return generated registry paths, item counts, duplicates, missing metadata and status.

## Errors and stop conditions
Return `BLOCKED` for duplicate canonical names. Return `HOLD` when required metadata cannot be derived.

## Limits
Do not invent ownership, approval or runtime evidence. Generated registries must reflect the repository state.

## Examples
A skill is indexed from its YAML frontmatter, while an agent is indexed from its Markdown filename and heading.

## Tests and acceptance criteria
Repeated generation from an unchanged repository must produce identical output.
