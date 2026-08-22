# Implementation Process

1. Run Git preflight:

   ```bash
   git status --short
   git branch --show-current
   git log -1 --oneline
   git diff --stat
   ```

2. Read `AGENTS.md`, `.ai/repo/context.md`, and `.ai/governance/engineering.md`.
3. Inspect `calculator.py`, `sprint_cli.py`, `sprint_app.py`, `README.md`, and `requirements.txt` before changing behavior.
4. Make the smallest scoped change.
5. Preserve shared calculation logic in `calculator.py`.
6. Run relevant validation:

   ```bash
   python sprint_cli.py
   streamlit run sprint_app.py
   git diff --check
   ```

7. Update documentation if commands, calculation assumptions, or user-facing behavior change.
8. Report files changed, validation, risks, and commit message.
