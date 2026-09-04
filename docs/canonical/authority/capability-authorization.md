# Capability Authorization & Restricted Analysis

**Canonical key:** `auth.capability-authorization`

**Kind:** AUTHORITY

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.AUTH`

**Owns current question:** What exact action/detail a principal may perform or view, and how can useful analysis remain least-privilege without treating permission as truth or enforcement?

**Stable IDs:** AUTH-024–AUTH-032

## Current semantics

### AUTH-024 — Capability Target Binding and Canonical Capability Vocabulary
Authorization binds exact principal, capability/action, subject, context/time and material detail level. Raw rows, metrics, thresholds, schema, Lineage/RCA and controls are independent capability classes.

### AUTH-025 — Authorization State, Conditions, and Resolution Semantics
Accepted states include allowed, denied, conditional, unknown, conflicting and unavailable. Missing/conflicting/unavailable never becomes permission; runtime fail-safe refusal does not rewrite unresolved truth into fabricated deny.

### AUTH-026 — Principal Composition, Membership, Role, and Service Identity
User/group/role/service-principal composition is provenance- and history-bearing. Membership and role assumption do not create hidden precedence or universal inheritance.

### AUTH-027 — Capability Scope, Inheritance, and Derived Grants
Capability inheritance/derived grants require explicit rules and bounded scope. Containment, Lineage or role hierarchy does not imply permission by itself.

### AUTH-028 — Analytical Visibility Decomposition and Least Privilege
Rows, sensitive fields, semantics, schema, metrics, Assessment, thresholds, Baselines, Lineage, Investigation/RCA, causal/Impact/control/governance detail, Annotation and Explanation may be independently visible.

### AUTH-029 — Normative Governance Action Capabilities
View, propose, edit, approve, waive, suspend, retire and high-consequence-use approval are separately resolvable actions. Permission to edit does not give the resulting assertion authoritative standing.

### AUTH-030 — Authorized Analytical Projection, Opacity, and Evidence Minimization
Authorized Analytical Projection is a view over existing truth, not a concept or declassification mechanism. It may expose exact, safely abstracted, opaque, restricted-basis or withheld detail while preserving limitations.

### AUTH-031 — Restricted Derived Evidence and Inference-Leakage Constraints
Aggregates, counts, thresholds, schema, topology, causal/Impact/control and authority metadata can remain sensitive; aggregation/redaction is not automatic declassification and combined facts can leak state.

### AUTH-032 — Authorization History, Revocation, and Enforcement Separation
Authorization history is non-rewriting. Historical entitlement cannot be reused as current permission. Permission never proves action occurrence, enforcement or success.

## Invariants / boundaries

Authentication ≠ Capability Authorization ≠ Assertion Authority. Requester visibility ≠ service/framework processing permission. Unknown authorization may cause safe refusal but remains epistemically unknown.

## Provenance

- `docs/concepts/phase_005/04_capability_authorization_and_restricted_analysis/README.md`
