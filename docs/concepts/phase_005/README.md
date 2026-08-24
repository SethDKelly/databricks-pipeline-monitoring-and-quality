# Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** ACTIVE — Groups 01–06 accepted; AUTH-001–AUTH-053 accepted; Group 07 next

## Goal

Refine who/what is authoritative or permitted to establish, resolve, view, confirm, operate, override, or disclose accepted ecosystem state without weakening the evidence, temporal, causal, exposure, readiness, or control-proof standards completed in Phase 004.

Phase 005 is a governance/authority/capability refinement phase. It must not select IAM technology, redefine Phase 004 evidence sufficiency, silently treat vendor/source ownership as authority, or prematurely design the Phase 006 metric/statistical/schema-health model.

Phase 005 authority contracts use `AUTH-###` identifiers. They are refinement/governance contracts over accepted concepts, not new Phase 003 synchronizations and not substitutes for concept ownership. Group 01 exposed one genuine missing concept boundary: **Assertion Authority**, accepted as the 24th concept. Groups 02–06 required no additional concept.

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

Accepted contracts:

- AUTH-001 — Authority Target Binding and Vocabulary;
- AUTH-002 — Authority Rule Provenance and Governing Basis;
- AUTH-003 — Assertion Standing and Conditional Authority;
- AUTH-004 — Assertion Disagreement and Authority Conflict;
- AUTH-005 — Explicit Precedence, Co-Authority, and Fallback;
- AUTH-006 — Authority Revision, Correction, Supersession, and Time;
- AUTH-007 — Unknown, Unavailable, and Resolution Limits;
- AUTH-008 — Authority Separation from Evidence, Permission, Responsibility, Policy, and Enforcement.

Key results:

- authority is category/facet/context/time scoped, never universal by default;
- assertion recording and authoritative standing are separate;
- source count, recency, ingestion order, availability, repository ownership, title, responsibility, and apparent specificity do not create authority;
- co-authoritative disagreement remains authoritative conflict unless an explicit resolver applies;
- conditional/fallback authority requires an explicit rule plus evidence that its condition holds;
- authority rules require provenance/governing basis and cannot self-validate;
- authority history is bitemporal and corrections do not rewrite what was known then;
- authority cannot waive REF-001–REF-030 evidence burdens or prove enforcement.

See [`01_authority_vocabulary_and_conflict/README.md`](01_authority_vocabulary_and_conflict/README.md).

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

Accepted contracts:

- AUTH-009 — Semantic Facet and Schema-Meaning Authority;
- AUTH-010 — Responsibility-Type Authority and Assignment Governance;
- AUTH-011 — Classification-Scheme and Criticality Authority;
- AUTH-012 — Policy-Context Applicability Authority;
- AUTH-013 — Contextual Overrides, Local Governance, and Cross-Facet Conflict;
- AUTH-014 — Derived, Inherited, and Propagated Governance Assertions;
- AUTH-015 — Governance State Separation from Normative Health and Operational Truth.

Key results:

- semantic authority is facet-specific across business definition, technical schema declaration, grain, units, population, calculation meaning, field roles, and key roles;
- **declared/governed schema meaning ≠ normative schema contract ≠ realized schema state**;
- declared key role does not prove uniqueness/nullability health;
- column rename identity is not inferred from drop/add names alone;
- responsibility authority is responsibility-type scoped;
- Classification authority is scheme/context specific;
- business/operational/consumer/delivery criticality remains Classification under explicit schemes/contexts rather than a new concept;
- policy text/reference authority may differ from subject/context policy-applicability authority;
- narrower/local governance does not automatically override broader governance;
- Lineage, repository/container membership, schema/tag inference, and parent state do not implicitly propagate governance assertions or authority;
- descriptive governance authority does not become normative health, Capability Authorization, control enforcement, compliance, or actual Impact truth.

See [`02_semantic_governance_authority/README.md`](02_semantic_governance_authority/README.md).

## Accepted pre-phase metric-health handoff

[`pre_phase_metric_health_handoff.md`](pre_phase_metric_health_handoff.md) establishes that successful execution is insufficient for table/pipeline health and that metric selection/propagation must be purposeful rather than exhaustive.

Phase 005 owns governance around metric/schema normative state; Phase 006 owns the actual metric/statistical/schema-health model; Phase 007 owns Lineage-aware propagation/change behavior; Phase 009 characterizes concrete source support/latency; Phase 010 chooses technical realization.

## Accepted Group 03 — Normative Health, Metric & Threshold Governance

Accepted contracts:

