# Phase 007 Agent Handoff

Applies to work under `docs/concepts/phase_007/` and complements the repository root `AGENTS.md` without replacing accepted cross-phase rules.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 006 is complete with HLTH-001–HLTH-066 final.
- Phase 007 grouping is accepted.
- **Group 01 is complete with OPS-001–OPS-009; L01-01–L01-18 pass.**
- **Group 02 is complete with OPS-010–OPS-020; C02-01–C02-24 pass.**
- **Group 03 — Prospective Blast Radius & Change-Aware Review is next.**
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
- generic edge `confidence` is superseded by REF applicability/coverage/conflict/sufficiency semantics;
- `absent` requires opportunity-to-observe plus sufficient coverage;
- runtime/catalog/code/human/platform sources have no hidden universal precedence;
- Assertion Authority ≠ evidence sufficiency;
- traversal relevance is question-bound and can be relevant/not relevant/indeterminate;
- multi-hop relevance requires semantic scope composition;
- Lineage need not be a DAG; traversal must remain bounded/cycle-safe;
- topology completeness is bounded and authorization-aware, never a universal score;
- restricted/opaque path ≠ absent path.

## Accepted Group 02 Change/Deployment rules

Preserve:

- Change Intent, Deployment and Change remain independent truth owners;
- intent-to-realization comparison is derived, not a new concept/state owner;
- historical comparison binds exact intent revision/component/target, not latest intent by convenience;
- source revision/build/config/job/transformation/schema/interface may be separate implementation-state facets;
- no universal deployment/version token is accepted;
- repository commit ≠ deployed runtime identity absent evidence;
- same commit + different config may be different operating state;
- attempt ≠ attempt outcome ≠ activation;
- activation is target/facet/slice specific;
- activation ≠ intended/downstream effect ≠ execution ≠ health ≠ cause;
- intent/deployment association requires provenance-bearing linkage and is many-to-many;
- temporal/name/repository proximity alone does not prove association;
- realized Change binds before/after state, facet/context, transition time and evidence;
- implementation-state Change ≠ automatically downstream data/schema/topology Change;
- realization comparison keeps association, activation, realized-state, conformance and limitations separate;
- `matched`, `partially matched`, `diverged`, `not realized`, `not evidenced`, `indeterminate`, `conflicting`, `unavailable` are bounded comparison results;
- `not evidenced` ≠ `not realized`; negative realization claims require REF coverage;
- no universal percent-realized/confidence score;
- partial/canary/region/cohort rollout ≠ global activation;
- overlapping intents remain distinct and do not establish causal attribution;
- no matching registered intent known ≠ unregistered ≠ outside declared scope ≠ proven unplanned;
- unregistered ≠ unauthorized;
- undeclared anticipated effect ≠ proven humanly unintended effect;
- rollback attempt ≠ rollback activation ≠ downstream restoration;
- reactivated prior revision creates a new interval and does not erase intervening history;
- same code revision ≠ restored composite state when configuration/facets differ;
- code rollback does not automatically restore data/schema/topology/exposure/health;
- effective/event time ≠ framework knowledge time ≠ derived comparison time;
- realized topology transition consumes Lineage truth rather than manufacturing an edge.

See [`02_change_intent_deployment_realized_change/README.md`](02_change_intent_deployment_realized_change/README.md).

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

## Group 03 entry contract

Group 03 consumes OPS-001–OPS-020 and must refine prospective blast-radius/change-aware review before activation without turning candidate reachability into Impact.

It should explicitly test:

- field/key/population/consumer-scoped candidate reachability;
- proposed new/removal/change relationships that remain planned-only topology;
- consumer-specific schema/interface compatibility review;
- metric/profile/Baseline/reconciliation review triggered by proposed structural/semantic changes;
- readiness/control-use review triggers without automatically enabling control;
- incomplete/conflicting/restricted topology limiting candidate conclusions;
- phased rollout where some slices are active and others remain prospective;
- overlapping intents and competing proposed scopes;
- registered intent with missing anticipated-effect detail;
- no matching registered intent not becoming zero prospective risk;
- criticality/priority context remaining separate from actual Impact/evidence strength.

Do not let Group 03 create a universal risk score, predicted-defect truth, automatic CI gate, actual exposure or causal claim from proposed topology/change.

## Architecture boundary

Do not select graph database, graph query language, Lineage ingestion source, event store, CI/CD event integration, deployment fingerprinting mechanism, static-analysis engine, change-risk scoring algorithm, scheduler/orchestrator, safeguard/quarantine mechanism, gate implementation, queue/event bus, cache/streaming topology, RCA algorithm, persistence schema, source integration or concrete latency/timeout SLA in Phase 007 functional refinement.
