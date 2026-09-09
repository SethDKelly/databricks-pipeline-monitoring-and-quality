# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; IN EXECUTION DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

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
| Concepts | follow the ownership ledger; DPTN-C promotes `docs/canonical/concepts/` to `docs/concepts/` |
| Contracts | follow the ownership ledger; DPTN-C promotes `docs/canonical/contracts/` to `docs/contracts/` |
| Technical architecture | follow the ownership ledger; DPTN-C promotes `docs/canonical/architecture/` to `docs/architecture/` |
| Questioning/Explanation | follow the ownership ledger; DPTN-C promotes `docs/canonical/experience/` to `docs/experience/` |
| Authority/AUTH | follow the ownership ledger; DPTN-C promotes `docs/canonical/authority/` to `docs/authority/` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references during DPTN-C

Default exact-ID lookup must return the current `owner_path::ID` selected by the ownership inventory. Before the atomic C cutover that is the CKR path; after it, the normalized first-class path. Add `--history` only for explicit historical/provenance inspection. Legacy compatibility redirects may keep unrebound links navigable temporarily but are not current owners and must not appear as resolver locators.

## Current state

- ADF — COMPLETE / EXIT ACCEPTED.
- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- **DPTN-A–B — COMPLETE / ACCEPTED.**
- **DPTN-C — IN EXECUTION.**
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN-C may execute only MOVE-007 through MOVE-014 and directly necessary ownership/resolver/validation compatibility. `docs/history/` remains provenance-only; DPTN-D/E/F/G and product implementation remain unauthorized.
