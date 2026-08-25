# OPS-032 — Partial Rollout, Mixed Prospective/Realized State & Historical Review

**Status:** Accepted — Phase 007 Group 03

## Purpose

Support change review when some rollout slices are already active while others remain prospective, and preserve what the review actually knew over time.

## Mixed rollout semantics

Resolve each environment/region/cohort/population/interface slice under OPS-016:

- not activated / still prospective;
- activated with realized-state evidence;
- activation or realization indeterminate/conflicting/unavailable.

Prospective review of remaining slices may use newly observed evidence from active slices as **additional evidence/context**, but must not project that outcome onto future slices as fact.

A canary that exhibits an incompatibility can legitimately increase review attention for the remaining rollout. It does not prove every future slice will encounter the same effect.

## Historical review

Retain separately:

- actual prospective review/profile produced at the historical knowledge cut;
- reconstructed `as-known-then` review when no retained artifact exists;
- current retrospective recomputation using later Lineage/semantic/consumer evidence.

Late discovery of a downstream consumer can expand today's retrospective blast radius without rewriting the candidate set actually available to the pre-deployment reviewer.

## Overlapping intents

Analyze exact intent components separately and compose only material interactions explicitly. Do not merge overlapping intents because they share a deployment or candidate. No automatic Cartesian-product scenario expansion is required.

## Invariants

- active slice ≠ global realization;
- observed canary outcome ≠ future-slice outcome;
- later topology knowledge ≠ knowledge available during original review;
- retained historical review ≠ reconstructed review;
- overlapping intent ≠ causal or semantic equivalence.

## Handoff

OPS-033 closes Group 03 ownership and hands actual runtime/version reconstruction to Group 04.