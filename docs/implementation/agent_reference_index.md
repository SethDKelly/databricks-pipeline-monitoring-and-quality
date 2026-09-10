# DMTZ Agent Reference Index

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN exit: ACCEPTED — Implementation 001-A NEXT / READY / NOT STARTED.**

## Universal start

| Need | Read first |
|---|---|
| Unknown-location discovery | `docs/index.md` |
| History/provenance | `docs/history/README.md` |
| CKR durable authority/routing | `docs/canonical_knowledge_retrofit/README.md` |
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
| Implementation state | `docs/implementation/README.md` |
| Generic OKF compatibility | generated `knowledge/index.md` |
| Conformance | `scripts/agentic/run_conformance.py` |
| Completed DPTN provenance | `docs/history/retrofits/dptn/README.md` |

## Current state

- ADF — COMPLETE / EXIT ACCEPTED.
- CKR-A–K — COMPLETE / ACCEPTED.
- CKR EXIT — ACCEPTED.
- DPTN-A–G — COMPLETE / ACCEPTED.
- DPTN EXIT — ACCEPTED.
- **Implementation 001-A — NEXT / READY / NOT STARTED.**

Repository-native agents use `docs/index.md`; generated OKF is compatibility only; exact IDs resolve to first-class current owners; history remains explicit provenance. DPTN is no longer a live routing layer.

Implementation readiness is not implementation authorization. Begin 001-A only when the human explicitly selects it.
