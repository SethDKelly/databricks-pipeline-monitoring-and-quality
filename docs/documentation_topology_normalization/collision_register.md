# DPTN Collision Register

**Status:** ACTIVE — DPTN-A inventory accepted; DPTN-B/C resolutions recorded; later-phase collisions remain open

A collision is any target path whose current contents or role would make a later physical move ambiguous or unsafe. DPTN-A registered the collision set. DPTN-B resolved history/collision preparation; DPTN-C resolved the current-owner promotion and ownership-ledger responsibilities assigned to it. **Vacancy, redirect presence, and path recency do not assign current authority.**

| ID | Target path / concern | Accepted condition | Required / remaining resolution | Earliest phase |
|---|---|---|---|---|
| COL-001 | `docs/concepts/` | Historical Phase 002–010 corpus preserved at `docs/history/phases/`; DPTN-C promoted the accepted current concept tree to `docs/concepts/` | RESOLVED for DPTN-B/C; later route cleanup only | DPTN-B → C |
| COL-002 | `docs/reference/` | Legacy reference corpus preserved at `docs/history/reference-legacy/`; DPTN-C promoted accepted current reference to `docs/reference/` | RESOLVED for DPTN-B/C; later route cleanup only | DPTN-B → C |
| COL-003 | `docs/decisions/` | Phase-scoped decisions relocated to `docs/history/decisions/`; source path remains vacant/unassigned | Any future current ADR namespace requires separate authority/design decision | DPTN-B |
| COL-004 | `docs/history/` | Explicit HISTORY / PROVENANCE ONLY root created and populated by exact-tree relocation | Preserve non-current authority contract through later phases | DPTN-B |
| COL-005 | `docs/design_history/` | Prior design-history tree preserved at `docs/history/design-history/`; old root vacated | Permanent reference rebinding remains later routing work | DPTN-B |
| COL-006 | `docs/canonical_knowledge_retrofit/` | Mixes durable current ownership/routing mechanics with CKR execution evidence | File-level decomposition; bulk move prohibited | DPTN-D |
| COL-007 | `docs/agentic_development_foundation/` | Mixes durable human-directed/context/security policies with completed-program evidence | File-level decomposition; bulk move prohibited | DPTN-D |
| COL-008 | `knowledge/` vs `docs/index.md` | Separate manually maintained routing plane can drift from docs | Determine compatibility requirement; converge into docs or generate projection | DPTN-E |
| COL-009 | stable-ID resolver paths | DPTN-C rebound current locators to first-class owner paths; broad agent/link cleanup remains | Resolver current-owner side resolved; complete cross-surface rebinding/retirement in DPTN-F | DPTN-C → F |
| COL-010 | CKR ownership inventory paths | DPTN-C atomically rebound current target owners to first-class paths and historical pointers to `docs/history/` | RESOLVED for DPTN-C; later operational decomposition/rebinding may relocate the ledger itself | DPTN-C/F |
| COL-011 | agent/OKF links | Agent rules, skills, bridges and OKF body links may still reference compatibility routes | Rebind after physical topology stabilizes | DPTN-F |
| COL-012 | implementation traceability | Implementation has not started | Keep 001-A blocked until DPTN exit | DPTN-A–G |
| COL-013 | `docs/canonical/README.md` and future `docs/index.md` | `docs/canonical/README.md` is now routing/compatibility only after promotion | Merge routing/orientation during DPTN-E | DPTN-E |

## DPTN-B resolution record

- **COL-001 — DPTN-B SIDE RESOLVED.** MOVE-001 preserved the former `docs/concepts` history tree at `docs/history/phases` before path reclaim.
- **COL-002 — DPTN-B SIDE RESOLVED.** MOVE-002 preserved the former `docs/reference` history tree at `docs/history/reference-legacy` before path reclaim.
- **COL-003 — RESOLVED BY DPTN-B.** MOVE-005 preserves the exact former `docs/decisions` tree at `docs/history/decisions`; `docs/decisions` remains vacant/non-authoritative.
- **COL-004 — RESOLVED BY DPTN-B.** `docs/history/` exists with an explicit HISTORY / PROVENANCE ONLY contract.
- **COL-005 — RESOLVED BY DPTN-B.** MOVE-006 preserves the prior design-history tree at `docs/history/design-history`; `docs/design_history` is vacated.

## DPTN-C resolution record

- **COL-001 — FULLY RESOLVED FOR B/C.** MOVE-007 promoted the exact accepted current concept tree to `docs/concepts` after history relocation.
- **COL-002 — FULLY RESOLVED FOR B/C.** MOVE-014 promoted the exact accepted current reference tree to `docs/reference` after history relocation.
- **COL-009 — CURRENT-LOCATOR SIDE RESOLVED BY DPTN-C.** Stable-ID resolution now follows first-class owner paths; broad routing/link retirement remains DPTN-F.
- **COL-010 — RESOLVED BY DPTN-C.** The CKR ownership inventory was rebound atomically with MOVE-007 through MOVE-014 and no longer selects `docs/canonical/<family>` substantive owners.

COL-006–008 and COL-011–013 remain open for their assigned later phases. COL-009 retains only its DPTN-F cross-surface cleanup portion.

## Resolution-order invariant

History relocation must precede reuse of an occupied first-class name. A resolved collision does not authorize its dependent later phase. No collision may be resolved by deleting preserved history, silently overwriting a target, or choosing authority by path recency, vacancy, or redirect presence.
