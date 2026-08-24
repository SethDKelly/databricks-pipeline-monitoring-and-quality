# REF-012 — Actual Retained State versus Reconstructible Historical State

**Status:** Accepted — Phase 004 Group 02

## Purpose

Define the evidence boundary between claiming that a historical Assessment/decision/control/communication actually existed and reconstructing what could now be concluded from a historical evidence cut.

## Rule

To represent a state as **actually recorded/decided/communicated historically**, the framework needs retained provenance-bearing evidence that the owning concept state/action existed at the historical knowledge time.

If that evidence is unavailable, the framework may still reconstruct a historical view from eligible source state under REF-007, but the output is labeled **replay-derived/reconstructed** and receives the current evaluation/generation time.

## Functional retention implications

The model does not select storage technology or retention duration, but it requires enough historical evidence to distinguish actual from reconstructed state for material cases, including where applicable:

- actual Assessment/status versions;
- Causal Claim status/review transitions;
- Investigation closure/reopen state;
- Execution Gate hold/admit/override actions;
- Propagation Safeguard proposal/activation/release actions;
- actual retained Explanation/report/communication;
- correction/supersession relationships;
- historical Capability Authorization when it is being asserted as a past fact.

If such evidence is not retained, current replay must acknowledge the limitation rather than fabricating historical action/belief/communication.

## Reconstruction does not create historical action

A reconstructed `as-known-at-08:15` Assessment does not prove an Assessment ran at 08:15. A reconstructed explanation does not prove anyone received it. A current gate evaluation over historical readiness evidence does not replace the gate action that actually occurred.

## Authorization

Current requester authorization governs disclosure of both retained historical state and reconstructed state. Historical actor privilege is not reusable access.

## Timing and performance implication

Not every post-operations question needs to be precomputed or retained as prose. Later architecture may choose to retain high-consequence state/actions while reconstructing other views on demand, provided the actual-versus-reconstructed distinction remains reliable.

## Non-goals

- choosing database/event-store/snapshot architecture;
- setting retention periods;
- requiring every generated Explanation to be retained;
- treating reconstructibility as evidence that a historical conclusion actually existed.
