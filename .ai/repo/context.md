# Repository Context

## Purpose

`Sprint-coverage-calculator` calculates sprint coverage using shared calculation logic and exposes it through both CLI and Streamlit UI entry points.

## Stack

- Python
- Streamlit

## Key files

- `calculator.py` — shared calculation module.
- `sprint_cli.py` — CLI entry point.
- `sprint_app.py` — Streamlit UI entry point.
- `README.md` — tracked project documentation; preserve during standards-only work.
- `requirements.txt` — Streamlit dependency.
- `.gitignore` — repository ignore rules.
- `.github/workflows/` — CI and mirror workflows.

## Architecture

Both runtime entry points depend on `calculator.py`. Keep calculation rules centralized there and avoid duplicating logic in CLI or UI files.

## Ownership and non-ownership

Owns sprint coverage calculation only. Does not own team delivery truth, external agile tooling data, Dulvarn platform governance, production services, auth, or billing.

## External dependencies

- Python runtime
- Streamlit runtime for the web UI
