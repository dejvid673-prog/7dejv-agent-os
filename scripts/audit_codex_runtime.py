#!/usr/bin/env python3
"""Audit an installed 7DEJV Codex runtime without printing secrets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError as exc:  # pragma: no cover - Python <3.11
    raise SystemExit("Python 3.11+ is required for tomllib") from exc

BASELINE_SKILLS = (
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
)

EXPECTED_AGENTS = {
    "docs-researcher.toml": "read-only",
    "reviewer.toml": "read-only",
    "test-runner.toml": "workspace-write",
}

DOCS_MCP_URL = "https://developers.openai.com/mcp"


def parse_args() -> argparse.Namespace:
    home = Path.home()
    default_codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=default_codex_home)
    parser.add_argument("--skills-home", type=Path, default=home / ".agents" / "skills")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Canonical 7dejv-agent-os checkout used for drift comparison.",
    )
    parser.add_argument("--skip-command-check", action="store_true")
    return parser.parse_args()


def tree_fingerprint(path: Path) -> str | None:
    if not path.is_dir():
        return None
    digest = hashlib.sha256()
    files = sorted(p for p in path.rglob("*") if p.is_file())
    for file_path in files:
        rel = file_path.relative_to(path).as_posix().encode("utf-8")
        digest.update(rel)
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def load_toml(path: Path) -> dict:
    with path.open("rb") as handle:
        value = tomllib.load(handle)
    if not isinstance(value, dict):
        raise ValueError("TOML root must be a table")
    return value


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    codex_home = args.codex_home.expanduser()
    skills_home = args.skills_home.expanduser()

    results: list[dict[str, str]] = []
    blocked = False
    hold = False

    def add(state: str, check: str, detail: str) -> None:
        nonlocal blocked, hold
        results.append({"state": state, "check": check, "detail": detail})
        blocked = blocked or state == "BLOCKED"
        hold = hold or state == "HOLD"

    if not args.skip_command_check:
        codex = shutil.which("codex")
        if not codex:
            add("HOLD", "codex-command", "Codex executable is not available on PATH.")
        else:
            try:
                completed = subprocess.run(
                    [codex, "--version"],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                version = (completed.stdout or completed.stderr).strip().splitlines()
                if completed.returncode == 0:
                    add("PASS", "codex-command", version[0] if version else "codex --version succeeded")
                else:
                    add("HOLD", "codex-command", f"codex --version exited {completed.returncode}")
            except (OSError, subprocess.SubprocessError) as exc:
                add("HOLD", "codex-command", f"Could not execute codex --version: {type(exc).__name__}")

    global_agents = codex_home / "AGENTS.md"
    if not global_agents.is_file():
        add("HOLD", "global-agents", f"Missing {global_agents}")
    else:
        text = global_agents.read_text(encoding="utf-8", errors="replace")
        required_phrases = ("Source of truth", "Security", "Evidence")
        missing = [phrase for phrase in required_phrases if phrase not in text]
        if missing:
            add("HOLD", "global-agents", f"File exists but expected 7DEJV markers are missing: {missing}")
        else:
            add("PASS", "global-agents", "Global 7DEJV guidance is present.")

    profile = codex_home / "7dejv.config.toml"
    if not profile.is_file():
        add("HOLD", "7dejv-profile", f"Missing {profile}")
    else:
        try:
            cfg = load_toml(profile)
            if cfg.get("approval_policy") != "on-request":
                add("HOLD", "7dejv-profile-approval", "Expected approval_policy = on-request.")
            else:
                add("PASS", "7dejv-profile-approval", "Approval policy is on-request.")

            if cfg.get("sandbox_mode") != "workspace-write":
                add("HOLD", "7dejv-profile-sandbox", "Expected sandbox_mode = workspace-write.")
            else:
                add("PASS", "7dejv-profile-sandbox", "Sandbox mode is workspace-write.")

            if cfg.get("web_search") not in {"live", "indexed"}:
                add("HOLD", "7dejv-profile-web", "Expected live or indexed web search for current-source verification.")
            else:
                add("PASS", "7dejv-profile-web", f"Web search mode is {cfg.get('web_search')}.")

            agents = cfg.get("agents", {})
            if not isinstance(agents, dict) or agents.get("enabled") is not True:
                add("HOLD", "7dejv-profile-subagents", "Multi-agent tools are not explicitly enabled.")
            else:
                add("PASS", "7dejv-profile-subagents", "Multi-agent tools are enabled.")

            mcp = cfg.get("mcp_servers", {})
            docs = mcp.get("openaiDeveloperDocs", {}) if isinstance(mcp, dict) else {}
            if not isinstance(docs, dict) or docs.get("url") != DOCS_MCP_URL:
                add("HOLD", "developer-docs-mcp", "OpenAI Developer Docs MCP is missing or points elsewhere.")
            else:
                add("PASS", "developer-docs-mcp", "OpenAI Developer Docs MCP is configured.")
        except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
            add("BLOCKED", "7dejv-profile", f"Profile cannot be parsed: {type(exc).__name__}: {exc}")

    agents_home = codex_home / "agents"
    for filename, expected_sandbox in EXPECTED_AGENTS.items():
        path = agents_home / filename
        if not path.is_file():
            add("HOLD", f"agent:{filename}", f"Missing {path}")
            continue
        try:
            cfg = load_toml(path)
        except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
            add("BLOCKED", f"agent:{filename}", f"Invalid TOML: {type(exc).__name__}: {exc}")
            continue
        missing = [key for key in ("name", "description", "developer_instructions") if not cfg.get(key)]
        if missing:
            add("BLOCKED", f"agent:{filename}", f"Missing required fields: {missing}")
        elif cfg.get("sandbox_mode") != expected_sandbox:
            add("HOLD", f"agent:{filename}", f"Expected sandbox_mode={expected_sandbox!r}.")
        else:
            add("PASS", f"agent:{filename}", "Agent runtime adapter is present and structurally valid.")

    registry_path = repo_root / "registry" / "skills.json"
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        canonical = {
            item.get("name")
            for item in registry.get("skills", [])
            if isinstance(item, dict) and item.get("status") == "canonical"
        }
    except (OSError, json.JSONDecodeError) as exc:
        add("BLOCKED", "skill-registry", f"Cannot read canonical skill registry: {type(exc).__name__}: {exc}")
        canonical = set()

    for skill_name in BASELINE_SKILLS:
        if skill_name not in canonical:
            add("BLOCKED", f"skill:{skill_name}", "Baseline skill is not canonical in registry/skills.json.")
            continue
        source = repo_root / "skills" / skill_name
        installed = skills_home / skill_name
        if not (installed / "SKILL.md").is_file():
            add("HOLD", f"skill:{skill_name}", f"Not installed at {installed}")
            continue
        source_fp = tree_fingerprint(source)
        installed_fp = tree_fingerprint(installed)
        if source_fp and installed_fp and source_fp == installed_fp:
            add("PASS", f"skill:{skill_name}", "Installed copy matches canonical checkout.")
        else:
            add("HOLD", f"skill:{skill_name}", "Installed copy differs from the canonical checkout; review/sync required.")

    status = "BLOCKED" if blocked else "HOLD" if hold else "PASS"
    payload = {
        "status": status,
        "codex_home": str(codex_home),
        "skills_home": str(skills_home),
        "repo_root": str(repo_root),
        "checks": results,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 2 if blocked else 1 if hold else 0


if __name__ == "__main__":
    sys.exit(main())
