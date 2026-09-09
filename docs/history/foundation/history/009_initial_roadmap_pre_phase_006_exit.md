# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, evidence semantics, governance/authority, health/metric/schema semantics, integration evidence, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery
**Status:** Complete.

## Phase 002 — Concept Specifications
**Status:** **Complete with four accepted post-exit addenda.**

The original five groups accepted 20 concepts. Later work added **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and during Phase 005 Group 01 **Assertion Authority** after review exposed independent missing behavior. Current catalog: **24 concepts**.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Complete — Groups 01–06 accepted; SYN-001–SYN-035 accepted; E-01–E-22 pass.**

Phase 003 defines end-to-end coordination for subject/governance context; planned change/reference transition; runtime timing/health/change; optional execution gating; safeguards; Investigation/causality; layered downstream Impact; Annotation; authorized analytical projection/Explanation; and bitemporal historical replay.

## Phase 004 — Evidence, Time, and Causality Refinement

**Status:** **Complete — Groups 01–05 accepted; REF-001–REF-030 accepted.**

Accepted groups:

1. **Evidence Sufficiency, Coverage & Negative Evidence — REF-001–REF-005.** Proposition binding, applicability, bounded coverage/opportunity-to-observe, negative/absence/exclusion evidence, corroboration/conflict/independence, conclusion-specific sufficiency.
2. **Event/Effective Time, Knowledge Cut & Correction — REF-006–REF-012.** Event/source-availability/framework-knowledge/evaluation time, exact `as-known` eligibility, negative epistemic claims, progressive analytical availability, late/corrected evidence classes, material reassessment/reopen behavior, actual-retained versus reconstructed historical state.
3. **Causal Epistemics, Confirmation & Multiple Contributors — REF-013–REF-020.** Causal proposition/status, multidimensional support/contradiction, bounded alternatives, claim-class confirmation profiles, evidence/authority separation, multiple contributors, qualitative roles, progressive RCA, post-confirmation challenge.
4. **Exposure, Consumption, Readiness & Control Evidence — REF-021–REF-030.** Encounter-bound exposure, non-exposure coverage, criterion-relative readiness, gate decision/enforcement/execution separation, safeguard enforcement/prevention, fallback evidence, control-effect causality, retrospective revision.
5. **Consolidation / Exit Review — accepted.** E-01–E-22 and all Phase 004 scenario checks pass. No additional Concept, SYN, or REF contract required.

### Progressive monitoring-result and RCA availability

Phase 004 establishes functional sequences rather than fixed SLAs:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**

Within RCA:

**candidate/proposed → supported/weakened/unresolved → deeper investigation → retrospective/confirmation review**

For controls/exposure:

**readiness/output facts → gate decision → enforcement evidence → execution/consumption evidence → negative/prevention/causal conclusions as coverage matures**.

Return the narrowest trustworthy result as soon as its evidence standard is satisfied. Faster job lifecycle evidence should not wait for slower schema/Metric View/DQ/RCA evidence, while early results must not overstate health, causality, exposure, or control enforcement.

Concrete timing targets remain later work:

- **Phase 006** defines functional health/schema/quality result timing and evidence/result freshness;
- **Phase 008** defines communication of progressive health/RCA/control maturity;
- **Phase 009** evaluates actual evidence-source availability, collection latency, retention, query cost, authorization-source availability, and enforcement observability;
- **Phase 010** selects fast-path/asynchronous architecture, validation placement, control-path availability strategy, and performance budgets;
- **Phase 011** later converts accepted timing objectives into MVP acceptance criteria.

## Pre-Phase-005 metric-health handoff

The project accepts that **table/pipeline health is broader than successful execution**.

The handoff establishes:

- Phase 005 governs who may define/approve/revise/waive/retire/disclose metric profiles, Expectations, thresholds, margins/tolerance bands, severity, and high-consequence metric use;
- Phase 006 defines actual metric families, per-asset metric profiles, statistical/Baseline/threshold semantics, metric-bloat controls, technical/business health projections, and selective metric propagation/reconciliation;
- Phase 007 refines Lineage-aware metric propagation behavior and operational use;
- Phase 009 determines actual Databricks/Metric Views/DQX/source metric availability, cost, latency, and retention;
- Phase 010 selects precomputation/on-demand/fast-path architecture.