- AUTH-016 — Expectation-Class and Normative Authority;
- AUTH-017 — Metric Profile Selection, Purpose, and Critical-Metric Authority;
- AUTH-018 — Threshold, Margin, Tolerance, and Severity Authority;
- AUTH-019 — Structural / Schema Compatibility Expectation Authority;
- AUTH-020 — Metric Applicability, Baseline Use, and Structural-Change Review Authority;
- AUTH-021 — Exception, Waiver, Suspension, and Retirement Governance;
- AUTH-022 — Normative Conflict, Business/Technical Coexistence, and Rule Composition;
- AUTH-023 — High-Consequence Metric / Expectation Use Eligibility.

Key results:

- Expectation authority is dimension/property/context/time scoped and may differ by lifecycle action;
- metric meaning, profile inclusion, threshold, severity, waiver, and high-consequence-use eligibility can have different authoritative holders;
- metric profiles are governed selection/applicability structures, not a new truth concept;
- metric availability does not justify profile inclusion;
- Baseline-derived ranges remain descriptive until explicitly adopted through an authoritative Expectation;
- structural/schema compatibility Expectations require explicit normative authority;
- authority may retire/suspend metric/Baseline use but cannot manufacture empirical Baseline comparability;
- bounded exceptions/waivers change normative applicability or required response without rewriting Observations, structural state, Baseline deviations, or historical evidence;
- `strictest wins`, `business wins`, `technical wins`, `highest severity wins`, and recency are not implicit normative conflict resolvers;
- criticality can influence governance priority/review but does not automatically tighten thresholds or prove Impact;
- a metric/Expectation must be explicitly eligible before high-consequence control use, but eligibility is not control authority, evidence readiness, or enforcement.

See [`03_normative_health_metric_threshold_governance/README.md`](03_normative_health_metric_threshold_governance/README.md).

## Accepted Group 04 — Capability Authorization & Restricted Analytical Visibility

Group 04 refines **permission truth** and least-privilege analytical visibility without creating a new authorization/IAM architecture or weakening evidence truth.

Accepted contracts:

- AUTH-024 — Capability Target Binding and Canonical Capability Vocabulary;
- AUTH-025 — Authorization State, Conditions, and Resolution Semantics;
- AUTH-026 — Principal Composition, Membership, Role, and Service Identity;
- AUTH-027 — Capability Scope, Inheritance, and Derived Grants;
- AUTH-028 — Analytical Visibility Decomposition and Least Privilege;
- AUTH-029 — Normative Governance Action Capabilities;
- AUTH-030 — Authorized Analytical Projection, Opacity, and Evidence Minimization;
- AUTH-031 — Restricted Derived Evidence and Inference-Leakage Constraints;
- AUTH-032 — Authorization History, Revocation, and Enforcement Separation.

Key results:

- authorization binds exact principal + capability/action + subject + context/time and, where material, detail level;
- accepted states include `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable`;
- missing/conflicting/unavailable authorization never becomes permission;
- runtime fail-safe refusal is separate from authorization truth and must not invent a `denied` decision;
- no universal `deny wins`, `direct user wins`, `role wins`, `latest wins`, or `most specific wins` combination rule exists;
- user/group/role/service-principal entitlements require evidenced applicable membership/assumption and explicit combination rules;
- capability inheritance through domain/catalog/schema/table/pipeline/repository/Lineage relationships is never implicit;
- raw rows, sensitive fields, schema, governance metadata, metric values, Assessment summaries, thresholds, Baselines, Lineage identities/paths, RCA evidence, causal/Impact/control details, and Explanation can be independently authorized;
- permission to perform a normative action and Assertion Authority over its result are separate requirements;
- Authorized Analytical Projection is a requester-capability-filtered synchronization/view, not declassification or a 25th concept;
- requester visibility and framework/service-principal processing authorization are separate;
- derived/aggregate monitoring state can itself be sensitive and inference-leaking;
- historical authorization is non-rewriting and never reusable as current permission;
- authorization does not prove external enforcement, action occurrence, or action success.

See [`04_capability_authorization_and_restricted_analysis/README.md`](04_capability_authorization_and_restricted_analysis/README.md).

## Accepted Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority

Group 05 applies Capability Authorization to high-consequence actions without creating a workflow/control concept or weakening evidence/control truth.

Accepted contracts:

