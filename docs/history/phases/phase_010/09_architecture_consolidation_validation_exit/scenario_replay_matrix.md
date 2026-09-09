# Phase 010 Group 09 — Whole-Architecture Scenario Replay Matrix

**Status:** PASS — **ACV09-01–ACV09-120**

These are architecture/design validations, not executable runtime tests. Later implementation should convert applicable cases into contract/integration/end-to-end tests.

## A. Environment, capability and integration facts — ACV09-01–12

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-01 | Public docs describe a feature but target workspace has it disabled | Capability remains unavailable/unknown for that deployment | PASS |
| ACV09-02 | Feature exists in one region but not another | Capability instances remain region-specific | PASS |
| ACV09-03 | System table is present but requester lacks SELECT | Permission failure is integration state, not domain absence | PASS |
| ACV09-04 | Billing data arrives hours after workload activity | Billing/cost SLO differs from near-current operational fact SLO | PASS |
| ACV09-05 | Databricks API throttles during reconciliation | Coverage/freshness degrades; no negative fact is fabricated | PASS |
| ACV09-06 | GitHub secondary rate limit interrupts page retrieval | Partial page/window remains incomplete and checkpoint safe | PASS |
| ACV09-07 | Webhook arrives before reconciliation sees same source event | Records are common-derived/deduplicated, not corroborating sources | PASS |
| ACV09-08 | Source API adds an unknown field | Additive schema evolution tolerated with parser revision provenance | PASS |
| ACV09-09 | Source changes a required field incompatibly | Affected records quarantine/degrade; omission cannot become negative evidence | PASS |
| ACV09-10 | Optional Collibra integration is absent | Only Collibra-dependent capabilities degrade | PASS |
| ACV09-11 | Immuta is licensed but API/export capability unverified | Exact Immuta-dependent feature remains disabled/unknown | PASS |
| ACV09-12 | Capability inventory is stale after tenant change | Dependent feature requires re-verification/revision; old capability not assumed current | PASS |

## B. Identity, scope, authority, authorization and disclosure — ACV09-13–24

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-13 | Two source objects share the same name | No identity merge without source binding evidence | PASS |
| ACV09-14 | Asset is renamed | Identity continuity requires evidence; alias/path history retained | PASS |
| ACV09-15 | Asset is deleted and recreated with same name | New incarnation remains distinct unless identity evidence establishes continuity | PASS |
| ACV09-16 | Connector can see only half of governed Monitoring Scope | Expected population stays larger; missing half is unresolved coverage | PASS |
| ACV09-17 | Vendor owner field names a person | Responsibility evidence does not automatically grant Assertion Authority | PASS |
| ACV09-18 | Two eligible authority sources conflict | Conflict retained until explicit resolution rule/authority applies | PASS |
| ACV09-19 | Service principal can read sensitive canonical evidence | End requester does not inherit service permission | PASS |
| ACV09-20 | User may see conclusion but not exact basis | Statement visible; basis projected opaque/redacted/withheld itemwise | PASS |
| ACV09-21 | Basis count itself reveals a hidden source | Disclosure policy can hide count/type/existence metadata | PASS |
| ACV09-22 | User membership changes after historical incident | Current membership not projected backward into historical authorization | PASS |
| ACV09-23 | Authorization changes while a privileged response is cached | Cache context/revision/horizon prevents unsafe reuse | PASS |
| ACV09-24 | Control authorization revoked after Gate decision but before delayed action | Revalidation occurs when policy/horizon requires it | PASS |

