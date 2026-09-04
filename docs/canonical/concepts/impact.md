# Impact

**Canonical key:** `concept.impact`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.impact`

**Owns current question:** What downstream candidate, encounter/exposure, effect, and consequence state is evidenced for an originating condition and bounded consumer/use context?

**Stable IDs:** N/A

## Current semantics

Impact owns origin/time context; downstream candidate identity/path; candidate/reachability basis; encounter opportunity/availability/publication context; consumer-mode actual encounter/exposure; downstream Observation/Assessment/Change effect links; technical/analytical/business consequence evidence; timing/coverage/uncertainty; context such as criticality/responsibility; history; and authorization/redaction.

## Actions

- `identifyCandidates` — derive plausible downstream candidates from authorized typed topology/scenario context.
- `evaluateExposure` — resolve actual encounter/exposure for exact state/consumer/use/time.
- `linkDownstreamEffect` — associate downstream source-owned condition/effect evidence.
- `recordConsequence` — associate provenance-bearing consequence evidence.
- `revise` — update the layered picture non-rewriting as evidence arrives.

## Invariants / boundaries

- Candidate/reachability ≠ encounter opportunity ≠ actual exposure ≠ downstream effect ≠ consequence ≠ causal attribution.
- Exposure results can include `exposed`, `not exposed`, `safe/other-state encounter`, `encountered-state unknown`, `no relevant encounter opportunity`, `indeterminate`, `conflicting`, `unavailable`; authorization/redaction is separate.
- `not exposed`, `no downstream effect`, and `no consequence` are bounded negatives requiring adequate opportunity/path/version/consumer coverage; missing telemetry is not reassurance.
- Exposure is not transitively propagated through multi-hop Lineage; alternate paths matter.
- A safe prior-state encounter can establish non-exposure to suspect state while freshness/currentness remains degraded.
- Criticality/Classification/client-facing context may prioritize but cannot create realized Impact or universal severity/harm score.
- Business-facing publication ≠ view ≠ decision reliance ≠ adverse consequence.
- If origin caused/contributed to effect/consequence, that proposition belongs to Causal Claim.
- Prospective Change Intent/Lineage analysis populates candidate/review context only, never realized exposure/effect/consequence.

## Ambiguity / evidence

Incomplete/restricted Lineage, consumer telemetry, version binding, or business-use evidence leaves the relevant layer unresolved rather than collapsed into generic `affected`.

## Synchronizations / related canonical resources

Lineage supplies candidate paths; Execution History/Observation/Deployment/Change can establish encounters/effects; Causal Claim owns attribution; Semantic/Responsibility/Classification/Policy provide context; Explanation preserves the layers.

## Non-goals

Lineage truth, causal root determination, criticality definition, remediation, universal risk/impact scoring, or graph implementation.

## Provenance

- `docs/concepts/phase_002/05_investigation_impact_explanation/impact.md`
- `docs/concepts/phase_007/03_prospective_blast_radius_change_aware_review/`
- `docs/concepts/phase_007/06_impact_consumer_encounter_exposure_consequence/`
