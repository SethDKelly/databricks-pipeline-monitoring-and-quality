# Phase 004 Group 01 — Evidence Sufficiency, Coverage & Negative Evidence

**Status:** Accepted

## Goal

Define a common evidence-strength framework that can later be applied to absence, Assessment, exposure/non-exposure, gate readiness/enforcement, causal support/contradiction, and historical knowledge claims without creating a universal confidence score or a new evidence-owning concept.

## Accepted refinements

1. [`REF-001 — Evidence Applicability and Proposition Binding`](001_evidence_applicability_and_proposition_binding.md)
2. [`REF-002 — Coverage Profile and Opportunity to Observe`](002_coverage_profile_and_opportunity_to_observe.md)
3. [`REF-003 — Negative, Absence, and Exclusion Evidence`](003_negative_absence_and_exclusion_evidence.md)
4. [`REF-004 — Corroboration, Conflict, and Evidence Independence`](004_corroboration_conflict_and_independence.md)
5. [`REF-005 — Conclusion-Specific Evidence Sufficiency Evaluation`](005_conclusion_specific_sufficiency.md)

See [`scenario_checks.md`](scenario_checks.md) for the accepted positive/negative/duplicate/conflict/restricted/control evidence checks.

`REF-###` identifies a refinement contract, not a new Concept or Phase 003 synchronization.

## Core model

Evidence evaluation proceeds conceptually through five separable questions:

1. **What proposition is being evaluated?** A fact/conclusion must be bounded by subject, property, context, event time/window, grain/version, and intended conclusion strength.
2. **Is this evidence applicable to that proposition?** Subject identity, semantics, time, grain/version, and derivation must align enough for the evidence to bear on the proposition.
3. **What does the evidence actually cover?** Coverage describes the bounded opportunity to observe: temporal interval, population/partition, source/query scope, version/consumer scope, collection success, sampling/estimation, and known gaps.
4. **How do the evidence items relate?** Supporting, contradicting, duplicated, derived, and common-source evidence remain distinguishable; repetition is not automatically independence.
5. **Is the resulting evidence set sufficient for this particular conclusion under the applicable standard?** Sufficiency is a conclusion-specific evaluation, not an intrinsic score attached permanently to the evidence.

## Boundary decisions

### Sufficiency is claim-relative
The same Observation may be sufficient to prove existence and insufficient to prove exclusivity or absence. For example, observing one qualifying output proves at least one exists; it does not prove no additional outputs exist.

### Coverage is bounded, not universal
`Complete coverage` is meaningful only relative to an explicitly declared observation universe/window. The framework does not claim globally complete evidence about a pipeline, table, or business process.

### Negative evidence needs opportunity-to-observe
A negative conclusion requires evidence from a mechanism capable of detecting the relevant event/state plus adequate coverage of the bounded opportunities where it could have occurred. Silence from a failed or incomplete source is not evidence of absence.

### Missing telemetry is neither false nor zero
Unavailable query, collection outage, restricted evidence, unmonitored interval, or unresolved identity/version association produces a limitation/unknown result—not a fabricated negative Observation.

### Corroboration is not source counting
Several records derived from the same underlying event/source do not become independent corroboration merely because they appear in several systems. Common derivation and duplicated telemetry remain visible.

### Conflict is not cancellation
Contradictory applicable evidence remains explicit. Phase 004-A does not choose which source is authoritative merely to force a conclusion; source authority/conflict precedence is refined later in Phase 005.

### No universal evidence score
The framework does not introduce a single `trust`, `confidence`, or evidence-quality number. Later statistical methods may expose appropriate uncertainty for specific measurements, but conclusion sufficiency remains traceable to explicit standards and limitations.

### Evidence truth and disclosure remain separate
Capability Authorization can restrict which evidence details a requester sees without changing the internal evidence relationship itself. If the framework itself lacks access to required evidence, that is an availability/sufficiency limitation rather than merely a display redaction.

## Cross-domain examples

### Observed absence
A complete successful query of the accepted run-enumeration evidence source for the required interval returns zero qualifying runs. That can support an absence Observation when the source/query has sufficient opportunity-to-observe and coverage. A telemetry outage during the interval cannot.

### Exposure / non-exposure
Evidence that Report R refreshed from affected version V supports exposure. To conclude `not exposed`, the evidence must adequately cover relevant refresh/consumption opportunities; no refresh telemetry is not reassurance.

### Gate readiness
A successful upstream job run may support a completion proposition but may be insufficient for a gate criterion requiring a current qualifying output/version. Evidence sufficiency follows the declared readiness proposition.

### Causal contradiction
Evidence that a degradation began before Deployment D activated can contradict `D caused the degradation` only when timing/identity coverage is sufficiently aligned to establish that ordering.

### Restricted analyst
The system may have sufficient internal evidence for `quality criterion violated` while the analyst sees only the authorized Assessment, safe basis summary, and limitation that exact values are restricted. Disclosure does not manufacture or destroy evidence sufficiency.

## Group 01 exit gate

**Satisfied.** The project now has a common refinement vocabulary for evidence applicability, coverage, negative evidence, corroboration/conflict, and conclusion-specific sufficiency that can be specialized by later Phase 004 groups without creating a new evidence concept or universal score.

## Handoff to Group 02

Group 02 must apply this framework to temporal questions, especially:

- how an event/effective-time target and knowledge cutoff select eligible evidence;
- what evidence is sufficient to say something was `known by`, `not known by`, or `learned after` a cutoff;
- how late/corrected evidence creates reassessment/supersession without erasing prior knowledge;
- what dependent conclusions need reevaluation or reopen prompts after material corrections;
- how actual retained state differs from reconstruction.
