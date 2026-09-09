# Phase 007 Group 04 — Execution Reconstruction, Dependency Sequence & Version Use

**Status:** Review complete — accepted

## Goal

Refine how the framework reconstructs actual execution/dependency sequence and version use from incomplete, late, duplicated or conflicting operational evidence.

## Group result

Group 04 accepts **OPS-034–OPS-049**. No new concept is required; **Execution History** remains the truth owner for actual execution reconstruction.

The central reconstruction chain is:

**opportunity/expected context → evidence-established execution instance → lifecycle/attempt assembly → actual sequence → run-specific implementation/input binding → produced output/version binding → bounded historical reconstruction**.

No link automatically manufactures the next.

## Accepted OPS contracts

1. [`OPS-034 — Execution Proposition Identity & Lifecycle Event Binding`](034_execution_proposition_identity_lifecycle_event_binding.md)
2. [`OPS-035 — Execution Opportunity, Expected Work, Gate State & Actual Instance Separation`](035_execution_opportunity_expected_work_gate_actual_instance.md)
3. [`OPS-036 — Logical Execution Assembly, Parent/Child & Multi-Job Association`](036_logical_execution_assembly_parent_child_multi_job_association.md)
4. [`OPS-037 — Attempt, Retry, Restart, Rerun, Backfill & Execution Continuity`](037_attempt_retry_restart_rerun_backfill_continuity.md)
5. [`OPS-038 — Actual Dependency Sequence, Runtime Precedence & Waiting`](038_actual_dependency_sequence_runtime_precedence_waiting.md)
6. [`OPS-039 — Run-Specific Input / Version Consumption Binding`](039_run_specific_input_version_consumption_binding.md)
7. [`OPS-040 — Produced Output / Version Binding & Qualification`](040_produced_output_version_binding_qualification.md)
8. [`OPS-041 — Execution ↔ Implementation-State Binding & Deployment Context`](041_execution_implementation_state_binding_deployment_context.md)
9. [`OPS-042 — Mid-Execution Activation, Rollback & Dynamic State`](042_mid_execution_activation_rollback_dynamic_state.md)
10. [`OPS-043 — Telemetry Normalization, Duplication, Common Derivation & Conflict`](043_telemetry_normalization_duplicate_common_derivation_conflict.md)
11. [`OPS-044 — Temporal Ordering, Clock Domains & Sequence Strength`](044_temporal_order_clock_domains_sequence_strength.md)
12. [`OPS-045 — Execution / Output / Consumption Negative Claims & Coverage`](045_execution_output_negative_claim_coverage.md)
13. [`OPS-046 — Partial Execution Evidence, Terminal Resolution & Level Scope`](046_partial_execution_terminal_resolution_level_scope.md)
14. [`OPS-047 — Multi-Input Version Set & Current-Cycle Alignment`](047_multi_input_version_set_current_cycle_alignment.md)
15. [`OPS-048 — Historical Execution Replay, Correction & Reassembly`](048_historical_execution_replay_correction_reassembly.md)
16. [`OPS-049 — Execution Reconstruction Ownership & Group 05 Handoff`](049_cross_concept_ownership_group05_handoff.md)

## Execution truth is evidence-backed, not schedule-backed

Group 04 explicitly separates:

**expected work ≠ execution opportunity ≠ Gate HOLD/ADMIT/override ≠ actual execution instance**.

Expected-but-missing work is represented through Expectation + sufficient negative Observation/Assessment evidence. Execution History never creates a phantom failed/cancelled execution to make the timeline look complete.

Lifecycle evidence can also be partial. Start, progress and terminal evidence mature independently; a missing completion does not automatically mean the run is still running, failed or cancelled.

## Logical execution / attempt continuity

One logical execution can span several platform jobs/tasks, and one job definition can participate in many execution instances. Assembly requires provenance-bearing identity/correlation/dependency evidence rather than name/time/repository proximity.

Retry, restart/resume, rerun and backfill are not universal synonyms. Source semantics determine whether repeated activity is another attempt within the same logical execution or a separate execution. Later success never rewrites an earlier failed attempt.

## Dependency sequence

Group 04 preserves a deliberate ladder:

**effective dependency → expected/scheduled order → actual temporal precedence → evidenced waiting/hold relationship → run-specific version consumption**.

