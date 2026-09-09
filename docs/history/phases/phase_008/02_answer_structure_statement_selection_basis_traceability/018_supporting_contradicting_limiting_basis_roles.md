# EXPL-018 — Supporting, Contradicting & Limiting Basis Roles

**Status:** Accepted — Phase 008 Group 02

## Requirement

For each material answer statement, retain statement-relative basis roles as applicable:

- **supporting basis** — source proposition/evidence that supports the statement;
- **contradicting basis** — source proposition/evidence that materially conflicts with or weakens the statement;
- **limiting basis/context** — missing, restricted, stale, incomplete, conflicting or otherwise bounded evidence/context that limits the proposition that may safely be stated.

These roles do not mutate the underlying source evidence or create a universal evidence status.

## Invariants

- evidence role is relative to a particular statement;
- one item may support one proposition while limiting another;
- contradiction cannot be hidden merely to simplify the narrative;
- missing evidence is not contradicting evidence by default;
- source-owned epistemic states remain unchanged by their Explanation basis role.
