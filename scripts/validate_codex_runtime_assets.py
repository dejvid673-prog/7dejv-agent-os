#!/usr/bin/env python3
"""Validate canonical 7DEJV Codex runtime-kit assets."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import tomllib

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "runtime" / "codex"
ERRORS: list[str] = []

BASELINE_SKILLS = {
    "repository-inventory-skill",
    "7dejv-repository-quality-audit-skill",
    "7dejv-secret-scanner",
    "7dejv-external-dependency-auditor",
    "7dejv-prompt-injection-defense",
    "7dejv-eval-generator",
    "7dejv-eval-grader",
    "7dejv-readiness-status-calculator",
    "7dejv-skill-linter",
    "7dejv-skill-factory",
}

EXPECTED_AGENTS = {
    "docs-researcher.toml": "read-only",
    "reviewer.toml": "read-only",
    "test-runner.toml": "workspace-write",
}


def fail(message: str) -> None:
    ERRORS.append(message)


def read_toml(path: Path) -> dict:
    try:
        with path.open("rb") as handle:
            value = tomllib.load(handle)
    except (FileNotFoundError, OSError, tomllib.TOMLDecodeError) as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a TOML table")
        return {}
    return value


def validate_required_paths() -> None:
    required = [
        RUNTIME / "README.md",
        RUNTIME / "global" / "AGENTS.md",
        RUNTIME / "config" / "7dejv.config.toml",
        ROOT / "scripts" / "install_codex_runtime.ps1",
        ROOT / "scripts" / "audit_codex_runtime.py",
    ]
    required.extend(RUNTIME / "agents" / name for name in EXPECTED_AGENTS)
    for path in required:
        if not path.is_file():
            fail(f"missing Codex runtime asset: {path.relative_to(ROOT)}")


def validate_profile() -> None:
    path = RUNTIME / "config" / "7dejv.config.toml"
    cfg = read_toml(path)
    if not cfg:
        return

    if "model" in cfg:
        fail("runtime profile must not hard-code a model slug; use current Codex default or explicit user selection")
    if cfg.get("approval_policy") != "on-request":
        fail("runtime profile must use approval_policy = on-request")
    if cfg.get("sandbox_mode") != "workspace-write":
        fail("runtime profile must use sandbox_mode = workspace-write")
    if cfg.get("web_search") not in {"live", "indexed"}:
        fail("runtime profile must keep current-source web search available")

    agents = cfg.get("agents")
    if not isinstance(agents, dict) or agents.get("enabled") is not True:
        fail("runtime profile must explicitly enable subagents")
    else:
        concurrency = agents.get("max_concurrent_threads_per_session")
        if not isinstance(concurrency, int) or not 1 <= concurrency <= 8:
            fail("subagent concurrency must be bounded to an integer from 1 to 8")

    mcp_servers = cfg.get("mcp_servers")
    docs = mcp_servers.get("openaiDeveloperDocs") if isinstance(mcp_servers, dict) else None
    if not isinstance(docs, dict):
        fail("runtime profile must configure openaiDeveloperDocs MCP")
    else:
        if docs.get("url") != "https://developers.openai.com/mcp":
            fail("openaiDeveloperDocs MCP must use the official developers.openai.com endpoint")
        if docs.get("required") is not False:
            fail("openaiDeveloperDocs MCP must remain non-required so documentation outages do not block all Codex startup")


def validate_agents() -> None:
    for filename, expected_sandbox in EXPECTED_AGENTS.items():
        path = RUNTIME / "agents" / filename
        cfg = read_toml(path)
        if not cfg:
            continue
        for key in ("name", "description", "developer_instructions"):
            if not isinstance(cfg.get(key), str) or not cfg[key].strip():
                fail(f"{path.relative_to(ROOT)} missing non-empty {key}")
        if cfg.get("sandbox_mode") != expected_sandbox:
            fail(f"{path.relative_to(ROOT)} must use sandbox_mode = {expected_sandbox}")
        if "model" in cfg:
            fail(f"{path.relative_to(ROOT)} must not hard-code a model slug")


def validate_global_guidance() -> None:
    path = RUNTIME / "global" / "AGENTS.md"
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return
    for marker in ("## Source of truth", "## Required work pattern", "## Security", "## Evidence and status"):
        if marker not in text:
            fail(f"global AGENTS template missing required section: {marker}")
    if "7dejv-agent-os" not in text:
        fail("global AGENTS template must route shared 7DEJV artifacts to 7dejv-agent-os")


def validate_installer_contract() -> None:
    path = ROOT / "scripts" / "install_codex_runtime.ps1"
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return
    required_fragments = (
        "[switch]$Apply",
        "[switch]$Force",
        "[switch]$AllCanonicalSkills",
        '"7dejv.config.toml"',
        '"AGENTS.md"',
        '"backups/7dejv-$Timestamp"',
    )
    for fragment in required_fragments:
        if fragment not in text:
            fail(f"installer missing safety/runtime contract fragment: {fragment}")
    if 'Join-Path $CodexHome "config.toml"' in text:
        fail("installer must not overwrite the user's primary config.toml")
    if "Remove-Item" in text and "-Force" not in text:
        fail("installer contains removal logic without explicit force-gating evidence")


def validate_baseline_skills() -> None:
    path = ROOT / "registry" / "skills.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        fail(f"cannot read skill registry: {exc}")
        return
    canonical = {
        item.get("name")
        for item in data.get("skills", [])
        if isinstance(item, dict) and item.get("status") == "canonical"
    }
    missing = sorted(BASELINE_SKILLS - canonical)
    if missing:
        fail(f"Codex baseline references non-canonical skills: {missing}")


def main() -> int:
    validate_required_paths()
    validate_profile()
    validate_agents()
    validate_global_guidance()
    validate_installer_contract()
    validate_baseline_skills()

    for item in ERRORS:
        print(f"ERROR: {item}")
    print(json.dumps({"status": "PASS" if not ERRORS else "BLOCKED", "errors": len(ERRORS)}, sort_keys=True))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