Metric selection should be purposeful rather than exhaustive: a small core plus critical-field/business, transformation-specific, and diagnostic/on-demand metrics. Metrics do not recursively propagate through Lineage by default; join/filter/aggregation/grain/business semantics determine valid relationships.

## Pre-Group-02 schema / DDL validation handoff

Schema/DDL compatibility is a first-class validation dimension.

Preserve:

**governed schema meaning → normative schema contract → realized schema evidence/change → compatibility Assessment**

as separate truths, with Change Intent and Lineage/Impact supplying planned/downstream context.

Key implications:

- successful run/load does not prove structural compatibility;
- add/drop/rename/type/nullability/key/grain/nested-schema changes can affect downstream correctness, metrics, joins, and Baseline comparability;
- schema changes trigger scoped metric/Baseline/applicability review rather than automatic global reset;
- proposed/pre-deployment validation, realized-state platform validation, and independent monitoring validation can coexist because they answer different temporal questions;
- GitHub Actions, Databricks/Unity Catalog, and the monitoring framework remain candidate later validation locations rather than universal mechanisms.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** **COMPLETE — Groups 01–07 accepted; AUTH-001–AUTH-053 final.**

Phase 005 uses `AUTH-###` governance/refinement contracts over accepted concept state. Group 01 exposed one genuine missing concept boundary: **Assertion Authority**, accepted as the **24th concept**. Groups 02–07 require no additional concept.

### Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution
**Status:** Accepted — Assertion Authority + AUTH-001–AUTH-008.

Target/context/time-scoped authority; provenance-bearing rules; explicit conflicts; no hidden precedence; explicit co-authority/fallback; bitemporal authority history; strict separation from evidence sufficiency, permission, and enforcement.

### Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance
**Status:** Accepted — AUTH-009–AUTH-015.

Facet-specific semantic/schema authority; responsibility-type authority; scheme/context-specific Classification/criticality authority; separate policy-reference/applicability authority; explicit contextual override semantics; no implicit governance propagation; descriptive governance separated from normative/operational truth.

### Group 03 — Normative Health, Metric & Threshold Governance
**Status:** Accepted — AUTH-016–AUTH-023.

Dimension/context/action-scoped Expectation authority; purposeful anti-bloat metric-profile governance; Baseline/Expectation separation; explicit schema-compatibility authority; scoped structural-change review; non-rewriting waivers; explicit normative conflict; separate high-consequence-use eligibility.

### Group 04 — Capability Authorization & Restricted Analytical Visibility
**Status:** Accepted — AUTH-024–AUTH-032.

Exact capability/detail authorization; explicit allowed/denied/conditional/unknown/conflicting/unavailable states; no hidden principal-combination precedence; explicit inheritance rules; least-privilege metric/schema/Lineage/RCA visibility; Authorized Analytical Projection without declassification; framework-processing versus requester visibility separation; inference-leakage constraints; historical authorization; permission/enforcement separation.

### Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority
**Status:** Accepted — AUTH-033–AUTH-043.

Exact action/lifecycle-stage authority; jointly evidence- and authority-gated causal confirmation; granular job operations; decomposed gate/safeguard authority; explicit multi-party/separation-of-duties conditions; bounded delegation; break-glass; narrowly scoped automation; action-specific authorization-outage fallback; request/approval/issuance/acceptance/enforcement/outcome audit separation.

### Group 06 — Disclosure, Explanation & Audience Governance
**Status:** Accepted — AUTH-044–AUTH-053.

Audience/purpose/context/delivery-scoped disclosure; result/basis visibility separation; safe abstraction and opaque existence; mosaic/repeated-query inference leakage; one truth across technical/business/executive/audit views; high-consequence communication review; status-preserving language; sensitive actor/authority/control metadata; historical disclosure separation; unresolved disclosure state without fabricated permission/deny.

### Group 07 — Consolidation / Exit Review
**Status:** Accepted — Phase 005 exit.

G07-01–G07-26 replay the authority stack across metric/schema governance, threshold conflict/waiver, structural-change comparability, restricted RCA, causal confirmation, gating, safeguard release, break-glass, automation, audience disclosure, and historical replay.

Exit result:

