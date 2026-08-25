#!/usr/bin/env python3
"""Deterministic static validation for the canonical 7DEJV agent OS repository.

The validator intentionally ignores sources/** as an active instruction surface.
It uses only the Python standard library so it can run on a clean GitHub Actions runner.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SECRET_PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    "openai-key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".txt", ".toml"}
SKIP_DIRS = {".git", "sources", "__pycache__"}


def error(message: str) -> None:
    ERRORS.append(message)


def warning(message: str) -> None:
    WARNINGS.append(message)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        error(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return {}


def validate_repository_registry() -> None:
    path = ROOT / "registry" / "repositories.json"
    data = load_json(path)
    if not isinstance(data, dict):
        error("repository registry root must be an object")
        return

    required_root = {"schema_version", "snapshot_date", "owner", "repositories"}
    missing_root = required_root - data.keys()
    if missing_root:
        error(f"repository registry missing fields: {sorted(missing_root)}")

    repositories = data.get("repositories", [])
    if not isinstance(repositories, list) or not repositories:
        error("repository registry must contain a non-empty repositories array")
        return

    valid_visibility = {"public", "private", "internal"}
    valid_status = {"active", "review", "empty", "archived"}
    valid_classification = {
        "canonical-control-plane",
        "primary-migration-source",
        "product-or-domain-repository",
        "reference-low-signal",
        "empty",
    }

    seen: set[str] = set()
    for index, repo in enumerate(repositories):
        if not isinstance(repo, dict):
            error(f"repository registry item {index} must be an object")
            continue
        required = {"name", "visibility", "status", "classification", "default_branch"}
        missing = required - repo.keys()
        if missing:
            error(f"repository item {index} missing fields: {sorted(missing)}")
            continue
        name = repo["name"]
        if not isinstance(name, str) or not name:
            error(f"repository item {index} has invalid name")
            continue
        if name in seen:
            error(f"duplicate repository name in registry: {name}")
        seen.add(name)
        if repo["visibility"] not in valid_visibility:
            error(f"{name}: invalid visibility {repo['visibility']!r}")
        if repo["status"] not in valid_status:
            error(f"{name}: invalid status {repo['status']!r}")
        if repo["classification"] not in valid_classification:
            error(f"{name}: invalid classification {repo['classification']!r}")
        if repo["classification"] == "empty" and repo["status"] != "empty":
            error(f"{name}: empty classification requires empty status")

    canonical = [r for r in repositories if isinstance(r, dict) and r.get("classification") == "canonical-control-plane"]
    if len(canonical) != 1 or canonical[0].get("name") != "7dejv-agent-os":
        error("exactly one canonical-control-plane repository is required: 7dejv-agent-os")

    index_path = ROOT / "inventory" / "repositories-index.md"
    try:
        index_text = index_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        error("missing inventory/repositories-index.md")
        return
    for name in sorted(seen):
        if f"`{name}`" not in index_text:
            error(f"repository registry/index mismatch: {name} missing from Markdown index")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        error(f"{path.relative_to(ROOT)}: missing YAML frontmatter start")
        return {}
    try:
        end = text.index("\n---\n", 4)
    except ValueError:
        error(f"{path.relative_to(ROOT)}: missing YAML frontmatter end")
        return {}
    values: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def validate_skills() -> None:
    skills_root = ROOT / "skills"
    if not skills_root.is_dir():
        error("missing skills directory")
        return

    seen_names: dict[str, Path] = {}
    skill_files = sorted(skills_root.glob("*/SKILL.md"))
    if not skill_files:
        error("no canonical skills found")
        return

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text, path)
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if not name:
            error(f"{path.relative_to(ROOT)}: missing frontmatter name")
        elif not NAME_RE.fullmatch(name):
            error(f"{path.relative_to(ROOT)}: invalid skill name {name!r}")
        elif name in seen_names:
            error(
                f"duplicate canonical skill name {name!r}: "
                f"{seen_names[name].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )
        else:
            seen_names[name] = path
        if not description:
            error(f"{path.relative_to(ROOT)}: missing frontmatter description")
        if name and path.parent.name != name:
            warning(f"{path.relative_to(ROOT)}: folder name differs from skill name {name!r}")


def validate_required_paths() -> None:
    required = [
        "AGENTS.md",
        "README.md",
        "SOURCE_OF_TRUTH.md",
        "agents",
        "skills",
        "workflows",
        "prompts",
        "registry",
        "schemas",
        "scripts",
        "inventory",
        "docs",
        "sources",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            error(f"missing required canonical path: {rel}")


def scan_high_confidence_secrets() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for rule, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                error(f"potential high-confidence secret ({rule}) in {path.relative_to(ROOT)}")


def main() -> int:
    validate_required_paths()
    validate_repository_registry()
    validate_skills()
    scan_high_confidence_secrets()

    for item in WARNINGS:
        print(f"WARNING: {item}")
    for item in ERRORS:
        print(f"ERROR: {item}")

    print(
        json.dumps(
            {
                "status": "PASS" if not ERRORS else "BLOCKED",
                "errors": len(ERRORS),
                "warnings": len(WARNINGS),
            },
            sort_keys=True,
        )
    )
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
