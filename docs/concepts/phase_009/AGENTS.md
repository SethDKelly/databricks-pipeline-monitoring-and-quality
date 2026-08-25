# Phase 009 Agent Handoff

Applies to work under `docs/concepts/phase_009/` and complements the repository root `AGENTS.md`.

## Current status

- Phase 008 is complete with EXPL-001–EXPL-160 final.
- Phase 009 logical grouping is accepted.
- **Group 01 is complete with INTG-001–INTG-022; IC01-01–IC01-40 pass.**
- **Group 02 is complete with INTG-023–INTG-050; GOV02-01–GOV02-48 pass.**
- **Group 03 is complete with INTG-051–INTG-083; RTE03-01–RTE03-54 pass.**
- **Group 04 is complete with INTG-084–INTG-119; HME04-01–HME04-56 pass.**
- **Group 05 is complete with INTG-120–INTG-153; LIE05-01–LIE05-60 pass.**
- **Group 06 is complete with INTG-154–INTG-200; ICE06-01–ICE06-72 pass.**
- **Group 07 is complete with INTG-201–INTG-238; EBR07-01–EBR07-64 pass.**
- **Group 08 — Cross-Source Coverage, Latency, Retention, Cost & Consolidation / Exit Review is next.**
- Accepted concept count remains 24.
- Canonical repository status remains in `../../README.md#current-state`.

## Phase purpose

Phase 009 maps accepted functional semantics to actual source/integration capabilities. It discovers feasibility and limitations; it does not redesign the accepted truth model around vendor convenience.

## Accepted Group 01 rules

Preserve:

- integration contracts are capability mappings, not new product truth concepts;
- capability identity binds exact source surface/API/table/event/query/export/object class plus material semantic/version/edition context;
- vendor/system name alone is too coarse;
- every capability row binds an accepted proposition and bounded subject/context;
- evidence role is descriptive and does not create Assertion Authority;
- source availability ≠ relevance ≠ eligibility ≠ authority ≠ sufficiency ≠ authorization;
- internal retrievability ≠ requester-visible disclosure;
- source-local IDs require reconciliation before becoming Entity Identity or another ecosystem identity;
- name equality and timestamp proximity do not prove identity/association;
- exact cross-system associations require explicit join/reconciliation evidence;
- event/effective, recorded/knowledge/availability and retrieval times remain distinct;
- old event timestamp returned today does not prove historical availability;
- grain/cardinality/context constrain the conclusion grain;
- positive-evidence capability does not imply corresponding negative-evidence capability;
- strong negatives require the exact opportunity/population/path/window plus sufficient source/query coverage and source health;
- no record returned during outage/partial pagination/permission failure/throttling/unknown coverage is not evidence of absence;
- coverage is bounded and non-transitive;
- current-state availability does not imply historical replay;
- retention, mutation, correction, backfill, deletion and tombstone behavior are material to replay;
- late evidence does not enter an earlier knowledge cut without evidence it was available then;
- duplicate/common-derived surfaces are not independent corroboration;
- source conflicts remain conflicts absent accepted authority/evidence rules;
- fallback accessibility does not inherit authority;
- support classification is proposition + source set + context bound;
- accepted feasibility outcomes are supported, partially supported, unsupported, unknown/not yet verified and not applicable;
- unsupported is allowed and never weakens REF/AUTH/HLTH/OPS/EXPL semantics;
- quotas/rates/cost may reduce feasible coverage/latency but cannot change truth;
- integration observability is separate from monitored-product state;
- no universal vendor support/confidence/completeness score is accepted;
- capability rows compose only through explicit product semantics, not matrix adjacency.

See [`01_integration_contract_vocabulary_source_roles_capability_matrix/README.md`](01_integration_contract_vocabulary_source_roles_capability_matrix/README.md).

## Accepted Group 02 rules

Preserve:

