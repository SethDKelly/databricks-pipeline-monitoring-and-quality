# Group 05 — Downstream Impact, Annotation & Explanation

**Status:** Review complete — synchronizations accepted

## Goal

Define how downstream Lineage becomes evidence-layered Impact, how safeguards can prevent exposure while creating separate operational consequences, how human Annotation contributes without stealing structured truth, and how Capability Authorization enables useful analyst-facing health/governance/RCA Explanation even when direct data access is restricted.

## Accepted synchronizations

- [`SYN-023 — Historical Downstream Lineage → Impact Candidate Discovery`](023_downstream_lineage_impact_candidate_discovery.md)
- [`SYN-024 — Impact Candidate + Consumption Evidence → Exposure Determination`](024_candidate_consumption_exposure_determination.md)
- [`SYN-025 — Downstream Candidate + Health Evidence → Observed Effect`](025_downstream_health_observed_effect.md)
- [`SYN-026 — Impact Evidence + Business Context → Consequence Evidence`](026_impact_consequence_evidence.md)
- [`SYN-027 — Originating Condition + Downstream Outcome → Explicit Causal Attribution`](027_impact_effect_causal_attribution_boundary.md)
- [`SYN-028 — Propagation Safeguard + Impact → Prevented Exposure / Operational Consequence`](028_safeguard_prevented_exposure_and_consequence.md)
- [`SYN-029 — Human Annotation + Structured State → Contextual Enrichment`](029_annotation_contextual_enrichment.md)
- [`SYN-030 — Capability Authorization + Concept State → Authorized Analytical Projection`](030_capability_authorized_analytical_projection.md)
- [`SYN-031 — Authorized Analytical Projection → Evidence-Grounded Explanation`](031_authorized_projection_explanation.md)

## Accepted handoff

Group 05 consumes Groups 01–04 plus the Capability Authorization addendum without changing their truth ownership. Historical Lineage remains candidate discovery; Causal Claim remains the only home for causal attribution; Propagation Safeguard remains protective state; Capability Authorization remains permission truth rather than IAM/enforcement implementation.

## Boundary decisions

### 1. Impact has four evidence strengths, not one `affected` flag
Reachability/candidate, actual exposure/consumption, observed downstream effect, and evidenced technical/analytical/business consequence remain separately resolvable. Stronger layers cannot be inferred merely because a weaker layer exists.

### 2. Exposure requires encounter evidence
Reachability and temporal proximity do not prove consumption. `Not exposed` also requires sufficient negative coverage; missing refresh/version telemetry is not reassuring evidence.

### 3. Downstream effect can be known while exposure remains unknown
A downstream metric or delivery Assessment can fail independently of whether the product has proven consumption of the originating state. Preserve both facts; causal attribution remains separate.

### 4. Criticality prioritizes; it does not manufacture Impact
Client-facing, regulated, executive, or otherwise high-criticality consumers may warrant immediate review while still only candidates. Criticality is context/risk significance, not exposure/effect/consequence evidence.

### 5. Business consequence requires evidence
A reachable/exposed report is not automatically a business consequence. Evidence of client delivery, report use, process interruption, decision use, application behavior, or another consequence is recorded with provenance. `No harm` requires appropriate coverage.

### 6. Policy sensitivity is not compliance harm
Classification/Policy Context can govern handling and disclosure but cannot be converted into policy breach, regulatory harm, or non-compliance without separate authoritative evidence.

### 7. Downstream causal attribution always uses Causal Claim
If the product says an upstream/originating condition caused/contributed to a downstream effect or consequence, that statement must be an explicit Causal Claim at its actual epistemic status.

### 8. Safeguards can establish prevented exposure only with enforcement evidence
An active/enforced safeguard plus sufficient consumption coverage can support `not exposed due protection`. A proposed safeguard or unknown enforcement cannot. Blocking a suspect version also does not prove fresh/healthy downstream delivery.

### 9. Safeguard consequences remain separate
Quarantine may correctly prevent suspect exposure while causing lateness/non-delivery. Those operational effects are Observations/Assessments/Impact evidence; attributing them to the safeguard uses Causal Claim.

### 10. Annotation remains attributed context
Human facts/claims are routed to the concept owning their meaning. Impact may cite human consequence context while preserving human provenance; disputed/withdrawn notes cannot become uncontested Explanation facts.

### 11. Restricted raw data does not imply unusable monitoring
Capability Authorization can permit an analyst to see approved health metrics/Assessments, execution timing, Lineage abstractions, policy/restriction summaries, responsibility context, Causal Claim status, Impact, safeguard state, and Explanation even while row/column access is denied.

### 12. Derived evidence is not automatically safe
Counts, thresholds, table names, Lineage paths, classifications, policy details, responsibility metadata, causal conclusions, client identities, and safeguard information may each be independently restricted.

