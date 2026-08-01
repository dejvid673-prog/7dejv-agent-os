---
name: 7dejv-external-dependency-auditor
description: Audit external repositories, packages and services used by 7DEJV for provenance, versioning, licensing, maintenance, permissions and security risk. Use before adoption, upgrade or release.
---

# 7DEJV External Dependency Auditor

## Inputs
- dependency registry,
- source repository or package identifier,
- pinned version or commit,
- license and deployment information,
- required credentials and permissions.

## Procedure
1. Verify source identity and ownership.
2. Require a pinned version, tag or commit for runtime use.
3. Record license, maintenance status and deployment model.
4. Identify required secrets, network access and filesystem permissions.
5. Check whether the dependency can be isolated or replaced.
6. Classify unresolved provenance, license and permission risks.

## Output
Return dependency findings, approved version, license status, required permissions, risk score, remediation and `PASS`, `HOLD` or `BLOCKED`.

## Errors and stop conditions
Return `BLOCKED` for unknown source, prohibited license, unreviewed executable code or unjustified privileged access. Return `HOLD` for unpinned versions or incomplete metadata.

## Limits
Do not copy or execute third-party code during a metadata-only audit. Do not mark a dependency approved without source and license evidence.

## Examples
A Git repository referenced only by its default branch remains `HOLD` until a reviewed commit is pinned.

## Tests and acceptance criteria
Every runtime dependency must have source, version, license, owner, permissions, update policy and approval status.
