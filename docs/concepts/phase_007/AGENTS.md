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
- **Group 05 is complete with OPS-050–OPS-066; I05-01–I05-34 pass.**
- **Group 06 is complete with OPS-067–OPS-085; IM06-01–IM06-36 pass.**
- **Group 07 is complete with OPS-086–OPS-104; SG07-01–SG07-36 pass.**
- **Group 08 — Execution Gate, Fallback/Override & Control-Induced Operational Effects is next.**
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

## Accepted Group 05 Investigation / Localization / Causal Handoff rules

Preserve:

- Investigation remains the bounded-inquiry truth owner; Causal Claim remains the causal proposition/epistemic owner;
- exact Investigation question/outcome, subject/population/use scope, event/effective window and knowledge cut are first-class;
- scope revision is versioned/non-rewriting;
- Investigation lifecycle `open`/`active`/`paused`/`closed`/reopen is independent of causal status;
- candidate/lead state belongs to Investigation and does not use Causal Claim epistemic labels;
- lead generation basis/provenance/limitations remain explicit;
- linked evidence remains source-owned; Investigation may assign inquiry-specific evidence roles only;
- contradiction, gaps, restrictions and common derivation remain first-class;
- first observed deviation ≠ earliest evidenced state change ≠ first reconciliation/transformation boundary ≠ first downstream consumer effect;
- every `first` localization claim is bounded to searched semantic/topology/time/version/coverage scope;
- first observed/earliest evidenced/localized boundary ≠ root cause;
- Lineage reachability/path length/directness ≠ causal ranking;
- reconciliation/structural/health boundary localization ≠ causality;
- first post-change run/shared version/rollback/retry contrast/temporal precedence are evidence, not cause;
- mixed/unknown version or ordering evidence limits localization instead of being guessed;
- multiple simultaneous/competing/compatible branches remain valid;
- lead exclusion/narrowing requires REF-sufficient negative/discriminating evidence;
- lack of lead support ≠ exclusion/rejection;
- causal language (`caused`, `contributed`, `enabled`, `triggered`, `prevented`, `materially influenced`) requires an explicit Causal Claim;
- Investigation priority/localization does not transfer as Causal Claim status;
- Causal Claim statuses remain REF-014 `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`;
- `confirmed` requires REF-017 evidence plus AUTH-034/Capability Authorization; closure/consensus/remediation/model output cannot substitute;
- operational resolution/actionability ≠ causal confirmation;
- unresolved/no-actionable-conclusion closure is valid;
- historical Investigation/localization is bitemporal and late evidence can justify reopen without rewriting prior closure;
- restricted/opaque evidence limits localization without becoming absence or an authorization bypass;
- analyst and automated assistance follow identical provenance/evidence discipline; origin does not create truth or authority;
- no universal RCA/hypothesis/confidence score is accepted;
- prospective blast-radius membership does not become retrospective causal support by itself.

See [`05_investigation_localization_causal_handoff/README.md`](05_investigation_localization_causal_handoff/README.md).

## Accepted Group 06 Impact / Encounter / Exposure / Consequence rules

Preserve:

