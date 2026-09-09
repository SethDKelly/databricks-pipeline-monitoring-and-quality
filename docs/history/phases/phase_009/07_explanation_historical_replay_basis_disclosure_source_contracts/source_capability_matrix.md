# Group 07 Source Capability Matrix

Support is **proposition + source set + temporal perspective + requester context** bound. `Conditional` means required retention, stable identity, availability timing, exact retained content or current authorization must be established.

| Proposition / capability | Primary evaluated surfaces | Group 07 result | Key boundary / residual gap |
|---|---|---|---|
| Internal statement→basis traceability | Groups 02–06 source identities + accepted proposition records | Supported by contract / implementation required | Requires durable source IDs/provenance; presentation text is insufficient |
| Stable basis identity | Source event/object IDs, revision/version context, Entity Identity joins | Conditional / strong where IDs exist | Rename/recreate/mutable source objects require reconciliation |
| Statement-relative supporting/contradicting/limiting roles | Accepted Explanation composition + source states | Supported by contract | Role is statement-relative, not source-global |
| Event/effective-time binding | Source event/effective timestamps | Partially supported | Semantics differ by source; some sources expose only action/change time |
| Source-recorded/availability-time binding | Source ingestion/received/change/system availability metadata | Conditional | Many sources do not expose exact first-available time |
| As-known-at-cut reconstruction | historical source facts + availability-by-K evidence | Conditional | Event time alone is insufficient |
| Late-evidence separation | source received/change/export timing | Conditional | Requires retained availability/correction timing |
| Current retrospective re-evaluation | retained current/historical source facts | Supported where history survives | Must stay distinct from incident-time knowledge |
| Source correction/supersession replay | SCD/history/audit/revision sources | Conditional | Destructive mutation/history-disable can erase detail |
| Historical source-state replay | per-source historical surfaces | Partially supported | Retention ranges differ materially |
| Exact retained prior communication | retained Explanation/snapshot/comment/message content | Environment-specific / Conditional | Not supplied by telemetry reconstruction alone |
| Reconstructed historical Explanation | source history + accepted semantics | Conditional | Reconstruction ≠ actual communication |
| Communication audience/context/time | retained communication metadata | Environment-specific / Conditional | Source fact history often lacks communication context |
| Notification delivery | Databricks alert history, dashboard snapshot/audit, external channel receipts | Conditional / supported for qualifying delivery event | Delivery ≠ exact rendered content/read/reliance |
| Exact notification content | communication archive/snapshot | Unknown/environment-specific | Databricks alert delivery state alone insufficient |
| GitHub issue/comment current body | GitHub issue/comment API/UI | Supported current state | Current body ≠ arbitrary historical revision |
| GitHub comment edit history | GitHub UI edit history | Partially supported | 100-edit cap; revision content can be deleted |
| GitHub deleted/removed historical comment content | surviving edit/history/audit/export | Conditional / often unsupported natively | Deleted revision payload can be unavailable |
| Databricks audit replay | `system.access.audit` | Supported within scope/retention | ~365-day free retention; action log ≠ all target-state detail |
| Databricks query history replay | `system.query.history` | Supported within scope/retention | Public Preview; ~365 days; regional/compute coverage |
| Databricks exact SQL statement basis | query history `statement_text` | Conditional | CMK can blank text; long text can be truncated |
| Databricks query parameter basis | query history `query_parameters` | Conditional | Truncation/sensitivity possible |
| Databricks alert definition-at-time | `system.alert.alerts` SCD2 | Supported within retention | Public Preview; ~365-day horizon |
| Databricks alert evaluation | `system.alert.alert_evaluation_history` | Supported within retention | Evaluation record ≠ exact Explanation communication |
| Databricks notification delivery status | alert evaluation history | Supported for source-owned delivery status | Does not prove human receipt/read or rendered body |
| Databricks long-horizon generic system replay | native system tables | Partially supported | Retention varies; no uniform indefinite ledger |
| Databricks current admin/system-table access | system catalog permissions | Supported when authorized | Internal access ≠ requester basis disclosure |
| GitHub enterprise audit replay | enterprise/org audit | Partially supported | ~180-day ordinary events; Git events ~7 days unless retained externally |
| GitHub audit external long retention | audit streaming/export destination | Conditional | Requires configured external retention/integrity; at-least-once duplicates |
| GitHub PR/review/issue communication context | GitHub repository records | Conditional / strong current/surviving history | Mutable/deletable content and repository permissions apply |
| Collibra asset/resource history | resource History | Supported for logged facets | History is not every possible facet/change |
| Collibra actor/time change provenance | resource History | Supported where logged | Some edits represented delete+create |
| Collibra inherited-responsibility history | resource History | Partially supported / gap | Current docs state inherited responsibility changes are not shown |
| Collibra selected-attribute history | operating-model history setting | Conditional | History logging can be disabled per attribute assignment |
| Collibra current basis visibility | resource/view permissions | Conditional | Hidden resource ≠ absent resource |
| Immuta application/policy audit | UAM/application audit | Supported within configured scope | Default SaaS retention ~90 days |
| Immuta query audit | Databricks/UC integration audit | Conditional / strong | Coverage depends on integration/version/config; sensitive content |
| Immuta long-horizon audit | UAM export | Conditional | Requires export destination, completeness and retention verification |
| Current requester historical-basis authorization | current UC/Collibra/Immuta/GitHub/IAM policy composition | Environment-specific / Conditional | Historical access does not grant current disclosure |
| Historical actor authorization | retained historical grants/policy/IAM evidence | Partially supported | Retention gaps can make exact historical permission unresolved |
| Result vs basis visibility separation | AUTH/EXPL + source permissions | Supported by contract | Requires architecture to enforce independently |
| Coarse/redacted/opaque basis projection | source metadata + disclosure rules | Conditional | Must remain epistemically monotone |
| Basis-existence disclosure | authorization/policy source | Environment-specific | Existence/count/type can themselves be sensitive |
| Query text/parameter/error disclosure | Databricks/Immuta audit/query sources | Environment-specific / sensitive | Admin retrievability does not authorize display |
| Actor/consumer identity disclosure | audit/query/lineage/dashboard/source identities | Environment-specific / sensitive | Redaction cannot merge materially distinct subjects |
| Observer-relative negative evidence | filtered metadata/history surfaces | Generally unsupported without coverage proof | Non-return can reflect permission/region/workspace scope |
| Partial Explanation | source-by-source answerability | Supported | No global completeness score |
| Explanation under source outage/lag | integration health + surviving basis | Supported as partial/limited | Outage ≠ proposition-level negative |
| Statement identity across refresh | retained proposition identity | Supported by contract | Changed scope/time is new proposition/comparison |
| Basis-only refresh | new/removed basis with unchanged source status | Supported | New basis ≠ stronger confidence automatically |
| Authorization-only projection change | current policy/permission change | Supported | Visibility change ≠ truth change |
| Retained-vs-reconstructed delta | retained communication + reconstruction | Conditional | Requires authentic retained artifact on retained side |
| Comparative historical sides | independently evaluated source sets/cuts | Conditional | Different retention/detail ≠ truth difference |
| Exact prior `inspectBasis` view | retained prior communication + prior projection metadata | Environment-specific / often unsupported | Current source access cannot reconstruct what prior UI exposed |
| Current `inspectBasis` for historical statement | stable internal basis + current authorization | Conditional | Source may have expired even if reference survives |

