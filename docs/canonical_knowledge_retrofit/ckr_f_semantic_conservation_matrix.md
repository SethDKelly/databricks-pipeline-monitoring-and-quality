# CKR-F Semantic Conservation Matrix — Lineage, Change, Investigation, Impact & Control

**Status:** ACCEPTED — CKR-F COMPLETE

**Scope:** OPS-001–OPS-123 canonicalized from accepted Phase 007 semantics.

## Conservation objective

CKR-F migrates accepted Phase 007 operational semantics into bounded canonical resources without changing the 24-concept model, introducing OPS-124, selecting architecture, or collapsing adjacent truth layers.

## Required conserved boundaries

| Boundary | Conserved rule |
|---|---|
| Lineage | Lineage ≠ causality |
| Topology | reachable ≠ operationally relevant ≠ exposed/affected |
| Propagation | Lineage does not propagate metric, health, governance, Impact or causal status |
| Historical topology | planned topology ≠ effective topology ≠ specific runtime encounter |
| Negative topology | missing edge/path evidence ≠ absent edge/path |
| Authority | Assertion Authority ≠ evidence sufficiency |
| Change | Change Intent ≠ Deployment ≠ Change |
| Runtime identity | repository revision ≠ deployed runtime identity absent evidence |
| Deployment | attempt ≠ success ≠ activation ≠ effect |
| Realization | association ≠ activation ≠ conformance |
| Realization negatives | not evidenced ≠ not realized |
| Rollback | rollback/reversion ≠ historical erasure ≠ universal downstream restoration |
| Prospective analysis | planned scenario topology ≠ effective Lineage |
| Blast radius | candidate ≠ exposure ≠ effect ≠ consequence ≠ cause |
| Review | review relevance ≠ obligation ≠ approval ≠ control |
| Risk | Criticality/priority ≠ probability/Impact; no universal risk score |
| Execution | expected work ≠ opportunity ≠ Gate state ≠ actual execution |
| Runtime sequence | intended dependency ≠ actual sequence ≠ waiting ≠ consumption |
| Version use | active Deployment ≠ run-specific implementation state absent evidence |
| Output | run success ≠ output existence ≠ currentness/freshness/health |
| Telemetry | duplicate/common-derived telemetry ≠ independent corroboration |
| Execution negatives | missing telemetry ≠ no run/output/consumption |
| Investigation | question/trigger ≠ presumed cause |
| Investigation lead | lead ≠ Causal Claim |
| Localization | first observed ≠ earliest evidenced ≠ first reconciliation boundary ≠ first consumer effect |
| Cause | localization/reconciliation/version proximity ≠ cause |
| Exclusion | lack of evidence ≠ exclusion/rejection |
| Causal confirmation | confirmation requires REF-017 plus AUTH-034 |
| Closure | Investigation closure/operational resolution ≠ causal confirmation |
| Exposure | candidate/reachable ≠ encounter opportunity ≠ actual exposure |
| Publication/use | available/published/served ≠ actual use |
| Version encounter | refresh/run timing ≠ consumed-version proof |
| Multi-hop | exposure does not transitively propagate through Lineage |
| Non-exposure | one safe path ≠ global non-exposure |
| Impact | exposed ≠ downstream effect ≠ consequence ≠ causal attribution |
| Impact negatives | not exposed/no effect/no consequence require bounded negative evidence |
| Safeguard lifecycle | proposal/configuration/authorization/request ≠ effective enforcement |
| Safeguard scope | active safeguard ≠ global path protection |
| Prevention | not exposed ≠ prevented by Safeguard |
| Prevention opportunity | no encounter opportunity ≠ prevention evidence |
| Safeguard release | release request ≠ effective release ≠ recovery |
| Control telemetry | missing telemetry ≠ fail-open/fail-closed/fallback application |
| Control types | Propagation Safeguard ≠ Execution Gate |
| Gate inputs | health/result outcome ≠ exact-use suitability ≠ readiness |
| Gate lifecycle | readiness ≠ Gate decision ≠ delivery/acceptance ≠ enforcement ≠ execution |
| HOLD | HOLD ≠ execution failure; no run ≠ successful HOLD without coverage |
| ADMIT | ADMIT ≠ execution occurrence |
| Override | override ≠ ready |
| Fallback | fallback ≠ override; configured fallback ≠ trigger ≠ application ≠ enforcement |
| Multiple Gates | one Gate ADMIT ≠ all barriers removed; no hidden most-restrictive precedence |
| Gate/Safeguard | Gate HOLD ≠ Safeguard protection; Safeguard release ≠ Gate ADMIT |
| Control effects | control action/enforcement ≠ broader causal attribution |
| History | actual retained historical state ≠ as-known-at-cut reconstruction ≠ current retrospective interpretation |
| Disclosure | current authorization is independent of historical authorization; restricted ≠ absent |
| Scores | no universal topology/completeness/risk/RCA/Impact/control/replay score |

## Phase 007 reasoning chains retained

**Lineage:** bounded relationship proposition → evidence resolution → question-bound relevance → bounded/historical topology.

**Change:** exact intent revision/component → Deployment association → attempt/outcome → activation → realized Change → derived intent-to-realization comparison.

**Prospective review:** proposal + knowledge cut → effective topology + planned delta → candidate/relevance → scoped health/reference/reconciliation/readiness/control review → limitations.

**Execution:** opportunity/expected context → actual execution identity → lifecycle/attempt assembly → actual sequence/waiting → run-specific implementation/input/output binding → historical reconstruction.

**Investigation:** bounded question/scope/cut → evidence-backed leads → localization → evidence-bearing narrowing → explicit Causal Claim handoff → independent causal evaluation → closure/reopen.

**Impact:** originating state + consumer/use → encounter opportunity/availability/publication → actual encounter/exposure → effect → consequence → optional causal attribution.

**Safeguard:** protected state/surface → proposal/authorization/request → effective enforcement → path-specific protection → REF-028 prevented-exposure determination → release → independent recovery evidence.

**Gate:** Gate/profile/opportunity → suitable evidence → readiness → decision basis → issuance/delivery/acceptance → enforcement → actual execution/non-execution → independently evidenced effects.

**Historical replay:** event/effective question + knowledge cut → source-owned facts available by that cut → valid derived reasoning at cut → separately labeled current retrospective reevaluation → current authorized projection.

No arrow in any chain automatically creates the next proposition.

## Scope isolation

CKR-F did not migrate EXPL-001–EXPL-160, INTG-001–INTG-270 or ARCH-001–ARCH-500. Phase 008–010 retain those authorities until CKR-G–I.

## Architecture / semantic-change disposition

No A4 semantic change was required. CKR-F is an authority/routing migration over accepted Phase 007 meaning. Graph storage, event persistence, source mapping, control implementation, agentic RCA, scoring, polling/streaming and concrete SLAs remain later integration/architecture concerns.
