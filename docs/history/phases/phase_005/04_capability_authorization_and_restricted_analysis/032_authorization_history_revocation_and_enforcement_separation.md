# AUTH-032 — Authorization History, Revocation, and Enforcement Separation

**Status:** Accepted — Phase 005 Group 04

## Purpose

Preserve authorization as historical decision/entitlement truth while separating it from current requester permission and from evidence that an external system actually enforced the decision or an authorized action succeeded.

## Historical semantics

Authorization state retains effective time, recorded/knowledge time, source/rule provenance, conditions, supersession/revocation/correction, and relevant principal membership history.

A historical question can distinguish:

- what capability applied to actor P at incident time T as known by cutoff K;
- whether that capability was later granted/revoked/corrected;
- what a present requester is currently permitted to inspect about that historical authorization.

## Invariants

- Current authorization does not rewrite historical authorization.
- Historical authorization does not grant current permission.
- A present requester must satisfy current Capability Authorization to inspect historical restricted evidence, even when another actor legitimately could see it then.
- Later raw-data access does not imply an actor could see raw data during an earlier incident.
- Revocation changes future/current permission according to its effective semantics but preserves prior legitimate actions and authorization history.
- Authorization decision ≠ enforcement. `Denied` does not prove an external source system blocked an attempted access; `allowed` does not prove access succeeded.
- Permission to perform a job/gate/safeguard/governance action does not prove the action occurred or succeeded; the owning operational concepts/evidence remain authoritative for action outcome.
- Missing enforcement telemetry remains an evidence limitation, not permission/enforcement proof.