- Impact remains candidate/exposure/effect/consequence association owner; source facts and causal attribution retain their existing owners;
- realized Impact binds exact origin condition/state/version/window, consumer/use/interface/population, historical path, encounter mode, event/effective time and knowledge cut;
- candidate/reachable ≠ encounter opportunity ≠ state available ≠ published/served ≠ actual encounter;
- encounter evidence is mode-specific across execution input, refresh/materialization, publication, query/read, cache/replica/snapshot, application/report and human/business-process use;
- accepted bounded exposure vocabulary is `exposed`, `not exposed`, `safe/other-state encounter`, `encountered-state unknown`, `no relevant encounter opportunity`, `indeterminate`, `conflicting`, `unavailable`;
- authorization/redaction is separate from epistemic exposure state;
- Group 04 run/input/output/version evidence establishes exposure only when encounter binding is sufficient;
- latest upstream output, prior completion, active Deployment or timing do not prove consumer version;
- stale safe prior-state use can mean `not exposed to suspect V` while freshness/currentness fails separately;
- cache/replica/snapshot state can lag and later transition to suspect exposure without rewriting the safe interval;
- exposure is not transitively propagated through multi-hop Lineage; indirect exposure needs intermediary transmission/state and downstream encounter evidence appropriate to the proposition;
- alternate paths are path-specific; one safe path ≠ global non-exposure;
- `not exposed` requires REF-023 opportunity/path/version coverage;
- no opportunity, no encounter and safe-state encounter remain distinct;
- exposure is event/interval specific and first exposure can change retrospectively with late evidence;
- exposure ≠ downstream effect; effect remains source-owned dimension/scope/time-bound Observation/Assessment/Change evidence;
- `no effect` requires bounded downstream coverage and one satisfied dimension is not a global negative;
- consequence categories may be technical/operational, analytical or business/process without creating universal severity;
- publication ≠ view ≠ decision reliance ≠ adverse consequence;
- no complaint/report ≠ no business consequence;
- consequence ≠ causal attribution; origin→effect/consequence causal language requires Causal Claim;
- confirmed upstream cause ≠ every reachable consumer exposed/affected;
- multiple origins/contributors remain first-class;
- Criticality/Classification/priority ≠ realized Impact/probability/evidence strength;
- no universal Impact/exposure/severity score is accepted;
- restricted ≠ absent and safe projection cannot strengthen state;
- historical Impact is bitemporal and non-rewriting.

See [`06_impact_consumer_encounter_exposure_consequence/README.md`](06_impact_consumer_encounter_exposure_consequence/README.md).

## Accepted Group 07 Propagation Safeguard rules

Preserve:

- Propagation Safeguard remains the protection-control truth owner; Impact owns encounter/exposure/effect/consequence and Capability Authorization owns permission;
- every safeguard binds exact suspect/protected state or missing-output/current-cycle context, protection surface, path/cohort/environment scope and effective interval;
- generic asset-wide `quarantined` state is insufficient when protected versions/paths differ;
- protection surface/placement is explicit and implementation-neutral; no universal upstream-most/downstream-most placement rule;
- proposal ≠ authorization ≠ activation request ≠ control acceptance ≠ effective enforcement;
- `active` requires REF-027 evidence-backed enforcement for the bounded scope/time;
- enforcement may be partial across consumer/path/region/cohort/version/interval; no universal protection percentage is accepted;
- active interval overlap ≠ safeguard materiality to an encounter opportunity;
- one protected path ≠ all alternate paths protected;
- bypass possibility ≠ actual bypass occurrence;
- `prevented exposure` is a derived REF-028 + Group 06 result, not a Safeguard lifecycle state;
- `active + not exposed` ≠ prevented exposure without operative opportunity/materiality/path coverage;
- no relevant encounter opportunity can coexist with valid active protection but does not create prevention credit;
- blocked suspect state can coexist with safe stale serving, delivery delay or non-delivery;
- missing output is not a quarantined object; current-cycle advancement/presentation can be protected instead;
- extension/renewal/scope revision is separately authorized/evidenced and preserves prior history;
- scheduled expiry ≠ effective expiry unless applicable semantics/evidence establish it;
- release rationale/authorization/request/control acceptance/effective release remain separate;
- release can be partial and release ≠ health/currentness/causal resolution/recovery;
- post-release recovered state is independently evidenced through Execution/Observation/Assessment/Impact; Safeguard does not own recovery truth;
- missing/conflicting control telemetry does not prove success/failure/fail-open/fail-closed;
- configured fallback ≠ actual fallback application;
- overlapping safeguards keep independent scope/materiality/release history; first activated is not automatically primary protector;
- safeguard-induced delay/staleness/non-delivery remains separate domain evidence;
- broader control-effect causal attribution uses Causal Claim; REF-028 retains the narrowly bounded prevented-exposure result;
- historical safeguard enforcement/prevention/release is bitemporal and non-rewriting;
- Propagation Safeguard ≠ Execution Gate; safeguard release ≠ Gate ADMIT and safeguard hold ≠ Gate HOLD.

