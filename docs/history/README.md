# DMTZ Documentation History

**Authority:** HISTORY / PROVENANCE ONLY — NOT CURRENT SEMANTIC AUTHORITY

This namespace preserves design chronology, superseded planning, rationale, historical definitions, completed program reviews/evidence, prior routing surfaces, handoffs and other provenance relocated by Documentation Physical Topology Normalization (DPTN).

## Current-truth rule

`docs/history/` never establishes current DMTZ meaning or current operational policy merely because a historical file exists, is newer in Git, appears first in search, contains a stable ID, or resembles a current contract.

For current semantics use `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`; for a known stable ID use `python3 scripts/agentic/resolve_stable_id.py <ID>` without `--history`. Use `--history` only for provenance, rationale, chronology or prior wording.

History occurrences never compete with current ownership or strengthen epistemic, authority, authorization, causal, health, implementation or deployment status.

## Preservation rule

Historical documents are preserved as accepted-at-the-time records. DPTN relocation does not rewrite them to read like current documentation. A cleared or relocated source path is **vacant/unassigned** until a specifically authorized later phase assigns a role; vacancy never creates current authority.

## Relocation map

| Previous physical root / class | Historical physical root | Role |
|---|---|---|
| former `docs/concepts/` design corpus | `docs/history/phases/` | Phase 002–010 design chronology |
| former `docs/reference/` legacy corpus | `docs/history/reference-legacy/` | Legacy glossary/authority provenance |
| former `docs/foundation/` | `docs/history/foundation/` | Foundation provenance |
| former `docs/planning/` | `docs/history/planning/` | Historical planning |
| former `docs/decisions/` | `docs/history/decisions/` | Historical phase decisions |
| former `docs/design_history/` | `docs/history/design-history/` | Prior design-history routing/provenance |
| completed CKR evidence | `docs/history/retrofits/ckr/` | CKR reviews, matrices, manifests and fixtures |
| completed ADF program evidence | `docs/history/foundations/adf/` | ADF phase-design, reviews and fixtures |
| pre-DPTN-E authored `knowledge/` tree | `docs/history/routing/okf-pre-dptn-e/` | Exact authored OKF/routing state before discovery-root convergence |

DPTN-B performed the first six relocations. DPTN-D performed CKR/ADF lifecycle decomposition. DPTN-E preserved the full authored OKF tree before replacing live `knowledge/` with a generated compatibility projection.

## DPTN-E routing provenance

The tree at `routing/okf-pre-dptn-e/` preserves the complete hand-maintained OKF routing plane accepted before DPTN-E. It is retained so historical CKR-J/ADF reasoning and completed-era validators remain reproducible. It is **not** a fallback current routing source.

Current authored discovery is [`../index.md`](../index.md). Live top-level `knowledge/` is generated from `docs/routing/okf_projection.json` plus repository-owned workflow and implementation catalogs.

## History boundaries

- No file under this namespace is a current semantic owner solely because it is here.
- Stable IDs found here are provenance occurrences, not current definitions.
- CKR execution evidence proves the completed retrofit; it does not become the ownership ledger.
- ADF execution evidence proves the completed foundation; it does not replace current ADF policy/configuration.
- Archived OKF routing proves prior routing state; it does not compete with `docs/index.md` or current generated projection.
- Implementation 001-A remains blocked until DPTN-G exit acceptance.
