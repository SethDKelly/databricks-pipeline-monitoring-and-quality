# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, governance/authority, integration authority, health/metric/schema semantics, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery
**Status:** Complete.

## Phase 002 — Concept Specifications
**Status:** **Complete with four accepted post-exit addenda.**

The original five groups accepted 20 concepts. Later work added **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and during Phase 005 Group 01 **Assertion Authority** after review exposed independent missing behavior. Current catalog: **24 concepts**.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Complete — Groups 01–06 accepted; SYN-001–SYN-035 accepted; E-01–E-22 pass.**

Phase 003 defines end-to-end coordination for subject/governance context; planned change/reference transition; runtime timing/health/change; optional execution gating; safeguards; Investigation/causality; layered downstream Impact; Annotation; authorized analytical projection/Explanation; and bitemporal historical replay.

## Phase 004 — Evidence, Time, and Causality Refinement

**Status:** **COMPLETE — Groups 01–05 accepted; REF-001–REF-030 accepted.**

Phase 004 uses `REF-###` refinement contracts over accepted concepts/synchronizations. These are not new truth-owning concepts and do not extend the Phase 003 SYN sequence.

Accepted groups:

1. **Evidence Sufficiency, Coverage & Negative Evidence — REF-001–REF-005.** Proposition binding/evidence applicability, bounded coverage/opportunity-to-observe, negative/absence/exclusion evidence, corroboration/conflict/independence, conclusion-specific sufficiency.
2. **Event/Effective Time, Knowledge Cut & Correction — REF-006–REF-012.** Event/source-availability/framework-knowledge/evaluation time, exact `as-known` eligibility, negative epistemic claims, progressive analytical availability, late/corrected evidence classes, material reassessment/reopen behavior, actual-retained versus reconstructed historical state.
3. **Causal Epistemics, Confirmation & Multiple Contributors — REF-013–REF-020.** Causal proposition/status, multidimensional support/contradiction, bounded alternatives, claim-class confirmation profiles, evidence/authority separation, multiple contributors, qualitative roles, progressive RCA, post-confirmation challenge.
4. **Exposure, Consumption, Readiness & Control Evidence — REF-021–REF-030.** Encounter-bound exposure, non-exposure coverage, criterion-relative readiness, gate decision/enforcement/execution separation, safeguard enforcement/prevention, fallback evidence, control-effect causality and retrospective revision.
5. **Consolidation / Exit Review — accepted.** E-01–E-22 and all Phase 004 scenario checks pass under REF-001–REF-030. No additional Concept, synchronization, or REF contract is required for Phase 004 exit.

### Progressive monitoring-result and RCA availability

Phase 004 establishes functional sequences rather than fixed SLAs:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**

Within RCA:

**candidate/proposed claim → early supported/weakened/unresolved evaluation → deeper investigative RCA → retrospective/confirmation review**

For controls/exposure:

**readiness/output facts → gate decision → enforcement evidence → execution/consumption evidence → negative/prevention/causal conclusions as coverage matures**.

The project should return the narrowest trustworthy result as soon as its evidence standard is satisfied. Faster job lifecycle evidence should not wait for slower schema/Metric View/DQ/RCA evidence, while early results must not overstate health, causality, exposure, or control enforcement.

Concrete timing targets remain intentionally deferred:

- **Phase 006** defines which health/schema/quality results need immediate, near-real-time, delayed, or post-ops availability and their evidence/result freshness objectives;
- **Phase 008** defines communication of progressive health/RCA/control maturity;
- **Phase 009** evaluates actual evidence-source availability, collection latency, retention, query cost, schema-evidence support, authorization-source availability, and enforcement observability;
- **Phase 010** selects fast-path/asynchronous architecture, validation placement, control-path availability strategy, and performance budgets while preserving passive-monitoring non-interference;
- **Phase 011** converts accepted timing objectives into MVP acceptance criteria.

## Pre-Phase-005 metric-health handoff

Before Phase 005, the project accepted that **table/pipeline health is broader than successful execution** and that metric design needs explicit later treatment.

The handoff establishes:

- Phase 005 governs who may define/approve/revise/waive/retire/disclose metric profiles, Expectations, thresholds, margins/tolerance bands, severity, and high-consequence metric use;
- Phase 006 defines actual metric families, per-asset metric profiles, statistical/Baseline/threshold semantics, metric bloat controls, technical/business health projections, and selective metric propagation/reconciliation;
- Phase 007 refines Lineage-aware metric propagation behavior and operational use;
- Phase 009 determines actual Databricks/Metric Views/DQX/source metric availability, cost, latency, and retention;
- Phase 010 selects precomputation/on-demand/fast-path architecture.

Metric selection should be purposeful rather than exhaustive: a small core plus critical-field/business, transformation-specific, and diagnostic/on-demand metrics. Metrics do not recursively propagate through Lineage by default; join/filter/aggregation/grain/business semantics determine valid relationships.

