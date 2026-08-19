# Decision Records — Phase 003 Group 04 Additions

This file continues the numbered durable decisions. D-001–D-039 remain in [`README.md`](README.md); D-040–D-046 remain in [`phase_003_group_03_runtime_health_and_safeguard.md`](phase_003_group_03_runtime_health_and_safeguard.md).

### D-047 — Investigation scope begins from the outcome/question rather than a presumed cause

**Status:** Accepted — Phase 003 Group 04

An Investigation records the subject, question/outcome, effective/event-time window, initiating evidence, and known gaps. Scope may be refined as evidence arrives, but opening the inquiry cannot encode a presumed root cause as fact.

### D-048 — Historical Lineage discovers evidence candidates and localization, not causes

**Status:** Accepted — Phase 003 Group 04

Typed Lineage effective during the incident window is used to discover structurally relevant upstream/dependency candidates. Reachability, directness, path length, repository proximity, and first-observed deviation do not establish causal status.

The earliest monitored point where a related deviation is observed may be reported as localization. If the path crosses an out-of-scope/restricted/unobserved boundary, the causal origin may remain upstream/unknown.

### D-049 — Causal evaluation preserves separate evidence dimensions and explicit contradiction

**Status:** Accepted — Phase 003 Group 04

Causal Claim evaluation considers temporal ordering, relationship applicability, actual encounter/consumption when required, realized state/change, semantic/mechanism compatibility, contrasts/interventions, alternative explanations, and evidence coverage. Supporting and contradicting evidence are retained separately rather than collapsed into an unexplained score.

Reliable evidence that the effect predates the proposed cause materially contradicts the claim. Negative/unchanged evidence can exclude only when source/topology coverage is sufficient; missing telemetry cannot become exclusion evidence.

### D-050 — Causal propositions must be explicit Causal Claims

**Status:** Accepted — Phase 003 Group 04

No causal proposition should be hidden in Lineage traversal, Deployment proximity, Change Intent consistency, Prospective Impact Profile, safeguard state, or Explanation narrative. A proposition that X caused/contributed/enabled/prevented Y belongs in Causal Claim with explicit epistemic state and evidence links.

### D-051 — Confirmation remains gated; automated RCA must stop short without an accepted standard

**Status:** Accepted — Phase 003 Group 04

Automated or analyst reasoning may propose claims and attach support/contradiction. `confirmed` requires an explicit accepted evidence/authority standard. Phase 003 does not invent that standard; until later refinement accepts one, a compelling automated explanation may be `supported` but cannot be labeled confirmed root cause merely because it ranks first or lacks known alternatives.

### D-052 — Multiple contributors and unresolved Investigation outcomes are first-class

**Status:** Accepted — Phase 003 Group 04

Several Causal Claims may remain supported as contributing explanations. Investigation closure may be multi-causal, unresolved, resolved for an operational purpose, or no-actionable-conclusion. Closing an Investigation never promotes a claim's epistemic status.

### D-053 — Analyst research enters the owning structured concept rather than an Annotation shadow store

**Status:** Accepted — Phase 003 Group 04

Reproducible analyst measurements/facts use Observation semantics; supported realized differences may use Change; causal propositions use Causal Claim; contextual commentary uses Annotation; structured plan/norm/responsibility/governance assertions use their respective owning concepts. Human title alone does not create universal authority or confirmation.

### D-054 — Prospective blast radius and safeguard state remain distinct from retrospective causal evidence

**Status:** Accepted — Phase 003 Group 04

A Prospective Impact Profile can inform where to inspect after a planned change but cannot support a retrospective cause merely because the incident occurred within the predicted blast radius. Incident-time Lineage and realized evidence are required.

An active Propagation Safeguard may itself be a causal condition for a delivery delay if enforcement/timing evidence supports that proposition, while remaining no proof that the protected data was defective.

### D-055 — Phase 003 Group 04 causal-reasoning synchronization exit gate is satisfied

**Status:** Accepted

Groups 01–04 now compose subject/governance context, planned-change/prospective blast radius, runtime timing/health/change/safeguard state, bounded Investigation, historical evidence candidate discovery, evidence assembly, explicit competing Causal Claims, support/contradiction, analyst research, and honest multi-causal/unresolved outcomes without forced root cause.

Group 05 — Downstream Impact, Annotation & Explanation is next.
