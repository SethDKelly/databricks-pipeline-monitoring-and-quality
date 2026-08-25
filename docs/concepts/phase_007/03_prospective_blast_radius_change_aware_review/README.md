# Phase 007 Group 03 — Prospective Blast Radius & Change-Aware Review

**Status:** Next — not started

## Goal

Refine prospective downstream reasoning from a proposed Change using then-relevant Lineage without confusing candidate reachability or review need with actual exposure, Impact or causality.

## Accepted input from Groups 01–02

Group 03 consumes:

- OPS-001–OPS-009 bounded Lineage relationship taxonomy, semantic scope, historical/effective topology, relevance and completeness rules;
- OPS-010 exact Change Intent revision/component/target binding;
- OPS-011 implementation-state references without assuming repository commit equals runtime identity;
- OPS-012–OPS-013 Deployment attempt/activation and intent-association separation;
- OPS-015–OPS-017 partial realization and careful registered/unregistered/unplanned semantics when review occurs during an active rollout;
- OPS-020 ownership boundaries and prospective handoff.

Prospective review normally begins from the exact registered intent/proposed state. If some rollout slices are already active, known Deployment/Change state may constrain which remaining slices are still prospective, but actual realized state must never be projected onto slices where it is not evidenced.

## Primary questions

- Which downstream entities/consumers are plausible candidates under the proposed change and the topology expected to apply?
- How should field/key/population/consumer relevance narrow asset-level reachability?
- Which Phase 006 surfaces should be reviewed prospectively: schema compatibility, metric/profile applicability, Baseline regime, reconciliation definitions, readiness criteria or control-use conditions?
- How should incomplete/conflicting Lineage limit blast-radius claims?
- How should planned compatibility/risk checks be represented when deployment or realization has not occurred?
- How should phased/partial rollout affect the prospective candidate set without turning active-slice facts into global state?
- How should prospective criticality/priority differ from evidence that an actual downstream consequence occurred?

## Required boundaries

Preserve:

- prospective candidate/reachability ≠ actual exposure;
- planned compatibility result ≠ realized compatibility result;
- review trigger ≠ predicted defect;
- criticality ≠ Impact;
- Change Intent ≠ realized Change;
- deployment activation in one slice ≠ realization in every slice;
- prospective blast radius ≠ retrospective root cause;
- Lineage reachability ≠ causal transmission;
- planned downstream effect ≠ actual downstream effect;
- no matching registered intent ≠ no possible change risk.

## Handoff to Group 04

Group 04 should consume the accepted topology/change semantics to reconstruct what actually ran and which versions were actually involved. Prospective expectations must not substitute for runtime evidence.

## Deferred

Do not select dependency graph algorithms, static-analysis engines, CI gates, change-risk scoring, graph storage or UI visualization in this group.
