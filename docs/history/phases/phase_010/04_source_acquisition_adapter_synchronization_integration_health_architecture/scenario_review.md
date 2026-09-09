# Phase 010 Group 04 — Acquisition / Integration-Health Scenario Review

**Suite:** AHI04-01–AHI04-96

All scenarios pass against ARCH-133–ARCH-190.

| ID | Scenario | Expected architecture result |
|---|---|---|
| AHI04-01 | Vendor docs describe source but target tenant lacks it | capability unavailable/unverified; plan cannot assume source |
| AHI04-02 | Surface exists but integration principal lacks permission | authz degraded; source/domain state unknown |
| AHI04-03 | Entity is in Monitoring Scope but source cannot currently list it | remains in scope; collection coverage partial/unknown |
| AHI04-04 | Optional Collibra/Immuta integration absent | exact dependent capabilities degrade; no benign defaults |
| AHI04-05 | Complete bounded snapshot returns no matching rows | negative candidate only if prior proposition-specific burden is satisfied |
| AHI04-06 | First page succeeds with zero matches but pagination unresolved | no strong negative; coverage partial/unknown |
| AHI04-07 | Page 2 of 3 fails after page 1 persisted | run partial; page 1 usable; full population not complete |
| AHI04-08 | Continuation token missing in malformed response | ambiguous terminal state; not assumed complete |
| AHI04-09 | Same page fetched twice after retry | idempotent evidence; physical duplicate not second event |
| AHI04-10 | Source rejects old cursor | checkpoint-invalid; reconcile/backfill or explicit gap |
| AHI04-11 | Late record arrives inside overlap window | ingest once with later availability; preserve event time |
| AHI04-12 | Current query is empty but source publication SLA allows lag | current negative unresolved until publication envelope permits |
| AHI04-13 | GitHub webhook delivered twice | same delivery/event deduplicated |
| AHI04-14 | GitHub webhook delivery fails | webhook health degraded; reconciliation required |
| AHI04-15 | No GitHub webhook received | does not prove no event occurred |
| AHI04-16 | GitHub webhook redelivery uses same delivery ID | linked retry, not independent event |
| AHI04-17 | Missed GitHub event older than redelivery window | use REST/audit reconciliation if available; otherwise explicit gap |
| AHI04-18 | GitHub primary rate budget declines | adapt cadence/priorities from headers |
| AHI04-19 | GitHub returns 429 + Retry-After | stop until permitted; record throttled state |
| AHI04-20 | GitHub secondary rate limit occurs without inspectable budget | backoff; quota state constrained/unknown |
| AHI04-21 | Authenticated conditional GET returns 304 | representation unchanged for exact request; preserve bounded meaning |
| AHI04-22 | ETag changes | retrieve new representation; not automatically a domain Change concept |
| AHI04-23 | GitHub App installed but repo excluded from installation | collection unavailable for repo; no absence inference |
| AHI04-24 | GitHub private resource returns 404 due permission | observer-relative; not object absence |
| AHI04-25 | Databricks system table lacks a just-finished event | publication lag possible; do not infer no run/event |
| AHI04-26 | Databricks system-table streaming runtime requirements met | stream may accelerate, reconciliation/lag tracking retained |
| AHI04-27 | Runtime lacks required streaming feature | select verified pull/batch path; capability difference explicit |
| AHI04-28 | Databricks stream falls behind source recoverable horizon | checkpoint/retention gap; backfill/reconcile or unresolved interval |
| AHI04-29 | Databricks system table adds column | raw/additive capture survives; normalized model unchanged until supported |
| AHI04-30 | API removes/renames required field | breaking drift; quarantine/narrow publication, no guessed mapping |
| AHI04-31 | System-table query rejected as insufficiently selective | repartition/query narrower without marking missing interval complete |
| AHI04-32 | Databricks REST returns 429 | rate-limited integration state; backoff per endpoint/scope |
| AHI04-33 | Databricks REST returns 401 | authentication failure; no domain inference |
| AHI04-34 | Databricks REST returns 403 | permission failure; exact principal/action/surface recorded |
| AHI04-35 | Safe Databricks read gets transient 503 | bounded retry; original failure retained |
| AHI04-36 | Source write/mutative operation would be non-idempotent | acquisition architecture does not blindly retry unsafe writes |
| AHI04-37 | Lineage API budget cannot support per-object polling | use quota-aware targeted demand/reconciliation; no evidence-burden reduction |
| AHI04-38 | Databricks system table plus REST expose same source event | common derivation preserved; not two corroborators |
| AHI04-39 | REST recent history shorter than product requirement | acquire/retain while available or preserve explicit later gap |
| AHI04-40 | Public Collibra throttle default differs from tenant | target-environment value wins; public default remains reference fact |
| AHI04-41 | Collibra tenant throttles below expected cadence | quota dimension degraded; adapt plan |
| AHI04-42 | Collibra license/role unavailable | optional capability unavailable; no governance default |
| AHI04-43 | Collibra history exists but principal cannot view it | observer-relative history limitation |
| AHI04-44 | Immuta UC audit sync configured hourly | availability envelope includes sync schedule |
| AHI04-45 | Immuta UC audit sync configured every 24h for SC-01 need | source insufficient for near-current class; slower use may remain supported |
| AHI04-46 | Immuta workspace filter excludes incident workspace | audit coverage explicitly partial for broader proposition |
| AHI04-47 | Immuta Spark user/data source outside registered coverage | missing audit cannot prove no query/use |
| AHI04-48 | Immuta UAM export arrives every 12h | export arrival determines availability, not event time |
| AHI04-49 | Expected export file/batch missing | export acquisition degraded; no empty interval assumption |
| AHI04-50 | Missing export later restored | later availability recorded; prior K remains missing |
| AHI04-51 | Raw payload capture forbidden by minimization policy | retain permitted reference/digest/normalized facts only |
| AHI04-52 | Query parameters contain secrets/PII | safe provenance without unauthorized parameter disclosure |
| AHI04-53 | Malformed payload may affect coverage | quarantine + parser failure; do not silently drop |
| AHI04-54 | Parser v2 supports new source field | new normalized derivation binds parser v2 |
| AHI04-55 | Reparse old raw material changes normalized interpretation | new derived record/supersession; historical prior K not rewritten |
| AHI04-56 | Same event received via webhook and REST | deduplicate logically; preserve two transport observations as common-derived |
| AHI04-57 | Source offers no stable event ID | dedup remains bounded/uncertain; no aggressive merge by timestamp alone |
| AHI04-58 | Worker crashes after fetch before persistence | checkpoint unchanged; source material re-fetched/replayed |
| AHI04-59 | Worker crashes after persistence before checkpoint | replay is duplicate-safe; then checkpoint advances |
| AHI04-60 | Evidence and checkpoint commit succeed | downstream evidence eligible after durable provenance |
| AHI04-61 | Historical backfill finds old event today | event time old; availability/collection today; earlier K unchanged |
| AHI04-62 | On-demand query finds evidence absent from prior collection | current retrospective may use it; prior as-known cannot |
| AHI04-63 | Source retention expired but product copy survives | product-retained evidence remains with source limitation/provenance |
| AHI04-64 | Source retention expired and no product copy exists | exact history unavailable; do not reconstruct from current state |
| AHI04-65 | Archived product evidence restored | availability restored now; original evidence identity preserved |
| AHI04-66 | Source object deleted after prior observation | deletion/current absence does not erase retained historical occurrence |
| AHI04-67 | Credential expires midway through pagination | partial run; authn failure from failure page onward |
| AHI04-68 | Permission revoked midway through acquisition | partial/observer-relative coverage; historical earlier pages remain |
| AHI04-69 | Rate limit reached midway through acquisition | partial until resumed; no completed denominator |
| AHI04-70 | Timeout occurs on final partition | final partition unresolved; run partial |
| AHI04-71 | DNS/TLS outage prevents all requests | reachability failed; domain state unknown |
| AHI04-72 | One of ten partitions intentionally skipped by plan bug | coverage manifest reveals omission; cannot claim complete |
| AHI04-73 | Monitoring Scope expects 100 entities, 90 acquired | coverage partial 90/100 where count disclosure permitted |
| AHI04-74 | Ten expected entities are unresolved/hidden | unresolved segment retained; no implicit exclusion |
| AHI04-75 | Scope selector source unavailable during materialization | scope membership unknown, not reduced to visible set |
| AHI04-76 | Scope revision changes during long acquisition | run stays bound to pinned scope/plan revision; later run uses new revision |
| AHI04-77 | New assets enter scope after current run started | not silently added to old denominator; next effective plan/materialization includes them |
| AHI04-78 | Service principal reads evidence requester cannot see | collection allowed; disclosure independently filtered later |
| AHI04-79 | Source owner/admin metadata collected | no Assertion Authority promotion |
| AHI04-80 | Primary authority source unavailable, convenient lower source exists | no silent fallback |
| AHI04-81 | Group 03 rule explicitly activates fallback on proven outage | adapter may acquire fallback while preserving authority/provenance distinction |
| AHI04-82 | HTTP/API healthy but parser is broken | integration degraded despite source reachability |
| AHI04-83 | Parser healthy but Delta persistence fails | evidence not published; checkpoint not advanced |
| AHI04-84 | Persistence later recovers | new acquisition succeeds; earlier persistence failure interval remains historical |
| AHI04-85 | Old event collected now due delayed publication | source/event time and availability/collection lag remain separate |
| AHI04-86 | Source publishes old historical event after correction | late/correction semantics preserved; no prior-K backfill |
| AHI04-87 | Source clock is skewed relative to collector | clock quality/observed receipt prevents naive timestamp ordering |
| AHI04-88 | SC-01 operational source has sufficient quota for frequent acquisition | higher cadence allowed without authority promotion |
| AHI04-89 | SC-05 historical basis source only needs slow/on-demand collection | lower cadence valid if product promise satisfied |
| AHI04-90 | Storage/API cost rises for optional enrichment | reduce optional cadence via governed plan; dependent capability becomes less current |
| AHI04-91 | Cost pressure targets required negative-coverage source | cannot silently reduce promised coverage; change scope/service promise explicitly or pay cost |
| AHI04-92 | Optional governance integration degraded | only dependent governance/Explanation statements narrow |
| AHI04-93 | Optional integration fails while runtime source remains healthy | unrelated runtime answers remain available |
| AHI04-94 | Convenience integration summary says healthy but pagination dimension partial | proposition requiring complete pagination remains limited; summary cannot override dimension |
| AHI04-95 | Integration recovers after one-hour outage | current health restored; historical gap remains visible at earlier K |
| AHI04-96 | Group 05 asks if no execution/output/exposure occurred during connector gap | cannot infer negative from acquisition silence; inspect coverage/health first |

## Result

**AHI04-01–AHI04-96 pass.** The suite validates source-specific hybrid collection, durable checkpoints, pagination completeness, quota/retry behavior, deployment variability, delayed publication, schema/parser evolution, optional-source degradation and non-rewriting integration-health history without creating a global integration-health score.
