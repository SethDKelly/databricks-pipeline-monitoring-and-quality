# DPTN-C Execution Review

**Status:** IN EXECUTION

## Scope

DPTN-C promotes accepted CKR current semantic owners from nested `docs/canonical/<family>/` locations into first-class `docs/<family>/` locations. It is a path-only authority cutover: accepted meaning, stable IDs, concept count, architecture partitioning and implementation state must remain unchanged.

Authorized physical moves are MOVE-007 through MOVE-014 only. DPTN-D through DPTN-G and product implementation remain outside this phase.

## Candidate cutover design

The candidate uses exact Git-tree reuse for all eight promoted semantic roots. The physical tree move and CKR ownership-ledger rebinding must occur in one commit.

After cutover:

- substantive current owners live in `docs/concepts`, `docs/architecture`, `docs/authority`, `docs/contracts`, `docs/experience`, `docs/invariants`, `docs/policies` and `docs/reference`;
- `docs/canonical/README.md` remains an orientation/compatibility surface pending DPTN-E;
- temporary `docs/canonical/<family>` compatibility redirects may remain for unrebound links, but are not ownership-ledger targets and are not current owners;
- historical-source pointers in the ownership ledger resolve to the DPTN-B `docs/history/` namespace so reclaimed current paths cannot masquerade as provenance;
- stable-ID current resolution follows normalized ledger target paths;
- `--history` excludes normalized current roots;
- completed CKR validators may execute against a temporary pre-DPTN-C compatibility projection, while DPTN-C validation inspects the real normalized topology.

## Conservation baseline

DPTN-C must preserve:

- 24 accepted concepts;
- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500 plus the frozen reference architecture;
- all CKR semantic non-collapse rules;
- `docs/history/` as non-current provenance;
- mixed ADF/CKR directories for DPTN-D;
- Implementation 001-A blocked on DPTN exit.

## Validation evidence

Candidate validation pending.

## Handoff

DPTN-D is not authorized by DPTN-C execution or acceptance. A later phase requires explicit human selection.
