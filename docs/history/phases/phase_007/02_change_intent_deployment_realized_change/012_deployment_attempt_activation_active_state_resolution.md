# OPS-012 — Deployment Attempt, Activation & Active-State Resolution

**Status:** Accepted — Phase 007 Group 02

## Purpose

Make deployment history usable without collapsing workflow outcome, target activation, active implementation state and intended downstream effect into one `deployed` status.

## Contract

Deployment preserves separate propositions for:

1. **attempt** — an identified deployment activity targeted a bounded environment/subject with an intended payload/reference set;
2. **attempt outcome** — the deployment mechanism reported its own outcome, where known;
3. **activation** — evidence establishes that an implementation-state facet actually became effective for the bounded target;
4. **active-state interval** — the facet remained effective over an evidence-supported interval until superseded/deactivated/corrected;
5. **active-state resolution** — a historical/current query resolves the then-effective facet set with explicit uncertainty/conflict/availability limitations.

## Activation binding

Activation is target/facet/context specific. It binds:

- deployment identity;
- affected target Entity Identity/context;
- implementation-state facet/reference under OPS-011;
- supported effective/activation time or interval;
- provenance/evidence basis;
- framework knowledge time and later correction where material.

A single deployment attempt can have different activation outcomes across environments, regions, cohorts, jobs or configuration facets.

## Resolution vocabulary

For a bounded active-state proposition, preserve as applicable:

- `established`;
- `not established` only when sufficient negative evidence exists;
- `unknown`;
- `conflicting`;
- `unavailable`.

`No activation evidence found` is not automatically `not established`.

## Invariants

- attempt ≠ attempt success ≠ activation;
- activation ≠ intended effect realization;
- activation ≠ health/suitability/readiness;
- activation ≠ actual execution;
- current active state is not projected backward;
- one target's activation does not globally activate every target;
- an authoritative deployment declaration cannot manufacture missing empirical activation evidence;
- active-state resolution may be composite rather than one version.

## Handoff

OPS-013 relates exact intent components to deployment activity. OPS-014 separately describes evidence-established realized Change.