- AUTH-033 — High-Consequence Action Target and Lifecycle Decomposition;
- AUTH-034 — Causal-Confirmation and High-Consequence Causal Status Authority;
- AUTH-035 — Job and Run Operational Action Authority;
- AUTH-036 — Execution Gate Configuration, Operation, and Override Authority;
- AUTH-037 — Propagation Safeguard Proposal, Activation, Release, and Recovery Authority;
- AUTH-038 — Multi-Party Approval, Separation of Duties, and Conditional Authorization;
- AUTH-039 — Delegation, Temporary Grant, Expiry, and Revocation of High-Consequence Capability;
- AUTH-040 — Emergency / Break-Glass High-Consequence Authorization;
- AUTH-041 — Automated and Service-Principal High-Consequence Authority;
- AUTH-042 — Authorization Unavailability, Conflict, Fallback, and Control-Path Recovery;
- AUTH-043 — Action, Approval, Enforcement, Outcome, and Historical Audit Separation.

Key results:

- high-consequence authorization is exact-action and lifecycle-stage scoped: proposal/request, approval, execution/issuance, override/release/cancel, and review may differ;
- causal confirmation remains jointly evidence- and authority-gated, with human-versus-automation rules scoped by claim profile/class;
- job operational permissions are granular and independent from raw-data, gate, safeguard, and deployment authority;
- gate registration/configuration, normal hold/admit operation, override, fallback-policy configuration, enable/disable, and retirement may have different authorized principals;
- gate override never rewrites readiness or proves enforcement;
- safeguard proposal, activation, and release are independently governable, and release does not prove health;
- multi-party approval/separation-of-duties rules are explicit conditions on Capability Authorization rather than a new workflow concept;
- capability exercise does not imply delegation authority; temporary grants are bounded, expiring, revocable, and non-transitive by default;
- break-glass is explicit, bounded emergency permission rather than universal superuser state and cannot manufacture evidence/readiness/health/causality;
- automation/service principals can perform high-consequence actions only through exact explicit grants and cannot bypass required human approval;
- authorization-outage fallback is action-specific; there is no universal fail-open/fail-closed/always-hold/always-release behavior;
- existing control state during an authorization outage is separate from authority to change that state;
- request → authorization/approval → issuance → control-plane acceptance → enforcement/effect → resulting state/outcome remain separate facts.

See [`05_high_consequence_control_confirmation_authority/README.md`](05_high_consequence_control_confirmation_authority/README.md).

## Accepted Group 06 — Disclosure, Explanation & Audience Governance

Group 06 governs **what an authorized audience may learn and how that truth may be released** without creating a separate truth model or allowing abstraction/publication to strengthen underlying state.

Accepted contracts:

- AUTH-044 — Disclosure Target, Audience, Purpose, Context, and Delivery Binding;
- AUTH-045 — Result, Basis, Provenance, and Detail-Level Disclosure Separation;
- AUTH-046 — Safe Abstraction, Redaction, Opaque Existence, and Minimization;
- AUTH-047 — Composite, Mosaic, and Repeated-Query Inference-Leakage Governance;
- AUTH-048 — Audience Projection Consistency Across Technical, Business, Executive, and Audit Views;
- AUTH-049 — High-Consequence Communication Review, Approval, Release, Correction, and Retraction;
- AUTH-050 — Status-Preserving Language and Non-Overstatement in Disclosure;
- AUTH-051 — Disclosure of Human Attribution, Authority, Authorization, and Control Metadata;
- AUTH-052 — Historical Disclosure, Retained Explanation, and Current-Authorization Separation;
- AUTH-053 — Disclosure Conflict, Unknown/Unavailable Review State, and Safe Non-Disclosure.

Key results:

- disclosure binds requester/audience, information/detail class, subject/context, purpose, temporal perspective, and delivery scope;
- audience labels such as technical/business/executive/client/audit are context, not permission sources;
- permission to inspect privately does not automatically grant permission to publish, export, forward, or disclose to another audience;
- result visibility can differ from metric/threshold/schema/evidence/source/actor/authority basis visibility;
- restricted basis remains restricted rather than absent, while material limitations remain visible at an authorized abstraction when needed to avoid misleading interpretation;
- safe abstraction can expose exact state, coarser category/range, redacted detail, opaque existence, or an explicit limitation only when the abstraction itself is authorized and semantically valid;
- opaque existence may be shown only when existence itself is disclosable;
- aggregation/redaction is not automatic declassification;
- disclosure review considers material inference from combinations, counts, topology, timing, differencing, repeated narrowing, prior disclosures, authority metadata, and control metadata rather than evaluating each field in isolation;
- technical, business, executive, and audit views are different authorized projections over the same truth and cannot intentionally contradict or strengthen it;
- high-consequence statements may require separate compose/review/approve/release/correct/retract authority even when the underlying fact is internally viewable;
- communication approval cannot create evidence sufficiency, causal confirmation, health, compliance, or enforcement;
- simplified wording must preserve accepted status: supported ≠ confirmed, reachable ≠ exposed, not exposed to suspect V ≠ fresh/healthy, hold decision ≠ hold enforced, active safeguard ≠ prevented exposure, release ≠ health, waiver ≠ clean pass, authoritative standing ≠ factual infallibility;
- Annotation author identity, Assertion Authority holder/basis, authorization membership path, causal confirmer/reviewer, gate/safeguard approver/operator, delegation, break-glass, service-principal identity, and other security/control metadata can be independently sensitive;
- Annotation content shown without exact author identity remains labeled as human-provided context where that distinction is material;
- historical retained Explanation, reconstructed `as-known-then` Explanation, retrospective Explanation, historical authorization/disclosure, and current requester disclosure remain separate;
- unknown/conflicting/unavailable/unsafe-to-project disclosure state never becomes permission, and safe withholding does not fabricate an explicit deny or false absence.

