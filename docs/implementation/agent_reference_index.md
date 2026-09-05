# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-I; IN EXECUTION CKR-J; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Universal start

| Need | Read first |
|---|---|
| CKR status | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| Stable ID | `python3 scripts/agentic/resolve_stable_id.py <ID>` |
| Stable-ID policy | `docs/agentic_development_foundation/stable_reference_policy.md` |
| Concepts | `docs/canonical/concepts/README.md` |
| SYN/REF/HLTH/OPS/INTG contracts | `docs/canonical/contracts/README.md` |
| Current integration/source capability | `docs/canonical/contracts/integration/README.md` |
| Current technical architecture | `docs/canonical/architecture/README.md` |
| Frozen reference architecture | `docs/canonical/architecture/reference-architecture.md` |
| Current health/quality semantics | `docs/canonical/contracts/health-quality-timing/README.md` |
| Current operational semantics | `docs/canonical/contracts/operations/README.md` |
| Current questioning/Explanation semantics | `docs/canonical/experience/README.md` |
| Authority/AUTH | `docs/canonical/authority/README.md` |
| Design history | `docs/design_history/README.md` |
| CKR-J routing review | `docs/canonical_knowledge_retrofit/ckr_j_execution_review.md` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Stable references

Default exact-ID lookup returns the current stable locator `owner_path::ID`. Add `--history` only for explicit historical/provenance inspection; history never changes current ownership. A successful stable lookup is routing evidence, not proof that implementation satisfies the contract.

## Current state

- CKR-A–I — COMPLETE / ACCEPTED.
- CKR-J — IN EXECUTION / ROUTING CUTOVER VALIDATION.
- CKR-K — PLANNED / NOT ACTIVE.
- Implementation 001-A — BLOCKED until CKR-K.

All accepted semantic families already resolve to canonical owners. Phase 001–010 is provenance/supporting rationale. CKR-J is validating the activated canonical-first OKF/stable-reference/agent-routing layer.
