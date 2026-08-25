# Phase 007 Group 04 — Execution Reconstruction, Dependency Sequence & Version Use

**Status:** Planned — not started

## Goal

Refine how the framework reconstructs actual execution/dependency sequence and version use from incomplete, late, duplicated or conflicting operational evidence.

## Primary questions

- Which events are needed to reconstruct qualifying execution opportunities, starts, completions, retries/restarts, outputs and dependency sequence?
- How should intended schedule/dependency order differ from actual observed execution order?
- What evidence supports identifying the specific input/output versions used by a run?
- How should late, duplicate or common-derived telemetry be normalized without creating independent corroboration?
- What bounded coverage is required to say a run/output did not occur?
- How should missing telemetry, ambiguous run identity or unknown consumed versions remain explicit?

## Required boundaries

Preserve:

- intended schedule ≠ actual execution;
- Lineage dependency ≠ proof one run consumed another run's output;
- job success ≠ healthy/fresh output;
- run timing ≠ affected-version encounter;
- retry/restart ≠ original execution rewrite;
- missing telemetry ≠ no run/output;
- duplicated telemetry ≠ independent corroboration;
- reconstructed execution ≠ causality.

## Handoff to Group 05

Group 05 should use the reconstructed sequence as Investigation evidence for localization and competing hypotheses. It must not promote sequence or temporal proximity directly into a Causal Claim.

## Deferred

Do not select event-store schema, Databricks event sources, scheduler APIs, telemetry normalization implementation or persistent replay architecture in this group.
