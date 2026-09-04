# Audience, Authorization, Safe Abstraction & Basis Inspection

**Canonical key:** `experience.audience-authorization-safe-abstraction`

**Kind:** EXPERIENCE CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.EXPL`

**Owns current question:** How does an internally valid Explanation become an authorized audience/purpose/delivery-specific projection without changing truth or leaking restricted inference?

**Stable IDs:** EXPL-101–EXPL-120

## Current semantics

### EXPL-101 — Audience-Specific Projection Proposition
Bind a visible Explanation projection to requester, target audience, purpose, delivery context and exact internal statement identity; audience labels alone grant no permission.

### EXPL-102 — Requester vs Target-Audience Authorization
Requester visibility and permission to disclose to another audience are separate; private inspection never implies export, forwarding, publication or client disclosure.

### EXPL-103 — Result, Context, Limitation, Basis & Provenance Visibility
Authorize conclusion, context, material limitations, basis, provenance and exact detail independently when required; permission to see one layer does not imply the others.

### EXPL-104 — Detail-Level & Delivery-Surface Binding
Bind disclosure detail and delivery surface explicitly because the same proposition may be permitted in one detail/surface and withheld or abstracted in another.

### EXPL-105 — Safe Abstraction & Epistemic Monotonicity
Safe abstraction may reduce detail or scope only when authorized and semantically valid; it cannot strengthen polarity, certainty, causality, exposure, health, control or governance status.

### EXPL-106 — Subject Identity Abstraction
Aliases/generalization may hide identity only when they preserve material subject distinctions; abstraction cannot merge subjects whose differences affect the proposition.

### EXPL-107 — Value, Threshold, Schema & Detail Abstraction
Coarsen numeric/value/schema detail only when the resulting statement remains true and does not invent severity, health, threshold compliance or other stronger meaning.

### EXPL-108 — Lineage & Path Abstraction
Hide or generalize topology only without inventing directness, completeness, relationship absence, encounter, exposure or causal significance.

### EXPL-109 — Causal, Impact & Control Abstraction
Abstract inferential/control detail without promoting support to confirmation, candidate to exposure, not-exposed to prevention, decision to enforcement or action to outcome.

### EXPL-110 — Governance & Authority Abstraction
Abstract responsibility/classification/policy/authorization/authority detail without converting it into blame, compliance, permission, factual truth or enforcement.

### EXPL-111 — Restricted/Omitted vs Absent & Opaque Existence
Restricted, redacted or omitted material is not absent; even disclosure that a hidden item exists is separately authorization-governed.

### EXPL-112 — Material Hidden-Limitation Constraint
If a hidden limitation materially narrows or weakens a visible conclusion, the visible statement must be narrowed, withheld or safely qualified rather than displayed in stronger form.

### EXPL-113 — Mixed-Authorization Derived Statement
A derived statement using mixed-visibility basis is publishable only when the derived conclusion itself is independently authorized and does not leak otherwise protected facts by inference.

### EXPL-114 — `inspectBasis` Projection
Basis inspection is requester/purpose specific and may expose exact basis, coarse provenance/status, redacted/opaque limitation or nothing according to current authorization.

### EXPL-115 — Internal Traceability Despite Restricted Basis
The framework retains complete internal statement-to-basis traceability even when current visible basis inspection is limited; hidden basis is restricted, not erased.

### EXPL-116 — Mosaic, Differencing & Repeated-Query Risk
Evaluate compositional inference leakage across multiple authorized responses; individually safe answers can become unsafe when combined.

### EXPL-117 — Cross-Audience Consistency Over One Truth
Different audiences may receive different detail/scope, but visible projections of the same proposition must not intentionally contradict or strengthen one another beyond their authorized abstraction.

### EXPL-118 — High-Consequence Communication Review & Release
Where policy requires, compose/review/approve/release/correct/retract communication actions remain separate from truth, evidence, causal, compliance or control authority.

### EXPL-119 — Historical Authorization, Retained Communication & Current Disclosure
Historical actor authorization, retained prior communication and current requester permission are independent; current authorization changes do not rewrite what was communicated historically.

### EXPL-120 — Progressive-Evolution Handoff
Provide Group 07 the authorized current projection plus stable internal proposition/basis identity so later refresh can distinguish truth change from visibility or presentation change.

## Invariants / boundaries

- audience/purpose/delivery ≠ permission;
- requester visibility ≠ target-audience disclosure permission;
- private inspection ≠ export/publish permission;
- conclusion visibility ≠ basis/detail visibility;
- safe abstraction can reduce detail but cannot strengthen truth;
- redacted/omitted ≠ absent;
- opaque existence is itself governed;
- hidden limitations still constrain visible conclusions;
- `inspectBasis` is separately authorized;
- visible citation ≠ source-inspection permission;
- cross-audience views share one truth;
- communication release authority ≠ truth/evidence authority.

## Architecture boundary

This contract does not choose IAM/RBAC/ABAC products, policy engines, redaction engines, differential-privacy mechanisms, query-history stores, LLM prompting, templates, UI visibility controls, citation widgets, persistence or technical architecture.

## Provenance

- `docs/concepts/phase_008/06_audience_authorization_safe_abstraction_basis_inspection/README.md`
- Phase 008 Group 06 accepted EXPL-101–EXPL-120.
