# Repository Commands

Only run commands supported by repository files. Do not invent validation commands.

## Detected commands

- **install/setup**: `python -m pip install -r requirements.txt`

## Always-safe governance validation

- `git diff --check`
- `git status --short`

Do not run deployment, migration, production startup or destructive cleanup commands merely as validation.
