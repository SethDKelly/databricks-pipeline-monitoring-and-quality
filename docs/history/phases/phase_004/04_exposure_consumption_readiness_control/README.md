# Phase 004 Group 04 — Exposure, Consumption, Readiness & Control Evidence

**Status:** Review complete — refinements accepted

## Goal

Specialize REF-001–REF-020 for evidence that proves or fails to prove downstream exposure/non-exposure, upstream readiness, gate decision/enforcement, safeguard enforcement/prevented exposure, and degraded/unavailable control integration.

## Accepted refinements

- **REF-021 — Exposure Proposition and Encounter Binding**
- **REF-022 — Positive Exposure / Consumption Evidence**
- **REF-023 — Non-Exposure and Negative Consumption Coverage**
- **REF-024 — Dependency Readiness Criterion Decomposition**
- **REF-025 — Execution Gate Decision, Enforcement, and Actual Execution**
- **REF-026 — Gate Enforcement Evidence and Degraded Control State**
- **REF-027 — Propagation Safeguard Activation and Enforcement Evidence**
- **REF-028 — Prevented Exposure Evidence Standard**
- **REF-029 — Control Telemetry, Fallback, and Unavailable-State Evidence**
- **REF-030 — Control-Effect Causality and Retrospective Revision**

## Accepted boundaries

1. **Exposure is encounter-specific.** Reachability, timing overlap, or downstream activity does not establish consumption of the affected state.
2. **Consumer class/encounter mode matters.** Execution input, refresh/materialization, publication, application use, and business-process use can require different evidence.
3. **Non-exposure is a negative conclusion.** It requires sufficient bounded coverage of the relevant encounter opportunities and material paths.
4. **Safe-version use is not the same as inactivity.** A consumer can be not exposed to the affected version while still stale or unhealthy.
5. **Readiness is criterion-relative.** `Upstream job succeeded` is not global readiness unless that is the entire declared criterion.
6. **Readiness predicates remain separate.** Completion, output existence, version/currentness, freshness, publication availability, and quality conditions do not substitute for one another.
7. **Unknown readiness remains unknown.** A fallback may control what happens next but does not turn missing evidence into `ready`.
8. **Gate decision ≠ gate enforcement ≠ actual execution.** Each requires its own evidence.
9. **Hold/admit evidence is asymmetric.** A reliable run during an unoverridden hold contradicts full hold enforcement; lack of a run does not prove hold enforcement without opportunity/telemetry coverage. An admit that is not followed by a run does not prove admission failed.
10. **Configured/enabled control ≠ specific enforcement.** External control effects require opportunity/boundary-specific evidence.
11. **Safeguard proposal/request ≠ enforced active safeguard.** Enforcement is boundary-, scope-, and time-specific.
12. **Prevented exposure is stronger than `safeguard active + not exposed`.** The safeguard must be materially operative on the relevant encounter path, with sufficient negative-consumption and alternate-path coverage.
13. **Blocking the suspect state does not prove current/fresh/healthy delivery.** Older state may remain served and must be assessed separately.
14. **Fallback policy ≠ actual fallback execution.** Degraded control telemetry cannot be translated into invented fail-open/fail-closed behavior.
15. **Control-effect causality uses the accepted causal framework.** Direct deterministic mechanism evidence may produce strong results quickly, but broader delay/non-delivery/business causal claims still require applicable alternative/coverage review.
16. **Late evidence changes retrospective understanding, not historical action.** Gate decisions, safeguard actions, actual executions, and historical Explanations remain non-rewriting.

## Representative results

See [`scenario_checks.md`](scenario_checks.md). The scenarios cover reports/Metric Views/jobs/business-process consumers, safe-version refreshes, missing version telemetry, readiness decomposition, unenforced holds, admitted-but-not-run cases, safeguard alternate paths, stale fallback, degraded gate/control telemetry, and late enforcement/consumption evidence.

No scenario requires a new Concept or Phase 003 synchronization. The accepted catalog remains 23 concepts and SYN-001–SYN-035.

## Timing and integration implication

Group 04 strengthens the progressive-result model:

- run/completion/readiness predicates may sometimes be available on the fast operational path;
- exposure, version association, and control-enforcement conclusions become available only when their specific evidence arrives;
- `not exposed`, prevented exposure, and causal control-effect conclusions may require broader negative/path coverage and therefore mature later;
- control-path evidence required for an enabled Execution Gate may need stronger availability guarantees than passive monitoring, but exact source latency/SLO/architecture remains deferred to Phases 006/009/010/011.

## Exit review

Group 04 exit gate is **satisfied**:

- exposure/non-exposure have explicit proposition/coverage standards;
- readiness is criterion-bound rather than globally inferred;
- gate decision, enforcement, and Execution History remain distinct;
- safeguard activation/enforcement and prevented exposure have explicit proof standards;
- degraded control telemetry/fallback semantics preserve unknowns rather than inventing behavior;
- causal and historical rules compose without control shortcuts;
- no implementation architecture was selected.

**Phase 004 Group 05 — Consolidation / Exit Review is next and has not started.**
