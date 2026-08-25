# OPS-020 — Change/Deployment Cross-Concept Ownership & Group 03 Handoff

**Status:** Accepted — Phase 007 Group 02

## Purpose

Close Group 02 with explicit ownership boundaries so prospective blast-radius review can use planned scope without confusing it with active topology, execution, actual Impact or cause.

## Ownership map

- **Change Intent** owns registered planned modification, intended target/facet, planned activation context and anticipated effects.
- **Deployment** owns deployment attempts, target/payload provenance, activation/effective implementation-state intervals, supersession and rollback deployment history.
- **Change** owns evidence-established realized differences/transitions.
- **Lineage** owns effective relationship/topology state under OPS-001–OPS-009; a realized topology Change can be derived from Lineage history without moving relationship truth into Change.
- **Execution History** owns actual execution instances/lifecycle; active deployment at a time does not prove a particular run used that state when version-use evidence is missing.
- **Observation/Assessment/Baseline/Expectation** retain Phase 006 evidence/health/reference/normative truth.
- **Investigation/Causal Claim** own inquiry and causality; intent/deployment/change chronology is evidence, not cause.
- **Impact** owns actual encounter/effect/consequence; prospective scope is not exposure.
- **Execution Gate/Propagation Safeguard** own active-control truth; deployment or change does not silently enable either.

## Topology transition handoff

A Change Intent may propose topology. Deployment may activate implementation intended to produce topology. Effective Lineage changes only when OPS-004/OPS-005 evidence establishes the relationship transition. Change may then describe that realized topology transition from Lineage evidence.

Preserve:

**planned topology → deployment context → effective Lineage relationship → realized topology Change description**

without allowing any arrow to manufacture the next proposition.

## Group 03 input

Prospective blast-radius review receives:

- exact Change Intent revision/components;
- proposed target/facet/topology/semantic scope;
- planned activation context;
- anticipated effects with their declared status;
- current/effective Lineage plus separately marked planned-only topology;
- known deployment/rollout context if review occurs after some slices have started;
- evidence/authority/authorization/completeness limitations.

Group 03 must continue to preserve:

- proposed scope ≠ realized state;
- candidate/reachable ≠ exposure/Impact;
- predicted review need ≠ defect;
- intended effect ≠ Expectation unless independently established;
- deployment activation ≠ downstream effect;
- intent conformance ≠ health/cause.

## Architecture boundary

Group 02 selects no Git diff engine, build fingerprint, deployment attestation, CI/CD event model, CDC mechanism, version store, runtime instrumentation or persistence architecture.