# Phase 004 Group 04 Scenario Checks

These synthetic checks apply REF-001–REF-030 to exposure, readiness, and control evidence. They validate evidence semantics only; they do not choose integrations or architecture.

| Scenario | Evidence / condition | Accepted result |
|---|---|---|
| Report refreshes affected C version | Refresh provenance binds Report R to C version V in the affected window | `exposed to V`; health/consequence/causality remain separate |
| Report refreshes but version is unknown | Refresh is proven; consumed C state cannot be resolved | exposure `unknown/insufficient`, not `exposed` or `not exposed` |
| Report uses earlier safe version | Version provenance proves pre-incident V-1 | `not exposed to V`; freshness may separately be stale |
| No report refresh with complete history | Refresh opportunities/history sufficiently cover the bounded window | `not exposed` may be supported |
| No refresh telemetry | Consumer integration unavailable | exposure unresolved; never infer `not exposed` |
| Metric View refresh | Materialization provenance binds affected table version/window | exposed if binding is sufficient; downstream metric health separate |
| Business process has report available | Publication is proven but no use/decision evidence exists | report publication exposure does not establish business-process use |
| Business process uses report | Proven process/decision use ties to affected report state | process-use exposure may be established at that boundary |
| Alternate consumer path unknown | Primary path shows non-consumption; alternate path coverage incomplete | global non-exposure remains unresolved |
| Upstream job succeeds only | Gate criterion requires current output + freshness | completion predicate satisfied; overall readiness not yet satisfied |
| Current output exists but is stale | Criterion requires freshness | output-existence predicate true; readiness false if freshness violation sufficiently evidenced |
| Completion-only gate | Criterion explicitly requires only successful completion | readiness may be satisfied even while DQ/Metric View evidence is pending; broader health unknown |
| Required predicate telemetry missing | Output-version evidence unavailable | readiness unknown/unavailable; fallback may act but does not create `ready` |
| Hold decision, downstream run starts | Reliable run begins while hold applies, no override/release | full hold enforcement contradicted |
| Hold decision, no run, telemetry incomplete | Run history unavailable | enforcement unknown; absence cannot prove hold |
| Hold decision, complete opportunity coverage, no run | Gate/control evidence plus complete execution opportunity history support suppression | hold enforcement supported for that opportunity |
| Admit decision, downstream does not run | Gate removed barrier; job never starts | admission can remain valid; non-run does not prove admission failure |
| Admit then downstream runs | Decision + enforcement + run timing are consistent | admission/enforcement may be supported; run remains Execution History |
| Safeguard requested | Operator/control request exists without external boundary proof | proposed/requested, not enforced active |
| Safeguard enforced on publication boundary | Boundary evidence proves suspect V blocked | active/enforced for that scope; exposure still requires consumer evidence |
| Safeguard enforced, no consumer refresh opportunity | Consumer never attempted/needed refresh | `not exposed` may hold, but do not claim safeguard `prevented exposure` without material control opportunity |
| Safeguard blocks only route during refresh opportunity | Enforced boundary + negative consumption + path coverage | prevented exposure supported |
| Safeguard blocks primary route, alternate route unknown | Alternate path could serve V | prevented exposure unresolved globally |
| Current suspect output blocked, prior output served | Consumer receives V-1 | not exposed to V; separately evaluate stale delivery |
| Control integration unavailable, fallback configured | Rule says hold on unavailable but runtime application is not observed | configured fallback known; actual fallback/enforcement unknown |
| Control integration unavailable, fallback application proven | Runtime evidence shows hold behavior under fallback | actual fallback/enforcement may be established |
| Gate hold coincides with client delay | Hold and delay both observed | causal claim can be supported only after applicable mechanism/alternative review |
| Late logs show hold was bypassed | Incident-time enforcement unknown; later run evidence appears | retrospective enforcement revised; historical decision/knowledge preserved |
| Late report logs show exposure | Incident-time exposure unknown; later provenance proves V consumed | retrospective exposure becomes exposed; contemporaneous view stays unknown |

## Result

The scenario set does not expose a missing truth-owning concept. REF-021–REF-030 specialize the accepted Impact, Execution Gate, Propagation Safeguard, Causal Claim, Execution History, Observation, Assessment, and historical-replay boundaries without selecting technical architecture.
