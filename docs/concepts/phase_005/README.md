# Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** ACTIVE — Groups 01–02 accepted; AUTH-001–AUTH-015 accepted; Group 03 next

## Goal

Refine who/what is authoritative or permitted to establish, resolve, view, confirm, operate, override, or disclose accepted ecosystem state without weakening the evidence, temporal, causal, exposure, readiness, or control-proof standards completed in Phase 004.

Phase 005 is a governance/authority/capability refinement phase. It must not select IAM technology, redefine Phase 004 evidence sufficiency, silently treat vendor/source ownership as authority, or prematurely design the Phase 006 metric/statistical/schema-health model.

Phase 005 authority contracts use `AUTH-###` identifiers. They are refinement/governance contracts over accepted concepts, not new Phase 003 synchronizations and not substitutes for concept ownership. Group 01 did expose one genuine missing concept boundary: **Assertion Authority**, accepted as the 24th concept. Group 02 required no additional concept.

## Accepted handoff from Phase 004

- evidence applicability, bounded coverage, corroboration/conflict, and conclusion-specific sufficiency are independent from source/actor authority;
- missing/restricted/unavailable evidence remains a limitation, never a negative fact;
- evidence sufficiency does not grant Capability Authorization or action authority;
- internal evidentiary sufficiency can coexist with requester-visible redaction/opacity;
- causal `confirmed` status requires both the accepted evidence gate and independently resolved confirmation authority/capability;
- raw-data read, metadata/health visibility, Lineage/RCA participation, job operation, safeguard actions, Execution Gate actions/override, causal confirmation, and Explanation access remain independently resolvable capabilities;
- responsibility, Classification, Policy Context, Monitoring Scope, repository ownership, job creator identity, administrator status, or analyst role do not silently grant those capabilities;
- gate/safeguard configuration/operation authority is separate from evidence that the control was actually enforced;
- historical authorization is reconstructable evidence about past capability but never overrides current requester disclosure authorization;
- restricted metadata/derived evidence can itself be sensitive and is not automatically safe to disclose;
- conflicting applicable evidence/assertions remain conflict until accepted category/context-specific authority semantics resolve them.

## Accepted Group 01 — Assertion Authority and AUTH-001–AUTH-008

Group 01 accepts **Assertion Authority** as a narrow post-Phase-002 addendum because source-precedence/conflict/history behavior recurs across Semantic Definition, Responsibility Assignment, Classification, Policy Context, Expectation, and later metric/threshold governance.

Assertion Authority answers:

> Which source/actor/role/governed process has authoritative standing for this exact assertion category/facet/subject scope/context/time?

It does not answer whether the assertion is factually infallible, whether evidence is sufficient, whether the principal is allowed to perform an action, or whether a control actually enforced something.

Accepted authority contracts:

- **AUTH-001** — Authority Target Binding and Vocabulary;
- **AUTH-002** — Authority Rule Provenance and Governing Basis;
- **AUTH-003** — Assertion Standing and Conditional Authority;
- **AUTH-004** — Assertion Disagreement and Authority Conflict;
- **AUTH-005** — Explicit Precedence, Co-Authority, and Fallback;
- **AUTH-006** — Authority Revision, Correction, Supersession, and Time;
- **AUTH-007** — Unknown, Unavailable, and Resolution Limits;
- **AUTH-008** — Authority Separation from Evidence, Permission, Responsibility, Policy, and Enforcement.

Key Group 01 decisions:

- authority is category/facet/context/time scoped, never universal by default;
- assertion recording and authoritative standing are separate;
- source count, recency, ingestion order, availability, repository ownership, title, responsibility, and apparent specificity do not create authority;
- co-authoritative disagreement remains authoritative conflict unless an explicit resolver applies;
- conditional/fallback authority requires an explicit rule plus evidence that its condition holds;
- authority rules require provenance/governing basis and cannot self-validate;
- authority history is bitemporal and corrections do not rewrite what was known then;
- authority cannot waive REF-001–REF-030 evidence burdens or prove enforcement.

See [`01_authority_vocabulary_and_conflict/README.md`](01_authority_vocabulary_and_conflict/README.md) and [`../phase_002/addenda/assertion_authority.md`](../phase_002/addenda/assertion_authority.md).

## Accepted pre-Group-02 schema / DDL validation handoff

[`pre_group_02_schema_ddl_validation_handoff.md`](pre_group_02_schema_ddl_validation_handoff.md) records schema/DDL compatibility as a first-class pipeline-health concern.

The accepted split is:

- governed schema/grain/key/field meaning → Semantic Definition;
- normative schema/compatibility requirement → Expectation;
- realized schema state/change → Observation/Change;
- planned schema evolution → Change Intent;
- conformance/health → Assessment;
- downstream compatibility/effect → Lineage/Impact/Investigation/Causal Claim as applicable.

Pre-deployment validation in source control/CI, realized-state validation from Databricks/Unity Catalog metadata, and independent monitoring validation may all be useful because they answer different temporal questions. No universal validation location is selected in Phase 005.

## Accepted Group 02 — Semantic / Governance Authority and AUTH-009–AUTH-015

Group 02 applies Assertion Authority to descriptive/governance truth while preserving descriptive, normative, observed, authorization, Impact, and enforcement boundaries.

Accepted contracts:

- **AUTH-009** — Semantic Facet and Schema-Meaning Authority;
- **AUTH-010** — Responsibility-Type Authority and Assignment Governance;
- **AUTH-011** — Classification-Scheme and Criticality Authority;
- **AUTH-012** — Policy-Context Applicability Authority;
- **AUTH-013** — Contextual Overrides, Local Governance, and Cross-Facet Conflict;
- **AUTH-014** — Derived, Inherited, and Propagated Governance Assertions;
- **AUTH-015** — Governance State Separation from Normative Health and Operational Truth.

