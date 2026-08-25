# OPS-073 — Cache, Replica, Snapshot & Stale Safe-State Semantics

**Status:** Accepted — Phase 007 Group 06

## Purpose

Represent consumers that read copied/lagging/materialized state without equating staleness with suspect-state exposure.

## Contract

For cache/replica/snapshot/materialized consumers, preserve:

- state/version actually served or read where known;
- copy/refresh/revalidation relationship and effective time;
- whether the copied state is the affected/suspect state, a safe prior state, another state or unknown;
- freshness/currentness Assessment separately from exposure.

A consumer can be **not exposed to suspect V** because it continued serving safe V-1 while simultaneously being stale, late or non-current.

Later cache revalidation may create a later exposure interval without rewriting the earlier safe-state interval.

## Invariants

- stale ≠ affected.
- safe prior state ≠ healthy/current delivery.
- source degradation ≠ cached consumer exposure.
- cache hit/time proximity ≠ exact source-version binding unless evidence supports it.
