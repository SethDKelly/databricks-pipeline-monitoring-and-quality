# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

## Universal start

| Need | Read first |
|---|---|
| Active topology program | `docs/documentation_topology_normalization/README.md` |
| DPTN topology authority | `docs/documentation_topology_normalization/topology_authority.md` |
| Accepted future move plan | `docs/documentation_topology_normalization/move_map.json` — planning only until each later phase is selected/cut over |
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
| Design history | `docs/design_history/README.md` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references after DPTN-A

Default exact-ID lookup continues to return the **current CKR canonical** `owner_path::ID`. DPTN-A accepted move-map targets are future physical destinations and must not be substituted into current locators. Add `--history` only for explicit historical/provenance inspection.

## Current state

- ADF — COMPLETE / EXIT ACCEPTED.
- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- **DPTN-A — COMPLETE / ACCEPTED.**
- **DPTN-B — NEXT / READY / NOT STARTED.**
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN-A performed inventory and planning only. No physical documentation move or product implementation occurred. DPTN-B requires explicit human selection before its bounded relocation work begins.
