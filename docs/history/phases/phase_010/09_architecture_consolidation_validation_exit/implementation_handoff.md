# Phase 010 — Implementation / Later MVP Validation Handoff

**Status:** ACCEPTED — Phase 010 exit handoff

The durable roadmap does not assign a numbered Phase 011. It states that **later MVP validation** should translate accepted architecture and timing objectives into implementation phases and measurable MVP acceptance criteria. This handoff therefore avoids inventing a new phase number.

## Stable implementation input

Implementation receives the complete accepted contract stack:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- **ARCH-001–ARCH-500 final**;
- Phase 010 Group 09 consistency/gap/scenario replay and exit review.

No implementation task may redefine those contracts by convenience.

## Recommended implementation sequencing

The sequence below is dependency-oriented, not a mandate for separate repositories/services.

### Implementation Group A — Contract schemas and executable invariants

Build first:

- canonical identifier types;
- temporal coordinate types;
- source/provenance/evidence references;
- status/enumeration vocabularies;
- Monitoring Scope / authority / authorization rule schemas;
- Statement IR / Answer IR schemas;
- control opportunity/decision/enforcement schemas;
- validation library for hard invariants.

Gate:

Representative fixtures must reject invalid shortcuts such as name/time joins, current-state backfill, missing-evidence negatives, unauthorized projection and merged Gate/Safeguard state.

### Implementation Group B — Canonical persistence and lifecycle

Build:

- Delta canonical journals/tables;
- non-rewriting append/correct/supersede patterns;
- payload/object references;
- retention/pin/hold/archive metadata;
- schema migration/version strategy;
- backup/restore baseline.

Gate:

Historical correction, late evidence, archive/restore and provenance identity tests pass without relying on Delta time travel as product replay.

### Implementation Group C — Identity, scope and governance runtime

Build:

- canonical Entity/Principal bindings;
- Monitoring Scope registry/materialization;
- Assertion Authority evaluator;
- Capability Authorization/disclosure evaluator;
- material decision/audit provenance.

Gate:

Rename/recreate, group-membership history, conflicting authority, unknown scope and itemwise disclosure scenarios pass.

### Implementation Group D — Databricks/GitHub acquisition foundation

Build:

- capability discovery inventory;
- source adapter contract;
- acquisition run/attempt/request/page/window/checkpoint records;
- Databricks/GitHub initial adapters;
- reconciliation + optional incremental accelerators;
- normalization/quarantine;
- coverage/integration-health/quota telemetry.

Gate:

Partial pagination, throttle, 401/403, source lag, schema drift and retry/redelivery scenarios never emit false negative facts or advance unsafe checkpoints.

### Implementation Group E — Runtime provenance / health / Lineage

Build:

- deployment/run correlation;
- implementation/input/output manifests;
- measurement definitions/results;
- Expectation/Baseline/Assessment evaluation;
- typed temporal Lineage;
- representative consumer encounter/exposure/effect/consequence records.

Gate:

Foundation MVP scenarios A–H can be represented with explicit unknowns where instrumentation is absent.

### Implementation Group F — Investigation / deterministic reasoning / replay

Build:

- canonical Investigation/lead/Causal Claim lifecycle;
- exact retrieval;
- Delta-backed graph projection/traversal;
- deterministic evidence/coverage/authority rules;
- availability-by-K historical replay;
- Statement IR / Answer IR and deterministic renderer;
- `inspectBasis` internal resolution.

Gate:

Multiple-contributor, unresolved cause, late-evidence correction and historical/as-known scenarios pass. No LLM is required to pass.

### Implementation Group G — Serving / authorization / UI boundary

Build:

- stateless API façade;
- authentication/canonical Principal binding;
- current Capability Authorization/disclosure on requests;
- query/reason/replay/basis endpoints;
- response epistemic envelope;
- safe caching if needed;
- initial business/engineering UI.

Gate:

Cross-user/cache leakage tests, hidden-basis metadata tests and business-vs-engineering explanation consistency pass.

### Implementation Group H — Operations, resilience and economics

Build:

- multidimensional operational telemetry;
- deployment-specific SC-01–SC-05 initial SLOs;
- capacity/backpressure;
- Databricks/GitHub quota budgets;
- cost attribution;
- backup/restore drills;
- documentation/version/capability drift checks.

Gate:

Failure/degradation matrix is executable for representative outages and cost/quota conditions.

### Optional Implementation Group I — Model/search assistance

Only after deterministic paths pass:

- semantic/vector candidate retrieval;
- model question decomposition/lead generation/rendering;
- bounded tool gateway;
- invocation provenance/output validation.

Gate:

Model outage and malicious/unsupported output cannot change domain truth or basic answerability.

### Optional Implementation Group J — Active control

Only for deployments requiring control:

- Gate profiles/criteria/opportunities/readiness/decision state;
- GitHub and/or governed Databricks enforcement adapter;
- override/fallback/degraded-control workflow;
- Safeguard profiles/path/cohort enforcement;
- REF-028 prevention manifest;
- SC-06 isolated capacity/observability.

Gate:

All Group 07 state transitions, bypass paths, stale decisions, enforcement reconciliation, release/recovery and historical control replay scenarios pass.

## First MVP implementation profile

A reasonable first proof deployment should include:

- one representative Databricks environment with Unity Catalog/system surfaces actually verified;
- a small set of representative pipelines/repos including A+B→C;
- GitHub revision/CI/deployment evidence where used by those pipelines;
- enough Measurement/Expectation/Baseline rules for foundation MVP health scenarios;
- representative temporal Lineage and consumer state;
- organization-owned Monitoring Scope/Assertion Authority/authorization rules for the pilot;
- deterministic Investigation/Explanation/replay;
- API/UI serving boundary;
- no mandatory Collibra, Immuta, LLM, graph database or active control.

## Required executable validation families

Convert design scenario suites into automated contract/integration/end-to-end tests where applicable. At minimum, implementation testing should cover:

1. canonical identity/rename/incarnation;
2. bitemporal/availability-by-K history;
3. correction/supersession/non-rewriting behavior;
4. scope/authority/authorization/disclosure;
5. adapter coverage/pagination/quota/schema failures;
6. run/deployment/input/output provenance;
7. health/quality distinctions and strong negatives;
8. typed Lineage and Impact boundaries;
9. Investigation/causal confirmation gates;
10. Statement/basis/renderer invariants;
11. cache/search/model security boundaries;
12. archive/restore/replay;
13. active-control semantics if enabled;
14. performance/SLO/cost behavior under representative load.

## Architecture change control

Implementation may discover environment constraints. Handle them in this order:

1. adjust concrete technology/configuration within frozen contracts;
2. explicitly reduce a deployment capability/product promise if source evidence cannot support it;
3. add instrumentation/attestation if the stronger proposition is required;
4. only reopen architecture if no compliant realization exists;
5. reopen functional semantics only if the product requirement itself intentionally changes.

Do not silently weaken a contract in code and later document the behavior as architecture.

## Phase 010 handoff conclusion

The implementation team now has a complete truth/evidence/governance model, real-source integration contracts, frozen technical ownership/topology boundaries, explicit MVP/enterprise split, failure/SLO/cost/security constraints, unresolved product-selection register and executable validation direction.

Implementation should no longer need to invent missing semantics in order to start building.
