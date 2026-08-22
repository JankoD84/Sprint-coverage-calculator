# Engineering Governance

- Keep shared sprint coverage calculation logic centralized in `calculator.py`.
- Keep `sprint_cli.py` and `sprint_app.py` as entry points around the shared module; do not fork formulas between them.
- Do not introduce a service backend, database, auth, or deployment surface unless explicitly requested.
- Changes to formulas, thresholds, validation ranges, or labels should be deliberate and documented in the completion report.
- Do not change `README.md`, dependencies, `.gitignore`, or CI workflows during standards-only work.
