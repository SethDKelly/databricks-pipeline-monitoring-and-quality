# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

## Universal start

| Need | Read first |
|---|---|
| Live DPTN topology state | `docs/documentation_topology_normalization/README.md` |
| Accepted DPTN move planning | `docs/documentation_topology_normalization/move_map.json` |
| CKR exit / current authority | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| Stable ID | `python3 scripts/agentic/resolve_stable_id.py <ID>` |
| Stable-ID policy | `docs/agentic_development_foundation/stable_reference_policy.md` |
| Concepts | `docs/canonical/concepts/README.md` |
| SYN/REF/HLTH/OPS/INTG contracts | `docs/canonical/contracts/README.md` |
| Integration/source capability | `docs/canonical/contracts/integration/README.md` |
| Technical architecture | `docs/canonical/architecture/README.md` |
| Frozen reference architecture | `docs/canonical/architecture/reference-architecture.md` |
| Health/quality semantics | `docs/canonical/contracts/health-quality-timing/README.md` |
| Operational semantics | `docs/canonical/contracts/operations/README.md` |
| Questioning/Explanation semantics | `docs/canonical/experience/README.md` |
| Authority/AUTH | `docs/canonical/authority/README.md` |
| Design history | `docs/design_history/README.md` |
| CKR-K exit acceptance | `docs/canonical_knowledge_retrofit/ckr_k_execution_review.md` |
| DPTN-A exit acceptance | `docs/documentation_topology_normalization/dptn_a_execution_review.md` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references

Default exact-ID lookup returns `owner_path::ID`. Add `--history` only for explicit historical/provenance inspection. A successful stable lookup is routing evidence, not proof that implementation satisfies the contract.

DPTN-A changed no current owner path. Future targets in the accepted DPTN move map remain planning metadata until the relevant later phase performs a validated cutover.

## Current state

- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- DPTN-A — COMPLETE / ACCEPTED.
- DPTN-B — NEXT / READY / NOT STARTED.
- DPTN-C–G — PLANNED.
- **Implementation 001-A — BLOCKED ON DPTN EXIT.**

All accepted semantic families still resolve to existing CKR canonical owners. Phase 001–010 remains provenance/supporting rationale. No product implementation or physical documentation relocation is authorized until the applicable later DPTN phase is explicitly selected.
