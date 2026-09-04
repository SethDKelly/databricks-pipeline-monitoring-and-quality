# Propagation Safeguard Scope, Enforcement, Release & Recovery

**Canonical key:** `operations.propagation-safeguard`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.OPS`

**Owns current question:** How does Propagation Safeguard protect exact suspect states and consumer paths, prove enforcement/prevented exposure, and handle extension, expiry, release and recovery without becoming health, Impact or causal truth?

**Stable IDs:** OPS-086–OPS-104

## Current semantics

Operational reasoning chain: **protected state/surface → proposal/authorization → activation request/issuance → evidence-established enforcement → path/opportunity-specific protection → REF-028 prevented-exposure determination → extension/expiry/release → independently evidenced post-protection state**.

### OPS-086 — Safeguard Proposition: Protected State, Surface & Scope
Bind Safeguard to exact protected/suspect state or missing-output context, propagation surface, path/consumer/cohort/environment scope and effective interval.

### OPS-087 — Safeguard Lifecycle & Action-Fact Decomposition
Separate proposal, authorization, activation request/issuance, control acceptance, effective enforcement, extension, expiry and release action facts.

### OPS-088 — Protection Surface Placement & Semantic Boundary
Define protection surface functionally—publication/current-state presentation/consumer path/downstream advancement—without selecting implementation.

### OPS-089 — Safeguard Applicability, Effective Scope & Interval
Resolve applicability and effective scope per protected state/path/cohort/version/interval; no global quarantined flag is implied.

### OPS-090 — Activation, Enforcement & Material Path Control
`Active` requires evidence-established enforcement for the relevant scope/time; configuration/request/approval alone is insufficient.

### OPS-091 — Partial Enforcement Across Consumers, Cohorts & Paths
Represent partial enforcement across consumers, regions, cohorts, versions and paths explicitly; no universal protection percentage is accepted.

### OPS-092 — Alternate Paths, Bypass & Protection Coverage
Evaluate alternate paths and bypass separately; one controlled route cannot prove global protection and theoretical routes are not automatically bypasses.

### OPS-093 — Prevented Exposure Determination Using Group 06 + REF-028
Prevented exposure is a derived REF-028 determination requiring material opportunity, enforced protected path, negative suspect-state encounter evidence and sufficient alternate-path coverage.

### OPS-094 — No-Opportunity / Incidental Safeguard Non-Prevention
No encounter opportunity can coexist with valid protection but does not grant causal prevention credit.

### OPS-095 — Safe Prior State, Stale Serving, Hold & Non-Delivery During Protection
Safe prior-state serving, delay, hold or non-delivery during protection are separate freshness/Impact facts, not generic Safeguard success/failure labels.

### OPS-096 — Missing Output & Current-Cycle Advancement Protection
When no qualifying current output exists, protect advancement/current-state presentation rather than inventing a nonexistent quarantined object.

### OPS-097 — Extension, Renewal, Scope Revision & Supersession
Extension/renewal/scope revision preserves prior intervals and requires separate authorization/evidence.

### OPS-098 — Expiry, Scheduled End & Effective End of Protection
Scheduled expiry is not automatically effective end; effective protection termination requires applicable control evidence.

### OPS-099 — Release Request, Effective Release & Path Reopening
Separate release rationale/authorization/request/control acceptance/effective release/path reopening; release may be partial.

### OPS-100 — Post-Release Recovery State & Independent Observation
Post-release recovered state belongs to health/currentness/Impact/source concepts and requires independent observation; Safeguard does not own recovery truth.

### OPS-101 — Safeguard Telemetry Conflict, Unavailability & Fallback Discipline
Missing/conflicting control telemetry does not prove success, failure, fail-open, fail-closed or actual fallback application.

### OPS-102 — Overlapping Safeguards, Composition & Attribution
Overlapping Safeguards retain separate scope/enforcement/release histories; activation order or visibility does not create materiality attribution.

### OPS-103 — Safeguard-Induced Effects, Impact & Causal Handoff
Safeguard-induced delay/staleness/non-delivery is Impact/runtime evidence; broader causal attribution belongs to Causal Claim.

### OPS-104 — Historical Safeguard Replay, Ownership & Group 08 Handoff
Historical Safeguard replay preserves then-effective action/enforcement state and as-known versus retrospective prevention conclusions; Safeguard remains separate from Gate.

## Invariants / boundaries

- proposal/configuration/authorization/request ≠ effective enforcement.
- active safeguard ≠ global path protection.
- partial enforcement ≠ global success/failure.
- one protected path ≠ no alternate path.
- `not exposed` ≠ `prevented by Safeguard`.
- no encounter opportunity ≠ prevention evidence.
- release request ≠ effective release.
- release ≠ recovery/health/currentness.
- control telemetry missing ≠ fail-open/fail-closed result.
- Propagation Safeguard ≠ Execution Gate.

## Cross-concept ownership

Propagation Safeguard owns bounded protection-control truth. Impact retains encounter/exposure/effect/consequence truth; Capability Authorization retains permission; Causal Claim owns broader attribution.

## Historical / disclosure rule

Safeguard history is bitemporal and non-rewriting. Later alternate-path or encounter evidence may revise retrospective prevention attribution without rewriting the action/enforcement history.

## Architecture boundary

This contract does not select quarantine views/tables, ACL/routing mechanisms, control services, enforcement integrations, event stores or technical architecture.

## Provenance

- `docs/concepts/phase_007/07_propagation_safeguard_scope_enforcement_recovery/README.md`
- Phase 007 Group 07 accepted OPS-086–OPS-104.
