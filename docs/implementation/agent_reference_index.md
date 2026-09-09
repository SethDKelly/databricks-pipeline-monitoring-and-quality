# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-C; NEXT DPTN-D; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

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
| Concepts | `docs/concepts/README.md` |
| Contracts | `docs/contracts/README.md` |
| Technical architecture | `docs/architecture/README.md` |
| Questioning/Explanation | `docs/experience/README.md` |
| Authority/AUTH | `docs/authority/README.md` |
| Invariants | `docs/invariants/README.md` |
| Policies | `docs/policies/README.md` |
| Reference | `docs/reference/README.md` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references after DPTN-C

Default exact-ID lookup returns the current first-class `owner_path::ID` selected by the ownership inventory. Add `--history` only for explicit historical/provenance inspection. Legacy `docs/canonical/<family>` compatibility redirects may keep unrebound links navigable temporarily but are not current owners and must not appear as resolver locators.

## Current state

- ADF — COMPLETE / EXIT ACCEPTED.
- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- **DPTN-A–C — COMPLETE / ACCEPTED.**
- **DPTN-D — NEXT / READY / NOT STARTED.**
- **Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.**

DPTN-C completed MOVE-007 through MOVE-014 and directly necessary ownership/resolver/validation compatibility. `docs/history/` remains provenance-only; DPTN-D/E/F/G and product implementation remain unauthorized until explicitly selected.
