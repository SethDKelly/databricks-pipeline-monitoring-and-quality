# Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** Next phase — not yet started

## Goal

Refine who/what is authoritative or permitted to establish, resolve, view, confirm, operate, override, or disclose accepted ecosystem state without weakening the evidence, temporal, causal, exposure, readiness, or control-proof standards completed in Phase 004.

Phase 005 is a governance/authority/capability refinement phase. It must not select IAM technology, redefine Phase 004 evidence sufficiency, silently treat vendor/source ownership as authority, or prematurely design the Phase 006 metric/statistical model.

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

## Pre-phase metric-health handoff

The accepted pre-Phase-005 metric consideration is documented in [`pre_phase_metric_health_handoff.md`](pre_phase_metric_health_handoff.md).

Phase 005 owns **governance around metrics**, not the metric/statistical model itself. In particular, Phase 005 should establish who may define/approve/revise/waive/retire metric profiles, Expectations, thresholds, margins/tolerance bands, severity and audience disclosure. Phase 006 will define the actual metric families, table/pipeline metric profiles, threshold semantics, bloat controls, audience health projections, and selective metric propagation behavior.

A metric used by an Execution Gate or other high-consequence control requires both accepted metric/Expectation authority and the Phase 004 evidence/control standards; authority does not make the metric timely or sufficient by itself.

## Delivery-group design

The phase will be reviewed in **seven logical groups**. The grouping is a design/review dependency, not an implementation or service boundary.

### Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution

**Purpose:** define the common authority model before applying it to specific governance categories.

Primary questions:

- What is the difference between a source assertion, authoritative assertion, advisory/enriching assertion, correction, supersession, and unresolved conflict?
- How is authority scoped by category, subject, environment, tenant/context, purpose, effective time, and knowledge time?
- What makes an authority rule itself valid and provenance-bearing?
- How do source/actor conflicts remain visible when no accepted precedence rule resolves them?
- How do corrections/supersessions change current authoritative state without deleting historical assertions?
- Which authority questions belong to Phase 005 versus source-specific evidence contracts in Phase 009?

**Boundary:** do not decide that Databricks, GitHub, Collibra, Immuta, or any human role is universally authoritative.

### Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance

**Purpose:** apply Group 01 authority semantics to descriptive/governance context.

Primary questions:

- Who/what may establish or revise Semantic Definition facets?
- Who/what may establish Responsibility Assignment and stewardship roles?
- Which sources/actors are authoritative for Classification and Policy Context by context?
- Who may establish business/operational criticality?
- How do governance conflicts, local overrides, context-specific definitions, and historical supersession behave?
- How do policy/classification assertions influence handling without becoming compliance or health conclusions?

**Boundary:** descriptive/governance authority does not automatically grant normative, access, or production-control authority.

### Group 03 — Normative Health, Metric & Threshold Governance

**Purpose:** define who is permitted/authoritative to establish the normative health rules that Phase 006 will later give detailed metric semantics.

Primary questions:

- Who may establish/revise an Expectation by asset, health dimension, environment, business context, or consumer?
- Who may approve a table/pipeline metric profile or declare a metric business-critical?
- Who may set/revise thresholds, warning/failure margins, tolerance bands, severity, or bounded exceptions?
- How are temporary waivers/exceptions authorized without changing Observation or pretending the underlying condition is healthy?
- Who may retire a metric/Expectation and what historical state must remain?
- How are conflicting technical and business thresholds resolved without majority vote or hidden source precedence?
- Which metric/Expectation authority is required before a metric may participate in an Execution Gate or other high-consequence decision?

**Boundary:** Group 03 decides authority/governance only. Phase 006 defines metric families, statistical behavior, Baseline comparison, propagation, aggregation, and health semantics.

### Group 04 — Capability Authorization & Restricted Analytical Visibility

**Purpose:** refine permission truth independently from governance authority and evidence sufficiency.

Primary questions:

