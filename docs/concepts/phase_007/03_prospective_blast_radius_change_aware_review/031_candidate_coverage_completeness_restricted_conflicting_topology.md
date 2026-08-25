# OPS-031 — Candidate Coverage, Completeness & Restricted/Conflicting Topology

**Status:** Accepted — Phase 007 Group 03

## Purpose

Keep prospective blast-radius conclusions honest when Lineage, planned topology, identity or authorization coverage is incomplete.

## Contract

A prospective profile should state the bounded candidate universe and material coverage dimensions, including where applicable:

- topology time/knowledge cut;
- permitted relationship families/direction/depth;
- field/key/population/interface scope;
- effective versus planned-only path coverage;
- known alternate paths;
- restricted/opaque nodes/relationships;
- identity ambiguity;
- conflicting relationship assertions;
- Monitoring Scope limitations.

The profile can return a known candidate set while explicitly saying the set is non-exhaustive.

## Negative conclusions

Statements such as `no downstream candidates`, `consumer X is not in blast radius`, or `no alternate path exists` require sufficient bounded opportunity/coverage under REF-001–REF-005 and OPS-008.

Failure to find a path is not sufficient by itself.

## Invariants

- incomplete topology ≠ no blast radius;
- restricted path ≠ absent path;
- conflicting topology ≠ choose convenient path;
- out-of-scope consumer ≠ nonexistent consumer;
- candidate count ≠ completeness;
- no universal topology/blast-radius completeness score is accepted.

## Handoff

OPS-032 preserves prospective/realized separation during phased rollout and historical review.