See `../concepts/phase_005/pre_phase_metric_health_handoff.md` and `../concepts/phase_006/README.md`.

## Pre-Group-02 schema / DDL validation handoff

Before Phase 005 Group 02, the project accepted **schema/DDL compatibility as a first-class validation dimension**.

The handoff preserves:

**governed schema meaning → normative schema contract → realized schema evidence/change → compatibility Assessment**

as separate truths, with Change Intent and Lineage/Impact supplying planned/downstream context.

Key implications:

- a successful run/load does not prove structural compatibility;
- column add/drop/rename/type/nullability/key/grain/nested-schema changes can affect downstream correctness, metric definitions, joins, and Baseline comparability;
- schema changes trigger scoped metric/Baseline/applicability review rather than automatic global reset;
- proposed/pre-deployment validation, realized-state platform validation, and independent monitoring validation can coexist because they answer different temporal questions;
- GitHub Actions, Databricks/Unity Catalog, and the monitoring framework are candidate future validation/integration locations, not selected universal mechanisms.

See `../concepts/phase_005/pre_group_02_schema_ddl_validation_handoff.md`.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** **ACTIVE — Groups 01–05 accepted; AUTH-001–AUTH-043 accepted; Group 06 next.**

Phase 005 uses `AUTH-###` governance/refinement contracts over accepted concept state. Group 01 exposed one genuine missing concept boundary: **Assertion Authority**, accepted as the **24th concept**. Groups 02–05 require no additional concept.

### Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution

**Status:** **Accepted — Assertion Authority + AUTH-001–AUTH-008.**

Accepted results include target/context/time-scoped authority, provenance-bearing authority rules, explicit conflict states, no hidden precedence, explicit co-authority/fallback rules, bitemporal authority history, and strict separation from evidence sufficiency/Capability Authorization/enforcement.

### Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance

**Status:** **Accepted — AUTH-009–AUTH-015; no new concept.**

Accepted results include facet-specific semantic/schema authority, responsibility-type authority, scheme/context-specific Classification/criticality authority, separate policy-reference/applicability authority, explicit local/context override semantics, no implicit governance propagation, and strict descriptive-governance separation from normative/operational truth.

### Group 03 — Normative Health, Metric & Threshold Governance

**Status:** **Accepted — AUTH-016–AUTH-023; no new concept.**

Accepted results include dimension/context/action-scoped Expectation authority; purposeful anti-bloat metric-profile governance; Baseline/Expectation separation; explicit schema-compatibility authority; scoped structural-change review; non-rewriting waivers; explicit normative conflict; and separate high-consequence-use eligibility.

### Group 04 — Capability Authorization & Restricted Analytical Visibility

**Status:** **Accepted — AUTH-024–AUTH-032; no new concept.**

Accepted results include exact capability/detail authorization; `allowed/denied/conditional/unknown/conflicting/unavailable`; no hidden principal-combination precedence; explicit inheritance rules; least-privilege metric/schema/Lineage/RCA visibility; separate normative action permissions; Authorized Analytical Projection without declassification; framework-processing versus requester visibility separation; inference-leakage constraints; historical authorization; and authorization/enforcement separation.

### Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority

**Status:** **Accepted — AUTH-033–AUTH-043; no new concept.**

Accepted results include:

- exact high-consequence action/lifecycle-stage authorization rather than broad operator/admin capability;
- claim-class/profile-scoped causal-confirmation authority that cannot waive REF-013–REF-020;
- granular job/run operational actions independent from raw-data/control authority;
- separately governable Execution Gate registration/configuration/normal operation/override/fallback/retirement;
- separately governable Propagation Safeguard proposal/activation/release/recovery;
- explicit multi-party approval/separation-of-duties conditions without a generic workflow concept;
- bounded delegation/temporary grants with explicit re-delegation, expiry, and revocation;
- explicit break-glass emergency authorization without universal superuser semantics;
- narrowly scoped automated/service-principal high-consequence authority;
- action-specific authorization-outage fallback and recovery without rewriting unresolved authorization truth;
- strict request/approval/action/control-plane-acceptance/enforcement/outcome audit separation.

### Remaining Phase 005 groups

6. **Disclosure, Explanation & Audience Governance — NEXT.** Govern metric/schema/threshold/policy/Lineage/causal/Impact/control disclosure, including high-consequence approval/override/break-glass/delegation/automation detail, opaque references, inference leakage, technical/business projections, and review requirements for high-consequence communication.
7. **Consolidation / Exit Review.** Compose Groups 01–06 and verify authority remains scoped/historical, permissions stay separate from truth/enforcement, restricted-data RCA remains useful, and no IAM/vendor/control/schema-validation architecture is selected.

