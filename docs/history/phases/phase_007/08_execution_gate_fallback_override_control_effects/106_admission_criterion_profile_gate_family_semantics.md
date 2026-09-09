# OPS-106 — Admission Criterion Profile & Gate-Family Semantics

**Status:** Accepted — Phase 007 Group 08

## Purpose

Define what exact question a Gate evaluates without inventing one universal readiness formula or implementation-oriented gate taxonomy.

## Contract

The exact criterion/profile is authoritative. It may explicitly compose accepted predicates such as:

- qualifying prerequisite execution completion;
- qualifying output existence;
- current-cycle/currentness;
- required version/state identity;
- freshness relative to a named requirement;
- publication/availability through a required boundary;
- structural/schema/quality/health condition only when explicitly control-eligible and suitable for this use;
- another accepted bounded prerequisite.

Descriptive labels such as dependency, current-cycle, version-specific, freshness-conditioned or quality-conditioned Gate may aid review, but do not create hidden behavior.

## Invariants

- successful upstream execution ≠ universal readiness;
- Gate label/class ≠ criterion logic;
- Phase 006 health evidence participates only when the exact criterion requires it;
- no universal default predicate set, risk score or Gate class is accepted;
- criterion/profile changes are versioned and non-rewriting.