- Unity Catalog object/principal identity is platform-local until explicit cross-system mapping proves wider identity;
- Collibra UUID and GitHub repository/path identity remain source-local;
- synchronized identity/group/attribute state retains upstream IAM provenance;
- no evaluated source natively owns DMTZ Monitoring Scope;
- Collibra operating-model `scope` is not Monitoring Scope;
- no vendor owner/role/permission surface automatically implements full Assertion Authority;
- semantic authority is facet-specific; Responsibility Assignment authority is responsibility-type specific; Classification authority is scheme/context specific;
- Unity Catalog comments are semantic assertions whose origin does not grant business authority;
- Unity Catalog ownership is platform-operational ownership rather than general business responsibility;
- Collibra Responsibilities retain direct/inherited role semantics; Collibra permissions authorize Collibra actions only;
- ordinary Collibra tags are not strictly governed Classification evidence; Data Classes/governed attributes require an accepted scheme-authority rule;
- Immuta tags/policies retain their policy-metadata/access-control meaning rather than becoming Classification or Policy Context truth by convenience;
- Unity Catalog privileges/ownership/ABAC/workspace state are authoritative only for exact Unity Catalog access propositions in their documented scope;
- Immuta is authoritative for Immuta-managed policy decisions in registered scope, with integration/user-registration semantics preserved;
- effective Immuta + Unity Catalog authorization may require composed evidence and population-specific reasoning;
- GitHub CODEOWNERS/rulesets/custom properties remain repository-governance facts;
- Information Schema and other principal-filtered metadata are observer-relative; hidden/non-returned ≠ absent;
- current governance state ≠ historical governance state;
- source history/retention/configuration limits remain explicit;
- optional-source absence creates gaps rather than benign defaults;
- source conflict/fallback still follows AUTH-001–AUTH-008 rather than source count, recency or product prominence.

See [`02_identity_scope_governance_authority_authorization_sources/README.md`](02_identity_scope_governance_authority_authorization_sources/README.md).

## Accepted Group 03 rules

Preserve:

- Git commit SHA is repository revision identity; PR/merge/commit metadata becomes Change Intent only under explicit governance;
- `github.sha` is event-semantic triggering revision and can differ in meaning from `github.workflow_sha`;
- GitHub `run_id` identifies a workflow run while `run_attempt` identifies a re-run attempt;
- a GitHub re-run retains the original triggering SHA/ref and does not become a new source revision by default;
- CI job/step/workflow success does not prove Databricks target activation;
- GitHub Deployment SHA/ref/environment records identify GitHub deployment requests/status, not target activation by default;
- GitHub→Databricks association requires explicit shared identifiers/manifests/fingerprints/target-recorded provenance;
- names, actors, branch labels and timestamp proximity cannot establish cross-system operational joins;
- Databricks job/task SCD2 configuration history constrains effective config but does not prove run-specific state;
- bundle/external-deployment metadata identifies management/provenance context but does not itself attest a commit;
- bundle/workspace-source run Git revision is unsupported out of the box unless explicit immutable attestation is retained;
- direct remote-Git Jobs can expose `git_snapshot.used_commit` as strong run-specific Git code evidence;
- implementation state remains composite across code, job/task configuration, params, runtime/libraries and target facets;
- trigger/schedule/opportunity ≠ actual run;
- run occurrence ≠ complete lifecycle;
- retry/repair/rerun/backfill retain distinct source semantics;
- task/root/source run associations use explicit IDs where available; missing older fields remain missing;
- configured dependency ≠ actual precedence ≠ waiting ≠ consumption;
- timeline rows must be assembled before deriving run/task duration/order;
- Lakeflow pipeline update identity remains distinct from Jobs execution identity;
- recent Jobs API detail and longer system-table history are different replay surfaces;
- audit events can support operational reconstruction but common derivation prevents automatic independent-corroboration credit;
- Delta output version binding is conditional and per output;
- run success ≠ output existence/version/currentness/health;
- Delta `readVersion` is not a generic upstream input manifest;
- exact generic multi-input version consumption is unsupported out of the box and requires explicit workload/query/source evidence when needed;
- no-run/no-output/no-consumption retain opportunity/coverage/source-health burdens.

See [`03_change_deployment_execution_version_runtime_evidence/README.md`](03_change_deployment_execution_version_runtime_evidence/README.md).

## Accepted Group 04 rules

Preserve:

