# Exposure, Readiness & Control-Proof Evidence

**Canonical key:** `ref.exposure-readiness-control-proof`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.REF`

**Owns current question:** What evidence proves exposure/non-exposure, dependency readiness, Gate/Safeguard enforcement, prevented exposure, or broader control effects?

**Stable IDs:** REF-021–REF-030

## Current semantics

### REF-021 — Exposure Proposition and Encounter Binding
Exposure binds the exact affected state/version/window to an actual consumer/use encounter. Reachability, timing overlap or downstream activity alone is insufficient.

### REF-022 — Positive Exposure / Consumption Evidence
Positive exposure requires applicable evidence that the consumer encountered/consumed the bound affected state through the relevant consumer mode.

### REF-023 — Non-Exposure and Negative Consumption Coverage
`not exposed` is a bounded negative conclusion requiring adequate encounter-opportunity, version and material-path coverage. Missing consumption telemetry is not reassuring evidence.

### REF-024 — Dependency Readiness Criterion Decomposition
Readiness is criterion-relative. Completion, output existence, version/currentness, freshness, publication availability and named quality predicates are separate possible criteria; upstream success is not global readiness.

### REF-025 — Execution Gate Decision, Enforcement, and Actual Execution
Readiness result, Gate decision, decision delivery/acceptance, effective enforcement and actual downstream execution are separate propositions with separate evidence.

### REF-026 — Gate Enforcement Evidence and Degraded Control State
Configured/enabled control does not prove opportunity-specific enforcement. A reliable start during an applicable unsuperseded HOLD contradicts full hold enforcement; no start proves enforcement only with adequate opportunity/telemetry coverage.

### REF-027 — Propagation Safeguard Activation and Enforcement Evidence
Safeguard proposal/request/configuration does not establish active protection. Effective safeguard state requires boundary/scope/time-specific enforcement evidence.

### REF-028 — Prevented Exposure Evidence Standard
`prevented exposure` requires materially operative safeguard enforcement on the relevant encounter path plus sufficient negative-consumption/version and alternate-path coverage. `safeguard active + not exposed` is insufficient by itself.

### REF-029 — Control Telemetry, Fallback, and Unavailable-State Evidence
Fallback configuration, fallback trigger and actual fallback action are distinct. Missing/conflicting control telemetry cannot be converted into invented fail-open, fail-closed, hold or release behavior.

### REF-030 — Control-Effect Causality and Retrospective Revision
Broader claims that a Gate/Safeguard caused delay, non-delivery or business effect use REF-013–REF-020. Late control/consumption evidence may revise retrospective conclusions but not historical actions.

## Invariants / boundaries

- reachability ≠ exposure;
- safe prior-version encounter can mean not exposed to suspect state while freshness remains stale;
- readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Safeguard configured/requested ≠ effective enforcement ≠ prevented exposure ≠ recovery;
- unknown evidence remains unknown even when an explicit fallback controls what action occurs.

## Synchronizations / related canonical resources

Uses Impact, Execution Gate, Propagation Safeguard, Execution History, Observation and Causal Claim. AUTH-033–AUTH-043 govern who may act without changing proof semantics.

## Provenance

- `docs/concepts/phase_004/04_exposure_consumption_readiness_control/README.md`
- Phase 004 Group 04 accepted REF-021–REF-030.
