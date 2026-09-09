# DPTN-A Collision Register

**Status:** CANDIDATE — complete for DPTN-A planning scope

A collision is any target path whose current contents or role would make a later physical move ambiguous or unsafe. DPTN-A registers collisions; it does not resolve them physically.

| ID | Target path / concern | Current condition | Required resolution | Earliest phase |
|---|---|---|---|---|
| COL-001 | `docs/concepts/` | Occupied by Phase 002–010 design corpus while current concepts live under `docs/canonical/concepts/` | Move phase corpus to `docs/history/phases/` before canonical concepts are promoted | DPTN-B → C |
| COL-002 | `docs/reference/` | Contains legacy glossary/authority vocabulary superseded by canonical owners | Move legacy reference corpus to `docs/history/reference-legacy/` before canonical reference promotion | DPTN-B → C |
| COL-003 | `docs/decisions/` | Occupied by phase-scoped decision/review records | Move to `docs/history/decisions/`; reserve first-class `docs/decisions/` for future current ADRs only | DPTN-B |
| COL-004 | `docs/history/` | Target namespace does not yet exist | Create explicit history namespace with non-current authority banner/index before history moves | DPTN-B |
| COL-005 | `docs/design_history/` | Existing history index/tree is separate from proposed unified history namespace | Merge/relocate without losing provenance links or role labels | DPTN-B |
| COL-006 | `docs/canonical_knowledge_retrofit/` | Mixes durable current ownership/routing mechanics with CKR execution evidence | File-level decomposition; bulk move prohibited | DPTN-D |
| COL-007 | `docs/agentic_development_foundation/` | Mixes durable human-directed/context/security policies with completed-program evidence | File-level decomposition; bulk move prohibited | DPTN-D |
| COL-008 | `knowledge/` vs `docs/index.md` | Separate manually maintained routing plane can drift from docs | Determine compatibility requirement; converge into docs or generate projection | DPTN-E |
| COL-009 | stable-ID resolver paths | 1,237 locators currently point into `docs/canonical/...` | Rebind only after current-owner promotion; history paths must never satisfy current resolution | DPTN-F |
| COL-010 | CKR ownership inventory paths | Canonical ownership ledger encodes `docs/canonical/...` targets | Update atomically with DPTN-C current-owner moves; do not pre-stage target authority | DPTN-C/F |
| COL-011 | agent/OKF links | Agent rules, skills, Cursor/Claude bridges and OKF body links reference current topology | Rebind after physical topology stabilizes, not before | DPTN-F |
| COL-012 | implementation traceability | Implementation has not started; future traceability would otherwise capture old paths | Keep 001-A blocked until DPTN exit | DPTN-A–G |
| COL-013 | `docs/canonical/README.md` and future `docs/index.md` | Current canonical index and future unified docs index overlap in orientation purpose | Merge routing/orientation only after canonical promotion; do not merge semantic contract prose | DPTN-E |

## Vacant first-class destinations

At DPTN-A review time, the intended first-class current destinations `docs/architecture/`, `docs/authority/`, `docs/contracts/`, `docs/experience/`, `docs/invariants/`, and `docs/policies/` are not identified as conflicting current semantic roots. Their promotion still requires DPTN-C ownership/routing conservation checks.

## Resolution order invariant

History relocation must precede reuse of an occupied first-class name. Specifically:

- COL-001 must close before `docs/canonical/concepts/** → docs/concepts/**`;
- COL-002 must close before `docs/canonical/reference/** → docs/reference/**`;
- COL-003 must close before any future use of `docs/decisions/` as a current ADR namespace.

No collision may be resolved by deleting preserved history, silently overwriting a target, or choosing authority by path recency.