- **24 concepts**;
- **AUTH-001–AUTH-053 final**;
- no AUTH-054;
- no architecture selected;
- Phase 005 authority stack composes without moving operational/health/causal/control truth into a policy umbrella.

See `../concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md`.

## Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** **NEXT — not started.**

Phase 006 owns the detailed health/metric/schema model, including:

- metric-family taxonomy;
- per-table/pipeline metric profiles;
- core versus critical-field/business versus transformation-specific versus diagnostic/on-demand metrics;
- output/load, volume, freshness, schema/DDL compatibility, completeness, uniqueness, validity, distribution/quantile, relational/join/reconciliation, and business-semantic dimensions;
- required/optional column, type/precision/scale, nullability, nested-field, key/grain, and consumer-specific schema-compatibility semantics;
- metric/schema-check bloat control and lifecycle/retirement principles consistent with AUTH-017;
- hard thresholds, warning/failure margins, absolute/relative/asymmetric tolerances, Baseline-derived ranges, seasonality/cohort behavior, low-volume/sample-size uncertainty, and structural-change comparability;
- bounded waiver/exception representation without false pass;
- scoped metric/Baseline applicability after schema/grain/key/type Change rather than global reset;
- Assessment/composite-health semantics without hiding dimension disagreement/conflict/unknown state;
- selective transformation-aware metric propagation/reconciliation;
- technical versus business health projections over the same truth under AUTH-044–AUTH-053;
- Metric Views/DQX semantic fit;
- functional availability expectations for immediate operational/schema checks, near-real-time core health, enriched DQ/distribution health, diagnostic/RCA metrics, and post-ops metrics;
- evidence/timing suitability for conditions made high-consequence-use eligible under AUTH-023.

Phase 006 must not blindly calculate every possible metric, treat every schema change as universally breaking, recursively copy every upstream statistic downstream, turn waivers into false passes, hide conflicts behind a universal health score, or make useful passive monitoring checks synchronous production dependencies by default.

## Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement

Refine Lineage taxonomy/historical topology evidence, Change Intent realization, planned/realized schema change and prospective downstream compatibility/blast radius, execution reconstruction, Investigation lifecycle, prospective/actual Impact, consumer/version encounter patterns, consequence categories, Lineage-aware health/metric propagation and transformation-reconciliation behavior, safeguard placement/release, Execution Gate classes, timeout/fallback/escalation/override/recovery policy, and control-induced operational effects.

## Phase 008 — Business Questioning and Explanation

Define question types, audience-specific Explanation structures, visible evidence citations, Authorized Analytical Projection/redaction behavior, layered Impact/control state, authority standing/conflict communication, contemporaneous/retrospective/comparison views, actual-retained versus reconstructed Explanation labeling, uncertainty communication, deterministic versus generative behavior, progressive result maturity, schema-change communication, normative conflict/waiver communication, and technical-versus-business metric/health presentation under AUTH-044–AUTH-053.

## Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

Determine required facts and actual support for Databricks/Unity Catalog, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream consumption/version evidence, Change Intent, declared/proposed/realized schema evidence, safeguard/gate enforcement, authorization sources, causal evidence inputs, authority-rule sources, disclosure/review authority, and accepted health/metric profiles.

Map concrete systems/actors to Phase 005 authority targets rather than treating source availability as authority. Characterize source production/availability time, collection latency, retention, query cost/availability, metric/schema-check computation cost, authority/authorization availability, and control-enforcement observability.

## Phase 010 — Technical Architecture

Only now select implementation architecture. Evaluate evidence/history storage; graph-compatible Lineage; temporal/ledger history; ingestion/synchronization; Assertion Authority and Capability Authorization realization; Databricks deployment model; out-of-band passive monitoring; proactive CI schema validation versus runtime Unity Catalog/Databricks validation versus monitoring-app validation; optional dependency-gating control-plane realization/availability/fallback; safeguard/quarantine realization; high-consequence approval/delegation/break-glass realization; disclosure/redaction mechanisms; metric precomputation/on-demand strategy; Explanation interface; testing/observability; causal reasoning implementation; and fast-path versus asynchronous/deeper analysis architecture and performance budgets.

A key architecture criterion remains that **ungated production jobs must not depend on monitoring-framework availability**. Explicitly gated paths may require deliberate production-critical evidence/authorization/control availability under accepted policies.