- current Unity Catalog structure is current/observer-relative evidence, not historical structure or consumer compatibility;
- schema/column name equality or change does not prove field continuity across rename/recreate without explicit mapping;
- declared PK/FK/key constraints do not prove empirical uniqueness/referential integrity when the platform treats them as informational;
- engine schema-evolution/cast support is not a consumer-specific compatibility Assessment;
- DQX is optional/version-specific and exact production behavior binds the deployed/pinned version;
- DQX rule availability, profiling or AI generation does not create governed Expectation authority;
- DQX detailed/summary results are Observations of the exact checked execution and require run/input/rule-set provenance for replay;
- DQX criticality/actions are not framework severity, waiver, Gate or other control semantics by default;
- Lakeflow expectation action and expectation result remain distinct;
- Lakeflow fail-update expectation violations can have incomplete tracking metrics; missing counts are unavailable, not zero;
- Metric Views can be semantic metric-definition sources when governed, but YAML spec version is not organization metric-definition revision;
- Metric View query values retain fields/filters/parameters/window/definition/source context;
- Metric View materialization is query optimization rather than an implicit freshness SLA;
- Metric View cardinality/rely declarations do not replace empirical key/cardinality evidence;
- data-profiling profile/drift/custom metrics are descriptive Observations/derived comparisons until governed otherwise;
- a configured profiling baseline table does not automatically become framework Baseline membership/authority;
- anomaly-detection freshness/completeness are learned vendor-model Assessments, not explicit normative criteria by default;
- Databricks anomaly table-level health is a source-owned composite assertion rather than universal HLTH-055 truth;
- vendor root-cause/downstream-impact fields are supporting/contextual and do not satisfy Causal Claim/Impact requirements;
- current anomaly detection supports commit freshness, not event-time/ingestion-latency freshness;
- Baseline membership, regime, comparability and version remain explicit;
- measurement window/slice/cohort is part of proposition identity and coverage;
- run-specific health requires exact measurement→run/output binding rather than latest/current table inference;
- reconciliation requires exact transformation/version/populations/keys/measures/window/current-cycle semantics;
- exact current-cycle alignment remains conditional where Group 03 exact consumed-version evidence is unavailable;
- result production/evaluation/scan/refresh/availability/retrieval clocks remain distinct;
- historical health replay requires retained definitions/Baselines/profile semantics as well as result values;
- skipped/disabled/failed checks/scans or expired history do not support clean health negatives;
- health sources can disagree without a global precedence when they evaluate different propositions.

See [`04_health_schema_metrics_expectations_baselines_reconciliation_evidence/README.md`](04_health_schema_metrics_expectations_baselines_reconciliation_evidence/README.md).

## Accepted Group 05 rules

Preserve:

- lineage system tables expose captured events, not a complete universal read/write ledger;
- captured lineage event ≠ permanent/effective relationship interval;
- missing table/column lineage ≠ no relationship/read/use;
- `direct_access` is source traversal semantics, not relevance/exposure/causal strength;
- lineage source-local table/path/entity identity requires reconciliation where ecosystem identity matters;
- native rename continuity is not assumed;
- availability/publication ≠ actual encounter;
- query execution ≠ table read absent source association;
- lineage `statement_id` ↔ query history is accepted explicit association evidence when present;
- query actor/client/query-source context ≠ external report/human/business identity;
- cached query-result receipt ≠ fresh source read;
- dashboard access ≠ dashboard query execution ≠ query-result receipt;
- dashboard cache can serve results without a new warehouse query and may carry safe/affected/unknown prior state;
- dashboard schedule configuration ≠ refresh execution; refresh ≠ later human view;
- snapshot/email/Slack/Teams delivery ≠ reading or decision reliance;
- external BI query and JDBC/application read establish only the covered platform boundary by default;
- generic lineage/query history does not universally expose the exact table/data version consumed;
- object-level encounter with unresolved state/version is a valid intermediate result;
- query time/proximity ≠ consumed version;
- explicit time-travel/version evidence is conditional on retained/resolvable statement/parameter/history evidence;
- refresh/materialization, copy, cache, export and snapshot are distinct encounter paths;
- safe stale state ≠ affected-state exposure;
- multi-hop exposure is non-transitive;
- one safe path ≠ global non-exposure;
- positive exposure is consumer/path/state/version bound;
- `not exposed` retains opportunity/path/version/source-health coverage burden;
- exposure ≠ downstream effect ≠ consequence ≠ Causal Claim;
- dashboard/report access/delivery ≠ decision reliance;
- table popularity/insights and vendor downstream-impact labels are context, not realized Impact/severity;
- historical Impact replay composes heterogeneous source windows and remains non-rewriting.

