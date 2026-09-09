# Phase 010 Group 09 — Failure / Degradation Matrix

**Status:** PASS — consolidated failure behavior

| Failure / degradation | What may degrade | What must remain true | Prohibited shortcut |
|---|---|---|---|
| Databricks source API outage | Fresh acquisition for dependent propositions | Prior retained evidence remains historically valid; current coverage/availability becomes degraded | Treat outage as `no run/no change/no issue` |
| Databricks system-table publication delay | SC-01/02 freshness for those surfaces | Source publication lag is explicit and service-class specific | Backdate knowledge or emit strong current negatives |
| GitHub API throttle/secondary limit | GitHub freshness/coverage | Rate state and affected windows are observable; reconciliation resumes later | Treat missing pages as no CI/deployment/change |
| Source permission revoked | Dependent source coverage | Authz/reachability failure remains distinct from domain absence | Convert 403/observer-relative 404 into negative fact |
| Pagination/partition incomplete | Population completeness | Partial usable evidence may publish with coverage limitation | Advance to complete/negative result |
| Schema/API breaking drift | Affected normalization path | Raw/quarantined evidence and parser failure remain visible; other sources continue | Silently drop unsupported fields/records |
| Parser/normalizer defect | Affected normalized evidence | Parser revision/provenance supports repair/reparse; prior state not invisibly overwritten | Rewrite history without correction provenance |
| Canonical persistence unavailable | New evidence publication and canonical commands | Checkpoints cannot outrun durable persistence; prior canonical history remains source of truth | Acknowledge source progress then lose evidence |
| Derived graph projection lost | Graph traversal convenience | Exact canonical retrieval/rebuild remains possible | Treat graph loss as source-history loss |
| Search/vector index unavailable | Semantic candidate recall | Exact retrieval/deterministic reasoning still works | Make truthful basic answers unavailable solely because vector service failed |
| LLM/model unavailable | Natural-language convenience/rendering | Deterministic renderer and accepted proposition state remain available | Degrade domain truth or control readiness |
| LLM returns unsupported/strengthened prose | Model rendering | Output validation rejects/regenerates/falls back; Statement IR remains unchanged | Publish stronger/wider statement |
| Serving cache stale | Interactive latency/freshness | Watermark/applicability rules detect stale cache | Cache hit becomes evidence freshness |
| Serving cache authorization mismatch | Cache reuse | Context-keying/re-evaluation prevents cross-requester/purpose/detail leakage | Post-hoc UI hiding of privileged cached result |
| API façade unavailable | Interactive access | Canonical acquisition/history can continue where independently deployed | Infer monitored pipeline outage from UI outage |
| Authentication provider unavailable | Human/app login | Security degradation is explicit; background authorized workloads may follow their own policy | Fail open to anonymous access |
| Authorization/policy evaluator unavailable | Protected read/export/control operations | Service-specific degraded policy is explicit; no implicit permissive fallback | Authentication alone grants access/control |
| Secret/federation failure | Affected workload/source integration | Credential failure is observable and source coverage degrades explicitly | Treat inaccessible source as empty |
| Callback signature/authenticity failure | Webhook/attestation/control callback | Callback rejected/quarantined; no canonical semantic event created | Trust body because source IP/name looks plausible |
| Duplicate/replayed callback | Transport attempt count | Idempotency/opportunity identity prevents duplicate semantic action | Create second decision/enforcement/communication |
| Reasoning worker saturated | Investigation/replay latency | Supported narrow source facts/serving siblings can remain available | Invent global `analysis incomplete = unhealthy` score |
| Historical archive cold/unavailable | SC-04/05 replay retrieval | Current state remains separate; restore state/limitations are explicit | Fill old answer using current source/config/policy |
| Archive payload expired | Exact historical basis | Provenance stub may show existence/expiry only | Recreate exact historical payload from metadata |
| Backup restore partially succeeds | Recovered history | Missing intervals/objects and restore provenance remain explicit | Mark history complete because service recovered |
| Control service unavailable | SC-06 decision/enforcement | Passive monitoring/reasoning remains independent; degraded control profile governs behavior | Hidden fail-open/fail-closed |
| Gate decision arrives after applicability horizon | Control opportunity | Stale decision rejected/re-evaluated according to policy | Reuse old ADMIT/HOLD for convenience |
| Gate delivery succeeds but enforcement adapter fails | Control delivery | Decision/delivery/enforcement remain separate; actual execution reconciled | Mark execution blocked from HTTP success |
| Databricks cancellation after run starts | Execution interruption | It remains asynchronous interruption, not pre-start HOLD | Reclassify as successful Gate prevention |
| Safeguard protects one path but alternate path fails open | Partial protection | Protection remains path/cohort-specific; global prevention withheld | One blocked route = globally prevented |
| Safeguard release requested but adapter does not release | Release lifecycle | Request != effective release; recovery independent | Mark recovered/released from configuration change |
| Cost budget threshold reached | Optional enrichment/retention tier/scheduling | Required evidence/control/retention promises remain hard constraints | Shrink Monitoring Scope or skip required reconciliation silently |
| Compute capacity exhausted | Latency/throughput | Priority/backpressure preserves high-consequence/required work per policy and exposes degradation | Drop required evidence without coverage record |
| Collibra unavailable/not licensed | Collibra-dependent governance facets | Other sources and DMTZ organization-owned policy remain; exact dependent propositions partial/unknown | Assume benign classification/ownership |
| Immuta unavailable/not licensed | Immuta-dependent policy/enforcement evidence | Exact dependent policy/control propositions degrade | Assume allowed/denied by default |
| External BI telemetry absent | Exact display/use/exposure claims | Reachability remains candidate only; unsupported Impact siblings explicit | Convert no telemetry into not exposed |
| Business consequence source absent | Business/customer/financial consequence claims | Technical effect can remain supported independently | Treat no consequence evidence as no consequence |
| Current policy changes after incident | Current projection/historical evaluation | Historical actual decisions/as-known state remain non-rewriting | Backfill current rule into past |
| Current group membership changes | Current authorization | Historical membership/authorization uses historical evidence where available | Project current membership backward |
| Canonical schema migration fails mid-rollout | Write/read compatibility | Versioned migration/compatibility and rollback preserve semantic history | Partially reinterpret old rows under new schema silently |
| Application deployment rollback | Serving/runtime code | Canonical evidence/history remains non-rewriting; old/new code revision is observable | Roll back canonical history with application binary |
| Region failure under residency policy | Regional serving/acquisition | Failover only to permitted region/data copy; explicit capability/coverage loss otherwise | Copy sensitive evidence across forbidden boundary |

## Global degradation invariant

A degraded subsystem may reduce **availability, freshness, coverage, convenience, latency or supported proposition set**. It may not silently create stronger positive/negative truth, new authority, historical knowledge, causal confirmation, exposure/consequence, disclosure permission or active-control success.
