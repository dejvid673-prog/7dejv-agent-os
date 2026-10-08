# GitHub repository and root README audit — 2026-10-08

Owner: `dejvid673-prog`  
Scope: **21 repositories** visible to the connected GitHub account.  
Method: repository list, default-branch README reads, root tree inspection, Markdown relative-path link checks, selected PR/issue/workflow evidence and current canonical registry comparison.  
Excluded: deployed service tests, local workstation tests, production authentication, comprehensive secrets/license audit and verification of all external websites.

## Results

- **21/21 root README.md files exist after the documented changes**; initially the `n8n` repository was completely empty.
- Six repositories received low-risk README changes directly on `main`: `n8n`, `n8n_7d`, `Agent-repo`, `WATAHA`, `7dejv_os`, `7dejv-dawid`.
- Root README Markdown **relative file links** were compared with default-branch file trees where present; no broken links were found in this check. External URLs, inline-code paths, anchors and claims about runtime were not exhaustively validated.
- The canonical `7dejv-agent-os` registry on `main` had 16 entries; pending PR #6 has 19; this branch extends that pending state to **21**. This change is stacked deliberately to avoid conflicts with PR #6.
- No repositories, branches, agents, automations or customer data were deleted or archived.

## Repository inventory and root README review

| Repository | Root README after audit | Observation |
| --- | --- | --- |
| 7dejv-agent-os | present | Canonical control plane; branch alignment required before merging this update |
| 7dejv-ai-command-center | present | Older June status/map documentation; review alongside existing routing PR |
| 7dejv-dawid | improved on main | Documents YAML lab and manually-triggered branch runner |
| 7dejv-staw-expert | present | Product/research source |
| 7dejv-skills-prompts | present | Skills/prompts migration and routing guidance |
| 7dejv-prestashop | present | Older pause/implementation language should be reconciled with recent RaFish module PRs |
| bufor-github | present | Source catalog and acquisition guidance |
| n8n | created on main | Documentation-only placeholder, no runnable n8n workflow |
| n8n_7d | improved on main | Documentation-only placeholder |
| Agent-repo | improved on main | Unmerged order-panel work is not part of default branch |
| repetytorium | one-line README on main | **HOLD**: rich README is on pending draft PR #1 with 139 changed files; avoid competing edit |
| airtable-agent | present but misleading on main | **HOLD**: main is documentation-only while executable implementation is proposed in PR #1 |
| 7dejv.os | present | 7DEJV OS UI/mockup materials, not proof of runtime |
| 7dejv-prestashop-resources | present | PrestaShop official/community sources and skills catalog |
| allegro | present | Clear product/operator guidance; scheduled OpenAPI freshness check needs attention |
| ideas | present | Project ideas/decisions index |
| WATAHA | improved on main | Domain agent documentation; read-only declaration is not a connectivity test |
| Explorer--najciekawsze | present | Technology research radar |
| 7dejv-mcp | present | MCP architecture/docs, not the executable implementation repo |
| mcp | present | MCP foundation/code; unresolved CI failures |
| 7dejv_os | improved on main | Documentation-only placeholder, not interchangeable with 7dejv.os |

## CI and automation findings

1. **allegro**: daily scheduled `Validate Allegro knowledge base` failures confirmed October 1–7. The October 7 job passes repository validation and fails `check_openapi_freshness.py` because the recorded Allegro OpenAPI fingerprint differs from the current one. Correct remediation: rebuild the API catalog, review the generated diff and verify compatible data/contracts; do **not** disable the safety check to turn CI green.
2. **7dejv-prestashop**: five inspected latest RaFish ZIP workflows on September 22 were successful. Earlier error emails do not mean the latest run failed.
3. **7dejv-ai-command-center**: the last inspected `Python package` runs failed; requires log-based follow-up.
4. **mcp**: a September 19 `CI` run failed while `Diagnose ERLI OpenAPI Drift` succeeded; requires separate investigation.
5. **7dejv-agent-os**: the repository-quality pipeline on an isolated initial audit PR had catalog consistency failures on base `main` (two status formats and two absent workflow registrations). Existing PR #6 already contains the corresponding catalog corrections and passed CI through dependent work. To avoid overlapping six changed paths, the repository count is updated on a fresh branch based on PR #6.

## Safety and handoff

- Keep `repetytorium` PR #1 draft until its project's phase gates allow it; do not copy the unmerged README into `main` because it links to unmerged paths.
- Do not assert that `airtable-agent` works on default `main` until implementation is merged and tested.
- Existing PR #6 in `7dejv-agent-os` is the **base of this audit branch**; merge order and CI must be checked before accepting the inventory.
- Repository similarity (`mcp` / `7dejv-mcp`; `7dejv.os` / `7dejv_os`) alone is insufficient evidence to archive or merge repositories.
- No executable agent/runtime readiness is claimed by this report. Further secret scanning and full cross-file documentation consistency checks remain separate audit tasks.

## Acceptance evidence

- README existence: 21/21 after the six committed changes.
- Canonical inventory: 21 distinct repository names, matched to linked-account visibility and branch metadata.
- Markdown root README relative-path references: no missing targets detected in the checked repository trees; external URLs untested.
- GitHub Actions evidence for previous catalog consistency issue: successful [Repository quality run](https://github.com/dejvid673-prog/7dejv-agent-os/actions/runs/37715221686) on original audit branch; stacked branch CI to be checked independently.
