# Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** ACTIVE — Group 01 accepted; AUTH-001–AUTH-008 accepted; Group 02 next

## Goal

Refine who/what is authoritative or permitted to establish, resolve, view, confirm, operate, override, or disclose accepted ecosystem state without weakening the evidence, temporal, causal, exposure, readiness, or control-proof standards completed in Phase 004.

Phase 005 is a governance/authority/capability refinement phase. It must not select IAM technology, redefine Phase 004 evidence sufficiency, silently treat vendor/source ownership as authority, or prematurely design the Phase 006 metric/statistical model.

Phase 005 authority contracts use `AUTH-###` identifiers. They are refinement/governance contracts over accepted concepts, not new Phase 003 synchronizations and not substitutes for concept ownership. Group 01 did expose one genuine missing concept boundary: **Assertion Authority**, accepted as the 24th concept.

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

## Pre-phase metric-health handoff

The accepted pre-Phase-005 metric consideration is documented in [`pre_phase_metric_health_handoff.md`](pre_phase_metric_health_handoff.md).

Phase 005 owns **governance around metrics**, not the metric/statistical model itself. In particular, Phase 005 should establish who may define/approve/revise/waive/retire metric profiles, Expectations, thresholds, margins/tolerance bands, severity and audience disclosure. Phase 006 will define the actual metric families, table/pipeline metric profiles, threshold semantics, bloat controls, audience health projections, and selective metric propagation behavior.

A metric used by an Execution Gate or other high-consequence control requires both accepted metric/Expectation authority and the Phase 004 evidence/control standards; authority does not make the metric timely or sufficient by itself.

## Delivery-group design

The phase is reviewed in **seven logical groups**. The grouping is a design/review dependency, not an implementation or service boundary.

### Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution
**Status:** **Accepted — AUTH-001–AUTH-008; Assertion Authority added as 24th concept.**

Defines common authority targets, assertion standing, authority-rule provenance, conflict vocabulary, explicit precedence/co-authority/fallback, temporal correction, and separation from evidence/permission/enforcement.

### Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance
**Status:** **Next — not started.**

Apply Group 01 authority semantics to descriptive/governance state: Semantic Definition facets, Responsibility Assignment types, Classification schemes, Policy Context applicability, criticality, contextual overrides, stewardship, and historical supersession.

Boundary: descriptive/governance authority does not automatically grant normative, access, or production-control authority.

### Group 03 — Normative Health, Metric & Threshold Governance
**Status:** Planned.

Define who may establish/revise Expectations, metric profiles, thresholds, warning/failure margins, tolerance bands, severity, exceptions/waivers, retirement, and high-consequence metric use.

Boundary: Phase 006 owns metric families, statistical behavior, Baseline comparison, propagation, aggregation, and health semantics.

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

Govern which metric, threshold, policy, Lineage, causal, Impact, safeguard, gate, Annotation, and consequence details may be disclosed; opaque references; inference leakage; technical versus business projections; and review requirements for high-consequence communication.

### Group 07 — Phase 005 Consolidation / Exit Review
**Status:** Planned.

Compose Groups 01–06 and verify authority remains scoped/historical, conflicts remain representable, permissions stay separate from truth/enforcement, restricted-data RCA remains useful, and no IAM/vendor/control architecture is selected.

## Phase boundaries

Phase 005 must not:

- redefine Phase 004 evidence sufficiency/coverage or causal-confirmation evidence semantics;
- grant authority merely from source count, recency, repository ownership, technical availability, synchronization order, job creator identity, organizational title, or responsibility;
- treat authority as factual infallibility;
- treat policy applicability as enforcement/compliance proof;
- make derived evidence automatically unrestricted;
- define the detailed Phase 006 metric taxonomy/statistical model or blindly propagate metrics through Lineage;
- select RBAC/ABAC/IAM/provider architecture;
- select Databricks/Collibra/Immuta/GitHub/Unity Catalog as universally authoritative by default;
- select scheduler/orchestrator, quarantine, causal, graph, LLM, metric storage, rule engine, or persistence architecture;
- begin Phase 006 health/statistical/timing refinement without explicit user direction.

## Phase direction

**Phase 005 Group 01 is accepted. Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance is next and has not started.**
