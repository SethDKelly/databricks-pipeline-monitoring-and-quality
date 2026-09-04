# Composite Health, Readiness Suitability & Result Timing

**Canonical key:** `health.composite-readiness-timing`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.HLTH`

**Owns current question:** How do component Assessments compose into bounded health summaries, and when are those results fresh, mature and suitable for an exact readiness/high-consequence use without becoming gate/control state?

**Stable IDs:** HLTH-055–HLTH-066

## Current semantics

### HLTH-055 — Composite Health Proposition, Profile, Scope & Use Binding
Composite health binds subject, consumer/use/context, profile/version, component set/roles, current-cycle/window and evaluation/knowledge time. It is not an unqualified intrinsic scalar property of an asset.

### HLTH-056 — Component Eligibility, Required/Optional Roles & Explicit Composition Logic
Required, optional, conditional, alternative and informational components are explicit profile semantics. No universal majority, weighted average, severity-weighted score or generic worst-child algorithm is accepted.

### HLTH-057 — Structured Composite Health Vocabulary & Decisive-State Semantics
Profile-derived shorthand may include `healthy`, `healthy with warning`, `degraded`, `indeterminate`, `conflicting`, `unavailable` and `not applicable` when justified by explicit composition logic. Component evidence/provenance remains inspectable.

### HLTH-058 — Unresolved State, Conflict, Waiver & Exception Preservation in Composite Health
Required indeterminate/conflicting/unavailable state remains visible. `violates + waived response` remains a violation; only genuine bounded non-applicability changes component applicability. Hidden/restricted required problems cannot become a clean result.

### HLTH-059 — Severity, Criticality, Priority & Health-Truth Separation in Composition
Severity, criticality and priority can govern membership/escalation/presentation but do not change component truth. Low-severity required violation still degrades the relevant composite; high-criticality meeting state remains meeting.

### HLTH-060 — Technical, Business, Executive & Consumer Health Projection over One Truth
Audience projections may reduce detail or vocabulary while preserving the same underlying bounded proposition. Different consumer/use profiles can legitimately differ because their propositions differ; the same profile result cannot be rewritten by audience.

### HLTH-061 — Health Result Age, Evidence Freshness & Use-Specific Staleness
Result timing distinguishes evidence event/window time, source availability, framework knowledge, Assessment evaluation, evidence age and intended opportunity. Recent recomputation over old evidence can be stale; no universal TTL is accepted.

### HLTH-062 — Progressive Health Result Maturity, Pending Evidence & Analytical Horizons
Functional horizons are immediate operational facts; fast core/schema/current-cycle health; enriched DQ/reconciliation/distribution health; diagnostic/Investigation support; and retrospective review. Maturity follows sufficient evidence, never elapsed time alone.

### HLTH-063 — Exact-Use Readiness Suitability of Health Evidence
Suitability is exact-use and outcome-neutral, considering sufficiency, availability/conflict, comparability/reference validity, current-cycle alignment, permitted evidence age and required maturity. Fresh well-evidenced violation may be suitable for `not ready`; stale `meets` may be unsuitable for `ready`.

### HLTH-064 — High-Consequence Control-Use Suitability & AUTH-023 Composition
Where high-consequence use applies, AUTH-023 eligibility and evidence suitability are independent prerequisites. Eligibility does not create freshness/suitability/readiness, control authorization, Gate decision, enforcement or execution.

### HLTH-065 — Late Evidence, Progressive Summary Revision & Non-Rewriting History
Late/enriched/corrected evidence may revise broader composite/suitability results while retaining earlier narrow facts and provenance. Reassessment/supersession never counterfactually rewrites what was assessed or communicated earlier.

### HLTH-066 — Historical Composite Health, Suitability & Readiness Replay
Historical replay binds then-effective profiles/components, Baselines/Expectations/reconciliation definitions, warning/waiver state, evidence/current-cycle state, freshness/suitability rules, readiness criterion and knowledge cut. Historical health/suitability remains separate from historical gate/control action and execution.

## Invariants / boundaries

Component Assessment ≠ composite health Assessment ≠ result freshness/suitability ≠ readiness result ≠ Gate decision ≠ enforcement ≠ actual execution.

Eligible ≠ fresh/mature/comparable/suitable ≠ ready ≠ authorized to operate control ≠ Gate decision ≠ enforcement ≠ execution.

Passive monitoring remains non-blocking for ungated production. No universal health/confidence score, TTL, latency SLA or fallback policy is accepted here.

## Provenance

- `docs/concepts/phase_006/06_composite_health_readiness_timing/README.md`
- `docs/concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md`
- Phase 006 Group 06 accepted HLTH-055–HLTH-066; Group 07 confirmed phase-wide composition.