## C. Canonical persistence, time and retention — ACV09-25–36

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-25 | Source event timestamp precedes evidence arrival by hours | Event time and availability-by-K remain distinct | PASS |
| ACV09-26 | Late evidence would have changed incident conclusion | Earlier as-known replay excludes it; current retrospective may include it | PASS |
| ACV09-27 | Source correction supersedes prior record | Canonical history appends correction/supersession without erasing prior knowledge | PASS |
| ACV09-28 | Delta compaction rewrites physical files | Semantic history/evidence identity remains unchanged | PASS |
| ACV09-29 | Delta time travel cannot reach product retention horizon | Product replay uses retained canonical journals/archive, not table-history promise | PASS |
| ACV09-30 | Exact basis is pinned by audit promise | Lifecycle optimization cannot downsample/delete it during promised horizon | PASS |
| ACV09-31 | Old low-value payload expires but provenance stub survives | Stub proves limited provenance/existence, not exact payload content | PASS |
| ACV09-32 | Cold archive restore is partial | Missing objects/intervals remain explicit after recovery | PASS |
| ACV09-33 | Backup restore occurs after an earlier outage | Recovery does not rewrite historical unavailability/knowledge gaps | PASS |
| ACV09-34 | Archived record is requested by unauthorized user | Archive state does not broaden disclosure permission | PASS |
| ACV09-35 | Current policy differs from historical policy | Replay uses applicable historical policy/state; current policy governs current projection only | PASS |
| ACV09-36 | Application deployment rolls back | Runtime binary/config can roll back; canonical semantic history does not | PASS |

## D. Runtime provenance, health and data quality — ACV09-37–48

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-37 | GitHub workflow succeeds but Databricks run cannot be correlated | No claim that workflow deployed/triggered exact run | PASS |
| ACV09-38 | Branch points to new commit after run | Run revision cannot be inferred from current branch | PASS |
| ACV09-39 | Bundle deployment lacks exact commit attestation | Code facet remains partial/unknown | PASS |
| ACV09-40 | Current job config differs from historical run config | Current config not backfilled into run manifest | PASS |
| ACV09-41 | Multi-input job exposes one exact input version and one unknown | Manifest remains partially exact with sibling unknown | PASS |
| ACV09-42 | Run succeeds but expected output is absent | Run status and output existence remain separate propositions | PASS |
| ACV09-43 | Output exists but freshness expectation fails | Output existence does not create healthy/current state | PASS |
| ACV09-44 | Row count is atypical but within explicit Expectation | Baseline atypicality and normative health remain distinct | PASS |
| ACV09-45 | Metric is within historical Baseline but violates new Expectation | Normative violation remains possible despite typicality | PASS |
| ACV09-46 | Reconciliation mismatch localizes boundary | Mismatch evidence does not become cause automatically | PASS |
| ACV09-47 | Source health is degraded during a `no output` query | Strong negative is suppressed/narrowed due to coverage limitation | PASS |
| ACV09-48 | Platform serving SLO is breached while monitored data is healthy | DMTZ operational health remains separate from domain health | PASS |

## E. Lineage, encounter, exposure and consequence — ACV09-49–60

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-49 | Native Lineage omits a known dependency due to capture limitation | Missing edge under incomplete coverage is not `no dependency` | PASS |
| ACV09-50 | Graph shows downstream reachability | Reachability creates candidate only, not exposure/effect | PASS |
| ACV09-51 | Consumer query runs but human never views result | Query encounter does not become human view/reliance | PASS |
| ACV09-52 | Dashboard serves cached safe prior state while upstream current state is defective | Consumer can be not exposed to affected version while freshness/currentness is stale | PASS |
| ACV09-53 | Consumer reads exact affected version | Exposure can be supported without automatically asserting downstream effect | PASS |
| ACV09-54 | Technical effect observed but no business source exists | Technical effect supported; business consequence unknown/unavailable | PASS |
| ACV09-55 | One branch of a multi-hop path is safe | Global non-exposure withheld until alternate material paths are covered | PASS |
| ACV09-56 | Two-hop Lineage path exists with no encounter evidence at hop 2 | Exposure does not propagate transitively | PASS |
| ACV09-57 | Vendor tool labels asset `impacted` | Vendor assessment retained at bounded semantics; DMTZ realized Impact not manufactured | PASS |
| ACV09-58 | Critical asset has no observed exposure | Criticality does not manufacture realized consequence | PASS |
| ACV09-59 | No external BI telemetry is installed | DMTZ reports consumer-use capability limitation, not `not viewed` | PASS |
| ACV09-60 | Incident source records financial loss after exposure | Consequence can be evidenced while causal attribution remains separate | PASS |

