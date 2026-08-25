# Phase 007 Group 04 — Execution Reconstruction, Dependency Sequence & Version Use

**Status:** Next — not started

## Goal

Refine how the framework reconstructs actual execution/dependency sequence and version use from incomplete, late, duplicated or conflicting operational evidence.

## Accepted input from Groups 01–03

Group 04 consumes:

- OPS-001–OPS-009 effective/historical Lineage, semantic relevance and bounded completeness;
- OPS-010–OPS-020 exact intent/deployment/change identity, activation slices, active implementation-state intervals and non-rewriting rollback semantics;
- OPS-021–OPS-033 prospective scenario topology, candidate/review findings and the explicit boundary that proposal/review state is not runtime evidence.

In particular, Group 04 must not use a proposed version, planned dependency, planned-added path, path-loss scenario, prospective compatibility result, review approval or canary expectation as proof that an execution actually used that state.

## Primary questions

- Which events/evidence are needed to reconstruct qualifying execution opportunities, starts, completions, retries/restarts, outputs and dependency sequence?
- How should intended schedule/dependency order differ from actual observed execution order?
- What evidence supports identifying the specific active implementation/input/output versions used by a run?
- How should deployment active-state intervals constrain but not automatically prove run-specific version use?
- How should late, duplicate or common-derived telemetry be normalized without creating independent corroboration?
- What bounded coverage is required to say a run/output did not occur?
- How should missing telemetry, ambiguous run identity, partial execution evidence or unknown consumed versions remain explicit?
- How should rollback/activation changes during a long-running execution affect version-use reconstruction?

## Required boundaries

Preserve:

- intended schedule ≠ actual execution;
- prospective scenario topology ≠ actual dependency sequence;
- Lineage dependency ≠ proof one run consumed another run's output;
- Deployment active-at-time ≠ specific run version use unless the runtime binding is sufficiently evidenced;
- proposed/reviewed version ≠ executed version;
- job success ≠ healthy/fresh output;
- run timing ≠ affected-version encounter;
- retry/restart ≠ original execution rewrite;
- missing telemetry ≠ no run/output;
- duplicated/common-derived telemetry ≠ independent corroboration;
- reconstructed execution ≠ causality.

## Handoff to Group 05

Group 05 should use the reconstructed sequence/version evidence as Investigation evidence for localization and competing hypotheses. It must not promote sequence, deployment proximity or first post-change execution directly into a Causal Claim.

## Deferred

Do not select event-store schema, Databricks event sources, scheduler APIs, telemetry normalization implementation, persistent replay architecture or concrete source support in this group.
