# Phase 007 Agent Handoff

Applies to work under `docs/concepts/phase_007/` and complements the repository root `AGENTS.md` without replacing accepted cross-phase rules.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 006 is complete with HLTH-001–HLTH-066 final.
- Phase 007 grouping is accepted.
- **Phase 007 Group 01 is complete with OPS-001–OPS-009 accepted; L01-01–L01-18 pass.**
- **Group 02 — Change Intent, Deployment Realization & Realized Change is next.**
- Accepted concept count remains 24; SYN-001–SYN-035, REF-001–REF-030, AUTH-001–AUTH-053 and HLTH-001–HLTH-066 remain unchanged.

## Accepted Group 01 Lineage rules

Preserve:

- a Lineage relationship is a bounded proposition, not a generic edge;
- minimum families are `data_derivation`, `production`, `operational_dependency`, `publication`, `consumption_path`;
- repository/deployment/control/authority/causal facts do not become Lineage merely because they are graph-representable;
- source/target field/key/population/consumer/version scope can materially narrow a relationship;
- asset reachability ≠ field/population relevance;
- planned topology ≠ effective Lineage ≠ specific execution/consumer encounter;
- event/effective time ≠ framework knowledge/correction time;
- generic edge `confidence` is superseded by REF-001–REF-005 applicability/coverage/conflict/sufficiency semantics;
- established/absent/unknown/conflicting/unavailable are bounded relationship-existence results;
- `absent` requires opportunity-to-observe plus sufficient coverage;
- runtime/catalog/code/human/platform sources have no hidden universal precedence;
- Assertion Authority ≠ evidence sufficiency;
- traversal relevance is question-bound and can be relevant/not relevant/indeterminate;
- multi-hop relevance requires semantic scope composition;
- Lineage need not be a DAG; traversal must remain bounded/cycle-safe;
- topology completeness is bounded and authorization-aware, never a universal score;
- restricted/opaque path ≠ absent path;
- relationship transition ≠ Change Intent ≠ Deployment ≠ Change ≠ causal attribution.

See [`01_lineage_relationship_taxonomy_historical_topology/README.md`](01_lineage_relationship_taxonomy_historical_topology/README.md).

## Permanent Phase 007 boundaries

Preserve:

- Lineage ≠ causality;
- Lineage relation ≠ metric/status propagation;
- planned topology ≠ active/effective topology ≠ historical topology;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective blast radius ≠ actual Impact;
- intended schedule/dependency ≠ actual execution sequence;
- execution occurrence ≠ specific consumed-version proof unless evidenced;
- missing telemetry ≠ no event;
- first-deviation localization ≠ root cause;
- Investigation ≠ Causal Claim truth;
- candidate/reachable ≠ exposed ≠ effect ≠ consequence ≠ causal attribution;
- `not exposed` requires adequate opportunity/path coverage;
- Safeguard proposal/configuration/active state ≠ enforcement ≠ prevented exposure;
- safeguard release ≠ healthy/fresh output;
- Phase 006 health suitability ≠ readiness ≠ gate decision ≠ enforcement ≠ execution;
- gate HOLD ≠ execution failure;
- gate ADMIT ≠ execution occurrence;
- override ≠ prerequisite ready;
- configured fallback ≠ actual fallback application;
- Execution Gate ≠ Propagation Safeguard;
- control-induced delay/staleness/non-delivery remains observable/assessable and is not automatically defect/cause;
- historical operational replay uses event/effective time plus knowledge cut and remains non-rewriting.

## Group 02 entry contract

Group 02 consumes OPS-001–OPS-009 and must refine how intended modifications, Deployment attempts/activation and realized Change coordinate.

It should explicitly test:

- one Change Intent realized across several Deployments;
- one Deployment containing several independent intents;
- partial realization;
- mismatched realization;
- unregistered/unplanned Change;
- activation without intended effect;
- rollback/reversion/supersession;
- repository revision ≠ deployed runtime identity absent evidence;
- historical active version/effective interval reconstruction;
- topology transition evidence under OPS-004/OPS-005.

Do not let Group 02 make Change Intent, Deployment and Change one lifecycle object or let deployment success manufacture realized state.

## Architecture boundary

Do not select graph database, graph query language, Lineage ingestion source, event store, CI/CD event integration, deployment fingerprinting mechanism, scheduler/orchestrator, safeguard/quarantine mechanism, gate implementation, queue/event bus, cache/streaming topology, RCA algorithm, persistence schema, source integration or concrete latency/timeout SLA in Phase 007 functional refinement.