Each proposition is stronger/different than the previous one and requires its own evidence. `A completed before C started` does not establish that C waited for A or consumed A's output. Lineage itself remains logical topology rather than runtime sequence.

## Run-specific version use

A consuming execution can be bound to a specific input/output/version only when applicable evidence establishes the encounter. `Latest upstream output`, `most recent successful run`, `active Deployment`, or temporal proximity are not substitutes.

Similarly, a run's implementation state can be composite across code/build, job/transformation definition, configuration, schema/interface and target facets. Deployment active-state intervals constrain possible state but do not automatically establish every run-specific facet.

Long-running executions that span activation/rollback boundaries are resolved by the actual binding semantics/evidence for each facet. Start-time or completion-time state is not chosen by convenience.

## Output truth

Execution success and output existence are independent propositions.

A successful run can have unknown output evidence. A failed/partial run can still have produced/committed material output. `Output exists` is also weaker than published/current-cycle/fresh/healthy/ready output, which remain separately owned criteria.

## Telemetry and sequence evidence

Duplicate/common-derived telemetry does not become independent corroboration. Out-of-order arrival does not reverse event time. Applicable conflicts remain visible rather than being resolved by latest/majority/source-count shortcuts.

Cross-source clocks may not support exact ordering. Group 04 therefore distinguishes explicit sequence/orchestration order, source-local order, compatible timestamp order and indeterminate order. Claims such as `first run after activation` carry these ordering limitations.

## Negative evidence

`No run`, `no start`, `no terminal event`, `no output`, `no retry`, and `no consumption` are strong bounded negative claims. They require REF-002/003/005 opportunity-to-observe and adequate coverage for the exact event/version/interface proposition.

A telemetry outage, missing event or unavailable source therefore remains an evidence limitation rather than a reassuring negative.

## Multi-input/current-cycle reasoning

Group 04 reconstructs the exact **input-version set** actually used by a multi-input execution where evidence permits. Unknown members remain explicit.

Whether those versions were current, fresh, expected or ready remains Phase 006/REF-024 Assessment/readiness semantics. A successful run can legitimately be reconstructed as consuming stale or mixed-cycle input.

## Historical behavior

Execution reconstruction is bitemporal and non-rewriting. Late events can complete a lifecycle, reassign child tasks, resolve version use or change which run qualifies as first/last around a deployment boundary. Current retrospective reconstruction may improve while the incident-time `as-known` state remains historically accurate.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **X04-01–X04-32**, including opportunities without runs, gate hold/admit without execution, partial lifecycle/output evidence, retry/rerun/backfill continuity, multi-job assembly, duplicate/conflicting/out-of-order telemetry, clock skew, actual dependency order, stale/old version consumption, active-deployment-versus-run-version ambiguity, mid-run activation/rollback, partial outputs, bounded no-output claims and late reconstruction.

## Durable boundaries

- expected/opportunity/gate state ≠ execution;
- execution instance ≠ complete lifecycle;
- attempt/retry/restart/rerun/backfill retain distinct evidence semantics;
- intended dependency ≠ actual sequence ≠ waiting ≠ consumption;
- active Deployment ≠ run-specific implementation state absent evidence;
- latest upstream output ≠ consumed output;
- run success ≠ output existence/qualification/health;
- duplicate/common-derived telemetry ≠ independent corroboration;
- event time ≠ arrival/knowledge time;
- cross-source timestamp order may be indeterminate;
- missing telemetry ≠ no run/output/consumption;
- current/fresh/ready input ≠ execution fact;
- reconstructed sequence/version evidence ≠ causality.

## Architecture boundary

Group 04 does not select event schemas/stores, Databricks/GitHub runtime telemetry sources, scheduler APIs, run-ID normalization implementation, deployment fingerprinting, persistence/replay architecture, stream/poll design, source-specific version-attestation mechanisms or concrete latency SLAs.

## Group exit gate

**Satisfied.** OPS-034–OPS-049 and X04-01–X04-32 establish evidence-backed execution identity, partial lifecycle/attempt continuity, actual ordering, run-specific input/output/implementation binding, telemetry normalization, negative evidence and bitemporal replay without a 25th concept.

**Next: Phase 007 Group 05 — Investigation Lifecycle, First-Deviation Localization & Causal Handoff.**