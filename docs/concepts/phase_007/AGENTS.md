# Phase 007 Agent Handoff

Applies to work under `docs/concepts/phase_007/` and complements the repository root `AGENTS.md` without replacing accepted cross-phase rules.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 006 is complete with HLTH-001–HLTH-066 final.
- Phase 007 grouping is accepted.
- **Group 01 is complete with OPS-001–OPS-009; L01-01–L01-18 pass.**
- **Group 02 is complete with OPS-010–OPS-020; C02-01–C02-24 pass.**
- **Group 03 is complete with OPS-021–OPS-033; P03-01–P03-30 pass.**
- **Group 04 is complete with OPS-034–OPS-049; X04-01–X04-32 pass.**
- **Group 05 — Investigation Lifecycle, First-Deviation Localization & Causal Handoff is next.**
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

## Accepted Group 03 Prospective Review rules

Preserve:

- prospective review binds exact Change Intent revision/component, target/slice, evaluation time and knowledge cut;
- effective Lineage plus explicit planned topology additions/removals/modifications form a derived scenario topology only;
- planned topology never becomes effective Lineage from analysis;
- planned relationship removal creates a path-loss/change candidate; it does not make the still-effective dependent disappear;
- Impact owns candidate/reachability state; candidate ≠ exposure/effect/consequence/cause;
- candidate basis can be effective-path, planned-added-path, path-loss/change or indeterminate;
- field/key/population/interface/consumer/version scope narrows candidate relevance;
- asset reachability ≠ narrower semantic relevance;
- proposal-bound structural compatibility consumes HLTH-009–HLTH-018 and is not realized compatibility;
- metric/profile/Expectation/Baseline/composite review is scoped rather than global;
- prospective Baseline break/review ≠ empirical non-comparability/new Baseline;
- transformation changes trigger exact HLTH-041–HLTH-054 reconciliation review, not generic status propagation;
- readiness/AUTH-023/Gate/Safeguard assumptions may require review without creating readiness/control state;
- analytical review relevance ≠ governed review obligation ≠ review/approval action ≠ deployment/control decision ≠ enforcement;
- AUTH-020/other authority can govern review/use decisions but cannot manufacture topology/compatibility/comparability evidence;
- Criticality/priority ≠ probability/Impact/evidence strength;
- no universal numeric/qualitative risk score, path-count probability or shortest-path importance rule;
- incomplete/conflicting/restricted topology remains explicit and candidate sets may be non-exhaustive;
- `not relevant`, `not candidate`, `no alternate path` and `no blast radius` require sufficient bounded negative coverage;
- active canary evidence may inform remaining-slice review but is not future-slice realized fact;
- overlapping intents remain separate unless a material interaction is explicitly composed;
- retained historical review ≠ reconstructed as-known-then review ≠ current retrospective recomputation.

See [`03_prospective_blast_radius_change_aware_review/README.md`](03_prospective_blast_radius_change_aware_review/README.md).

## Accepted Group 04 Execution Reconstruction rules

Preserve:

- Execution History remains the actual execution truth owner; no new concept is required;
- actual execution identity is evidence-bound and cannot be created from schedule/job/repository/prospective state;
- expected work ≠ execution opportunity ≠ Gate HOLD/ADMIT/override ≠ actual execution;
- start/progress/terminal lifecycle facts may remain partial; missing transitions are not fabricated;
- logical execution assembly from jobs/tasks requires identity/correlation/dependency evidence;
- overlapping windows/name/repository membership alone do not prove common logical execution;
- retry/restart/rerun/backfill continuity is source/evidence specific;
- attempt outcome ≠ logical-execution outcome absent explicit composition semantics;
- effective dependency ≠ expected order ≠ actual precedence ≠ evidenced waiting ≠ run-specific consumption;
- Lineage/latest upstream output/prior completion/time proximity do not prove consumed version;
- successful run ≠ output existence; failed/partial run may still produce material output;
- output exists ≠ committed/published/current-cycle/fresh/healthy/ready;
- Deployment active-at-time constrains but does not universally prove run-specific code/config/schema/transformation state;
- no universal `run version` token is accepted when implementation state is composite;
- mid-run activation/rollback is facet/task/binding-semantics specific; no automatic switch/reversion rule;
- duplicate/common-derived telemetry ≠ independent corroboration;
- out-of-order arrival ≠ event chronology; applicable conflict remains explicit;
- cross-source clocks can make close sequence indeterminate; explicit sequence evidence can be stronger;
- `no run`, `no output`, `no consumption` and similar negatives require REF opportunity/coverage;
- partial lifecycle/child/root outcomes remain level-specific;
- multi-input version set can be incomplete/mixed/stale; currentness/freshness/readiness remain Assessment semantics;
- historical execution reconstruction is bitemporal and non-rewriting.

See [`04_execution_reconstruction_dependency_sequence/README.md`](04_execution_reconstruction_dependency_sequence/README.md).

## Permanent Phase 007 boundaries

Preserve:

- Lineage ≠ causality;
- Lineage relation ≠ metric/status propagation;
- planned topology ≠ active/effective topology ≠ historical topology;
- Change Intent ≠ Deployment ≠ realized Change;
- prospective blast radius ≠ actual Impact;
- intended schedule/dependency ≠ actual execution sequence;
- expected/opportunity/control state ≠ actual execution;
- proposed/reviewed version ≠ executed version;
- Deployment active-at-time ≠ run-specific version use by default;
- execution occurrence ≠ specific consumed-version proof unless evidenced;
- actual precedence ≠ waiting ≠ consumption;
- run success ≠ output existence/health;
- missing telemetry ≠ no event/run/output/consumption;
- duplicate/common-derived telemetry ≠ independent corroboration;
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

## Group 05 entry contract

Group 05 consumes OPS-001–OPS-049 and must turn topology/change/health/execution evidence into a structured Investigation without causal promotion.

It should explicitly test:

- investigation question/outcome/scope/time binding;
- candidate generation from Lineage, Change, execution and reconciliation evidence;
- first-observed deviation versus earliest evidenced state change versus transformation-boundary mismatch versus first downstream effect;
- multiple simultaneous/compatible upstream deviations;
- first post-change run with insufficient discriminatory causal evidence;
- retries/reruns/backfills altering apparent sequence;
- stale/mixed input versions relevant to localization;
- incomplete/ambiguous run/version evidence limiting localization;
- late evidence changing retrospective first-deviation localization without rewriting what investigators knew then;
- handoff from operational hypothesis/lead into explicit Causal Claim REF-013–REF-020 state;
- Investigation closure with causal status still unresolved/weakened/rejected/supported rather than confirmed.

Do not let Group 05 promote first deviation, temporal precedence, shared version, dependency path, deployment proximity, reconciliation mismatch or analyst closure into root cause/confirmation.

## Architecture boundary

Do not select graph database, graph query language, Lineage ingestion source, event store, event schema, CI/CD/runtime telemetry source integration, deployment fingerprinting mechanism, static-analysis/change-risk algorithm, scheduler/orchestrator, safeguard/quarantine mechanism, gate implementation, queue/event bus, cache/streaming topology, RCA algorithm, persistence schema, source integration or concrete latency/timeout SLA in Phase 007 functional refinement.