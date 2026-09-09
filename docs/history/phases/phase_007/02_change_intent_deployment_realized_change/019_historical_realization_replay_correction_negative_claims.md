# OPS-019 — Historical Realization Replay, Correction & Negative Claims

**Status:** Accepted — Phase 007 Group 02

## Purpose

Make intent/deployment/change reconstruction bitemporal and honest when associations, activation evidence, intent registration or realized-state evidence arrives late or is corrected.

## Historical coordinates

Group 02 preserves independently:

- intent registration/revision/withdrawal knowledge time;
- intended activation time/window/condition;
- deployment attempt event time;
- activation/effective time per target/facet;
- realized Change transition time/interval;
- source evidence availability where material;
- framework collection/recorded/knowledge time;
- correction/supersession time;
- derived comparison evaluation time.

## Contemporaneous versus retrospective comparison

For the same event interval:

- an **as-known-then** comparison uses intent/deployment/change evidence known by the selected cutoff;
- a **retrospective** comparison may use later-but-applicable evidence;
- later discovery can change current realization/conformance interpretation without rewriting what was known or concluded earlier.

Example: runtime evidence learned at 14:00 may establish that R2 activated at 10:00. A current retrospective view can place activation at 10:00; a 10:30 knowledge-cut view still reports activation was not yet known.

## Corrections

Correction may revise:

- target identity;
- source/configuration mapping;
- activation time;
- intent/deployment association;
- realized before/after state;
- conformance result.

Prior recorded evidence/results remain historically reconstructable.

## Negative claims

The following require conclusion-specific opportunity/coverage:

- no deployment attempt occurred;
- no activation occurred;
- no matching registered intent existed;
- intended state did not realize;
- rollback did not restore the selected facet;
- no other overlapping deployment/intent applied.

Missing source data or unsuccessful search is not sufficient by itself.

## Invariants

- event/effective time ≠ knowledge time ≠ derived comparison time;
- evidence available at source ≠ framework knew it;
- later intent registration does not backdate contemporaneous planning knowledge;
- later activation correction does not rewrite historical control/action records;
- `not known by K` and `did not occur` remain different propositions;
- actual historical Deployment/Change state ≠ replay-derived comparison result.

## Handoff

Group 09 later composes these semantics with Lineage, execution, Investigation, Impact and active controls.