# Phase 007 Group 06 — Impact, Consumer Encounter, Exposure & Consequence

**Status:** Planned — not started

## Goal

Refine the path from prospective downstream candidate to actual consumer/version encounter, observed downstream effect and technical/analytical/business consequence without collapsing those layers into one Impact status.

## Primary questions

- What evidence establishes that a consumer encountered a particular producer state/version/window?
- How should no opportunity, no encounter, safe-version encounter, suspect-version encounter, unknown-version encounter and unavailable evidence remain distinct?
- What coverage is required for `not exposed`?
- How should observed downstream effect differ from exposure and from consequence?
- How should consumer classes with different refresh/query/cache behavior affect encounter evidence?
- How should stale safe-version use differ from healthy/current delivery?
- When does causal attribution between upstream state and downstream effect/consequence require an explicit Causal Claim?

## Required boundaries

Preserve:

- candidate/reachable ≠ exposed;
- exposed ≠ downstream effect;
- downstream effect ≠ technical/analytical/business consequence;
- consequence ≠ causal attribution;
- `not exposed` ≠ missing telemetry;
- `not exposed to suspect V` ≠ fresh/current/healthy;
- refresh/run timing ≠ consumed-version proof;
- Criticality/Classification ≠ actual Impact;
- prospective blast radius ≠ actual Impact.

## Handoff to Group 07

Group 07 should use these encounter/path semantics to evaluate whether an active Propagation Safeguard was materially positioned and enforced to protect a relevant path, and whether any prevented-exposure claim has adequate opportunity and alternate-path coverage.

## Deferred

Do not select consumer-instrumentation mechanisms, query-log ingestion, cache telemetry, downstream-report integrations or Impact UI in this group.
