# Phase 005 Group 04 — Capability Authorization & Restricted Analytical Visibility

**Status:** Accepted — AUTH-024–AUTH-032

## Goal

Refine permission truth independently from Assertion Authority, evidence sufficiency, normative governance, and action/enforcement success while preserving useful least-privilege monitoring and RCA.

## Accepted handoff from Groups 01–03

- Assertion Authority and AUTH-001–AUTH-023 are accepted;
- authoritative governance standing does not grant Capability Authorization;
- metric meaning, profile selection, threshold/severity, waiver, and high-consequence-use eligibility are independently governable;
- an authoritative or control-eligible metric/Expectation does not grant a principal permission to view its values, edit the rule, configure a gate, or perform an operational action;
- restricted metric/schema/threshold/authority details may themselves be sensitive;
- waiver/exception state does not declassify the underlying metric, rule, or evidence;
- Phase 004 evidence sufficiency and control-enforcement meanings remain unchanged.

## Accepted contracts

- **AUTH-024 — Capability Target Binding and Canonical Capability Vocabulary**
- **AUTH-025 — Authorization State, Conditions, and Resolution Semantics**
- **AUTH-026 — Principal Composition, Membership, Role, and Service Identity**
- **AUTH-027 — Capability Scope, Inheritance, and Derived Grants**
- **AUTH-028 — Analytical Visibility Decomposition and Least Privilege**
- **AUTH-029 — Normative Governance Action Capabilities**
- **AUTH-030 — Authorized Analytical Projection, Opacity, and Evidence Minimization**
- **AUTH-031 — Restricted Derived Evidence and Inference-Leakage Constraints**
- **AUTH-032 — Authorization History, Revocation, and Enforcement Separation**

## Core accepted distinctions

### Authorization is exact-capability truth

Authorization binds the requester/principal, action/capability, subject, environment/tenant/purpose/consumer context, time, and where material the requested detail level. Asset-level labels such as `can access C` are insufficient when raw rows, metrics, thresholds, schema, Lineage, RCA, and controls have different permissions.

### Resolution state is not runtime fallback

Accepted states include `allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable`. Missing/conflicting authorization never becomes permission. A future implementation may conservatively refuse actions without a positive allow, but that does not rewrite `unknown/conflicting/unavailable` into an explicit deny.

There is no implicit `deny wins`, `direct grant wins`, `role wins`, `latest wins`, or `most specific wins` rule. Such combination semantics require an explicit accepted rule.

### Principal composition is provenance-bearing

User, group, role, and service-principal relationships are resolved with historical membership/assumption evidence. Direct and inherited decisions preserve their provenance; no role hierarchy, group nesting, or direct-versus-group precedence is inferred silently.

### Least privilege is detail-specific

Raw data, sensitive fields, schema, semantic/governance metadata, metric values, Assessment summaries, thresholds, Baselines, Lineage identities/paths, RCA evidence, causal status/basis, Impact, control state, authority basis, Annotation, and Explanation can be authorized independently.

An analyst can therefore be denied rows while permitted a safe health/RCA view. Conversely, `metadata` or `aggregate` is never automatically unrestricted.

### Normative governance actions require permission and authority

Viewing, proposing, editing, approving, waiving, suspending, retiring, and approving high-consequence use are independently resolvable actions. A principal may have Capability Authorization to submit/edit a rule while the resulting assertion remains advisory because the principal lacks the relevant Assertion Authority. Authority standing likewise does not grant permission to perform the action.

### Authorized Analytical Projection is not a concept or declassification

Authorized Analytical Projection remains a synchronization/view over existing truth. It can expose exact permitted state, a safe authorized abstraction, an opaque reference, a restricted-basis limitation, or nothing where existence itself is restricted.

A conclusion can be visible while some basis remains hidden, but hidden evidence must not be described as absent. The framework/service principal must itself be authorized to process any evidence counted internally; requester visibility and framework processing authorization are separate.

### Derived evidence can leak sensitive state

Counts, thresholds, schema, topology, hidden-node existence, causal/Impact/control state, and authority/authorization metadata can reveal restricted information. Aggregation/redaction is not automatic declassification, and combinations of individually permitted facts can create inference leakage.

### Historical authorization is non-rewriting

Historical authorization can reconstruct what an actor was permitted to know/do at incident time. Current requester authorization still governs present disclosure. Later grant/revocation does not rewrite past entitlement state, and entitlement state never proves external enforcement or action success.

## Scenario result

[`scenario_checks.md`](scenario_checks.md) passes the representative least-privilege, principal-composition, normative-action, restricted-evidence, opaque-Lineage, historical, and enforcement-separation cases.

No new Concept is required. **Capability Authorization remains the existing truth owner and the catalog remains 24 concepts.** Authorized Analytical Projection remains a synchronization/view rather than a 25th concept.

## Boundaries preserved

Group 04 does **not**:

- select RBAC, ABAC, IAM, identity provider, Immuta/Databricks ACL realization, or declassification technology;
- decide exact job/gate/safeguard/causal-confirmation high-consequence approval/delegation/break-glass semantics — Group 05 owns that refinement;
- decide audience wording or disclosure-review policy — Group 06 owns that refinement;
- weaken Phase 004 evidence sufficiency or treat inaccessible evidence as absent;
- treat authorized action as proof the action happened or was enforced.

## Exit

**Group 04 is accepted with AUTH-024–AUTH-032. AUTH-001–AUTH-032 are accepted overall. Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority is next and has not started.**