- What capability vocabulary is required for direct/raw data, metadata/governance, metric/Assessment visibility, Lineage/RCA, operational job actions, safeguard actions, gate actions/override, causal confirmation, Annotation, and Explanation?
- How do `allow`, `deny`, `conditional`, `unknown`, and `conflicting` authorization states behave?
- How are purpose, environment, tenant, subject, consumer, time, and emergency/break-glass conditions represented?
- How do user/group/role/service-principal grants combine without hidden precedence?
- What current-versus-historical authorization semantics are required?
- How can useful restricted-data analysis remain available through Authorized Analytical Projection without inference leakage?

**Boundary:** do not select RBAC, ABAC, IAM provider, enforcement architecture, or declassification mechanism.

### Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority

**Purpose:** refine who may perform or authorize actions whose consequences extend beyond ordinary viewing/analysis.

Primary questions:

- Who may confirm which Causal Claim classes under which accepted confirmation profiles?
- Which claim classes require explicit human confirmation versus possibly authorized automation?
- Who may configure/enable/retire/override an Execution Gate?
- Who may propose/activate/release/cancel/expire a Propagation Safeguard?
- Which job/run operational actions require distinct capability from gate/safeguard authority?
- What delegation, multi-party approval, emergency/break-glass, expiry, revocation, or separation-of-duties semantics are needed?
- How do action authority and actual enforcement/success evidence remain distinct?

**Boundary:** authority never weakens REF-013–REF-030 confirmation/control evidence standards and does not select scheduler/orchestrator/quarantine implementation.

### Group 06 — Disclosure, Explanation & Audience Governance

**Purpose:** govern what authorized audiences can learn from otherwise valid ecosystem truth.

Primary questions:

- Which metric, threshold, policy, Lineage, causal, Impact, safeguard, gate, Annotation, and business-consequence details may be disclosed by audience/capability?
- When may a restricted entity/path be acknowledged but remain opaque?
- How should technical teams receive detailed diagnostic metrics while business audiences receive smaller semantic health projections without creating different truth?
- Which high-consequence statements require additional review before business/client-facing Explanation?
- How should redaction/opacity preserve evidence limitations without implying hidden evidence is absent?
- What historical authorization/disclosure information may itself be safely exposed?

**Boundary:** Phase 006/008 define metric-health and Explanation presentation semantics; this group defines governance/permission constraints on disclosure.

### Group 07 — Phase 005 Consolidation / Exit Review

**Purpose:** compose Groups 01–06 across representative ecosystem scenarios and verify authority semantics do not steal truth from evidence-bearing concepts/refinements.

Exit checks should confirm:

- authority is category/context/time scoped rather than universal;
- conflicting authority/assertion state remains representable;
- semantic/governance authority does not imply access/control authority;
- metric/Expectation authority does not define metric statistical meaning;
- Capability Authorization remains independent from Responsibility Assignment, Policy Context, and source authority;
- causal confirmation/control permission never weakens Phase 004 evidence requirements;
- action authorization remains separate from action/enforcement success;
- disclosure governance supports restricted-data RCA without inference leakage;
- historical authority/authorization remains reconstructable without granting current access;
- no IAM, source-vendor, scheduler, metric engine, or technical architecture is selected.

## Phase boundaries

Phase 005 must not:

- redefine Phase 004 evidence sufficiency/coverage or causal-confirmation evidence semantics;
- grant authority merely from source count, recency, repository ownership, technical availability, synchronization order, job creator identity, or organizational title;
- treat policy applicability as enforcement/compliance proof;
- make derived evidence automatically unrestricted;
- define the detailed Phase 006 metric taxonomy/statistical model or blindly propagate metrics through Lineage;
- select RBAC/ABAC/IAM/provider architecture;
- select Databricks/Collibra/Immuta/GitHub as universally authoritative by default;
- select scheduler/orchestrator, quarantine, causal, graph, LLM, metric storage, or persistence architecture;
- begin Phase 006 health/statistical/timing refinement without explicit user direction.

## Phase start direction

When Phase 005 begins, start with **Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution**. Do not start later groups or Phase 006 unless explicitly requested.

**Phase 005 has not started.**