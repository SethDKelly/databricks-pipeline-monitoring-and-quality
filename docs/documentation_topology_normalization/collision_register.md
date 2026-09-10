# DPTN Collision Register

**Status:** ACTIVE — DPTN-A–F resolutions recorded; only DPTN-G exit/retirement work remains

A collision is any target path whose contents or role could make physical normalization ambiguous or unsafe. **Vacancy does not assign current authority.** Redirect presence, generated output, history occurrence, search rank and path recency likewise do not assign current authority.

| ID | Target path / concern | Accepted condition | Required / remaining resolution | Earliest phase |
|---|---|---|---|---|
| COL-001 | `docs/concepts/` | History preserved; accepted current concepts promoted to first-class path | RESOLVED | DPTN-B → C |
| COL-002 | `docs/reference/` | Legacy reference history preserved; accepted current reference promoted | RESOLVED | DPTN-B → C |
| COL-003 | `docs/decisions/` | Phase decisions preserved under history; source remains vacant/unassigned | Any future current ADR namespace requires separate authority decision | DPTN-B |
| COL-004 | `docs/history/` | Explicit HISTORY / PROVENANCE ONLY root exists | Preserve non-current role | DPTN-B |
| COL-005 | `docs/design_history/` | Prior design-history tree preserved under history | RESOLVED for routing; old-path retirement belongs to DPTN-G | DPTN-B → G |
| COL-006 | `docs/canonical_knowledge_retrofit/` | Durable mechanics current; completed CKR evidence historical | RESOLVED | DPTN-D |
| COL-007 | `docs/agentic_development_foundation/` | Durable operating policy/live residuals current; completed ADF evidence historical | RESOLVED | DPTN-D |
| COL-008 | `knowledge/` vs `docs/index.md` | `docs/index.md` authored discovery root; `knowledge/` generated OKF compatibility; prior authored tree preserved in history | RESOLVED | DPTN-E |
| COL-009 | stable-ID resolver paths | Deterministic current locators and agent/reference consumers use first-class owners; history is explicit `--history` only | RESOLVED BY DPTN-F | DPTN-C → F |
| COL-010 | CKR ownership inventory paths | Durable ledger retained; current targets first-class; provenance history paths explicit | RESOLVED | DPTN-C → F |
| COL-011 | agent/OKF links | Agent, adapter, scoped-rule, link-validation and impact-analysis consumers rebound to normalized paths | RESOLVED BY DPTN-F | DPTN-F |
| COL-012 | implementation traceability | Implementation has not started | Keep 001-A blocked until DPTN exit | DPTN-A–G |
| COL-013 | `docs/canonical/README.md` vs `docs/index.md` | Orientation merged into `docs/index.md`; canonical README compatibility-only | RESOLVED; physical compatibility retirement belongs to DPTN-G | DPTN-E → G |

## Resolution record

- **DPTN-B:** COL-001–005 history/collision preparation established `docs/history/` and preserved chronological provenance before path reuse.
- **DPTN-C:** promoted first-class semantic owner roots and atomically rebound current ownership; current-locator side of COL-009 completed.
- **DPTN-D:** resolved COL-006/007 by decomposing durable CKR/ADF policy from completed program evidence without semantic rewrite.
- **DPTN-E:** resolved COL-008/013 by making `docs/index.md` the sole authored discovery root, generating `knowledge/` as OKF compatibility, and demoting `docs/canonical/README.md` to compatibility orientation.
- **DPTN-F:** completed the remaining COL-009 cross-surface stable-reference rebinding and resolved COL-011. Current agents/rules/validators now use first-class paths; historical compatibility is isolated to completed CKR test projection only.

## Remaining DPTN-G boundary

COL-012 remains active until DPTN-G exit. DPTN-G also owns MOVE-020, physical legacy redirect/path retirement where safe, migration-scaffolding disposition, and final conservation/exit review. Resolving COL-009/011 does not authorize those actions early.

## Resolution-order invariant

History relocation must precede path reuse. A resolved collision does not authorize its dependent later phase. No collision may be resolved by deleting preserved history, silently overwriting a target, treating generated routing as semantic authority, or choosing authority by path recency, vacancy, redirect presence or search rank.
