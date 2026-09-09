# OPS-041 — Execution ↔ Implementation-State Binding & Deployment Context

**Status:** Accepted — Phase 007 Group 04

## Purpose

Refine SYN-009 so Deployment active-state history constrains run context without automatically becoming run-specific implementation proof.

## Contract

A run-specific implementation-state proposition may bind separate facets such as:

- source/build revision;
- job/transformation definition/version;
- configuration/feature state;
- schema/interface version;
- target/environment;
- other execution-material implementation facet.

Deployment `active at start` or `active during execution` is applicable context. It establishes run-specific use only when the runtime/deployment semantics and evidence are sufficient for that facet.

If a run was queued/launched under one state and began after another became active, or if the runtime may snapshot configuration at different boundaries, active-state timing alone remains insufficient.

## Result discipline

Each material facet can be established, indeterminate, conflicting or unavailable independently. Do not manufacture one universal `run version` token when the actual implementation state is composite.

## Invariants

- Deployment active-at-time ≠ run-specific version use by default;
- repository commit ≠ run implementation identity absent evidence;
- established code revision ≠ established configuration/schema facet;
- one known facet does not fill missing facets;
- run implementation binding ≠ intended effect/health/cause.