Key Group 02 results:

- semantic authority is facet-specific; business definition, technical schema declaration, grain, units, population, calculation meaning, field roles, and key roles may have different holders;
- **declared/governed schema meaning ≠ normative schema contract ≠ realized schema state**;
- declared key role does not prove uniqueness/nullability health;
- column rename identity is not inferred from drop/add names alone;
- responsibility authority is responsibility-type scoped and assignment does not grant semantic/policy/access/control authority;
- Classification authority is scheme/context specific;
- business/operational/consumer/delivery criticality remains Classification under explicit schemes/contexts rather than a new concept;
- criticality influences priority/context but does not prove exposure, consequence, health failure, or cause;
- policy text/reference authority may differ from subject/context policy-applicability authority;
- narrower/local governance does not automatically override broader governance unless an explicit authority rule defines the relationship;
- Lineage, repository/container membership, schema/tag inference, and parent state do not implicitly propagate governance assertions or authority;
- descriptive governance authority does not become normative health, Capability Authorization, control enforcement, compliance, or actual Impact truth;
- Group 02 schema/governance scenarios require no 25th concept.

See [`02_semantic_governance_authority/README.md`](02_semantic_governance_authority/README.md).

## Pre-phase metric-health handoff

The accepted pre-Phase-005 metric consideration is documented in [`pre_phase_metric_health_handoff.md`](pre_phase_metric_health_handoff.md).

Phase 005 owns **governance around metrics**, not the metric/statistical model itself. In particular, Phase 005 should establish who may define/approve/revise/waive/retire metric profiles, Expectations, thresholds, margins/tolerance bands, severity and audience disclosure. Phase 006 will define the actual metric families, table/pipeline metric profiles, threshold semantics, schema-health checks, bloat controls, audience health projections, and selective metric propagation behavior.

A metric or schema Expectation used by an Execution Gate or other high-consequence control requires both accepted normative authority and the Phase 004 evidence/control standards; authority does not make the condition timely or sufficient by itself.

## Delivery-group design

The phase is reviewed in **seven logical groups**. The grouping is a design/review dependency, not an implementation or service boundary.

### Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution
**Status:** **Accepted — AUTH-001–AUTH-008; Assertion Authority added as 24th concept.**

### Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance
**Status:** **Accepted — AUTH-009–AUTH-015; no new concept.**

Defines facet-specific semantic/schema authority, responsibility-type governance, scheme-specific Classification/criticality authority, Policy Context applicability authority, explicit contextual override/conflict semantics, no implicit governance propagation, and descriptive-governance separation from normative/operational truth.

### Group 03 — Normative Health, Metric & Threshold Governance
**Status:** **Next — not started.**

Define who may establish/revise Expectations, metric profiles, **schema compatibility Expectations**, thresholds, warning/failure margins, tolerance bands, severity, exceptions/waivers, retirement, and high-consequence metric/schema-condition use.

Boundary: Phase 006 owns metric families, schema-health/compatibility semantics, statistical behavior, Baseline comparison, propagation, aggregation, and health meanings.

### Group 04 — Capability Authorization & Restricted Analytical Visibility
**Status:** Planned.

Refine canonical capability vocabulary; allow/deny/conditional/unknown/conflicting states; purpose/environment/tenant/subject/time conditions; user/group/role/service-principal interactions; current versus historical authorization; and Authorized Analytical Projection.

Boundary: do not select RBAC/ABAC/IAM or declassification architecture.

### Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority
**Status:** Planned.

Refine causal-confirmation capability, job operations, safeguard/gate configuration/activation/release/override, delegation, multi-party approval, break-glass, expiry/revocation, and separation of duties.

Boundary: authority never weakens REF-013–REF-030 evidence/control standards or proves action success.

### Group 06 — Disclosure, Explanation & Audience Governance
**Status:** Planned.

Govern which metric, schema, threshold, policy, Lineage, causal, Impact, safeguard, gate, Annotation, and consequence details may be disclosed; opaque references; inference leakage; technical versus business projections; and review requirements for high-consequence communication.

### Group 07 — Phase 005 Consolidation / Exit Review
**Status:** Planned.

Compose Groups 01–06 and verify authority remains scoped/historical, conflicts remain representable, permissions stay separate from truth/enforcement, restricted-data RCA remains useful, and no IAM/vendor/control/schema-validation architecture is selected.

## Phase boundaries

Phase 005 must not:

- redefine Phase 004 evidence sufficiency/coverage or causal-confirmation evidence semantics;
- grant authority merely from source count, recency, repository ownership, technical availability, synchronization order, job creator identity, organizational title, or responsibility;
- treat authority as factual infallibility;
- treat policy applicability as enforcement/compliance proof;
- make derived evidence/governance state automatically unrestricted or authoritative;
- define the detailed Phase 006 metric/schema-health/statistical model or blindly propagate metrics/governance through Lineage;
- select RBAC/ABAC/IAM/provider architecture;
- select Databricks/Collibra/Immuta/GitHub/Unity Catalog as universally authoritative by default;
- select GitHub Actions, Unity Catalog, or the monitoring application as the universal schema-validation location;
- select scheduler/orchestrator, quarantine, causal, graph, LLM, metric storage, rule engine, or persistence architecture;
- begin Phase 006 health/statistical/timing refinement without explicit user direction.

## Phase direction

**Phase 005 Groups 01–02 are accepted with AUTH-001–AUTH-015. Group 03 — Normative Health, Metric & Threshold Governance is next and has not started.**
