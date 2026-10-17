# GitHub CI and repository remediation — 2026-10-17

Status: **partial remediation complete; follow-up items HOLD**  
Owner: `dejvid673-prog`  
Method: connected GitHub repository/PR/workflow reads, GitHub job logs, scoped patches, PR validation and merge evidence. No production marketplace requests or customer-data changes were made.

## Verified changes

| Repository | Scope | Pull requests / merged refs | Test evidence |
| --- | --- | --- | --- |
| `allegro` | Scheduled OpenAPI **drift (exit 2)** becomes warning + job summary; network/script errors and manual dispatch remain failing; daily check preserved | [PR #1](https://github.com/dejvid673-prog/allegro/pull/1), main `840e856d67d45f2b317138d184679343d42e34fc` | [PR CI PASS](https://github.com/dejvid673-prog/allegro/actions/runs/39008532844), [main CI PASS](https://github.com/dejvid673-prog/allegro/actions/runs/39008583514) |
| `7dejv-ai-command-center` | Replaced stale Python package/empty pytest matrix with accurate documentation and conditional Python checks; `NOT RUN` when no tests | [PR #7](https://github.com/dejvid673-prog/7dejv-ai-command-center/pull/7), main `fd137a61c8d5c21cdcd342ee9fc9d7e99dafed45` | [PR PASS](https://github.com/dejvid673-prog/7dejv-ai-command-center/actions/runs/39008673835), [main PASS](https://github.com/dejvid673-prog/7dejv-ai-command-center/actions/runs/39008722282) |
| `7dejv-ai-command-center` | Canonical routing corrected; `7dejv-agent-os` is shared control-plane, `7dejv-skills-prompts` is migration/reference; `7dejv-mcp` architecture vs executable `mcp` differentiated; old gotcha retained | [PR #6](https://github.com/dejvid673-prog/7dejv-ai-command-center/pull/6), main `4dca222c71df234b584aa8f5e25b5a755f906c1f` | [PR CI PASS](https://github.com/dejvid673-prog/7dejv-ai-command-center/actions/runs/39009331497) |
| `mcp` | CI validates locally pinned ERLI checksum rather than failing on upstream drift, so typecheck, unit and Docker tests run; cold Docker build timeout fixed | [PR #1](https://github.com/dejvid673-prog/mcp/pull/1), `feature/erli-write-mvp` `d35b4851a3f7461cea2e612cfa5daf166504d872` | [PR CI PASS](https://github.com/dejvid673-prog/mcp/actions/runs/39008879738), [feature push PASS](https://github.com/dejvid673-prog/mcp/actions/runs/39008957746); **59 unit tests PASS**, Docker PASS |
| `mcp` | Replaced CI auto-commit of unreviewed external ERLI OpenAPI data with read-only snapshot artifact for review | [PR #2](https://github.com/dejvid673-prog/mcp/pull/2), feature `a0fe0bc2a773ec071738fe07d4ae04aee5c2c763` | [PR CI PASS](https://github.com/dejvid673-prog/mcp/actions/runs/39009004185), [snapshot generation PASS](https://github.com/dejvid673-prog/mcp/actions/runs/39009191419) |
| `7dejv-agent-os` | Updated canonical-vs-runtime governance (PR #6), then reconciled registry from 16 to **21** repositories with prior inventory audit (PR #9), retaining correct branch lineage | [PR #6](https://github.com/dejvid673-prog/7dejv-agent-os/pull/6), [PR #9](https://github.com/dejvid673-prog/7dejv-agent-os/pull/9), main `224c122bdaf229f1686de1966d43ece16d4fc4b9` | [fresh PR #9 PASS](https://github.com/dejvid673-prog/7dejv-agent-os/actions/runs/39009142704), [main PASS](https://github.com/dejvid673-prog/7dejv-agent-os/actions/runs/39009178282) |

### Root cause of repetitive notification emails

The scheduled `allegro/.github/workflows/validate-docs.yml` ran daily and `scripts/check_openapi_freshness.py` returned exit code 2 for a persisted upstream SHA-256 mismatch. The old spec snapshot dates from 2026-08-20. GitHub Actions repeated failed-job emails for the unchanged mismatch. The new workflow makes this **specific** drift state advisory during schedule, not for manual dispatch or other errors. **An upcoming scheduled run is not yet verified**; PR and push jobs do not exercise the schedule-only branch.

## Open risks / next work

1. **Allegro API contract (HOLD):** The source changed. Fetch the current official OpenAPI, regenerate the catalog, inspect differences in operations, media types, scopes, deprecated endpoints, and update snapshots only after compatibility review. A quiet scheduled CI is **not** evidence of a current contract.
2. **MCP dependency review (HOLD):** Docker build output from [CI run](https://github.com/dejvid673-prog/mcp/actions/runs/39008798525) reported npm dependency advisories: 1 moderate and 1 high. Severity alone does not identify the affected package or exploitability. Obtain `npm audit --json`, verify package/advisory paths and plan narrow upgrades before any production use. Do not automatically run `npm audit fix --force`.
3. **Production readiness (BLOCKED):** The `mcp` ERLI implementation is still in feature branch, and passing unit/Docker tests do not authorize real marketplace writes or public deployment. Keep the defined product/connection/approval gates.
4. **GitHub administration (HOLD):** The connected GitHub app received 403 for branch-protection reads. Branch protection, secret-scanning settings, installed app privileges and full Git-history secret audit were **not verified**. Limited code search of three secret signatures produced no matches but is not a security certificate.
5. **Documentation/runtime backlogs:** Independent draft [7dejv-agent-os PR #7](https://github.com/dejvid673-prog/7dejv-agent-os/pull/7), other dashboard/implementation PRs and actual workstation/production tests remain separate work. Do not merge unrelated functional PRs merely to clear the queue.
6. **CI honesty:** Command Center `Repository hygiene` PASS validates instructions/files and optional Python syntax/tests, **not** application readiness where there are no tests. Add project-specific tests when runnable code lands.

## Scope boundary

No repository was deleted, archived or made public/private. No GitHub notifications were globally disabled. No marketplace offer, customer order, production data, API credential or deployment was changed. No branch-protection or secret-management changes were attempted without administration access.  
Evidence is limited to the specific repository files and CI runs listed above.
