# Decision Records — Phase 009 Group 05 Lineage / Consumer / Impact Sources

Continues after D-1071.

### D-1072 — Group 05 source facts require current documentation verification
**Status:** Accepted
Lineage/query/dashboard/audit semantics, retention and preview status are versioned external facts.

### D-1073 — Lineage event is observational evidence, not a permanent topology fact
**Status:** Accepted
A captured event does not create an indefinite dependency interval.

### D-1074 — Unity Catalog lineage coverage is explicitly incomplete
**Status:** Accepted
No-record negative claims require independent coverage proof.

### D-1075 — Column lineage retains source capture limitations
**Status:** Accepted
Missing field mapping is not evidence of no field dependency.

### D-1076 — `direct_access` retains Databricks source semantics only
**Status:** Accepted
It is not relevance, causal-strength or exposure-strength ranking.

### D-1077 — Lineage entity IDs are source-local consumer identities
**Status:** Accepted
Ecosystem consumer identity still requires reconciliation.

### D-1078 — Null lineage entity metadata does not mean no consumer
**Status:** Accepted
JDBC/other reads can lack a Databricks entity association.

### D-1079 — Lineage system-table and Catalog/API history are separate surfaces
**Status:** Accepted
Longer retention does not imply identical fields/detail.

### D-1080 — Rename continuity is not provided by native lineage by default
**Status:** Accepted
Entity Identity mapping is required across rename/recreate where continuity matters.

### D-1081 — Path lineage remains path identity until mapped
**Status:** Accepted
Path equality/name similarity cannot create table identity.

### D-1082 — Publication/availability is separate from lineage and producer success
**Status:** Accepted
A possible downstream relationship does not prove accessible state.

### D-1083 — Query-history statement execution is an encounter source within documented scope
**Status:** Accepted
It remains bounded by compute/retention/permission/source coverage.

### D-1084 — Lineage `statement_id` to query-history join is accepted explicit association evidence
**Status:** Accepted
It can strongly bind a captured table read to an exact SQL statement.

### D-1085 — Query-source/client fields provide context, not universal consumer identity
**Status:** Accepted
Client labels do not prove report view or human use.

### D-1086 — Query-result-cache use is distinct from fresh source read
**Status:** Accepted
Cached encounter retains its cache-origin provenance.

### D-1087 — Dashboard access is distinct from dataset query execution
**Status:** Accepted
`getDashboard`/`getPublishedDashboard` cannot prove every dataset ran.

### D-1088 — Dashboard query execution is distinct from result receipt
**Status:** Accepted
`executeQuery` and `getQueryResult` are separate encounter propositions.

### D-1089 — Dashboard cache makes safe/stale/affected state explicit
**Status:** Accepted
A view may be served without a fresh warehouse query.

### D-1090 — Dashboard cache age does not itself identify exact state version
**Status:** Accepted
Exact cached-state exposure needs state/version evidence.

### D-1091 — Dashboard schedule configuration is opportunity, not refresh execution
**Status:** Accepted
Execution must be evidenced separately.

### D-1092 — Snapshot/subscription delivery is encounter/delivery, not reliance
**Status:** Accepted
Email/Slack/Teams delivery does not prove reading or decision use.

### D-1093 — External BI query evidence stops at the Databricks query boundary by default
**Status:** Accepted
Report view/visual interaction requires external BI evidence.

### D-1094 — JDBC/application read does not prove application display or business use
**Status:** Accepted
Application-layer telemetry remains separate.

### D-1095 — Job/run source-read encounter uses explicit lineage/run identity
**Status:** Accepted
Name/time matching is not sufficient.

### D-1096 — Generic exact table-version consumption is unsupported out of the evaluated source pair
**Status:** Accepted
Lineage/query history do not universally emit the exact data version read.

### D-1097 — Object encounter with unresolved version is a valid state
**Status:** Accepted
Do not force exposed/not-exposed when exact affected-state identity is missing.

### D-1098 — Query time is not a substitute for consumed table version
**Status:** Accepted
Latest-at-time inference is not accepted.

### D-1099 — Explicit time-travel/version selection can support exact state encounter conditionally
**Status:** Accepted
Statement/parameter semantics and table history must be retained and resolvable.

### D-1100 — Truncated/encrypted/unavailable query text preserves version uncertainty
**Status:** Accepted
Missing detail cannot be reconstructed by convenience.

### D-1101 — Refresh/materialization is a distinct encounter mode
**Status:** Accepted
Refresh success does not mean human view or exact version use.

### D-1102 — Cache/copy/export/snapshot state can outlive source correction
**Status:** Accepted
Historical exposure is non-rewriting across copies.

### D-1103 — Safe stale state remains distinct from affected-state exposure
**Status:** Accepted
Avoiding affected V can coexist with freshness failure.

### D-1104 — Multi-hop exposure is not transitive
**Status:** Accepted
Per-hop affected-state propagation and consumer encounter are required.

### D-1105 — Alternate encounter paths require explicit coverage
**Status:** Accepted
One safe path cannot establish global non-exposure.

### D-1106 — Positive exposure is state/version and consumer-mode bound
**Status:** Accepted
Object-level read evidence cannot silently become suspect-version exposure.

### D-1107 — `Not exposed` retains strong negative-evidence burden
**Status:** Accepted
All material opportunities/paths/versions require sufficient coverage.

### D-1108 — Missing lineage/query/audit/external telemetry is not non-exposure
**Status:** Accepted
Source gaps remain limitations.

### D-1109 — Exposure and downstream effect remain independent
**Status:** Accepted
Either can be evidenced while the other remains absent/unresolved.

### D-1110 — Downstream effect consumes exact Group 04 evidence when properly bound
**Status:** Accepted
Generic health status does not create consumer effect.

### D-1111 — Consequence categories require category-specific source evidence
**Status:** Accepted
Technical, analytical and business consequences are not interchangeable.

### D-1112 — Business/customer consequence is generally not native Databricks truth
**Status:** Accepted
Business/application/decision/financial evidence is required where material.

### D-1113 — Dashboard/report view is not decision reliance
**Status:** Accepted
View → comprehension → reliance → action → consequence remain separate.

### D-1114 — Table popularity/insights are usage context, not realized Impact
**Status:** Accepted
Recent activity can inform priority without creating exposure/severity.

### D-1115 — Vendor downstream-impact labels remain contextual/supporting
**Status:** Accepted
They do not replace the accepted Impact ladder or Causal Claim.

### D-1116 — Historical Impact replay is source-set and retention bound
**Status:** Accepted
Lineage/query/audit/external histories have different windows and detail.

### D-1117 — Strong `no effect` and `no consequence` remain coverage-intensive negatives
**Status:** Accepted
Missing monitored change or complaints is insufficient.

### D-1118 — INTG-120–INTG-153 and LIE05-01–LIE05-60 are accepted
**Status:** Accepted — Phase 009 Group 05
Group 05 is complete; Group 06 is next.