## F. Investigation, causality and reasoning — ACV09-61–72

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-61 | Alert opens an Investigation | Alert references canonical Investigation; it is not the Investigation identity itself | PASS |
| ACV09-62 | Analyst suggests a cause | Suggestion becomes a lead/Causal Claim candidate with provenance, not confirmed truth | PASS |
| ACV09-63 | Model suggests a different cause | Model origin carries no additional authority | PASS |
| ACV09-64 | Graph centrality ranks one upstream node highly | Centrality may guide inquiry but not causal status | PASS |
| ACV09-65 | Deployment immediately precedes degradation | Temporal proximity supports chronology/lead, not confirmation | PASS |
| ACV09-66 | Cause has no supporting evidence yet | Status remains proposed/unresolved; lack of support is not rejection | PASS |
| ACV09-67 | Strong contradiction/exclusion evidence exists | Causal Claim may be rejected under accepted rule | PASS |
| ACV09-68 | Evidence sufficiency is strong but no eligible confirming authority exists | `confirmed` remains unavailable despite evidence strength | PASS |
| ACV09-69 | Eligible authority exists but REF-017 sufficiency is unmet | Authority cannot confirm unsupported claim | PASS |
| ACV09-70 | Investigation closes operationally with two unresolved contributors | Closure does not force a single root cause | PASS |
| ACV09-71 | Late evidence weakens the leading cause | Current Causal Claim state changes without rewriting earlier investigation knowledge | PASS |
| ACV09-72 | Vector index is unavailable | Exact retrieval/deterministic reasoning still provide truthful bounded answers | PASS |

## G. Explanation, historical replay and basis — ACV09-73–84

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-73 | Compound business question spans health, cause and Impact | Decompose into bounded sibling propositions before composition | PASS |
| ACV09-74 | One sibling is supported and another unavailable | Return supported partial answer plus explicit unavailable sibling | PASS |
| ACV09-75 | Summary renderer tries to omit a material limitation | Output validation rejects/rewrites/falls back | PASS |
| ACV09-76 | Model strengthens `supported` to `confirmed` | Render rejected because status is not epistemically equivalent | PASS |
| ACV09-77 | Basis has three common-derived copies of one source event | Copies do not count as independent corroboration | PASS |
| ACV09-78 | User can see redacted basis but not exact query text | Internal statement→basis link remains complete; visible detail is safely projected | PASS |
| ACV09-79 | User asks what was known at K before late evidence arrived | Replay excludes late evidence despite earlier event timestamp | PASS |
| ACV09-80 | Current source truth corrected an old erroneous record | Current retrospective may differ; prior as-known remains reconstructable | PASS |
| ACV09-81 | No authentic prior Explanation snapshot was retained | System may reconstruct but cannot claim exact prior communication | PASS |
| ACV09-82 | Authentic snapshot exists but current requester cannot see some old basis | Prior communication record and current projection remain separate; current disclosure controls current view | PASS |
| ACV09-83 | Prior `inspectBasis` projection was never retained | Current wider permission cannot recreate exactly what prior viewer saw | PASS |
| ACV09-84 | LLM service is down | Deterministic renderer returns semantically faithful answer | PASS |

## H. Serving, cache and security — ACV09-85–96

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-85 | UI attempts direct canonical mutation | Rejected; canonical writes use governed command/persistence path | PASS |
| ACV09-86 | UI directly queries account-wide sensitive system table | Reference architecture rejects unrestricted raw access; serving projection is required | PASS |
| ACV09-87 | Same query issued by two users with different basis permissions | Cache/projection contexts do not cross-leak detail | PASS |
| ACV09-88 | Page limit returns first 100 of 1000 expected entities | Page result cannot be labeled complete population coverage | PASS |
| ACV09-89 | Cached result watermark is outside SC-01 freshness requirement | Cache is rejected/refreshed or returned explicitly stale where allowed | PASS |
| ACV09-90 | Search index contains a restricted entity | Pre-retrieval corpus/authorization design prevents unauthorized existence/count leakage | PASS |
| ACV09-91 | Log line would contain a secret/token | Telemetry minimization prevents secret-value retention | PASS |
| ACV09-92 | Model grounding packet would include irrelevant sensitive evidence | Minimize/authorize before provider/tool exposure | PASS |
| ACV09-93 | Spoofed webhook resembles a valid source payload | Authenticity failure prevents canonical publication | PASS |
| ACV09-94 | Replayed valid control callback arrives twice | Idempotency/replay protection prevents second semantic action | PASS |
| ACV09-95 | Human login succeeds but Capability Authorization is unknown | Protected result/action remains conditional/unavailable, not implicitly allowed | PASS |
| ACV09-96 | Region policy prohibits cross-region evidence movement | Serving/backup/index topology respects residency even if centralization is cheaper | PASS |

