# DPTN Collision Register

**Status:** ACTIVE — DPTN-A inventory accepted; DPTN-B resolutions recorded; later-phase collisions remain open

A collision is any target path whose current contents or role would make a later physical move ambiguous or unsafe. DPTN-A registered the collision set. DPTN-B resolved only the history/collision responsibilities assigned to it.

| ID | Target path / concern | Accepted condition | Required / remaining resolution | Earliest phase |
|---|---|---|---|---|
| COL-001 | `docs/concepts/` | Pre-canonical Phase 002–010 corpus relocated to `docs/history/phases/`; source path now vacant/unassigned | DPTN-C may promote canonical concepts only after explicit selection and atomic authority cutover | DPTN-B → C |
| COL-002 | `docs/reference/` | Legacy reference corpus relocated to `docs/history/reference-legacy/`; source path now vacant/unassigned | DPTN-C may promote canonical reference only after explicit selection and atomic authority cutover | DPTN-B → C |
| COL-003 | `docs/decisions/` | Phase-scoped decisions relocated to `docs/history/decisions/`; source path now vacant/unassigned | Any future current ADR namespace requires separate authority/design decision | DPTN-B |
| COL-004 | `docs/history/` | Explicit HISTORY / PROVENANCE ONLY root created and populated by exact-tree relocation | Preserve non-current authority contract through later phases | DPTN-B |
| COL-005 | `docs/design_history/` | Prior design-history tree preserved at `docs/history/design-history/`; old root vacated | Permanent reference rebinding remains later routing work | DPTN-B |
| COL-006 | `docs/canonical_knowledge_retrofit/` | Mixes durable current ownership/routing mechanics with CKR execution evidence | File-level decomposition; bulk move prohibited | DPTN-D |
| COL-007 | `docs/agentic_development_foundation/` | Mixes durable human-directed/context/security policies with completed-program evidence | File-level decomposition; bulk move prohibited | DPTN-D |
| COL-008 | `knowledge/` vs `docs/index.md` | Separate manually maintained routing plane can drift from docs | Determine compatibility requirement; converge into docs or generate projection | DPTN-E |
| COL-009 | stable-ID resolver paths | 1,237 current locators still point into `docs/canonical/...` | Rebind only after current-owner promotion; history paths never satisfy current resolution | DPTN-F |
| COL-010 | CKR ownership inventory paths | Canonical ownership ledger encodes `docs/canonical/...` targets | Update atomically with DPTN-C current-owner moves; do not pre-stage target authority | DPTN-C/F |
| COL-011 | agent/OKF links | Agent rules, skills, bridges and OKF body links reference current/pre-normalization topology | Rebind after physical topology stabilizes | DPTN-F |
| COL-012 | implementation traceability | Implementation has not started | Keep 001-A blocked until DPTN exit | DPTN-A–G |
| COL-013 | `docs/canonical/README.md` and future `docs/index.md` | Current canonical index and future unified docs index overlap in orientation purpose | Merge routing/orientation only after canonical promotion | DPTN-E |

## DPTN-B resolution record

- **COL-001 — RESOLVED BY DPTN-B.** MOVE-001 preserves the exact former `docs/concepts` tree at `docs/history/phases`; `docs/concepts` is vacant and non-authoritative.
- **COL-002 — RESOLVED BY DPTN-B.** MOVE-002 preserves the exact former `docs/reference` tree at `docs/history/reference-legacy`; `docs/reference` is vacant and non-authoritative.
- **COL-003 — RESOLVED BY DPTN-B.** MOVE-005 preserves the exact former `docs/decisions` tree at `docs/history/decisions`; `docs/decisions` is vacant and non-authoritative.
- **COL-004 — RESOLVED BY DPTN-B.** `docs/history/` exists with an explicit HISTORY / PROVENANCE ONLY contract.
- **COL-005 — RESOLVED BY DPTN-B.** MOVE-006 preserves the prior design-history tree at `docs/history/design-history`; `docs/design_history` is vacated.

COL-006 through COL-013 remain open for their assigned later phases.

## Resolution-order invariant

History relocation must precede reuse of an occupied first-class name. A resolved collision does not authorize its dependent later move. No collision may be resolved by deleting preserved history, silently overwriting a target, or choosing authority by path recency/vacancy.
