# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; IN EXECUTION DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR exits are accepted. DPTN-A–B are complete/accepted; DPTN-C is IN EXECUTION. **Implementation 001-A is BLOCKED / NOT STARTED until DPTN-G exit acceptance.**

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — accepted CKR exit/current ownership model.
2. ownership inventory — exact current semantic owner; lifecycle `ckr_complete`.
3. during DPTN-C, current owner paths may change only through the atomic MOVE-007–MOVE-014 promotion + ownership-ledger cutover.
4. known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns the current `owner_path::ID` selected by the ledger.
5. `knowledge/` — optional bounded discovery while broader route rebinding remains deferred to DPTN-F.
6. `docs/history/` — physical provenance/history root; never current semantic authority.
7. `docs/documentation_topology_normalization/README.md` — live topology-normalization status and move authority.
8. `docs/implementation/README.md` — implementation program state.
9. root `AGENTS.md` — shared instructions.

DPTN-C authorizes only MOVE-007 through MOVE-014 plus directly necessary ownership/resolver/validation compatibility. It does not authorize DPTN-D/E/F/G work beyond compatibility required to keep current routing correct, and it does not authorize product implementation.

**Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.** DPTN exit will return 001-A to NEXT / READY / NOT STARTED; it will not start implementation.
