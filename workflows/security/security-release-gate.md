# Security Release Gate

Status: `canonical`

Provenance: adapted from `sources/7dejv-skills-prompts/main/04_workflows/security/security-release-gate.md` (source blob `199cd87f556cbd0bfa2d1d1b213023fb5e51153f`).

## Purpose

Block merge, deployment or privileged runtime execution when security evidence is incomplete or a blocking risk is active.

## Sequence

```text
SECRET_SCAN
→ DEPENDENCY_CHECK
→ TOOL_PERMISSION_AUDIT
→ NETWORK_SCOPE_CHECK
→ PROMPT_INJECTION_REVIEW
→ DESTRUCTIVE_ACTION_REVIEW
→ LICENSE_REVIEW
→ REQUIRED_HUMAN_REVIEW
→ PASS / HOLD / BLOCKED
```

## `BLOCKED`

- active credential/private key exposure;
- destructive or externally consequential action without the required approval gate;
- unknown provenance for executable runtime code;
- protected-data extraction/exposure attempt;
- unjustified privileged write, publish, delete, purchase or permission-escalation capability.

## `HOLD`

- runtime dependency is unpinned where pinning is required;
- license/provenance metadata is incomplete;
- network destination or permission scope is not justified;
- required adversarial/security test evidence is missing;
- a material risk requires an explicit human decision.

## `PASS`

- no blocking security findings remain;
- runtime dependencies have sufficient source/version/license evidence;
- permissions follow least privilege;
- required security checks have execution evidence;
- risks requiring a human decision are explicitly accepted.

## Evidence rule

Never include complete secret values in reports. Removal from Git history does not replace credential rotation when exposure may have occurred.
