# OPS-063 — Historical Investigation Replay, Late Evidence & Reopen

**Status:** Accepted — Phase 007 Group 05

## Purpose

Preserve what investigators knew and concluded at the time while allowing later evidence to improve retrospective localization and causal evaluation.

## Contract

Historical Investigation reasoning distinguishes:

- event/effective time of the operational evidence;
- source availability and framework knowledge time;
- Investigation scope/lead/localization state as known at a cutoff;
- Causal Claim status at that cutoff;
- later evidence/correction time;
- current retrospective reconstruction/evaluation time.

Late evidence may:

- move the retrospectively earliest evidenced deviation upstream/earlier;
- alter execution/version association;
- add or remove a lead under sufficient evidence;
- challenge a Causal Claim;
- justify Investigation reopen under REF-011 materiality.

None rewrites the original retained Investigation state or actions taken under that knowledge cut.

## Invariants

- current best reconstruction ≠ what investigators knew then.
- late discovery ≠ original investigative error automatically.
- reopen ≠ erase prior closure.
- corrected evidence creates reassessment/revision provenance rather than silent mutation.