See [`05_lineage_consumer_use_exposure_impact_evidence/README.md`](05_lineage_consumer_use_exposure_impact_evidence/README.md).

## Accepted Group 06 rules

Preserve:

- Investigation trigger/lead/localization does not create Causal Claim status;
- first observed, earliest evidenced state change, first reconciliation boundary and first consumer effect are different localizations;
- lead exclusion/rejection requires sufficient discriminating negative evidence;
- human approval, analyst seniority, GitHub review, vendor RCA and model output do not create causal authority by origin;
- explicit cause/effect/role/scope/mechanism/time proposition identity precedes causal evaluation;
- no evaluated Databricks/GitHub/Immuta surface automatically confirms causality;
- `confirmed` remains REF-017 + AUTH-034 gated;
- rollback/rerun/remediation contrasts are evidence and can remain confounded;
- `system.access.audit` is action/request/response history, not universal effective enforcement;
- asynchronous control API success requires later effective-state evidence;
- UC grant/revoke applies only to its exact privilege/control plane and current privilege state is not historical enforcement;
- Immuta policy configuration/change ≠ query-time policy application;
- Immuta applied-policy/denial audit is strong only in verified registered/instrumented scope;
- missing Immuta/control audit ≠ allow/deny/control outcome;
- Safeguard proposal/authorization/request ≠ effective enforcement;
- Safeguard enforcement binds exact state/path/cohort/interval and can be partial;
- one protected/denied path ≠ global protection;
- no encounter opportunity means no REF-028 prevention credit;
- REF-028 prevention needs Group 05 opportunity/path/state + enforcement + non-exposure + alternate-path coverage;
- Safeguard release/regrant ≠ recovery/currentness;
- Databricks Jobs cancellation is asynchronous post-start interruption, not pre-start Gate HOLD;
- no universal native DMTZ output quarantine/hold source is assumed;
- GitHub environment protection is strong pre-start evidence for its exact Actions job/deployment opportunity;
- required review approval/rejection/bypass/wait/custom protection rule events retain distinct GitHub semantics;
- GitHub Gate evidence applies to Databricks only with explicit Group 03 correlation;
- Databricks `Run if`/`If/else` are conditional-control candidates and require explicit DMTZ Gate criterion/opportunity mapping;
- Gate criterion/evidence suitability/readiness/decision/delivery/acceptance/enforcement/execution stay distinct;
- actual start during an applicable unsuperseded HOLD contradicts full HOLD enforcement;
- no start alone does not prove HOLD;
- ADMIT does not prove execution;
- override/fallback/timeout/escalation are separate source facts and preserve readiness truth;
- multiple Gates/Safeguards have no hidden universal precedence;
- missing/conflicting control telemetry ≠ fail-open/fail-closed/success/failure;
- broader delay/staleness/harm/prevention attribution remains Causal Claim work except REF-028.

See [`06_investigation_causality_safeguard_gate_control_evidence/README.md`](06_investigation_causality_safeguard_gate_control_evidence/README.md).

## Accepted Group 07 rules

Preserve:

