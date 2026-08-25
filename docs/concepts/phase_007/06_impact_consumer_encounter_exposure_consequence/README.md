# Phase 007 Group 06 — Impact, Consumer Encounter, Exposure & Consequence

**Status:** Next — not started

## Goal

Refine the path from prospective downstream candidate to actual consumer/version encounter, observed downstream effect and technical/analytical/business consequence without collapsing those layers into one Impact status.

## Accepted input from Groups 01–05

Group 06 consumes:

- OPS-001–OPS-009 effective/historical Lineage, semantic consumption/publication paths and bounded path completeness;
- OPS-010–OPS-020 exact Change/Deployment/realization state where affected/suspect versions are known;
- OPS-021–OPS-033 prospective candidate/reachability and planned-path context without treating it as actual Impact;
- OPS-034–OPS-049 run-specific input/output/version evidence, multi-input version sets and bounded negative-consumption evidence;
- OPS-050–OPS-066 Investigation question/localization context and explicit Causal Claim handoff/epistemic state.

Investigation and causality are context, not encounter truth. In particular:

- a localized upstream deviation does not prove a consumer encountered it;
- a supported or confirmed upstream Causal Claim does not prove every reachable consumer was exposed;
- first downstream consumer effect from OPS-054 is an evidenced effect position, not proof of exposure mechanism or business consequence by itself;
- prospective blast-radius membership does not become exposure after an incident merely because the candidate later has a problem.

## Primary questions

- What evidence establishes that a consumer encountered a particular producer state/version/window?
- How should no opportunity, no encounter, safe-version encounter, suspect-version encounter, unknown-version encounter and unavailable evidence remain distinct?
- What coverage is required for `not exposed`?
- How should observed downstream effect differ from exposure and from consequence?
- How should consumer classes with different refresh/query/cache behavior affect encounter evidence?
- How should stale safe-version use differ from healthy/current delivery?
- How should execution/output/version reconstruction combine with publication/consumption Lineage without letting timing manufacture encounter?
- How should investigation localization and causal claims inform, but not replace, downstream effect/consequence attribution?
- When does causal attribution between upstream state and downstream effect/consequence require a separate explicit Causal Claim?

## Group 06 entry scenarios

Group 06 should explicitly test:

- reachable report never refreshed after suspect output;
- report refreshed but consumed a safe prior version;
- report refreshed with unknown producer version;
- query consumer definitely read suspect version;
- cache served stale safe version while source was degraded;
- consumer effect observed but encounter evidence missing;
- encounter established but no downstream degradation observed;
- technical effect with no business consequence evidence;
- business decision consequence with provenance-bearing evidence;
- supported/confirmed upstream cause with one unexposed reachable consumer;
- `not exposed` under complete version/path coverage versus telemetry outage;
- multiple alternate publication/consumption paths;
- restricted consumer/path evidence;
- first consumer effect differing from first actual encounter.

## Required boundaries

Preserve:

- candidate/reachable ≠ exposed;
- localized upstream deviation ≠ exposed consumer;
- confirmed upstream cause ≠ consumer exposure;
- exposed ≠ downstream effect;
- downstream effect ≠ technical/analytical/business consequence;
- consequence ≠ causal attribution;
- `not exposed` ≠ missing telemetry;
- `not exposed to suspect V` ≠ fresh/current/healthy;
- refresh/run timing ≠ consumed-version proof;
- Criticality/Classification ≠ actual Impact;
- prospective blast radius ≠ actual Impact;
- Investigation closure/localization ≠ downstream Impact truth.

## Handoff to Group 07

Group 07 should use these encounter/path semantics to evaluate whether an active Propagation Safeguard was materially positioned and enforced to protect a relevant path, and whether any prevented-exposure claim has adequate opportunity and alternate-path coverage.

## Deferred

Do not select consumer-instrumentation mechanisms, query-log ingestion, cache telemetry, downstream-report integrations, Impact UI, exposure algorithms or technical architecture in this group.
