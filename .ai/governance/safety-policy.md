# Safety Policy

## Mandatory start for implementation work

Check and report:

```bash
git status
git branch --show-current
git diff --stat
```

Then read:

- `AGENTS.md`
- `.ai/repo/profile.md`
- `.ai/repo/boundaries.md`
- `.ai/repo/commands.md`

## Protected areas

Ask before changing:

- `README.md`
- `calculator.py`
- `requirements.txt`
- `.gitignore`
- `.github/workflows/`
- public calculation formulas, thresholds, or assumptions

Do not modify `README.md` as part of standards-only rollout work. Never edit `.git/`, virtual environments, caches, generated files, or secrets.

## Prohibited during normal AI implementation

- Do not expose or print secret values.
- Do not edit `.env*`, credentials or private keys.
- Do not run deployments, migrations or destructive cleanup commands without explicit approval.
- Do not modify provider credentials, model routing, LiteLLM, MCP runtime configuration, OAuth, AWS, Azure or ChatGPT subscription settings as part of AI-standards work.
- Do not commit, push, force-push, reset or stash automatically.
- Preserve unrelated working-tree changes.
