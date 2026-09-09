# DPTN Collision Register

**Status:** ACTIVE — DPTN-A inventory accepted; DPTN-B/C/D resolutions recorded; later-phase collisions remain open

A collision is any target path whose current contents or role would make a later physical move ambiguous or unsafe. DPTN-A registered the collision set. DPTN-B resolved history/collision preparation; DPTN-C resolved current-owner promotion; DPTN-D resolved the mixed-lifecycle CKR/ADF decomposition. **Vacancy does not assign current authority.** Redirect presence and path recency likewise do not assign current authority.

| ID | Target path / concern | Accepted condition | Required / remaining resolution | Earliest phase |
|---|---|---|---|---|
| COL-001 | `docs/concepts/` | Historical Phase 002–010 corpus preserved at `docs/history/phases/`; DPTN-C promoted the accepted current concept tree to `docs/concepts/` | RESOLVED for DPTN-B/C; later route cleanup only | DPTN-B → C |
| COL-002 | `docs/reference/` | Legacy reference corpus preserved at `docs/history/reference-legacy/`; DPTN-C promoted accepted current reference to `docs/reference/` | RESOLVED for DPTN-B/C; later route cleanup only | DPTN-B → C |
| COL-003 | `docs/decisions/` | Phase-scoped decisions relocated to `docs/history/decisions/`; source path remains vacant/unassigned | Any future current ADR namespace requires separate authority/design decision | DPTN-B |
| COL-004 | `docs/history/` | Explicit HISTORY / PROVENANCE ONLY root created and populated by exact-tree relocation | Preserve non-current authority contract through later phases | DPTN-B |
| COL-005 | `docs/design_history/` | Prior design-history tree preserved at `docs/history/design-history/`; old root vacated | Permanent reference rebinding remains later routing work | DPTN-B |
| COL-006 | `docs/canonical_knowledge_retrofit/` | Durable ownership/routing mechanics remain current; completed CKR evidence relocated to `docs/history/retrofits/ckr/` | RESOLVED BY DPTN-D; later route cleanup only | DPTN-D |
| COL-007 | `docs/agentic_development_foundation/` | Durable agentic operating policy/live residuals remain current; completed ADF evidence relocated to `docs/history/foundations/adf/` | RESOLVED BY DPTN-D; later route cleanup only | DPTN-D |
| COL-008 | `knowledge/` vs `docs/index.md` | Separate manually maintained routing plane can drift from docs | Determine compatibility requirement; converge into docs or generate projection | DPTN-E |
| COL-009 | stable-ID resolver paths | DPTN-C rebound current locators to first-class owner paths; broad agent/link cleanup remains | Resolver current-owner side resolved; complete cross-surface rebinding/retirement in DPTN-F | DPTN-C → F |
| COL-010 | CKR ownership inventory paths | DPTN-C atomically rebound current target owners to first-class paths and historical pointers to `docs/history/`; DPTN-D retained the durable ledger at its existing path | RESOLVED for DPTN-C/D; later broad routing cleanup may rebind references but must not invent another ownership ledger | DPTN-C → F |
| COL-011 | agent/OKF links | Agent rules, skills, bridges and OKF body links may still reference compatibility routes | Rebind after physical topology stabilizes | DPTN-F |
| COL-012 | implementation traceability | Implementation has not started | Keep 001-A blocked until DPTN exit | DPTN-A–G |
| COL-013 | `docs/canonical/README.md` and future `docs/index.md` | `docs/canonical/README.md` is now routing/compatibility only after promotion | Merge routing/orientation during DPTN-E | DPTN-E |

## DPTN-B resolution record

- **COL-001 — RESOLVED BY DPTN-B.** MOVE-001 preserved the exact former `docs/concepts` history tree at `docs/history/phases` before path reclaim. DPTN-C later reused `docs/concepts` only after that preservation boundary was accepted.
- **COL-002 — RESOLVED BY DPTN-B.** MOVE-002 preserved the exact former `docs/reference` history tree at `docs/history/reference-legacy` before path reclaim. DPTN-C later reused `docs/reference` only after that preservation boundary was accepted.
- **COL-003 — RESOLVED BY DPTN-B.** MOVE-005 preserves the exact former `docs/decisions` tree at `docs/history/decisions`; `docs/decisions` remains vacant/non-authoritative.
- **COL-004 — RESOLVED BY DPTN-B.** `docs/history/` exists with an explicit HISTORY / PROVENANCE ONLY contract.
- **COL-005 — RESOLVED BY DPTN-B.** MOVE-006 preserves the prior design-history tree at `docs/history/design-history`; `docs/design_history` is vacated.

## DPTN-C resolution record

- **COL-001 — FULLY RESOLVED FOR B/C.** MOVE-007 promoted the exact accepted current concept tree to `docs/concepts` after history relocation.
- **COL-002 — FULLY RESOLVED FOR B/C.** MOVE-014 promoted the exact accepted current reference tree to `docs/reference` after history relocation.
- **COL-009 — CURRENT-LOCATOR SIDE RESOLVED BY DPTN-C.** Stable-ID resolution now follows first-class owner paths; broad routing/link retirement remains DPTN-F.
- **COL-010 — RESOLVED BY DPTN-C.** The CKR ownership inventory was rebound atomically with MOVE-007 through MOVE-014 and no longer selects `docs/canonical/<family>` substantive owners.

## DPTN-D resolution record

- **COL-006 — RESOLVED BY DPTN-D.** MOVE-015 decomposed CKR at file lifecycle boundaries: the durable ownership ledger/authority mechanics remain current and completed retrofit evidence is historical.
- **COL-007 — RESOLVED BY DPTN-D.** MOVE-016 decomposed ADF at file lifecycle boundaries: durable operating policy/live residual obligations remain current and completed program evidence is historical.
- **COL-010 — DPTN-D PORTION RESOLVED.** The durable CKR ownership ledger remains at `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`; no relocation was necessary or authorized merely for aesthetic normalization.

COL-008, COL-011 and COL-013 remain open for their assigned later phases. COL-009 retains only its DPTN-F cross-surface cleanup portion. COL-012 remains active through DPTN-G exit.

## Resolution-order invariant

History relocation must precede reuse of an occupied first-class name. A resolved collision does not authorize its dependent later phase. No collision may be resolved by deleting preserved history, silently overwriting a target, or choosing authority by path recency, vacancy, or redirect presence.
