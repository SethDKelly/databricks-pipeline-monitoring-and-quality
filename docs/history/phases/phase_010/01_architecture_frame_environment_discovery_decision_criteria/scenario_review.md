# Phase 010 Group 01 — Architecture Frame Scenario Review

**Suite:** AFE01-01–AFE01-60

All scenarios pass against ARCH-001–ARCH-032.

| ID | Scenario | Expected architecture result |
|---|---|---|
| AFE01-01 | Databricks docs list feature; target region unknown | documented possibility; deployment usability unknown |
| AFE01-02 | Feature supported in AWS but target is GCP | no cross-cloud promotion; verify GCP capability instance |
| AFE01-03 | Feature supported in one GCP region but target region differs | region-bound unknown/unavailable per evidence, not global support |
| AFE01-04 | System table exists generally; AWS GovCloud target | verify GovCloud-supported subset before relying on table |
| AFE01-05 | System table regional but question is account-global | capability partially usable; global conclusion unsupported without composition |
| AFE01-06 | Preview documented but workspace preview state unknown | enablement unknown; not usable assumption |
| AFE01-07 | Account preview enabled but specific workspace scope differs | preserve scope; no automatic workspace fact beyond vendor semantics |
| AFE01-08 | Designated Service requires cross-Geo setting | residency/enablement dimension governs use |
| AFE01-09 | Databricks feature visible to admin but integration principal denied | presence yes; authorization no; unusable to integration |
| AFE01-10 | API endpoint reachable but returns partial permission-filtered data | reachability yes; coverage partial |
| AFE01-11 | GitHub.com supports feature; deployment is GHE.com | verify GHE.com feature matrix; no equivalence assumption |
| AFE01-12 | GitHub environment protection documented; private repo plan unknown | plan entitlement unknown; Gate realization not assumed |
| AFE01-13 | GHES feature documented for newer version; target version older | version-bound unsupported/unknown until verified |
| AFE01-14 | GHES version itself unknown | capability unknown; discover version first |
| AFE01-15 | Collibra feature in commercial cloud; target is Government | verify government matrix; no commercial-cloud promotion |
| AFE01-16 | Collibra Cloud site supports fewer connectors than customer Edge | bind site model and exact connector capability |
| AFE01-17 | Immuta installed but license/API package unknown | integration capability remains unknown/environment-specific |
| AFE01-18 | Optional Immuta absent | exact Immuta-derived capabilities unavailable; core siblings remain |
| AFE01-19 | Optional Collibra temporarily unreachable | integration degraded; no benign governance defaults |
| AFE01-20 | Vendor documentation changes after discovery | retain dated public fact and revalidate affected assumptions |
| AFE01-21 | Capability verified six months ago; preview became GA/changed | revalidate according to freshness trigger; do not assume permanence |
| AFE01-22 | License expires while feature configuration remains | configuration present ≠ entitlement; usable capability changes |
| AFE01-23 | Permission revoked after successful probe | historical capability remains; current authorization updated non-rewriting |
| AFE01-24 | Network route fails while vendor source remains healthy | reachability degraded; domain-negative conclusions suppressed |
| AFE01-25 | API throttled | integration health degraded, not no records/events |
| AFE01-26 | Pagination stops early | coverage partial; strong negatives invalid |
| AFE01-27 | Schema parser fails after vendor change | source may be healthy; integration transform failed distinctly |
| AFE01-28 | Retention window expires | historical source unavailable; not evidence of no event |
| AFE01-29 | Feature disabled by org policy despite technical support | technical possibility remains; policy prevents use |
| AFE01-30 | Cross-region use technically possible but residency policy forbids it | policy constraint overrides architecture use, not source truth |
| AFE01-31 | Same source sufficient for run status but not exact consumed version | proposition-specific usability differs validly |
| AFE01-32 | Source supports positive read evidence but incomplete negative coverage | positive proposition may be supported; strong negative not |
| AFE01-33 | One vendor feature absent, equivalent evidence available elsewhere | alternate source requires explicit authority/evidence mapping; no silent fallback |
| AFE01-34 | Alternative source lower authority | availability does not create authority precedence |
| AFE01-35 | MVP excludes external BI telemetry | exposure beyond supported paths explicitly scoped, not declared safe |
| AFE01-36 | MVP excludes active controls | monitoring/RCA remains; Gate/Safeguard claims unavailable |
| AFE01-37 | MVP offers `confirmed` causality without authority source | invalid scope; either add authority workflow or cap status below confirmed |
| AFE01-38 | MVP offers basis inspection | sensitive-basis authorization becomes core security requirement |
| AFE01-39 | MVP promises exact historical communication | authentic snapshot retention becomes required, not optional vendor feature |
| AFE01-40 | MVP does not promise long-horizon replay | gap can be explicitly scoped with bounded retention contract |
| AFE01-41 | Architecture option is fastest but loses provenance | rejected by hard constraint |
| AFE01-42 | Architecture option is cheapest but converts source failure to empty result | rejected by hard constraint |
| AFE01-43 | Architecture option easier but joins deployments/runs by timestamp | rejected by identity/evidence hard constraint |
| AFE01-44 | Two compliant options trade cost vs latency | decision-specific tradeoff; no universal architecture score |
| AFE01-45 | Hard-to-reverse database choice depends on unknown tenant volume | defer or choose reversible path unless bounded rationale exists |
| AFE01-46 | Reversible adapter choice under uncertainty | can proceed with assumptions explicitly registered |
| AFE01-47 | SC-01 operational fact available before SC-02 health evidence | return narrow operational result without global wait |
| AFE01-48 | SC-03 RCA source is slow | RCA may mature later without delaying unrelated facts |
| AFE01-49 | SC-04 replay source lacks availability-by-K | exact as-known claim unsupported even if event time exists |
| AFE01-50 | SC-05 communication reference survives but payload expired | reference exists; exact basis/content unavailable |
| AFE01-51 | SC-06 control telemetry missing | do not infer fail-open/fail-closed or enforcement success |
| AFE01-52 | Same source has different SLO needs by service class | valid; no global source freshness number |
| AFE01-53 | Public vendor quota known but enterprise contract differs | contract/tenant fact supersedes public default for target decision |
| AFE01-54 | Cost unknown | decision records unknown and sensitivity; no invented estimate as fact |
| AFE01-55 | GAP-009 item has two technical owners | designate primary owner and secondary dependencies |
| AFE01-56 | GAP intentionally deferred | retain explicit scope/treatment and affected capability loss |
| AFE01-57 | Later group discovers initial assumption false | supersede assumption and re-evaluate dependent ADRs non-rewriting |
| AFE01-58 | Later group needs capability not in inventory | add/revise capability instance before relying on it |
| AFE01-59 | Technology selected because it is familiar but alternatives not evaluated | fails ADR acceptance for material decision |
| AFE01-60 | Group 02 begins with no database selected but accepted decision frame | correct Group 01 exit state |

## Result

**AFE01-01–AFE01-60 pass.** The suite establishes that deployment variability, unknown preservation, proposition-specific usability, hard constraints, service classes, scope discipline and ADR quality can constrain later architecture without prematurely selecting technology.
