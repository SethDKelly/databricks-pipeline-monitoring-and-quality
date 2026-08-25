# Phase 007 Group 03 — Prospective Blast Radius & Change-Aware Review

**Status:** Planned — not started

## Goal

Refine prospective downstream reasoning from a proposed Change using then-relevant Lineage without confusing candidate reachability or review need with actual exposure, Impact or causality.

## Primary questions

- Which downstream entities/consumers are plausible candidates under the proposed change and the topology expected to apply?
- How should field/key/population/consumer relevance narrow asset-level reachability?
- Which Phase 006 surfaces should be reviewed prospectively: schema compatibility, metric/profile applicability, Baseline regime, reconciliation definitions, readiness criteria or control-use conditions?
- How should incomplete/conflicting Lineage limit blast-radius claims?
- How should planned compatibility/risk checks be represented when deployment or realization has not occurred?
- How should prospective criticality/priority differ from evidence that an actual downstream consequence occurred?

## Required boundaries

Preserve:

- prospective candidate/reachability ≠ actual exposure;
- planned compatibility result ≠ realized compatibility result;
- review trigger ≠ predicted defect;
- criticality ≠ Impact;
- Change Intent ≠ realized Change;
- prospective blast radius ≠ retrospective root cause;
- Lineage reachability ≠ causal transmission;
- planned downstream effect ≠ actual downstream effect.

## Handoff to Group 04

Group 04 should consume the accepted topology/change semantics to reconstruct what actually ran and which versions were actually involved. Prospective expectations must not substitute for runtime evidence.

## Deferred

Do not select dependency graph algorithms, static-analysis engines, CI gates, change-risk scoring, graph storage or UI visualization in this group.
