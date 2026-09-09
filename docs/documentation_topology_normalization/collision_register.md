# DPTN Collision Register

**Status:** ACTIVE — DPTN-A inventory accepted; DPTN-B/C/D/E resolutions recorded; later-phase collisions remain open

A collision is any target path whose current contents or role would make a later physical move ambiguous or unsafe. **Vacancy does not assign current authority.** Redirect presence, generated output and path recency likewise do not assign current authority.

| ID | Target path / concern | Accepted condition | Required / remaining resolution | Earliest phase |
|---|---|---|---|---|
| COL-001 | `docs/concepts/` | History preserved; accepted current concepts promoted to first-class path | RESOLVED for DPTN-B/C; later route cleanup only | DPTN-B → C |
| COL-002 | `docs/reference/` | Legacy reference history preserved; accepted current reference promoted | RESOLVED for DPTN-B/C; later route cleanup only | DPTN-B → C |
| COL-003 | `docs/decisions/` | Phase decisions preserved under history; source remains vacant/unassigned | Any future current ADR namespace requires separate authority decision | DPTN-B |
| COL-004 | `docs/history/` | Explicit HISTORY / PROVENANCE ONLY root exists | Preserve non-current role | DPTN-B |
| COL-005 | `docs/design_history/` | Prior design-history tree preserved under history | Permanent reference cleanup remains later routing work | DPTN-B |
| COL-006 | `docs/canonical_knowledge_retrofit/` | Durable mechanics current; completed CKR evidence historical | RESOLVED BY DPTN-D | DPTN-D |
| COL-007 | `docs/agentic_development_foundation/` | Durable operating policy/live residuals current; completed ADF evidence historical | RESOLVED BY DPTN-D | DPTN-D |
| COL-008 | `knowledge/` vs `docs/index.md` | `docs/index.md` is authored discovery root; `knowledge/` is generated OKF compatibility projection; prior authored tree preserved in history | RESOLVED BY DPTN-E | DPTN-E |
| COL-009 | stable-ID resolver paths | Current locators point to first-class owners | Broad cross-surface link/rule cleanup remains | DPTN-C → F |
| COL-010 | CKR ownership inventory paths | Durable ledger retained; current targets first-class; provenance history paths explicit | RESOLVED for DPTN-C/D | DPTN-C → F |
| COL-011 | agent/OKF links | Physical topology now stable through discovery-root convergence | Rebind broad agent/rule/link surfaces | DPTN-F |
| COL-012 | implementation traceability | Implementation has not started | Keep 001-A blocked until DPTN exit | DPTN-A–G |
| COL-013 | `docs/canonical/README.md` vs `docs/index.md` | Orientation merged into `docs/index.md`; canonical README remains compatibility only | RESOLVED BY DPTN-E; retirement later | DPTN-E |

## DPTN-B resolution record

- **COL-001 — RESOLVED BY DPTN-B.** MOVE-001 preserved the former concept history tree before first-class path reclaim.
- **COL-002 — RESOLVED BY DPTN-B.** MOVE-002 preserved the legacy reference tree before first-class path reclaim.
- **COL-003 — RESOLVED BY DPTN-B.** Phase-scoped decisions are preserved under history; the old root is vacant/unassigned.
- **COL-004 — RESOLVED BY DPTN-B.** `docs/history/` is explicitly HISTORY / PROVENANCE ONLY.
- **COL-005 — RESOLVED BY DPTN-B.** Prior design-history routing is preserved under history.

## DPTN-C resolution record

- **COL-001 — FULLY RESOLVED FOR B/C.** MOVE-007 promoted accepted current concepts.
- **COL-002 — FULLY RESOLVED FOR B/C.** MOVE-014 promoted accepted current reference.
- **COL-009 — CURRENT-LOCATOR SIDE RESOLVED BY DPTN-C.** Stable-ID resolution follows first-class owners; broad rebinding remains DPTN-F.
- **COL-010 — RESOLVED BY DPTN-C.** The ownership inventory selects first-class substantive owners.

## DPTN-D resolution record

- **COL-006 — RESOLVED BY DPTN-D.** MOVE-015 separated durable CKR mechanics from completed retrofit evidence.
- **COL-007 — RESOLVED BY DPTN-D.** MOVE-016 separated durable ADF operating policy/live residuals from completed program evidence.
- **COL-010 — DPTN-D PORTION RESOLVED.** The durable ownership ledger remains at its established path rather than being moved for aesthetics.

## DPTN-E resolution record

- **COL-008 — RESOLVED BY DPTN-E.** MOVE-017 preserves the complete pre-convergence authored OKF tree at `docs/history/routing/okf-pre-dptn-e/`, establishes `docs/index.md` as the sole authored discovery root, and retains top-level `knowledge/` only as deterministic generated OKF v0.2 compatibility output.
- **COL-013 — RESOLVED BY DPTN-E.** MOVE-018 merges the former `docs/canonical/README.md` orientation responsibility into `docs/index.md`; the old path remains compatibility-only pending DPTN-F/G.

COL-011 and the remaining COL-009 cross-surface cleanup are next under DPTN-F. COL-012 remains active through DPTN-G exit.

## Resolution-order invariant

History relocation must precede path reuse. A resolved collision does not authorize its dependent later phase. No collision may be resolved by deleting preserved history, silently overwriting a target, treating generated routing as semantic authority, or choosing authority by path recency, vacancy, redirect presence or search rank.
