# Runtime Evidence, Health & Optional Control Synchronizations

**Canonical key:** `contract.synchronization.runtime_evidence_health_control`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.SYN`

**Owns current question:** How do Deployment, Execution History, Observation, reference context, Change, Assessment, Investigation, Safeguard and optional Gate coordinate at runtime without collapsing evidence, health and control?

**Stable IDs:** SYN-009–SYN-015, SYN-032

## Current semantics

Runtime coordination follows evidence provenance and exact identity/time bindings; success, timing, health, readiness and control propositions remain independent.

### SYN-009 — Execution + Active Deployment Context
Associate an execution with active Deployment/configuration state only where target/time and, when required, run-specific binding evidence support it. Active-at-time context alone is not universal proof of exact implementation use.

### SYN-010 — Operational Timing → Observation
Actual execution/output timing and lifecycle facts become provenance-bearing Observations/Execution History before health interpretation. Missing telemetry is not converted into observed absence.

### SYN-011 — Operational Dependency Timing + Readiness/Latency Assessment
Evaluate readiness/latency against explicit evidence/reference context while keeping dependency timing separate from freshness, consumed-version proof, data quality, causal attribution, or automatic blocking.

### SYN-012 — Runtime Observation + Applicable Reference Context
Resolve the exact time-valid authorized Expectation and/or comparable Baseline versions for the Observation before Assessment. Current references are not substituted retroactively.

### SYN-013 — Observation Difference → Realized Change
Promote a runtime/data difference to a Change only when comparison semantics/evidence establish a meaningful realized transition. Not every numeric difference becomes a Change, and Change remains non-causal/non-health by itself.

### SYN-014 — Material/Uncertain Assessment → Investigation
A material violation, atypicality, mismatch or unresolved state may open/enrich Investigation. Automatic opening requires explicit response criteria; Assessment never establishes cause.

### SYN-015 — Assessment/Investigation + Propagation Safeguard
A concern may motivate a bounded Safeguard proposal. Proposal/authorization/request/effective enforcement remain separate; Assessment or Investigation does not activate protection automatically.

### SYN-032 — Readiness Evidence + Explicit Execution Gate
Only an explicitly configured, authorized Gate may evaluate/hold/admit/override an execution opportunity. Passive monitoring remains non-blocking by default. Readiness ≠ Gate decision ≠ enforcement ≠ execution, and Gate ≠ Safeguard.

## Invariants / boundaries

- Execution success ≠ output existence ≠ freshness ≠ data health.
- Observation ≠ Assessment; missing evidence ≠ negative truth.
- Gate/Safeguard are optional active-control branches, not default monitoring semantics.
- A trigger/sequence does not establish causation.

## Provenance

- `docs/concepts/phase_003/03_runtime_evidence_health_and_change/`
- Phase 002 post-exit Gate/Safeguard synchronizations retained in `docs/concepts/phase_003/README.md`
