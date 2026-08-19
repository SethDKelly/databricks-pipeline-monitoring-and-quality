# Decision Records — Phase 003 Group 03 Additions

This file continues the numbered durable decisions in [`README.md`](README.md). Earlier decisions D-001–D-039 remain unchanged.

### D-040 — Add Propagation Safeguard as a narrow post-Phase-002 concept addendum

**Status:** Accepted — discovered during Phase 003 Group 03

The original 20-concept Phase 002 model did not contain functionality that could own a protective hold/quarantine/release state without overloading Assessment, Investigation, Impact, or Policy Context. **Propagation Safeguard** is therefore accepted as the 21st concept through an explicit post-exit addendum.

The earlier Phase 002 exit decision remains historically true for the requirements known then. This addendum is a later boundary correction, not a rewrite of that history.

### D-041 — Planned change supports prospective blast-radius reasoning without claiming actual Impact

**Status:** Accepted — Phase 003 Group 02 addendum

Change Intent + current Lineage + planned-only topology/context may identify downstream candidates before realization. Criticality, semantics, classification/policy, responsibility, and path completeness may enrich a **Prospective Impact Profile**.

Prospective reachability is not actual exposure, downstream effect, business consequence, causal proof, or a quantified probability/severity score. Planned topology remains distinct from active Lineage.

### D-042 — Execution timing and dependency latency are first-class ecosystem health dimensions

**Status:** Accepted — Phase 003 Group 03

Execution duration, actual start/completion, queue/wait behavior, dependency latency, and delivery readiness are operational Observations that can be compared with Baselines and/or Expectations. A run may succeed but still be too slow or too late for downstream needs.

Execution success, timely execution, freshness, and table-level data quality remain separate dimensions.

### D-043 — Runtime variation, health evaluation, and analyst intervention remain separate

**Status:** Accepted — Phase 003 Group 03

Raw run-to-run difference is not automatically a material Change. Baseline atypicality is descriptive and does not automatically become a normative violation or mandatory intervention.

Analysts may manually open Investigation from atypical, violated, unresolved, or otherwise suspicious Assessments where authorized. Automatic Investigation initiation requires explicit later-accepted response criteria. The system does not invent severity/urgency thresholds during Phase 003.

### D-044 — Propagation Safeguard activation and placement require explicit authority/context

**Status:** Accepted — Phase 003 Group 03

Assessment or prospective Impact may motivate a safeguard proposal but cannot automatically activate quarantine unless an explicit accepted response/authority rule permits it. Proposed and active safeguard states remain distinct, and enforcement evidence is required where applicable.

Safeguard placement is context-specific: origin output, environment/cohort, downstream publication boundary, or specific consumer set may be appropriate. Lineage/Impact inform placement but do not decide it automatically. Active quarantine does not prove defect; release does not prove health.

### D-045 — Missing output is distinct from missing telemetry and from quarantined output

**Status:** Accepted — Phase 003 Group 03

A missing run/output can be concluded only from sufficient coverage-bearing evidence. Monitoring-source failure remains insufficient evidence.

When no qualifying output exists, the product must not fabricate a quarantined data object. A Propagation Safeguard may instead hold downstream advancement/current-cycle publication so stale or absent state is not silently consumed as current.

### D-046 — Phase 003 Group 03 runtime synchronization exit gate is satisfied

**Status:** Accepted

Groups 01–03 now compose subject/governance context, planned-change/reference transition/prospective blast radius, active Deployment/execution timing, dependency readiness, time-valid health Assessment, realized Change, analyst Investigation handoff, and protective Propagation Safeguard behavior without conflating operational success, data quality, atypicality, cause, or quarantine.

Group 04 — Lineage, Investigation & Causal Reasoning is next.
