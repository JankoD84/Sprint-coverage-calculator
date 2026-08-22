# Quality Gates

Use targeted validation appropriate to the change.

## Repository validation

Use commands that exist here:

```bash
python sprint_cli.py
streamlit run sprint_app.py
git diff --check
```

For governance-only changes, `git diff --check` is sufficient.

## Governance-only validation

```bash
git diff --check
git status --short
```

Before completion, inspect the diff and confirm:

- `AGENTS.md` remains the universal AI entrypoint.
- `.ai/` remains IDE-neutral.
- IDE-specific files are adapters only and do not redefine repository standards.
- No secrets, provider credentials, production configuration, migrations or deployment behavior were changed.
- Repository-specific safety and architecture rules are preserved.
