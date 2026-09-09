# Phase 009 Group 01 — Integration Contract Scenario Review

**Result:** IC01-01–IC01-40 pass against INTG-001–INTG-022.

| ID | Scenario | Required result |
| --- | --- | --- |
| IC01-01 | `Databricks` is named as a source with no exact surface | Too coarse; source-surface identity unresolved. |
| IC01-02 | Two APIs from one product expose different history semantics | Separate capability rows. |
| IC01-03 | API version changes identifier/timestamp meaning | Re-evaluate affected capability; no silent inheritance. |
| IC01-04 | Source is queryable but has no authority rule for the metadata category | Available, authority unresolved/advisory as applicable. |
| IC01-05 | Authoritative policy assertion is offered as proof an execution occurred | Authority does not create factual sufficiency. |
| IC01-06 | Framework can read exact value but requester may not | Internal retrieval separate from disclosure. |
| IC01-07 | Same table name appears in two workspaces | Name equality cannot establish Entity Identity. |
| IC01-08 | Stable native ID plus provenance-bearing mapping resolves entity | Join supported for bounded validity context. |
| IC01-09 | Deployment and run timestamps are close but no shared key exists | Exact association unsupported/partial; proximity only candidate evidence. |
| IC01-10 | Deployment record contains explicit run correlation identifier | Association can be supported subject to identifier semantics. |
| IC01-11 | Historical event time exists but recorded/availability time does not | Event replay may be possible; as-known-at-cut remains unsupported/partial. |
| IC01-12 | Late event preserves event time and source recorded time | Earlier K excludes it; later retrospective view may include it. |
| IC01-13 | Framework extraction timestamp is mistaken for source knowledge time | Reject; retrieval time alone does not prove prior availability. |
| IC01-14 | Run event record with exact run identity is returned | Positive occurrence can be supported at that grain. |
| IC01-15 | Complete closed run-opportunity window has no run record and source healthy | `No run` may be supported for that bounded opportunity. |
| IC01-16 | No run record returned during telemetry outage | Run absence unresolved; outage is not negative evidence. |
| IC01-17 | Query logs cover only one consumer mode | No consumer-wide non-exposure conclusion. |
| IC01-18 | All in-scope modes/paths/version encounters are covered and none used suspect V | Bounded `not exposed to V` may be supportable. |
| IC01-19 | Endpoint exposes only current object state | Exact prior state/knowledge replay unsupported without another retained source. |
| IC01-20 | Audit history preserves event/effective and recorded times | Historical replay capability may be supported for covered records. |
| IC01-21 | Mutable metadata overwrites prior values with no history | Earlier assertion state unavailable; do not reconstruct by assumption. |
| IC01-22 | Correction retains original assertion and correction recorded time | Non-rewriting retrospective correction supported. |
| IC01-23 | Old event is backfilled today | Do not include in earlier knowledge cut unless prior availability is independently evidenced. |
| IC01-24 | Records can disappear with no tombstone | Missing current record cannot prove historical nonexistence. |
| IC01-25 | API and export both derive from same audit table | Duplicate/common-derived, not two corroborators. |
| IC01-26 | Independent runtime and consumer systems evidence same bounded encounter | May provide independent corroboration if derivation is genuinely independent. |
| IC01-27 | Two governance assertions conflict and no authority rule applies | Preserve conflict; no winner by recency/count. |
| IC01-28 | Explicit authority rule selects source for exact facet/context/time | Resolve standing through that rule, not matrix order. |
| IC01-29 | Preferred source unavailable and fallback source available | Fallback does not inherit preferred source authority. |
| IC01-30 | Source records runs but cannot certify expected opportunities/collection completeness | Positive run supported; strong `no run` unsupported/partial. |
| IC01-31 | Control system records HOLD decision but not downstream enforcement | Decision supported; enforcement unsupported/unknown. |
| IC01-32 | Lineage source records downstream path | Reachability may be supported; actual use/exposure is not. |
| IC01-33 | Metric exists in a query surface but governed Expectation mapping is unknown | Observation capability may exist; normative health contract remains gapped. |
| IC01-34 | Source meets all requirements except retention is shorter than replay need | Current use supported, historical requirement partially supported/unsupported by horizon. |
| IC01-35 | Consumer evidence lacks consumed-version identity | Exposure to specific version is partial/unsupported despite consumer activity evidence. |
| IC01-36 | Product documentation/edition behavior not yet verified | `Unknown / not yet verified`, not unsupported by assumption. |
| IC01-37 | A source surface is irrelevant to a bounded proposition | `Not applicable`, not failure. |
| IC01-38 | Quota forces sampling below required population coverage | Support classification reflects reduced coverage; cost does not rewrite semantics. |
| IC01-39 | Integration pagination fails halfway and failure is observable | Retrieval incomplete; affected negatives withheld and integration limitation recorded. |
| IC01-40 | One proposition needs identity mapping + runtime event + authority rule | Compose explicit rows/joins; no row alone or matrix adjacency creates proof. |

## Exit finding

The suite confirms a common matrix can describe heterogeneous sources without a vendor-wide score or a new source-truth concept.