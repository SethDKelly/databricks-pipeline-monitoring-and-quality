# Decision Records — Pre-Group-06 Execution Gating and Non-Interference Addendum

This file continues the durable decision sequence after D-070 in [`phase_003_group_05_impact_annotation_explanation.md`](phase_003_group_05_impact_annotation_explanation.md).

### D-071 — Passive monitoring is non-blocking and out-of-band by default

**Status:** Accepted — pre-Group-06 refinement

The monitoring/quality framework should not become a mandatory production critical-path dependency merely because an asset is monitored. Baseline observation, evidence collection, health evaluation, Investigation, Impact analysis, and Explanation should prefer out-of-band/platform metadata integrations and should not delay production jobs when no explicit active-control feature is enabled.

Framework degradation must not silently delay otherwise ungated production execution.

### D-072 — Baseline monitoring should prefer production-repository independence

**Status:** Accepted — pre-Group-06 refinement

The framework should be independently deployable/versioned from the Git repositories and GitHub Actions workflows that deploy production Databricks jobs. Baseline monitoring should prefer no required ETL-code changes, library injection, or workflow-step changes in each production repository when required evidence can be obtained from Databricks/platform/source metadata instead.

This is an architectural objective rather than a guarantee that no future integration will ever require source changes. Any exception must be explicit, minimized, and justified by missing evidence/control capability.

### D-073 — Add Execution Gate as a narrow post-Phase-002 concept addendum

**Status:** Accepted — discovered before Phase 003 Group 06

The accepted model can assess dependency readiness and can protect output propagation, but no concept owns whether a downstream execution opportunity itself may start or must wait. **Execution Gate** is accepted as the 23rd concept.

Execution Gate owns explicit downstream admission/hold/admit/override state based on declared prerequisite readiness. It does not replace Execution History, Assessment, Capability Authorization, or Propagation Safeguard.

### D-074 — Dependency readiness gating is optional active control, not implicit monitoring behavior

**Status:** Accepted — pre-Group-06 refinement

Lineage, scheduling, or a readiness Assessment does not automatically enable gating. A downstream execution is blocked only when an explicit gate is applicable and active under accepted authority/control semantics.

When no gate applies, the framework remains observational: it may report that the downstream run started before the upstream dependency was ready, but it does not delay the run.

### D-075 — Execution Gate and Propagation Safeguard protect different boundaries

**Status:** Accepted — pre-Group-06 refinement

Execution Gate controls whether a downstream execution starts. Propagation Safeguard controls whether a produced/current state is allowed to propagate or be consumed at a defined boundary.

A gate can prevent stale recomputation before execution. A safeguard can protect consumers when suspect output already exists, when no qualifying output exists, or when a consumer boundary needs to be held. The controls may coexist; neither substitutes for the other.

### D-076 — Gate readiness and fallback must be evidence- and policy-explicit

**Status:** Accepted — pre-Group-06 refinement

A successful upstream run is not automatically a qualifying current dependency state unless the gate criterion explicitly says so. Gate criteria may require current-cycle output availability, freshness, version, completion, or another accepted readiness condition.

Missing readiness/control evidence is not automatically `ready`. The project does not adopt one universal fail-open or fail-closed behavior. Each gate class/configuration must eventually define explicit unavailable/unknown behavior, timeout, escalation, and override semantics.

### D-077 — Gate-induced delay remains first-class ecosystem health/Impact evidence

**Status:** Accepted — pre-Group-06 refinement

Holding a downstream job may be the correct stale-data prevention action while separately causing a start-time, completion-time, readiness, or client-delivery violation. Those effects remain observable and assessable. Any proposition that the gate caused a downstream consequence belongs in Causal Claim.

### D-078 — Reopen Group 03 with SYN-032; Group 06 remains next and unstarted

**Status:** Accepted

SYN-011 remains the observational readiness/latency synchronization. **SYN-032 — Dependency Readiness Evidence → Execution Gate Admission** is added as an explicit active-control extension discovered after Group 05.

Groups 01–05 remain accepted. Group 06 — Historical Replay & Phase 003 Consolidation remains next and has not started. Group 06 must compose passive observation, optional active gating, safeguard protection, and historical replay without making monitoring availability a universal production dependency.
