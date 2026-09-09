# Decision Records — Phase 006 Group 06 Composite Health, Readiness Suitability & Progressive Result Timing

Continues after D-357.

### D-358 — Group 06 requires no new concept
**Status:** Accepted — Phase 006 Group 06
Assessment remains sufficient for bounded composite-health and result-suitability evaluations. No Composite Health, Health Score, Readiness Suitability, Result Maturity or Timing concept is added.

### D-359 — Composite health is profile/use/context bound
**Status:** Accepted
A composite binds exact subject, consumer/use/context, profile/version, component roles/logic, current-cycle/window and evaluation/knowledge time. Unqualified global `healthy` is too broad for strong reasoning.

### D-360 — Composition logic is explicit
**Status:** Accepted
Required/optional/conditional/alternative/informational roles and AND/OR/conditional logic are declared by the profile. Majority vote, weighted averaging and post-hoc convenient composition are rejected.

### D-361 — No universal numeric health/confidence score
**Status:** Accepted
A scalar score that hides component violation, conflict, uncertainty, unavailability or waiver state is not accepted as canonical health truth.

### D-362 — Structured composite labels preserve component semantics
**Status:** Accepted
`healthy`, `healthy with warning`, `degraded`, `indeterminate`, `conflicting`, `unavailable` and `not applicable` can be derived shorthand only under explicit profile semantics with component drill-down/provenance retained.

### D-363 — Known violations and unresolved components can coexist
**Status:** Accepted
A decisive required violation may establish degradation while unresolved/unavailable components remain visible qualifiers. Unresolved state is not erased by another decisive result.

### D-364 — Waivers never create clean composite health
**Status:** Accepted
`violates + waived response` remains a violation during composition. A bounded rule that makes the criterion genuinely non-applicable is distinct.

### D-365 — Severity, criticality and priority remain separate from health truth
**Status:** Accepted
Low severity does not erase a violation; high criticality does not create one. These dimensions can guide governance/presentation/escalation but are not hidden evidence or Impact proof.

### D-366 — Audience projections share one underlying health truth
**Status:** Accepted
Technical/business/executive/audit views can vary authorized detail, but cannot strengthen or contradict the same bound composite proposition. Consumer-specific profiles may differ because their propositions differ.

### D-367 — Result freshness is use-specific
**Status:** Accepted
Evidence/result age is evaluated relative to an exact operational/readiness use, current-cycle context and governing freshness requirement. No universal health-result TTL is adopted.

### D-368 — Evaluation recency does not prove evidence recency
**Status:** Accepted
A newly recomputed Assessment over stale evidence remains stale for a use that requires current evidence. Assessment evaluation time and underlying evidence time stay distinct.

### D-369 — Cached prior results are not silently current
**Status:** Accepted
When current retrieval fails, retained prior evidence may be reused only when the exact use permits its age/context; otherwise current suitability remains unresolved/unavailable.

### D-370 — Health results mature progressively by evidence, not elapsed time
**Status:** Accepted
Immediate operational, fast core/schema, enriched DQ/reconciliation/distribution, diagnostic/RCA and retrospective horizons are functional evidence horizons. Elapsed time never upgrades a result.

### D-371 — Narrow trustworthy results should not wait for the slowest evidence
**Status:** Accepted
Emit a supported narrow proposition as soon as its evidence standard is met. Pending slower evidence can keep a broader composite incomplete without invalidating that narrow fact.

### D-372 — Readiness suitability is exact-use and outcome-neutral
**Status:** Accepted
Suitability asks whether a specific result may participate in an exact readiness criterion/opportunity. A suitable violation can support `not ready`; a stale `meets` result can be unsuitable.

### D-373 — Readiness suitability preserves evidence/comparability/cycle limitations
**Status:** Accepted
Required sufficiency, availability, conflict state, comparability/reference validity, current-cycle identity, permitted evidence age and required maturity remain part of suitability.

### D-374 — AUTH-023 eligibility and evidence suitability are independent prerequisites
**Status:** Accepted
High-consequence eligibility cannot make stale/immature/unavailable/non-comparable evidence usable, and fresh suitable evidence cannot create eligibility.

### D-375 — Suitability does not create readiness, control authority or enforcement
**Status:** Accepted
Health outcome ≠ suitability ≠ readiness result ≠ gate decision ≠ control authorization ≠ enforcement ≠ actual execution.

### D-376 — Active-control fallback remains separately governed
**Status:** Accepted
Unsuitable/unavailable health evidence does not silently become ready/not-ready or fail-open/fail-closed. Any fallback remains part of the explicit readiness/control policy.

### D-377 — Passive monitoring remains non-blocking by default
**Status:** Accepted
Monitoring degradation does not delay ungated production. Only explicitly configured active controls can make selected evidence a prerequisite.

### D-378 — Progressive late evidence revises broader summaries without rewriting narrow history
**Status:** Accepted
Later enriched/corrected evidence can produce new composite Assessments and retrospective understanding while preserving earlier narrow results and actual historical composites.

### D-379 — Historical composite and suitability replay is non-rewriting
**Status:** Accepted
Replay uses the then-effective profile, component/rule/reference/reconciliation versions, evidence/current-cycle state, freshness/suitability semantics and knowledge cut. Current rules are not projected backward.

### D-380 — Historical suitability remains separate from historical gate behavior
**Status:** Accepted
A historical result being suitable/ready does not prove gate decision, enforcement or execution; those remain independently evidenced.

### D-381 — Group 06 scenario review passes
**Status:** Accepted
H06-01–H06-44 pass under HLTH-055–HLTH-066 without a new concept, universal score, hidden precedence, latency shortcut or control conflation.

### D-382 — Phase 006 Group 06 exits; Group 07 is next
**Status:** Accepted
HLTH-001–HLTH-066 are accepted. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged. Phase 006 Group 07 — Consolidation / Exit Review is next and has not started.