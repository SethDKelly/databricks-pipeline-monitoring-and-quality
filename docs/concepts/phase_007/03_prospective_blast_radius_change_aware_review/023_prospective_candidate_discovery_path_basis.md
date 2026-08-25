# OPS-023 — Prospective Candidate Discovery & Path Basis

**Status:** Accepted — Phase 007 Group 03

## Purpose

Identify which downstream subjects plausibly require attention if a proposed change is realized while preserving the exact path basis and avoiding actual-Impact language.

## Contract

Impact `identifyCandidates` may consume the OPS-022 prospective scenario topology and record candidates with a basis such as:

- **effective-path candidate** — reachable/relevant through currently effective Lineage;
- **planned-added-path candidate** — reachable only if a planned relationship becomes effective;
- **path-loss/change candidate** — currently dependent through a relationship the proposal would remove or materially alter;
- **indeterminate candidate** — topology/relevance evidence is insufficient, conflicting or restricted.

Every candidate retains the relevant relationship path/delta, scope, review cut and completeness limitations.

## Candidate conclusion vocabulary

For one bounded candidate proposition, preserve at least:

- candidate;
- not a candidate only where sufficient topology/relevance coverage supports exclusion;
- indeterminate/insufficient;
- conflicting;
- unavailable.

Restricted identity/path detail is a disclosure condition, not absence.

## Invariants

- candidate ≠ exposure;
- candidate ≠ predicted effect;
- candidate ≠ business consequence;
- candidate ≠ cause;
- path length/directness does not create probability or severity;
- planned-only candidate remains planned-only until realization evidence establishes Lineage.

## Handoff

OPS-024 narrows candidate relevance using field/key/population/interface/consumer/version semantics.