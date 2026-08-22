# Documentation Policy

- Do not create duplicate sources of truth.
- Use `.ai/repo/architecture.md` as an AI navigation layer that points to canonical docs and current implementation.
- Keep `.ai/` compact; it should guide agents, not mirror full product documentation.
- When implementation changes architecture, API contracts, schemas, operational behavior, security, billing, release semantics or user-visible behavior, update the relevant canonical documentation in the same change.
- Historical reports, generated summaries, RAG output and chat context are reference material only until verified against current repository files.
