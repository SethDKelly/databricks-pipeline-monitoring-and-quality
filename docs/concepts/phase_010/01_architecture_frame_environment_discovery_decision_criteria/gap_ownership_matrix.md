# Phase 010 Group 01 — GAP-009 Ownership, Priority & Treatment Matrix

`MVP core` means the bounded MVP architecture must address the gap for the propositions it promises. `Conditional` means mandatory only when the related proposition/source mode is in MVP scope. `Enterprise` means an explicit extension rather than a hidden MVP dependency. `Optional vendor` means absence is allowed with capability-aware degradation.

| Gap | Primary Phase 010 owner | Priority | Group 01 treatment / exit expectation |
|---|---|---|---|
| GAP-009-01 Monitoring Scope | G03 | MVP core | organization-owned governed source required |
| GAP-009-02 Assertion Authority | G03 | MVP core | organization-owned authority rules required where assertions depend on them |
| GAP-009-03 cross-system Entity Identity | G03 (+G02/G04) | MVP core | durable identity/crosswalk architecture required |
| GAP-009-04 GitHub→Databricks correlation | G05 (+G04) | MVP core | explicit shared correlation/attestation for supported deployment reasoning |
| GAP-009-05 exact run Git commit | G05 | Conditional MVP | instrument/attest supported execution modes or degrade exact-version questions |
| GAP-009-06 composite implementation state | G05 | Conditional MVP | bind material facets required by promised run questions |
| GAP-009-07 exact multi-input manifest | G05 | Enterprise/conditional | instrument exact versions where current-cycle/exact-input questions are promised |
| GAP-009-08 compatibility contract | G03/G05 | Conditional MVP | governed consumer interface contracts where compatibility is in scope |
| GAP-009-09 empirical key/integrity | G05 | Conditional MVP | observed checks when proposition matters |
| GAP-009-10 governed DQ/metric revisions | G03/G05 | Conditional MVP | authoritative versioned definitions/applicability |
| GAP-009-11 event-time freshness | G05 | Conditional MVP | domain timestamp/watermark instrumentation when required |
| GAP-009-12 measurement→run/output | G05 | MVP core | exact association architecture required for run-specific health |
| GAP-009-13 historical lineage/rename | G02/G05 | Enterprise/conditional | durable identity/history where replay horizon requires it |
| GAP-009-14 exact consumer-version exposure | G05 | Enterprise/conditional | consumer/path instrumentation for material exposure questions |
| GAP-009-15 dashboard/cache state | G05 | Enterprise/conditional | cache/result provenance where dashboard exposure is promised |
| GAP-009-16 external BI/app use | G05 | Enterprise | external consumer telemetry integration |
| GAP-009-17 business consequence evidence | G05/G06 | Enterprise | incident/process/decision/financial integrations when in scope |
| GAP-009-18 strong multi-hop negatives | G05 | Enterprise | explicit population/path coverage; expensive by design |
| GAP-009-19 Investigation/Annotation record | G06 | MVP core for Investigation workflow | durable case/claim/annotation persistence |
| GAP-009-20 causal confirmation authority | G03/G06 | Conditional MVP | required if `confirmed` is offered; otherwise status ceiling explicit |
| GAP-009-21 universal Safeguard | G07 | Enterprise active control | design path-specific controls; do not promise universal native safeguard |
| GAP-009-22 REF-028 prevention evidence | G07 | Enterprise active control | opportunity+enforcement+negative encounter+alternate coverage |
| GAP-009-23 GitHub Gate→DB execution | G05/G07 | Enterprise active control | reuse explicit cross-system correlation |
| GAP-009-24 Gate rules/override/fallback | G03/G07 | Enterprise active control | governed criterion and exceptional-action authority |
| GAP-009-25 long-horizon replay | G02 | Product-commitment dependent | define retention tiers/horizons before persistence selection |
| GAP-009-26 availability-by-K | G02/G04 | Product-commitment dependent | retain arrival/availability time where exact as-known replay promised |
| GAP-009-27 retained Explanation | G02/G06 | Enterprise / audit commitment | authentic snapshot store when exact prior communication is promised |
| GAP-009-28 prior inspectBasis projection | G02/G03/G06 | Enterprise | persist projection/context if historical visible-view audit promised |
| GAP-009-29 historical authorization | G02/G03 | Enterprise | retain policy/auth state for promised audit horizon |
| GAP-009-30 basis payload durability | G02/G06 | Product-commitment dependent | retain permitted basis or expose unavailability |
| GAP-009-31 sensitive basis disclosure | G03/G06 | MVP core security | independent authorization/minimization required wherever basis exists |
| GAP-009-32 source latency/SLO | G01/G04/G08 | MVP core | use service classes; numeric targets wait for environment data |
| GAP-009-33 integration-health telemetry | G04/G08 | MVP core | explicit health state required before strong negatives |
| GAP-009-34 Databricks quota collection | G04/G08 | MVP core | endpoint/system-table-aware quota design |
| GAP-009-35 GitHub quota collection | G04/G08 | MVP core | auth/rate-aware incremental design |
| GAP-009-36 Collibra discovery | G01/G04 | Optional vendor | deployment/licensing/capability discovery before use |
| GAP-009-37 Immuta discovery | G01/G04 | Optional vendor | deployment/contract/API discovery before use |
| GAP-009-38 cost attribution | G08 | MVP core architecture concern | expose ingestion/query/storage/control cost dimensions |
| GAP-009-39 optional-source degradation | G01/G04/G08 | MVP core | optional source absence narrows exact capabilities only |
| GAP-009-40 deployment capability inventory | G01/G04 | MVP core | capability-instance inventory is mandatory architecture input |

## Cross-group rule

A secondary owner may realize storage, acquisition, security or serving mechanics, but the primary owner remains responsible for demonstrating that the gap's proposition is resolved/reduced/scoped/carried explicitly at its group exit.
