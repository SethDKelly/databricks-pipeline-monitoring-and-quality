# HLTH-049 — Freshness, Current-Cycle & Multi-Input Version Alignment

## Rule

Cross-input freshness reasoning binds the exact versions/windows/cycles of every material input actually used to produce the output. Output completion time alone does not establish current-cycle alignment.

Useful reconciliation observations can include:

- input version/event-time used per source;
- expected versus actual cycle/window alignment;
- source-to-output lag;
- mixed-current/stale input composition;
- intentionally permitted lag or safe-earlier-version use where explicitly defined.

## Invariants

- A successful/current C run can still have consumed a stale B version.
- The freshest input does not determine output freshness when other required inputs are older.
- Runtime dependency timing or Lineage reachability does not prove which input version was consumed.
- `not exposed to suspect version V` can coexist with stale delivery.
- Different inputs may have intentionally different allowed cadences; alignment is criterion-relative rather than universal timestamp equality.
- Missing consumption/version evidence yields unresolved alignment rather than presumed currentness.
- Current-cycle reconciliation can support later readiness evaluation but is not itself an Execution Gate decision or enforcement state.
