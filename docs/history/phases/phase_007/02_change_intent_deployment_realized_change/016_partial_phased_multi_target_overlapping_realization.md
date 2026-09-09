# OPS-016 — Partial, Phased, Multi-Target & Overlapping Realization

**Status:** Accepted — Phase 007 Group 02

## Purpose

Prevent one target, cohort, deployment or matched effect from being generalized into `the change is live everywhere` or `the intent is fully realized`.

## Realization slice

Where material, realization is evaluated for a bounded slice such as:

- environment/tenant/region;
- job/logical process;
- interface/consumer;
- population/cohort/partition;
- implementation facet;
- schema/transformation version;
- rollout interval or phase.

A realization slice is comparison context, not necessarily a separately persisted entity.

## Partial/phased behavior

- one intent can be active for one slice and pending/unknown/diverged for another;
- one deployment can activate only part of its intended payload;
- a canary/region rollout does not globally activate production;
- later phases create additional activation/Change intervals rather than backdating the first phase;
- a global `fully realized` shorthand is valid only if explicit composition rules and sufficient required-slice coverage justify it.

No percentage completion is inferred from target counts unless the intended proposition itself defines a meaningful weighted/percentage rollout measure.

## Overlapping intents

Several Change Intents can overlap in target/time/facet. A realized Change may be compatible with more than one intent.

Comparison may determine that:

- each intent had associated/active implementation components;
- one realized Change conforms to multiple declared expectations/effects;
- evidence cannot distinguish which implementation produced an observed downstream effect.

That ambiguity does not merge the intents and does not create causal attribution.

## Bundled Deployment

A Deployment that carries multiple intents preserves per-intent/per-component linkage and comparison. One failed or divergent component does not rewrite another valid component.

## Invariants

- partial activation ≠ global activation;
- one successful slice ≠ full realization;
- equal target count ≠ equal rollout significance;
- overlap compatibility ≠ causal attribution;
- bundled release outcome ≠ one aggregate intent outcome;
- one unresolved slice does not erase established state in another slice.

## Handoff

OPS-017 defines terminology for realized state that has no matching registered intent or falls outside declared intent scope.