- material Explanation statements retain exact internal statement→source-basis identity;
- rendered wording, display label, URL or citation does not replace stable source/event/object identity;
- supporting/contradicting/limiting evidence roles are statement-relative;
- basis/source count does not create confidence and common-derived evidence remains common-derived;
- event/effective time `T`, source-recorded/availability time, knowledge cut `K`, retrieval time and communication time remain distinct;
- an event timestamp before `K` does not prove the source fact was available by `K`;
- current retrieval of an old event cannot backfill historical knowledge;
- late evidence/corrections can change current retrospective Explanation without rewriting earlier as-known state;
- current source state/latest record ≠ historical source state;
- expired/deleted/truncated/blank/encrypted/disabled history remains missing or limited rather than reconstructed;
- reconstructed as-known-at-cut Explanation ≠ actual retained communication;
- actual retained communication requires authentic content/context evidence;
- delivery evidence ≠ exact rendered content ≠ reading/comprehension/reliance;
- mutable GitHub/ticket/comment history is communication evidence only to the extent revisions survive;
- missing retained communication remains missing; reconstruction must be labeled reconstruction;
- statement identity can persist across wording/detail/basis changes only when proposition-defining scope/time remains materially stable;
- basis enrichment does not automatically strengthen status/confidence;
- source outage/lag/permission failure is a basis limitation, not proposition-level negative truth;
- partial Explanation remains valid and no global completeness percentage is accepted;
- internal `inspectBasis` traceability is required independently of requester-visible disclosure;
- visible citation/reference ≠ source retrievability ≠ disclosure authorization;
- current requester authorization governs current disclosure of historical basis;
- historical actor authorization and current requester disclosure do not rewrite each other;
- result/context/limitation/basis/provenance/detail visibility can be separately authorized;
- safe coarse/redacted/opaque basis projection cannot strengthen/reverse/broaden the source proposition;
- source existence/count/type/timestamps/redaction state can themselves be sensitive;
- query text/parameters/errors and actor/consumer identities are independently disclosure-governed;
- permission/workspace/region-filtered source views are observer-relative; hidden/non-returned ≠ absent;
- Databricks system-table history has per-surface retention and no generic indefinite `system` ledger;
- Databricks query-content basis is conditional because CMK and truncation can remove detail;
- Databricks alert history can establish definition/evaluation/delivery status without proving exact message content;
- GitHub enterprise audit history is retention-bound and streamed duplicates remain common-derived;
- GitHub comment history is mutable, edit-capped and revision content can be removed;
- Collibra history is facet/configuration specific and visibility permission-filtered;
- Immuta audit is rich but short-lived by default; long-horizon basis inspection requires verified export/retention;
- exact prior `inspectBasis` presentation cannot be reconstructed from current source access alone;
- comparative Explanation evaluates source retention/coverage independently on each side;
- asymmetric basis availability is not automatically a source-truth difference.

See [`07_explanation_historical_replay_basis_disclosure_source_contracts/README.md`](07_explanation_historical_replay_basis_disclosure_source_contracts/README.md).

## Required evaluation dimensions

For every material source surface, evaluate as applicable:

- exact source surface and semantic/version/edition context;
- accepted proposition(s) it may inform;
- evidence role and proposition-specific authority applicability;
- source-local identity plus join/reconciliation keys;
- event/effective, recorded/knowledge/availability and retrieval-time semantics;
- granularity/cardinality and version/context binding;
- positive evidence support;
- strong-negative opportunity/coverage support;
- known completeness/coverage boundaries;
- access/authorization and disclosure sensitivity;
- availability and failure/unavailable behavior;
- latency and freshness characteristics;
- retention/history/replay behavior;
- correction, mutation, supersession and late-arrival behavior;
- retained-communication versus reconstruction capability where Explanation history is in scope;
- basis inspectability after native source retention expiry;
- rate/quota/cost characteristics where material;
- observability of the integration itself;
- duplicate/common-derivation relationships to other sources;
- support classification and residual gaps.

## Permanent boundaries

Never convert:

- available → authoritative;
- authoritative → sufficient;
- accessible → authorized for disclosure;
- missing → false/zero/no-event/no-path/no-exposure/no-effect/no-control;
- current state → historical state;
- event timestamp → knowledge availability;
- reconstructed historical answer → actual retained communication;
- notification delivery → exact message content/read/reliance;
- citation/reference → source access or basis-display permission;
- more visible basis → more true/more supported;
- hidden/expired basis → absent proposition;
- Lineage → encounter/exposure;
- lineage/read event → exact affected-version exposure absent state/version evidence;
- dashboard/report access → dataset execution/result receipt/business reliance;
- one safe cache/copy path → global non-exposure;
- exposure → effect/consequence/cause;
- workflow success → deployment activation or run-specific version;
- active Deployment → actual run version;
- latest upstream output → consumed input;
- metric/check availability → governed Expectation/Baseline/Assessment;
- vendor health/root-cause/impact label → DMTZ composite health/Causal Claim/Impact truth;
- Investigation lead/localization → Causal Claim status;
- remediation success → causal confirmation;
- control request/response → effective enforcement without source semantics/evidence;
- Safeguard active + non-exposure → prevented exposure without REF-028 evidence;
- Gate HOLD → failed execution;
- Gate ADMIT → run;
- GitHub environment approval → uncorrelated Databricks Gate result;
- restricted/redacted → absent;
- source count → confidence;
- synchronization order → authority or causality.

