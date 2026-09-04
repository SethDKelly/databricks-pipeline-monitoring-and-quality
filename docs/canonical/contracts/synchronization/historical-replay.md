# Historical Replay Synchronizations

**Canonical key:** `contract.synchronization.historical_replay`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.SYN`

**Owns current question:** How is historical/as-known state reconstructed and safely explained when evidence/authority/authorization can change after the event?

**Stable IDs:** SYN-033–SYN-035

## Current semantics

Historical synchronization is bitemporal and non-rewriting. Event/effective-time truth, what DMTZ knew by a knowledge cut, current retrospective interpretation, current requester authorization, and retained authentic historical communication remain distinct.

### SYN-033 — Event/Effective Time + Knowledge Cut → Historical Reconstruction
Resolve each concept's state for the requested event/effective context using only evidence/rules known by the requested knowledge cut. Current records/rules are not projected backward by convenience.

### SYN-034 — Late/Corrected Evidence → Retrospective Re-evaluation
Late/corrected evidence may change current retrospective reconstruction/Assessment/Claim/Impact understanding while preserving what was unknown/conflicting/concluded at the earlier knowledge cut. Actual historical Gate/Safeguard/Execution actions are not rewritten by later knowledge.

### SYN-035 — Historical State + Current Capability Authorization → Safe Replay Explanation
Apply current requester disclosure/Capability Authorization to the historical/as-known or retrospective state being requested. Historical authorization, current disclosure permission, retained communication and reconstructed truth are separate; current access cannot manufacture historical knowledge, and historical access cannot automatically grant current disclosure.

## Invariants / boundaries

- Event/effective time ≠ knowledge/record time.
- Current retrospective truth ≠ as-known-at-cut truth ≠ retained authentic communication.
- Late evidence cannot be backfilled into what the system/team knew then.
- Current authorization governs current disclosure without rewriting historical semantic/epistemic state.
- Unknown/conflicting/restricted historical state remains explicit.

## Provenance

- `docs/concepts/phase_003/06_historical_replay_and_consolidation/`
- `docs/concepts/phase_003/README.md`
