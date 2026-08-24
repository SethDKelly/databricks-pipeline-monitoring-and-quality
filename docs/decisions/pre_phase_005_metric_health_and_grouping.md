# Decision Records — Pre-Phase 005 Metric Health Handoff and Phase 005 Grouping

Continues after D-152.

### D-153 — Metric-health semantics belong primarily in Phase 006
**Status:** Accepted — pre-Phase-005 refinement
Metric families, per-asset metric profiles, threshold/margin semantics, Baseline/statistical behavior, metric propagation/reconciliation, metric-bloat control, and technical/business health composition belong primarily in Phase 006. Phase 005 governs who may define/approve/revise/waive/disclose those normative metric states.

### D-154 — Table health is broader than load occurrence
**Status:** Accepted — pre-Phase-005 refinement
A successful load/run does not establish that the produced table state is good. Health may require explicit evidence across output existence, freshness, volume, completeness, uniqueness, validity, distribution, relational/transformation integrity, and business-semantic dimensions as applicable.

### D-155 — Metric profiles should be purposeful rather than exhaustive
**Status:** Accepted — pre-Phase-005 refinement
The framework should distinguish a small core metric set, critical-field/business metrics, transformation-specific metrics, and diagnostic/on-demand metrics. Availability of a statistic is not sufficient reason to calculate, persist, alert on, or display it. Metric purpose, applicability, audience/use, cost/latency, authority, and lifecycle should constrain metric bloat.

### D-156 — Metric propagation is selective and transformation-aware
**Status:** Accepted — pre-Phase-005 refinement
Metrics do not recursively propagate through Lineage by default. Upstream health evidence may remain local context, be directly comparable, participate in a transformation-specific reconciliation, or be irrelevant downstream. Join/filter/aggregation/grain/business semantics determine valid relationships. Phase 006 defines health semantics; Phase 007 refines Lineage-aware propagation behavior.

### D-157 — Technical and business metric views are projections over one truth
**Status:** Accepted — pre-Phase-005 refinement
Technical users may need field-level diagnostic metrics, distributions, thresholds, join/reconciliation measures, and provenance, while business users may need freshness, critical-population completeness, business-metric validity, delivery readiness, and consequence-oriented summaries. These are audience-specific authorized projections, not separate health truths.

### D-158 — Metric timing follows progressive analytical availability
**Status:** Accepted — pre-Phase-005 refinement
Fast operational facts, inexpensive/core table health, richer Metric View/DQ/distribution metrics, diagnostic/RCA metrics, and retrospective/post-ops metrics may mature at different times. No metric becomes a synchronous production dependency merely because it is useful for monitoring. Metrics used by an explicit Execution Gate are a separate high-consequence case requiring accepted criterion, authority, evidence, and later control-path availability semantics.

### D-159 — Phase 005 will use seven review groups
**Status:** Accepted — phase-planning decision
Phase 005 will be reviewed as: (1) Authority Vocabulary, Source Assertions & Conflict Resolution; (2) Semantic, Responsibility, Classification, Policy & Criticality Governance; (3) Normative Health, Metric & Threshold Governance; (4) Capability Authorization & Restricted Analytical Visibility; (5) High-Consequence Action, Control & Causal-Confirmation Authority; (6) Disclosure, Explanation & Audience Governance; and (7) Consolidation / Exit Review. The grouping is a design-review sequence, not implementation architecture.

### D-160 — Phase 005 authority decisions must not steal Phase 006 metric semantics
**Status:** Accepted — phase-planning decision
Phase 005 may decide who is authoritative or permitted to define/approve metric profiles, Expectations, thresholds, margins, waivers, and disclosure. It must not decide the detailed metric taxonomy, statistical computation, propagation algorithm, overall-health aggregation, or technical realization reserved for later phases.