## Source-family discipline

Do not structure the product around vendor names. Databricks, Unity Catalog, GitHub, DQX, Metric Views, Collibra, Immuta and downstream/control/communication instrumentation may each support multiple accepted concepts, and one accepted proposition may require multiple source families.

A source may be authoritative for one metadata/control category and merely supporting/observational for another. Preserve proposition-, subject-, context- and time-specific authority.

## Group 02 gaps carried forward

- a deliberate governed Monitoring Scope source remains required;
- an explicit governed Assertion Authority rule source remains required;
- cross-system Entity Identity crosswalks remain required;
- long-horizon governance replay may require retention beyond vendor defaults;
- actual organizational IAM/IdP and synchronization mode remain environment-specific unknowns until verified;
- observer-relative metadata cannot support absence by non-return;
- effective multi-plane authorization may require composition rather than source precedence.

## Group 03 gaps carried forward

- generic CI→Databricks association requires explicit correlation where platform-native evidence is absent;
- bundle/workspace-source runs need explicit commit/content attestation when exact Git revision matters;
- composite run-specific implementation state requires multiple evidence facets;
- exact generic multi-input consumption requires explicit workload/query/source instrumentation or manifests;
- output version binding remains conditional and per output;
- recent Jobs API versus longer system-table history creates replay-detail boundaries;
- operational negative claims remain source-coverage bound.

## Group 04 gaps carried forward

- consumer-specific structural compatibility requires an explicit governed interface/contract beyond platform schema metadata;
- empirical key/relationship integrity needs observed checks where declared constraints are informational;
- DQX rule authority, exact version and result/check retention remain environment/governance specific;
- Metric View business-definition revision history must be explicitly retained/versioned where material;
- profiling/anomaly historical models and baseline tables do not self-authorize framework Baseline membership;
- event-time freshness requires a separate evidence source from current anomaly-detection commit freshness;
- exact measurement→run/output attribution requires explicit association where current/latest state is insufficient;
- exact multi-input current-cycle alignment inherits the Group 03 consumption-version gap;
- vendor health/root-cause/impact labels remain bounded source assertions, not truth shortcuts;
- health history and clean negative conclusions remain source/evaluation/retention-coverage bound.

## Group 05 gaps carried forward

- lineage capture is incomplete and cannot support universal negative topology/use claims;
- renamed/path-addressed objects require explicit identity reconciliation where continuity matters;
- generic exact table-version consumption is unsupported by the evaluated lineage/query-history pair without added state evidence;
- exact dashboard-cache state may require explicit cache/state attestation;
- external BI report views/interactions require external-BI telemetry where material;
- application fetch/display/business-use layers require application/business telemetry;
- multi-hop exposure requires per-hop affected-state propagation and encounter evidence;
- business/customer/financial consequence remains environment-specific rather than Databricks-native truth;
- historical Impact replay spans heterogeneous lineage/query/audit/external retention windows;
- strong non-exposure/no-effect/no-consequence conclusions remain path/population/version/dimension coverage intensive.

## Group 06 gaps carried forward

- no evaluated vendor automatically owns Causal Claim confirmation; organizational Assertion Authority remains required;
- a durable Investigation/Annotation/claim-status source remains environment-specific;
- Databricks audit request/response does not universally prove effective distributed control state;
- no single native Propagation Safeguard covers every output/cache/export/application path;
- Immuta enforcement/audit support depends on deployed version, integration mode, registered population and retained audit;
- REF-028 prevention remains opportunity/path/state/alternate-path coverage intensive;
- GitHub environment Gates only protect their exact GitHub job/deployment unless Group 03 correlation proves target execution linkage;
- Databricks conditional tasks require explicit Gate criterion/profile mapping;
- override/fallback/multiple-Gate composition remains organization/control-contract specific;
- control historical replay spans different audit/deployment/custom-control retention windows;
- missing/conflicting control telemetry cannot determine fail-open/fail-closed or effect attribution.

