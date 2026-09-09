# Decision Records — Phase 007 Group 04 Execution Reconstruction

Continues after D-461.

### D-462 — Group 04 requires no new concept
**Status:** Accepted — Phase 007 Group 04
Execution History remains the owner of actual execution reconstruction; new semantics are refinements/synchronizations over existing concepts.

### D-463 — Actual execution requires an evidence-bound execution proposition
**Status:** Accepted
Schedule slots, job names, repository revisions and prospective review state cannot create an execution instance.

### D-464 — Separate expected work, execution opportunity, Gate state and actual execution
**Status:** Accepted
A missed/held/admitted opportunity is not a phantom failed/successful run.

### D-465 — Lifecycle facts mature independently
**Status:** Accepted
Start, progress and terminal evidence may be partial; missing transitions are not fabricated.

### D-466 — Logical execution assembly is evidence-driven
**Status:** Accepted
Multi-job/task assembly requires identity/correlation/dependency evidence; overlap/name/repository proximity is insufficient.

### D-467 — Retry, restart, rerun and backfill are not universally interchangeable
**Status:** Accepted
Continuity follows source semantics/evidence and preserves each historical attempt/execution.

### D-468 — Attempt outcome is not automatically logical-execution outcome
**Status:** Accepted
No hidden `last attempt wins` or child-to-root outcome propagation rule is accepted.

### D-469 — Intended dependency, temporal precedence, waiting and consumption remain distinct
**Status:** Accepted
Ordering evidence cannot manufacture wait/consumption semantics.

### D-470 — Positive input/version use requires run-specific encounter evidence
**Status:** Accepted
Lineage, latest output, prior completion or time proximity alone does not establish consumption.

### D-471 — Run success and output existence/version are independent
**Status:** Accepted
Successful runs can have unknown outputs; failed/partial runs can still produce material output.

### D-472 — Qualifying output is criterion-specific
**Status:** Accepted
Exists/committed/published/current-cycle/fresh/healthy/ready remain distinct propositions.

### D-473 — Deployment active-state constrains but does not universally prove run implementation state
**Status:** Accepted
Run-specific code/config/schema/transformation facets require sufficient binding evidence.

### D-474 — Mid-run activation/rollback is facet-specific
**Status:** Accepted
No universal start-time/completion-time or automatic in-flight switch/reversion rule is accepted.

### D-475 — Duplicated/common-derived telemetry is not independent corroboration
**Status:** Accepted
Common-root evidence remains common-root under REF-004.

### D-476 — Conflict and out-of-order arrival remain explicit
**Status:** Accepted
Latest/majority/source-count does not silently resolve bounded conflict; arrival order does not rewrite event order.

### D-477 — Cross-clock timestamp comparison can be insufficient for sequence
**Status:** Accepted
Explicit sequence/orchestration evidence can be stronger; close cross-source time order may remain indeterminate.

### D-478 — `No run/output/consumption` requires strong bounded negative evidence
**Status:** Accepted
Missing/unavailable/restricted telemetry is not operational absence.

### D-479 — Partial lifecycle and level-specific outcomes remain partial
**Status:** Accepted
Child/root state and source-specific terminal semantics are not silently promoted or completed.

### D-480 — Currentness/freshness/readiness are not execution facts
**Status:** Accepted
Execution reconstruction supplies exact version-use evidence; Phase 006/REF-024 determine suitability/readiness.

### D-481 — Multi-input version set is role-bound and may be incomplete
**Status:** Accepted
One known input or same date/window does not manufacture a complete current-cycle set.

### D-482 — Historical execution reconstruction is bitemporal and non-rewriting
**Status:** Accepted
Late lifecycle/identity/version evidence improves retrospective reconstruction without rewriting what was known then.

### D-483 — Group 05 consumes sequence/version evidence without causal promotion
**Status:** Accepted
First post-change run, first deviation, shared version, temporal proximity and execution ordering remain Investigation evidence rather than root cause.

### D-484 — OPS-034–OPS-049 and X04-01–X04-32 are accepted; Group 04 exits complete
**Status:** Accepted
The concept catalog remains 24. OPS-001–OPS-049 is accepted through Group 04; SYN-001–SYN-035, REF-001–REF-030, AUTH-001–AUTH-053 and HLTH-001–HLTH-066 remain unchanged. Phase 007 Group 05 is next.