### 13. Authorized analytical projection is a view, not a new truth concept
SYN-030 composes independently authorized concept state for a principal/task. It does not persist a new canonical truth, declassify evidence by inference, or borrow authorization from raw-data access, responsibility, policy, scope, or operational authority.

### 14. Analysis authority and production-control authority remain independent
An analyst may investigate without job-operation/safeguard authority; an operator may update/retry a job without raw-data read. Explanation may display authorized capability state but does not execute actions.

### 15. Explanation communicates; it does not reason past the evidence
Explanation preserves health basis, Impact layer, causal status, human-source status, policy limitations, authorization/redaction, and event/knowledge-time perspective. Restricted evidence is never retrieved merely to make prose more complete.

### 16. Historical authorization cannot bypass current disclosure
A historical view may describe what a past actor was authorized to know/do, but the current requester receives only information allowed by current applicable disclosure authorization. Full end-to-end replay is tested in Group 06.

## Scenario review

### E-01 — A+B→C unplanned degradation
Pass. Downstream consumers become candidates; consumption evidence distinguishes exposed versus merely reachable; downstream health and business consequence are separately evaluated; origin→effect attribution remains Causal Claim.

### E-03 — Planned change with unintended violation
Pass. A valid planned volume change can coexist with an unintended completeness issue and downstream exposure/effect evidence without the plan suppressing Impact.

### E-05 — Stale upstream with successful downstream execution
Pass. A downstream run may succeed, consume stale state, exhibit its own freshness effect, or remain exposure-unknown; those layers remain independent.

### E-07 — Cross-repository dependency
Pass. Impact candidate/exposure reasoning crosses repositories while retaining typed historical Lineage and provenance.

### E-08 — Conflicting governance / expectation context
Pass. Explanation surfaces authorized conflict/uncertainty rather than choosing a policy/Expectation by synchronization order.

### E-09 — Restricted upstream/downstream context
Pass. Analysts can receive opaque/redacted health, Lineage, causal, Impact, policy, and responsibility context without raw-data or restricted-identity leakage.

### E-10 — Historical correction
Pass. Later exposure/effect/consequence/claim evidence can refresh retrospective Explanation while retained contemporaneous views remain reconstructable.

### E-12 — Missing output and protective hold
Pass. A missing output can lead to a held publication boundary; there is no fabricated quarantined object, and resulting non-delivery/delay is evaluated separately.

### E-14 — Material atypicality with analyst research
Pass. Analyst facts use structured evidence concepts; context remains Annotation; authorized derived evidence can support investigation despite row-level restrictions.

### E-15 — Safeguard creates delivery delay
Pass. Enforced protection may prevent suspect-version exposure while independently creating delivery-latency effect/consequence; causal attribution remains explicit.

### E-16 — Restricted-data analyst remains operationally useful
Pass. Raw-data read is denied while approved health, execution, governance, Lineage/RCA, Impact, safeguard, responsibility, and Explanation capabilities remain usable. Job-operation authority is resolved separately.

### E-17 — Safeguard prevents exposure
Pass. A reachable client report does not consume the suspect version because an enforced safeguard blocks the relevant path. `Prevented exposure` is evidence-backed rather than assumed from safeguard intent.

### E-18 — Critical but unexposed consumer
Pass. A critical report is prioritized for review but reliable consumption evidence shows it did not receive the affected state. Criticality does not manufacture Impact.

### E-19 — Downstream effect with unknown business consequence
Pass. A report metric fails after exposure, but evidence does not show whether any client/decision used it. Effect is known; business consequence remains unknown.

### E-20 — Historical authorization is not current access
Pass. Retrospective analysis can state that an incident responder had broader access at the time, but a current analyst cannot retrieve those historical restricted values unless currently authorized.

## Deferred questions

- first-MVP evidence standards for consumer/version exposure and negative non-exposure;
- minimum consequence taxonomy and evidence standards for client/business-process outcomes;
- criticality representation and prioritization semantics in later governance/Impact refinement;
- safe abstraction/disclosure vocabulary by health, Lineage, policy, causal, Impact, and Annotation evidence type;
- exact operational-action vocabulary surfaced alongside analysis capability;
- audience-specific Explanation schemas and visible citation requirements;
- deterministic versus generative composition rules for high-consequence statements;
- retained Explanation snapshot policy.

## Group exit gate

**Satisfied.** Downstream reasoning now distinguishes candidate, exposure, observed effect, consequence, and causal attribution; safeguard prevention and safeguard-induced consequences remain honest; Annotation stays attributed; and analysts can receive evidence-grounded health/governance/RCA transparency under explicit least-privilege capability boundaries without requiring direct data access or granting production control.

The next group is **Group 06 — Historical Replay & Phase 003 Consolidation**.