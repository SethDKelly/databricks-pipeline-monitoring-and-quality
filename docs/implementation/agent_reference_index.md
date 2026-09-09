# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A; IN EXECUTION DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

## Universal start

| Need | Read first |
|---|---|
| Active topology program | `docs/documentation_topology_normalization/README.md` |
| DPTN topology authority | `docs/documentation_topology_normalization/topology_authority.md` |
| Accepted future move plan | `docs/documentation_topology_normalization/move_map.json` — planning authority only |
| CKR exit / current authority | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| Stable ID | `python3 scripts/agentic/resolve_stable_id.py <ID>` |
| Stable-ID policy | `docs/agentic_development_foundation/stable_reference_policy.md` |
| Concepts | `docs/canonical/concepts/README.md` |
| SYN/REF/HLTH/OPS/INTG contracts | `docs/canonical/contracts/README.md` |
| Technical architecture | `docs/canonical/architecture/README.md` |
| Frozen reference architecture | `docs/canonical/architecture/reference-architecture.md` |
| Questioning/Explanation semantics | `docs/canonical/experience/README.md` |
| Authority/AUTH | `docs/canonical/authority/README.md` |
| History/provenance | `docs/history/README.md` after the DPTN-B relocation cutover |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references during DPTN-B

Default exact-ID lookup continues to return the **current CKR canonical** `owner_path::ID`. DPTN-B changes history locations only and must not alter current locators. Add `--history` only for explicit historical/provenance inspection.

## Current state

- ADF — COMPLETE / EXIT ACCEPTED.
- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- **DPTN-A — COMPLETE / ACCEPTED.**
- **DPTN-B — IN EXECUTION.**
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN-B may execute only MOVE-001 through MOVE-006 and necessary history-role/routing validation. Current semantic authority remains under `docs/canonical/`.
