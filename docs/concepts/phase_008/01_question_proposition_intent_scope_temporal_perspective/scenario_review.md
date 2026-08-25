# Phase 008 Group 01 Scenario Review

**Status:** Accepted — all scenarios pass

| Scenario | Question / condition | Required resolution | Result |
|---|---|---|---|
| BQ01-01 | `Is C healthy?` with no use/profile/dimension | Preserve underspecification or present bounded health dimensions; no universal asset-health score. | Pass |
| BQ01-02 | `Is C healthy for the finance report?` | Bind consumer/use-specific profile/context before answering. | Pass |
| BQ01-03 | `Why did C volume fall?` | Separate volume Assessment/change/execution evidence from causal Causal Claim. | Pass |
| BQ01-04 | `What changed after deployment R2?` | Bind deployment/event window and distinguish Deployment from realized Change. | Pass |
| BQ01-05 | `What ran last night?` | Resolve event window and Execution History; schedule/expected work does not create runs. | Pass |
| BQ01-06 | `What happened at 10:00?` with no knowledge cut | Treat as current retrospective interpretation of historical event, labeled where material. | Pass |
| BQ01-07 | `What did we know at 10:15 about 10:00?` | Bind event time and knowledge cut independently. | Pass |
| BQ01-08 | current topology differs from incident topology | Historical question uses then-effective/then-known Lineage, not current graph. | Pass |
| BQ01-09 | `Was report R affected?` | Route candidate/encounter/exposure/effect/consequence separately; no reachability shortcut. | Pass |
| BQ01-10 | `Was anyone impacted?` with partial consumer telemetry | Broad negative cannot be asserted without required consumer/path coverage. | Pass |
| BQ01-11 | `Did Safeguard S prevent exposure?` | Route to exact enforcement + opportunity/path/non-exposure REF-028 determination. | Pass |
| BQ01-12 | Safeguard active but consumer had no encounter opportunity | Answer protection state separately; do not award prevention. | Pass |
| BQ01-13 | `Why didn't D run?` | Decompose opportunity/Gate/execution facts from causal explanation. | Pass |
| BQ01-14 | `Did Gate G hold D?` but Gate decision exists and enforcement telemetry missing | HOLD decision answerable; enforcement remains unknown. | Pass |
| BQ01-15 | `Who owns C?` | Route to Responsibility Assignment, not authorization. | Pass |
| BQ01-16 | `Can I rerun C?` | Route to Capability Authorization; responsibility does not imply permission. | Pass |
| BQ01-17 | same display name `orders` in dev and prod | Preserve identity/environment ambiguity; no silent target choice. | Pass |
| BQ01-18 | historical rename produces old/new aliases | Resolve via Entity Identity effective/knowledge context rather than string match. | Pass |
| BQ01-19 | `What failed, why, and who was affected?` | Decompose independent health/execution, causal and Impact subquestions. | Pass |
| BQ01-20 | execution failure known, cause unresolved, exposure known | Return partial compound answer; answered siblings do not strengthen unresolved cause. | Pass |
| BQ01-21 | `Was the change planned?` and no registered intent found | State registration evidence/scope; do not infer humanly unplanned without sufficient proposition evidence. | Pass |
| BQ01-22 | `Which version did R use?` but only latest-upstream state known | Version question remains unknown absent run/encounter binding; latest is not consumed. | Pass |
| BQ01-23 | `Are all downstream consumers safe?` with one safe path and one unresolved alternate | Global safety/non-exposure not established; present path-specific state. | Pass |
| BQ01-24 | internally supported answer relies on evidence requester cannot receive | Separate answerability from authorization; later authorized projection decides allowed disclosure. | Pass |

## Exit

All scenarios are expressible with EXPL-001–EXPL-012 and accepted source-concept semantics. No Question concept or universal answerability/confidence score is required.
