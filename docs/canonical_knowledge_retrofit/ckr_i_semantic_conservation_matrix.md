# CKR-I Semantic Conservation Matrix — Technical Architecture

**Status:** CANDIDATE REVIEW

CKR-I changes documentation ownership, not accepted Phase 010 architecture semantics. The following boundaries are mandatory across all eight ARCH segments and the frozen reference architecture.

| Boundary | Canonical conservation rule |
|---|---|
| Vendor documentation vs deployment fact | documented capability ≠ deployment presence ≠ entitlement ≠ enablement ≠ permission ≠ reachability ≠ observable coverage ≠ proposition-specific usability |
| Architecture optimization | hard semantic/evidence/security/history constraints precede cost/performance/convenience optimization |
| Architecture scoring | no universal architecture score; decision-specific quality attributes remain explicit |
| Evidence ownership | framework retention authority ≠ source Assertion Authority |
| Copying | copied evidence ≠ newly authoritative evidence ≠ independent corroboration |
| Temporal state | event/effective time ≠ source-recorded time ≠ availability time ≠ collection/persistence time ≠ correction/supersession time |
| Historical replay | current state/config/policy ≠ historical state; Delta transaction-log time travel ≠ DMTZ historical replay contract |
| Expired detail | provenance stub ≠ recovered payload |
| Identity | source-local identifier/name ≠ ecosystem Entity Identity |
| Principal | authentication ≠ Capability Authorization ≠ Assertion Authority |
| Monitoring Scope | Monitoring Scope ≠ technical accessibility ≠ authorization ≠ successful observation |
| Authority | source prominence/recency/count/vendor role ≠ Assertion Authority |
| Authorization | authorization decision ≠ issuance ≠ enforcement ≠ action ≠ outcome |
| Disclosure | conclusion visibility ≠ basis/detail visibility; safe abstraction cannot strengthen truth |
| Acquisition | source acquisition transports evidence; integration success/failure ≠ monitored-domain truth |
| Checkpoints | checkpoint advancement follows durable evidence/provenance publication |
| Collection | empty result ≠ absence; partial pagination/window/partition ≠ complete coverage |
| Integration health | integration health ≠ monitored-domain health; no universal integration-health score |
| Cross-system joins | name equality/timestamp proximity ≠ exact identity/deployment/run/input/output join |
| Runtime | GitHub Actions success ≠ Databricks activation; deployment ≠ activation ≠ run |
| Implementation provenance | direct-Git evidence ≠ generic bundle/workspace-source exact revision unless separately attested |
| Input/output version | dependency/Lineage/write history ≠ exact consumed/produced version |
| Health | execution success ≠ output existence ≠ freshness/currentness ≠ health |
| Health concepts | Baseline ≠ Expectation ≠ Observation ≠ Assessment |
| Lineage | Lineage/reachability ≠ encounter/consumption ≠ exposure |
| Impact | exposure ≠ effect ≠ consequence ≠ causal attribution |
| Strong negatives | no run/output/dependency/exposure/effect/consequence requires bounded opportunity + sufficient coverage + known source health |
| Investigation | Investigation lead/localization ≠ Causal Claim |
| Causal confirmation | `confirmed` requires REF-017 evidence + AUTH-034 eligible authority |
| Graph/search/vector | graph/search/vector projection ≠ source truth/authority/completeness/causality |
| Model assistance | LLM/model output/confidence/agreement ≠ evidence strength, authority or independent corroboration |
| Reasoning | free-form prose ≠ semantic join; deterministic proposition/rule evaluation precedes rendering |
| Statement rendering | Statement IR/basis/limitations precede rendering; wording changes cannot strengthen state |
| Historical views | historical source state ≠ as-known-at-K Explanation ≠ retained actual communication ≠ current retrospective Explanation |
| Retained communication | reconstructed historical Explanation ≠ authentic retained communication |
| Basis inspection | source resolvability ≠ payload retention ≠ authorization to inspect |
| Gate | evidence suitability ≠ readiness ≠ Gate decision ≠ delivery/acceptance ≠ enforcement ≠ execution |
| Gate decision | HOLD ≠ failed run; ADMIT ≠ run; no run ≠ proven HOLD enforcement |
| Override/fallback | override/fallback action ≠ underlying readiness; no hidden universal fail-open/fail-closed |
| Safeguard | proposal/configuration/request ≠ enforcement ≠ prevented exposure ≠ release ≠ recovery |
| Prevention | Safeguard active + not exposed ≠ REF-028 prevention without opportunity/path/alternate-path evidence |
| Gate vs Safeguard | Execution Gate ≠ Propagation Safeguard |
| Active control | active control is optional over passive monitoring/reasoning truth |
| Serving | cache/page/index/derived read model ≠ canonical completeness/freshness/authority |
| UI/session state | UI/session/application store ≠ parallel truth database |
| Operational SLO | SLO breach ≠ monitored-domain health |
| Cost/quota | cost/quota/capacity pressure ≠ permission to weaken scope/evidence/retention/control promises |
| Backup/recovery | current restore/recovery ≠ rewrite of earlier evidence gaps |
| Optional integrations | absent optional integration narrows dependent propositions; it does not fabricate a replacement default |
| Technology choice | implementation technology ADR ≠ semantic/authority change |
| Stable range | ARCH-001–ARCH-500 final; no ARCH-501 |
| Reference topology | reference architecture composes ARCH-001–500; it does not create another truth layer |

## Required architecture shape

The frozen composed chain remains:

**deployment-verified capability + organization policy → reconciliation-first acquisition → Delta-first canonical evidence/identity/governance history → exact runtime/measurement/Lineage/encounter evidence → deterministic evaluation/reasoning/replay → Statement IR / Answer IR → current authorized serving projection → UI/API/retained communication**.

Execution Gate and Propagation Safeguard remain independent opt-in branches over the passive evidence/reasoning system.

## Migration non-goals

CKR-I does not:

- select a programming language or application framework;
- select an API gateway, queue/event bus, orchestrator or container/serverless platform;
- select a secrets manager, external IdP, policy engine or observability vendor;
- select a graph database, vector/search provider, LLM/provider or agent framework;
- invent numeric SLOs, target-environment capability facts or source instrumentation;
- reopen GAP-009 dispositions as semantic questions;
- authorize product implementation before CKR-K;
- start CKR-J.