Phase 005 may determine who/what is permitted or authoritative to confirm, configure, operate, disclose, define normative metric/schema state, or resolve assertions. It must **not** weaken/redefine Phase 004 evidence meanings, define Phase 006 metric/statistical/schema-health behavior, or select IAM/assertion-authority/control/approval implementation.

## Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** Future — not started.

Phase 006 explicitly owns the detailed health/metric/schema model, including:

- metric-family taxonomy;
- per-table/pipeline metric profiles and functional semantics for profile classes accepted in governance;
- core versus critical-field versus transformation-specific versus business-critical versus diagnostic/on-demand metrics;
- output/load, volume, freshness, **schema/DDL structural compatibility**, completeness, uniqueness, validity, distribution/quantile, relational/join/reconciliation, and business-semantic dimensions as applicable;
- required/optional column, type/precision/scale, nullability, nested-field, key/grain, and consumer-specific schema-compatibility semantics;
- metric/schema-check bloat control and lifecycle/retirement principles consistent with AUTH-017;
- hard thresholds, warning/failure margins, absolute/relative/asymmetric tolerance bands, Baseline-derived ranges, seasonality/cohort behavior, low-volume/sample-size uncertainty, and structural-change comparability;
- semantics for bounded exceptions/waivers without false pass presentation;
- scoped metric/Baseline applicability after schema/grain/key/type Change rather than global reset;
- Assessment/composite-health semantics without hiding dimension disagreement;
- selective transformation-aware metric propagation/reconciliation across pipelines;
- technical versus business health projections over the same truth;
- Databricks Metric Views/DQX semantic fit;
- functional availability expectations for immediate operational/schema checks, near-real-time core health, enriched DQ/distribution health, diagnostic/RCA metrics, and post-ops metrics;
- evidence/timing suitability for any criterion explicitly made high-consequence-use eligible under AUTH-023.

Phase 006 must not blindly calculate every possible metric, treat every schema change as universally breaking, recursively copy every upstream statistic downstream, turn waivers into false passes, or make useful passive monitoring checks synchronous production dependencies by default.

## Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement

Refine Lineage taxonomy/historical topology evidence, Change Intent realization, **planned/realized schema change and prospective downstream compatibility/blast radius**, execution reconstruction, Investigation lifecycle, prospective/actual Impact, consumer/version encounter patterns, consequence categories, Lineage-aware health/metric propagation and transformation-reconciliation behavior, safeguard placement/release, Execution Gate classes, timeout/fallback/escalation/override/recovery policy, and control-induced operational effects. Preserve Phase 004 evidence burdens, Phase 005 authority semantics, and Phase 006 metric/schema meanings.

## Phase 008 — Business Questioning and Explanation

Define question types, audience-specific Explanation structures, visible evidence citations, Authorized Analytical Projection/redaction, layered Impact/control state, authority standing/conflict communication, contemporaneous/retrospective/comparison views, reconstructed-versus-actual historical Explanation labeling, uncertainty communication, deterministic versus generative behavior, progressive result maturity communication, schema-change communication, normative conflict/waiver communication, and technical-versus-business metric/health presentation.

## Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

Determine required facts and actual evidence support for Databricks/Unity Catalog, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream consumption/version evidence, Change Intent, **declared/proposed/realized schema evidence**, safeguard/gate enforcement, authorization sources, causal evidence inputs, authority-rule sources, and accepted health/metric profiles.

Map concrete systems/actors to the Assertion Authority targets accepted in Phase 005 rather than treating source availability as authority. Determine what GitHub/GitHub Actions can prove about proposed schema contracts/DDL before deployment versus what Databricks/Unity Catalog can prove about realized schema after activation. Characterize **source production/availability time, collection latency, retention, query cost/availability, metric/schema-check computation cost, authority/authorization availability, and control-enforcement observability** needed to satisfy accepted evidence/timing semantics. Preserve the objective that baseline monitoring be independently deployed and avoid production repository/GitHub Actions changes where platform metadata is sufficient.

## Phase 010 — Technical Architecture

Only now select implementation architecture. Evaluate evidence/history storage; graph-compatible Lineage; temporal/ledger history; ingestion/synchronization; Assertion Authority and Capability Authorization realization; Databricks deployment model; out-of-band passive monitoring; **proactive CI schema validation versus runtime Unity Catalog/Databricks validation versus monitoring-app validation and their composition**; optional dependency-gating control-plane realization/availability/fallback; safeguard/quarantine realization; high-consequence approval/delegation/break-glass realization; metric precomputation/on-demand evaluation strategy; Explanation interface; testing/observability; causal reasoning implementation; and **fast-path versus asynchronous/deeper analysis architecture and performance budgets**.

A key architecture criterion remains that **ungated production jobs must not depend on monitoring-framework availability**. Explicitly gated paths may require deliberate production-critical control/authorization availability under accepted policies.