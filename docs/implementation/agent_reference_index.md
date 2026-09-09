# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; NEXT DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

## Universal start

| Need | Read first |
|---|---|
| Active topology program | `docs/documentation_topology_normalization/README.md` |
| DPTN topology authority | `docs/documentation_topology_normalization/topology_authority.md` |
| Accepted move plan | `docs/documentation_topology_normalization/move_map.json` — planning authority only |
| History/provenance | `docs/history/README.md` |
| CKR exit / current authority | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| Stable ID | `python3 scripts/agentic/resolve_stable_id.py <ID>` |
| Concepts | `docs/canonical/concepts/README.md` |
| Contracts | `docs/canonical/contracts/README.md` |
| Technical architecture | `docs/canonical/architecture/README.md` |
| Questioning/Explanation | `docs/canonical/experience/README.md` |
| Authority/AUTH | `docs/canonical/authority/README.md` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references after DPTN-B

Default exact-ID lookup continues to return the **current CKR canonical** `owner_path::ID`. History relocation does not alter current locators. Add `--history` only for explicit historical/provenance inspection.

## Current state

- ADF — COMPLETE / EXIT ACCEPTED.
- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- **DPTN-A–B — COMPLETE / ACCEPTED.**
- **DPTN-C — NEXT / READY / NOT STARTED.**
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN-C may not begin until explicitly selected. Current semantic authority remains under `docs/canonical/`; `docs/history/` is provenance-only.
