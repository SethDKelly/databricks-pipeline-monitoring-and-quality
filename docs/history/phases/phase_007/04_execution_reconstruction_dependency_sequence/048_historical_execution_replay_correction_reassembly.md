# OPS-048 — Historical Execution Replay, Correction & Reassembly

**Status:** Accepted — Phase 007 Group 04

## Purpose

Make execution reconstruction bitemporal and non-rewriting as late events, corrected identities and improved run/version associations arrive.

## Contract

Historical execution reasoning distinguishes:

- event/effective time of execution/lifecycle/output/use;
- source availability/production time where known;
- framework knowledge time;
- reconstruction/evaluation time;
- correction/supersession time.

An `as-known-at K` reconstruction may legitimately show an execution as partial/unknown even when later evidence completes it. A current retrospective reconstruction may use later evidence but must not claim the framework knew it at K.

## Reassembly/correction

Late evidence may:

- add missing lifecycle states;
- resolve duplicate/conflicting events;
- associate or disassociate child tasks;
- alter which run qualifies as first/last around a transition;
- establish a previously unknown input/output/implementation version;
- correct an event time or identity.

Corrections preserve prior as-known reconstruction/results where historically material.

## Invariants

- late evidence ≠ earlier knowledge;
- corrected run identity ≠ historical erasure;
- current assembly ≠ necessarily retained historical assembly;
- retrospective complete sequence ≠ contemporaneously complete sequence;
- current code/deployment/topology is never projected backward absent historical evidence.