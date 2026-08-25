# OPS-018 — Rollback, Reversion, Supersession & Restoration Semantics

**Status:** Accepted — Phase 007 Group 02

## Purpose

Keep recovery/change-history language precise so returning toward an earlier implementation state does not erase the intervening deployment or falsely imply every downstream effect was undone.

## Vocabulary

### Supersession / deactivation
An active Deployment/implementation-state interval ends because another state becomes applicable or the state is explicitly deactivated. This says nothing about why the replacement occurred.

### Rollback
A deployment/change action is intended to restore a prior implementation/configuration state or an equivalent prior operating context.

Rollback is action/intent context; whether restoration actually occurred requires activation/Change evidence.

### Reversion
Evidence establishes that a selected realized facet moved back toward or became equivalent to a prior known state.

### Restoration
The bounded proposition that the relevant state is sufficiently equivalent to the prior state for the stated use/context. Equality of a revision label alone does not prove restoration of configuration, data, topology, schema, references or downstream state.

### Roll-forward/fix-forward
A new state supersedes the problematic/current state without claiming identity/equivalence to the earlier state.

## Historical behavior

If R2 is active from 10:00–11:00 and R1-equivalent becomes active at 11:00, history retains both intervals. The later state has a new activation interval even if the implementation identity equals an earlier revision.

## Non-transitive downstream restoration

Rolling back code/configuration does not automatically revert:

- data already written/mutated;
- schema migrations;
- materialized outputs;
- Lineage/topology already changed;
- consumer exposure;
- external side effects;
- health/Assessment history.

Each owning concept requires its own evidence.

## Invariants

- rollback request/attempt ≠ rollback activation;
- rollback activation ≠ restored downstream state;
- reactivated prior revision ≠ erased intervening history;
- same code revision ≠ same composite operating state unless other facets match;
- restoration ≠ healthy/acceptable;
- rollback/reversion ≠ causal proof that the superseded state caused an incident;
- intent withdrawal ≠ rollback.

## Handoff

OPS-019 preserves rollback/reversion under event/effective time and historical knowledge cuts.