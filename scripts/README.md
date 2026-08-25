# Scripts

Executable, deterministic helpers used to validate and maintain the canonical 7DEJV Agent OS repository.

## `validate_repository.py`

Current static quality gate. It:

- validates required canonical paths;
- validates `registry/repositories.json` structure and uniqueness;
- checks that the Markdown repository index contains every registered repository;
- validates canonical `skills/*/SKILL.md` frontmatter and duplicate skill names;
- scans canonical text surfaces for a small set of high-confidence secret patterns;
- deliberately excludes `sources/**` from active-instruction/secret enforcement because it is an immutable migration archive;
- exits non-zero when blocking errors are found.

Run from the repository root:

```bash
python scripts/validate_repository.py
```

The GitHub Actions workflow `.github/workflows/repository-quality.yml` compiles and executes the validator on pull requests and pushes to `main`.

## Rules

- Keep scripts deterministic and dependency-light where practical.
- Never print complete secret values.
- Do not silently mutate audited files.
- Add tests/fixtures before materially broadening detection rules.
