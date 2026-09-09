# Decision Records — Phase 003 Group 05 Additions

This file continues the numbered durable decisions. D-001–D-039 remain in [`README.md`](README.md); D-040–D-046 in [`phase_003_group_03_runtime_health_and_safeguard.md`](phase_003_group_03_runtime_health_and_safeguard.md); D-047–D-055 in [`phase_003_group_04_lineage_investigation_causality.md`](phase_003_group_04_lineage_investigation_causality.md); D-056–D-060 in [`pre_group_05_capability_authorization.md`](pre_group_05_capability_authorization.md).

### D-061 — Impact preserves candidate, exposure, downstream effect, and consequence as separate evidence layers

**Status:** Accepted — Phase 003 Group 05

Historical downstream Lineage creates Impact candidates only. Actual encounter/consumption requires separate evidence; downstream Observation/Assessment/Change establishes effect; technical/analytical/business consequence requires its own evidence. No generic `affected` flag may silently collapse these strengths.

### D-062 — Exposure and non-exposure both require sufficient evidence

**Status:** Accepted — Phase 003 Group 05

Reachability, timing proximity, or downstream execution after an upstream event does not prove exposure. `Not exposed` likewise requires adequate refresh/version/consumption coverage; missing telemetry cannot become a reassuring negative.

A downstream effect may be observed while exposure remains unknown, and exposure may be proven while monitored downstream health remains acceptable.

### D-063 — Criticality and policy sensitivity influence context/priority but do not manufacture consequence

**Status:** Accepted — Phase 003 Group 05

Client-facing, regulated, executive, or otherwise high-criticality consumers may warrant rapid review while only reachable candidates. Criticality is not evidence of exposure/effect/consequence. Classification/Policy Context may govern handling and disclosure but do not establish policy breach, regulatory harm, compliance failure, or business consequence.

### D-064 — Business consequence and causal attribution require explicit evidence ownership

**Status:** Accepted — Phase 003 Group 05

Impact may record provenance-bearing technical, analytical, or business consequence evidence. If the product asserts that an originating condition caused/contributed to that downstream effect or consequence, the proposition belongs in Causal Claim under Group 04 semantics. Impact layering or Explanation prose cannot create causal attribution.

### D-065 — Enforced safeguards can support prevented-exposure conclusions without proving defect

**Status:** Accepted — Phase 003 Group 05

A proposed safeguard is insufficient. Where active enforcement evidence plus sufficient negative consumption coverage establishes that a suspect state did not cross the protected boundary, Impact may record non-exposure with the safeguard as basis and Explanation may state that exposure was prevented.

Protection does not prove the state was defective; blocked current state also does not guarantee freshness/healthy delivery. Safeguard-induced delay/non-delivery remains separate effect/consequence evidence, and causal attribution to the safeguard uses Causal Claim.

### D-066 — Annotation enriches reasoning but does not become a shadow structured-truth store

**Status:** Accepted — Phase 003 Group 05

Human context remains attributed Annotation. Reproducible facts belong in Observation/Change; causal propositions in Causal Claim; planned/normative/responsibility/governance assertions in their owning concepts. Impact may cite human consequence context while preserving human-source provenance, dispute, revision, and withdrawal state.

### D-067 — Authorized analytical projection supports useful RCA without direct data access

**Status:** Accepted — Phase 003 Group 05

Capability Authorization can expose a task-appropriate projection of approved health metrics/Assessments, execution timing, Lineage, policy/restriction summaries, responsibility context, Investigation/Causal Claim state, Impact, safeguards, and Annotation while direct rows/columns remain denied.

The projection is not a new truth concept. Derived/aggregate evidence is not automatically unrestricted, and hidden evidence is not retrieved merely to synthesize an unauthorized conclusion.

### D-068 — Analytical visibility remains separate from production-control authority

**Status:** Accepted — Phase 003 Group 05

Raw-data read, analytical visibility, job/run operational action, and safeguard-control capability remain independent. Explanation may disclose an authorized action capability when useful, but displaying permission does not execute an action and permission does not prove execution success.

### D-069 — Explanation consumes only authorized projected truth and preserves statement-to-basis traceability

**Status:** Accepted — Phase 003 Group 05

Explanation communicates authorized concept state; it cannot fetch hidden evidence for narrative completion, promote Impact layers, promote Causal Claim status, erase Annotation provenance, or infer compliance from policy metadata. Material statements remain internally traceable to projected basis and authorization/redaction context.

A historical authorization state may be described as evidence, but current requester authorization still governs present disclosure; historical replay cannot become an access-control bypass.

### D-070 — Phase 003 Group 05 downstream-impact/explanation exit gate is satisfied

**Status:** Accepted

Groups 01–05 now compose subject/governance context, planned change/prospective blast radius, runtime health/safeguards, Investigation/causal reasoning, layered downstream Impact, Annotation, capability-bounded analytical projection, and evidence-grounded Explanation without collapsing reachability, exposure, effect, consequence, causality, authorization, or operational control.

Group 06 — Historical Replay & Phase 003 Consolidation is next.