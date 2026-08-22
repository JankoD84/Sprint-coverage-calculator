# Sprint-coverage-calculator AI Context

`.ai/` is the repository-local AI navigation and governance layer.

It must not become a second copy of product documentation or an IDE-specific configuration directory.

Structure:

- `repo/` — repository identity, boundaries, commands and architecture pointers
- `governance/` — source-of-truth, safety, quality and documentation rules
- `process/` — reusable engineering workflows
- `templates/` — compact output and handoff templates

Authority model:

- `AGENTS.md` = universal AI entrypoint for Devin, Windsurf/Cascade, Cursor, VS Code + Roo Code, and Zed.
- `.ai/` = IDE-neutral repository context and governance.
- `.agents/skills/` = task-specific operational knowledge, when this repository has repeatable workflows worth encoding.
- IDE-specific directories such as `.zed/`, `.cursor/`, `.roo/`, `.windsurf/`, and `.vscode/` are execution adapters only.

Application/product truth remains in code, tests, schemas, current runtime state, and canonical repository documentation.

## Existing repository context

# Standards V2 Lite Authority

Authority hierarchy for this repository:

1. `AGENTS.md` — repository entry gate.
2. `.ai/` — canonical deeper repository context.
3. `docs/ai/` — compatibility/reference layer only.
4. Active global/IDE configuration — developer-agent provider selection.

Repository governance must not hard-code developer-agent provider choices.
