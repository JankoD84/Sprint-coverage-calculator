# Repository Boundaries

## Architecture boundaries

Owned here is the implementation and documentation present in this repository, especially: `.ai/`, `docs/`, `.github/`.

Do not move responsibilities into or out of this repository without an explicit architecture task and evidence from current code/docs.

## Ownership boundaries

- Changes must stay within this repository's documented purpose and current implementation boundaries.
- Do not duplicate business logic into prompts, adapters or generated governance files.
- Do not silently change external API, schema, billing, auth, deployment or persistence behavior.

## High-risk integration boundaries

Ask before changing:

- `README.md`
- `calculator.py`
- `requirements.txt`
- `.gitignore`
- `.github/workflows/`
- public calculation formulas, thresholds, or assumptions

Do not modify `README.md` as part of standards-only rollout work. Never edit `.git/`, virtual environments, caches, generated files, or secrets.