## Group 07 gaps carried forward

- exact retained communication is not provided by telemetry/source reconstruction and requires an explicit retention strategy where prior wording/context matters;
- exact availability-by-knowledge-cut is not uniformly exposed across sources;
- vendor-native history is heterogeneous and often shorter than enterprise replay goals;
- Databricks exact query basis can be blank/truncated under security/storage behavior;
- delivery evidence does not retain exact rendered Explanation content by default;
- GitHub discussion history is mutable/edit-capped and selected revision content can be removed;
- Collibra resource history is facet/configuration specific and can omit selected/inherited changes;
- Immuta native SaaS audit retention is short for long-horizon `inspectBasis` unless exported;
- historical authorization replay remains partial where old IAM/policy/grant state expires;
- current requester disclosure must be evaluated independently of historical access;
- sensitive basis metadata includes existence/count/type/provenance/query text/parameters/errors/actors/timestamps/redaction state;
- exact prior `inspectBasis` presentation is unavailable unless independently retained;
- observer-relative source views remain unsafe for strong negatives;
- comparative Explanation can differ because basis retention differs without implying a truth delta.

## Group 08 entry contract

Group 08 must consolidate all accepted Phase 009 source capabilities and residual gaps without weakening the underlying REF/AUTH/HLTH/OPS/EXPL contracts.

It must separately assess source-truth feasibility, as-known-at-cut replay, actual retained communication, current basis inspectability/disclosure, cross-system joins, latency, coverage, retention, cost/quota and integration observability. Planned Phase 010 retention/instrumentation cannot be counted as a capability that already exists, but explicit architecture prerequisites must be recorded.

## External-fact discipline

Groups 02–08 necessarily evaluate evolving vendor capabilities. Verify current external documentation when executing a group, distinguish product documentation from repository assumptions, record meaningful edition/feature/retention/permission limitations, and avoid treating undocumented behavior as guaranteed.

Group 02 records sources in [`02_identity_scope_governance_authority_authorization_sources/external_source_review.md`](02_identity_scope_governance_authority_authorization_sources/external_source_review.md); Group 03 records sources in [`03_change_deployment_execution_version_runtime_evidence/external_source_review.md`](03_change_deployment_execution_version_runtime_evidence/external_source_review.md); Group 04 records sources in [`04_health_schema_metrics_expectations_baselines_reconciliation_evidence/external_source_review.md`](04_health_schema_metrics_expectations_baselines_reconciliation_evidence/external_source_review.md); Group 05 records sources in [`05_lineage_consumer_use_exposure_impact_evidence/external_source_review.md`](05_lineage_consumer_use_exposure_impact_evidence/external_source_review.md); Group 06 records sources in [`06_investigation_causality_safeguard_gate_control_evidence/external_source_review.md`](06_investigation_causality_safeguard_gate_control_evidence/external_source_review.md); Group 07 records sources in [`07_explanation_historical_replay_basis_disclosure_source_contracts/external_source_review.md`](07_explanation_historical_replay_basis_disclosure_source_contracts/external_source_review.md).

## Architecture boundary

Do not select SDK/client libraries, polling versus streaming, event buses, storage schemas, graph databases, caches, credential mechanisms, deployment topology, retry infrastructure, orchestration, attestation implementation, metric/rule stores, anomaly models, consumer/BI instrumentation, incident/case tooling, causal engine, Safeguard/Gate implementation, control-state persistence, Explanation snapshot store, source archive, redaction engine, LLM/retrieval architecture or UI. Phase 010 owns technical architecture.

## Group sequence

1. integration contract vocabulary/source roles/capability matrix — **accepted**;
2. identity/scope/governance/authority/authorization sources — **accepted**;
3. change/deployment/execution/version/runtime evidence — **accepted**;
4. health/schema/metrics/Expectations/Baselines/reconciliation evidence — **accepted**;
5. Lineage/consumer use/exposure/Impact evidence — **accepted**;
6. Investigation/causality/Safeguard/Gate/control evidence — **accepted**;
7. Explanation/historical replay/basis/disclosure source contracts — **accepted**;
8. cross-source coverage/latency/retention/cost consolidation and exit — **next**.