## I. Gate, Safeguard and active control — ACV09-97–108

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-97 | Gate configuration exists but no execution opportunity occurs | No opportunity-specific decision/enforcement claim | PASS |
| ACV09-98 | Evidence is unsuitable but service is healthy | Readiness cannot be manufactured by infrastructure availability | PASS |
| ACV09-99 | Gate decides HOLD but decision never reaches enforcement point | HOLD decision is not effective enforcement | PASS |
| ACV09-100 | HOLD is enforced and no run occurs, but alternate trigger path is unobserved | Broad prevention/non-execution claim remains bounded | PASS |
| ACV09-101 | Gate ADMIT issued but downstream launch fails independently | ADMIT is not actual execution | PASS |
| ACV09-102 | Override admits execution despite unmet readiness | Underlying readiness remains unmet; override evidence/authority retained | PASS |
| ACV09-103 | Timeout occurs with no configured fallback action | Timeout does not invent ADMIT/HOLD/fallback | PASS |
| ACV09-104 | Gate decision exceeds applicability horizon | Stale decision rejected/re-evaluated | PASS |
| ACV09-105 | GitHub environment protection holds its job | Strong evidence only for exact protected GitHub opportunity; Databricks gating still requires correlation | PASS |
| ACV09-106 | Safeguard blocks one publication path but second path serves affected version | Protection remains partial; no global prevention | PASS |
| ACV09-107 | Safeguard is effective but no consumer exposure opportunity occurs | No REF-028 prevention credit without opportunity | PASS |
| ACV09-108 | Safeguard release succeeds while data remains stale/unhealthy | Effective release remains distinct from recovery/health | PASS |

## J. Operations, cost, capacity, DR and architecture freeze — ACV09-109–120

| ID | Scenario | Required architectural result | Result |
|---|---|---|---|
| ACV09-109 | Large replay workload saturates compute | Backpressure/priority may slow replay while preserving canonical truth and required work | PASS |
| ACV09-110 | LLM spending exceeds budget | Optional model work can be disabled/deferred without changing answers’ source-owned status | PASS |
| ACV09-111 | Storage budget pressure targets old evidence | Lifecycle policy may archive/expire eligible material but cannot delete pinned promised basis silently | PASS |
| ACV09-112 | Reconciliation is expensive | Cost policy may reschedule only within accepted service/coverage promise; cannot silently remove required coverage | PASS |
| ACV09-113 | SC-06 control and model workloads compete for resources | Control path receives required isolation/priority; model degrades first where policy dictates | PASS |
| ACV09-114 | Backup is green but restore test fails | DR readiness remains degraded; backup success alone is insufficient | PASS |
| ACV09-115 | Restored archive lacks an evidence payload | Replay exposes missing payload and does not reconstruct exact basis from stub | PASS |
| ACV09-116 | Enterprise requests a graph DB before benchmarks | Architecture retains Delta graph until measured need justifies extension | PASS |
| ACV09-117 | Team selects framework whose data model collapses unknown/false | Framework/configuration is rejected or adapted; semantic contract wins | PASS |
| ACV09-118 | Implementation discovers target source cannot support promised exact proposition | Product capability is narrowed or instrumentation added; source gap is not filled by inference | PASS |
| ACV09-119 | Group 09 replay finds no new semantic/architecture proposition | ARCH-001–500 freezes; no ARCH-501 created for ceremony | PASS |
| ACV09-120 | Later implementation needs to pick hosting/queue/cache/observability products | Product-selection ADR may proceed within frozen ownership/security/evidence boundaries | PASS |

## Replay conclusion

**ACV09-01–ACV09-120 PASS.**

No replay case requires a new concept, a new functional contract or ARCH-501. The remaining work after Phase 010 is implementation and measurable deployment validation.