See [`07_propagation_safeguard_scope_enforcement_recovery/README.md`](07_propagation_safeguard_scope_enforcement_recovery/README.md).

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
- missing telemetry ≠ no event/run/output/consumption/encounter/effect/control action;
- duplicate/common-derived telemetry ≠ independent corroboration;
- Investigation lead/localization ≠ Causal Claim;
- first-deviation localization ≠ root cause;
- Investigation closure/operational resolution ≠ Causal Claim confirmation;
- confirmed upstream cause ≠ consumer exposure;
- candidate/reachable ≠ encounter opportunity ≠ exposed ≠ effect ≠ consequence ≠ causal attribution;
- `not exposed`, `no effect`, `no consequence` require adequate bounded coverage for their exact propositions;
- available/published/served ≠ downstream actual use;
- stale safe state ≠ current/healthy;
- multi-hop exposure is not transitive;
- Safeguard proposal/configuration/authorization/request ≠ effective enforcement;
- active/enforced Safeguard ≠ prevented exposure;
- one protected path ≠ global protection;
- `not exposed` ≠ `prevented by Safeguard`;
- safeguard release/expiry ≠ healthy/fresh/recovered output;
- Phase 006 health suitability ≠ readiness ≠ gate decision ≠ enforcement ≠ execution;
- gate HOLD ≠ execution failure;
- gate ADMIT ≠ execution occurrence;
- override ≠ prerequisite ready;
- configured fallback ≠ actual fallback application;
- Execution Gate ≠ Propagation Safeguard;
- control-induced delay/staleness/non-delivery remains observable/assessable and is not automatically defect/cause;
- historical operational replay uses event/effective time plus knowledge cut and remains non-rewriting.

## Group 08 entry contract

Group 08 consumes OPS-001–OPS-104 and must refine Gate start/admission control without importing Safeguard output/consumption semantics.

It should explicitly test:

- exact downstream execution opportunity and then-applicable readiness criterion/profile;
- no Gate opportunity despite a not-ready prerequisite;
- HOLD/ADMIT decision versus delivery to scheduler/control plane versus actual enforcement;
- HOLD enforcement with no execution start during the opportunity;
- ADMIT with no actual run;
- override while underlying prerequisite remains not ready/unknown;
- configured timeout/fallback versus actual timeout/fallback application;
- fallback outcomes such as hold/admit/escalate only when explicitly configured and evidenced;
- control telemetry conflict/unavailability without universal fail-open/fail-closed assumptions;
- skipped/cancelled opportunity versus execution failure;
- Gate-held execution while older state remains consumable unless a separate Safeguard protects publication/consumption;
- Gate admission while Safeguard remains active;
- Safeguard release while Gate remains HOLD;
- gate-induced delay/skipped execution/older-version use/missed delivery as separate runtime/Impact evidence;
- causal attribution of gate effects under REF-013–REF-020 rather than decision proximity;
- late gate/enforcement/execution evidence changing retrospective interpretation without rewriting historical actions.

Do not let Group 08 convert readiness into a Gate decision, a decision into enforcement, HOLD into failure, ADMIT into execution, override into readiness, Safeguard state into Gate state, or configured fallback into actual fallback behavior.

## Architecture boundary

Do not select graph database, graph query language, Lineage ingestion source, event store, event schema, CI/CD/runtime/consumer telemetry source integration, deployment fingerprinting mechanism, static-analysis/change-risk/RCA/Impact algorithm, LLM/agent workflow, scheduler/orchestrator, safeguard/quarantine mechanism, gate implementation, queue/event bus, cache/streaming topology, persistence schema, source integration or concrete latency/timeout SLA in Phase 007 functional refinement.
