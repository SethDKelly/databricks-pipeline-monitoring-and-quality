# DMTZ Documentation History

**Authority:** HISTORY / PROVENANCE ONLY — NOT CURRENT SEMANTIC AUTHORITY

This namespace preserves the design chronology, superseded planning, rationale, historical definitions, reviews, handoffs and other provenance relocated by Documentation Physical Topology Normalization (DPTN).

## Current-truth rule

`docs/history/` never establishes current DMTZ meaning merely because a historical file exists, is newer in Git, appears first in search, contains a stable ID, or resembles a current contract.

For current semantics:

1. use the current ownership model selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`;
2. during DPTN-B, substantive current owners remain under `docs/canonical/`;
3. for a known stable ID, use `python3 scripts/agentic/resolve_stable_id.py <ID>` without `--history`;
4. use `--history` only when provenance, rationale, chronology or prior wording is actually required.

History occurrences never compete with current ownership or strengthen epistemic, authority, authorization, causal, health, implementation or deployment status.

## Preservation rule

Historical documents are preserved as accepted-at-the-time records. DPTN-B relocates their existing Git trees without semantically rewriting them to match the final design. Old internal wording, relative links and status-at-time statements may therefore describe historical topology or progression and must be interpreted in that historical context.

Current routing/orientation is maintained outside the historical corpus. A historical file must not be edited merely to make it read like current documentation.

## DPTN-B relocation map

| Previous physical root | Historical physical root | Role |
|---|---|---|
| `docs/concepts/` | `docs/history/phases/` | Phase 002–010 design corpus and pre-canonical concept scaffolding |
| `docs/reference/` | `docs/history/reference-legacy/` | Legacy glossary and authority-vocabulary provenance |
| `docs/foundation/` | `docs/history/foundation/` | Foundation provenance, roadmap, questions and handoffs |
| `docs/planning/` | `docs/history/planning/` | Historical planning records |
| `docs/decisions/` | `docs/history/decisions/` | Phase-scoped design decisions and review rationale |
| `docs/design_history/` | `docs/history/design-history/` | Prior logical design-history index/provenance guidance |

These moves clear first-class path collisions for later DPTN phases. **A cleared path is vacant/unassigned; vacancy does not make it current authority.** `docs/concepts/`, `docs/reference/` and `docs/decisions/` may be reused only by the specifically authorized later DPTN phase.

## History boundaries

- No file under this namespace is a current semantic owner solely because it is here.
- Stable IDs found here are provenance occurrences, not current definitions.
- The CKR inventory and canonical target documents continue to own current meaning during DPTN-B.
- `docs/agentic_development_foundation/` and `docs/canonical_knowledge_retrofit/` remain mixed-lifecycle current directories until DPTN-D; they are not part of DPTN-B's bulk relocation.
- Implementation 001-A remains blocked until DPTN-G exit acceptance.
