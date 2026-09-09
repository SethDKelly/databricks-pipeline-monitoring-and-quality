# OPS-088 — Protection Surface Placement & Semantic Boundary

**Status:** Accepted — Phase 007 Group 07

## Purpose

Represent what propagation boundary is being controlled without selecting an implementation mechanism.

## Contract

A protection surface may correspond functionally to:

- a produced output/version;
- publication/serving of a state;
- representation of a state as current for a cycle;
- a consumer/interface/consumption path;
- a downstream refresh or advancement opportunity;
- a population, cohort, region or bounded consumer set.

Placement is justified against the relevant Lineage and Impact encounter paths. `Upstream-most`, `closest to source`, `closest to consumer`, or `fewest controls` are not universal placement rules.

## Invariants

- placement candidate ≠ activated control.
- one protected surface ≠ all downstream surfaces.
- source-level protection is not automatically safest or least disruptive.
- planned topology is review context, not an active protection surface.
- Phase 007 does not select tables, aliases, ACLs, routing, storage or quarantine technology.
