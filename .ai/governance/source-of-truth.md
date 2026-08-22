# Source-of-Truth Policy

Default precedence for this repository:

1. Current repository source code
2. Current tests, schemas and contracts
3. Current runtime / Git state
4. Repository `AGENTS.md`
5. Canonical repository documentation
6. `.ai/repo/` navigation/context
7. Task-specific `.agents/skills/`, when present
8. Historical reports, summaries, RAG output and chat context

Rules:

- Current implementation beats stale historical documentation.
- Never infer current behavior solely from old reports.
- When documentation and implementation disagree, verify the implementation.
- Update stale canonical documentation when the current task depends on or changes it.
- Do not duplicate business logic into AI prompts, IDE adapters or skills.