## Consolidated Group 07 gaps carried forward

1. **Exact retained communication is not provided by source telemetry reconstruction.** Phase 010 needs an explicit retention strategy where actual prior wording/context matters.
2. **Availability-by-knowledge-cut is not uniformly exposed.** Event timestamps alone cannot support exact as-known replay for all sources.
3. **Vendor-native retention is heterogeneous and often short.** Databricks/GitHub/Immuta/Collibra histories cannot be treated as one indefinite ledger.
4. **Databricks query basis can be incomplete.** CMK configuration and truncation can remove exact statement/error/parameter detail.
5. **Delivery evidence is weaker than retained communication content.** Alert/snapshot delivery status cannot prove exact wording or reading.
6. **GitHub discussion history is mutable.** Edit caps and revision deletion prevent treating comments/issues as immutable communication storage by default.
7. **Collibra history is facet/configuration specific.** Inherited-responsibility gaps and optional attribute-history disabling limit full replay.
8. **Immuta long-horizon basis inspection requires export or external retention.** Native SaaS audit defaults are short relative to enterprise replay goals.
9. **Historical authorization replay remains partial.** Current permissions can govern present disclosure, but source-native histories may not reconstruct exact prior permissions indefinitely.
10. **Current requester disclosure must be independently evaluated.** Historical source access/communication does not grant current basis visibility.
11. **Sensitive basis metadata extends beyond raw values.** Existence, count, source type, actors, timestamps, query text, parameters and redaction markers can require minimization.
12. **Exact prior `inspectBasis` presentation is generally unavailable unless separately retained.** Current basis/reconstruction cannot prove the earlier visible projection.
13. **Observer-relative sources remain unsafe for strong negatives.** Missing visible history/basis can reflect filtering or scope.
14. **Comparative Explanation can be asymmetric due to retention rather than truth.** Group 08 must preserve basis/availability deltas explicitly.