See [`06_disclosure_explanation_audience_governance/README.md`](06_disclosure_explanation_audience_governance/README.md).

## Delivery-group design

The phase is reviewed in **seven logical groups**. The grouping is a design/review dependency, not an implementation or service boundary.

### Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution
**Status:** Accepted — AUTH-001–AUTH-008; Assertion Authority added as 24th concept.

### Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance
**Status:** Accepted — AUTH-009–AUTH-015; no new concept.

### Group 03 — Normative Health, Metric & Threshold Governance
**Status:** Accepted — AUTH-016–AUTH-023; no new concept.

### Group 04 — Capability Authorization & Restricted Analytical Visibility
**Status:** Accepted — AUTH-024–AUTH-032; no new concept.

### Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority
**Status:** Accepted — AUTH-033–AUTH-043; no new concept.

### Group 06 — Disclosure, Explanation & Audience Governance
**Status:** **Accepted — AUTH-044–AUTH-053; no new concept.**

### Group 07 — Phase 005 Consolidation / Exit Review
**Status:** **Next — not started.**

Compose Groups 01–06 across representative scenarios and verify that source standing, normative authority, permission, high-consequence action authority, and disclosure remain separate layers over the same evidence-backed truth.

Boundary: Group 07 is a consolidation/exit review. It must not add architecture merely to close the phase, and it should add another AUTH contract only if a genuine unresolved semantic gap is exposed.

## Phase boundaries

Phase 005 must not:

- redefine Phase 004 evidence sufficiency/coverage or causal-confirmation evidence semantics;
- grant authority merely from source count, recency, repository ownership, technical availability, synchronization order, job creator identity, organizational title, or responsibility;
- treat authority as factual infallibility;
- treat policy applicability as enforcement/compliance proof;
- make derived evidence/governance state automatically unrestricted or authoritative;
- promote Baseline typicality into normative truth without explicit Expectation authority;
- treat a waiver as a rewrite of observed evidence or a false health pass;
- make a critical or authoritative metric automatically control-eligible;
- treat metadata/aggregate/derived evidence as automatically safe to disclose;
- make group/role membership, asset containment, or Lineage imply capability inheritance without explicit rules;
- treat unresolved authorization or disclosure state as allow or silently rewrite it to explicit deny;
- treat Capability Authorization, high-consequence approval, or communication approval as proof of external enforcement, successful action, evidence sufficiency, or truth;
- treat break-glass as universal superuser access or automation as self-authorized;
- turn gate override into readiness, safeguard release into health, retry into successful execution, or confirmation authority into evidence sufficiency;
- create separate technical/business/executive truth models;
- let redaction/opacity imply restricted entities/evidence/authority do not exist;
- define the detailed Phase 006 metric/schema-health/statistical model or blindly propagate metrics/governance through Lineage;
- select RBAC/ABAC/IAM/provider architecture, approval/workflow engine, redaction/declassification/privacy-budget technology, scheduler/orchestrator, quarantine implementation, causal engine, graph, LLM, metric storage, rule engine, or persistence architecture;
- select Databricks/Collibra/Immuta/GitHub/Unity Catalog as universally authoritative by default;
- select GitHub Actions, Unity Catalog, or the monitoring application as the universal schema-validation location;
- begin Group 07 or Phase 006 without explicit user direction.

## Phase direction

**Phase 005 Groups 01–06 are accepted with AUTH-001–AUTH-053. Group 07 — Consolidation / Exit Review is next and has not started.**
