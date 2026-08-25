# Group 05 Scenario Review — LIE05-01–LIE05-60

All scenarios pass the Group 05 source-contract boundaries.

| ID | Scenario | Required result |
|---|---|---|
| LIE05-01 | Table lineage event captured | Observed relationship/read-write event only; no permanent topology promotion |
| LIE05-02 | No lineage event returned | Coverage limitation unless complete opportunity/capture proven |
| LIE05-03 | Column lineage captured | Field-level relationship for captured event only |
| LIE05-04 | UDF obscures column lineage | Missing mapping remains unknown, not no relationship |
| LIE05-05 | Source referenced by path | Preserve path identity until explicit table mapping |
| LIE05-06 | Table renamed | Do not assume native lineage continuity |
| LIE05-07 | Explicit identity crosswalk spans rename | Historical traversal may compose under crosswalk |
| LIE05-08 | `direct_access=true` | Direct source reference only; no causal/exposure score |
| LIE05-09 | `direct_access=false` through view | Intermediate dependency remains potentially relevant |
| LIE05-10 | Job entity metadata populated | Bind to source-local job/run identity |
| LIE05-11 | Entity metadata null on JDBC read | Preserve observed read; consumer entity remains contextual/partial |
| LIE05-12 | Lineage event >1 year old absent from system table | Do not infer historical non-use |
| LIE05-13 | Catalog lineage API retains old edge | Historical relationship supported with API-detail limits |
| LIE05-14 | Producer succeeded | Does not establish downstream publication/availability |
| LIE05-15 | Table exists and is selectable | Availability, not actual encounter |
| LIE05-16 | SQL query history record exists | Statement execution established |
| LIE05-17 | Query finished and lineage read joins by statement ID | Strong bounded table-read encounter |
| LIE05-18 | Query history exists but no lineage captured | Statement encounter without proven table source via that source set |
| LIE05-19 | Lineage read exists but exact statement unavailable | Object read established; statement context partial |
| LIE05-20 | Query `client_application=Power BI` | External BI client context, not report view |
| LIE05-21 | Query source identifies dashboard | Dashboard-origin query execution context established |
| LIE05-22 | Query read_rows > 0 | Read metric evidence; no version identity by itself |
| LIE05-23 | Query served from result cache | Cached encounter; source not freshly read at receipt |
| LIE05-24 | Cache origin statement retained | Link cached result to origin statement, not automatic table version |
| LIE05-25 | Dashboard `getPublishedDashboard` event | Dashboard access/view proposition only |
| LIE05-26 | Dashboard access but no query execution | Could be cache/definition access; no fresh dataset-query inference |
| LIE05-27 | Dashboard `executeQuery` + statement | Dataset query execution supported |
| LIE05-28 | Dashboard `getQueryResult` | Result receipt supported; version exposure still separate |
| LIE05-29 | Dashboard cache holds safe V-1 after V bad | Safe-state encounter possible while stale |
| LIE05-30 | Dashboard cache holds bad V after source repaired | Exposure can persist after upstream repair |
| LIE05-31 | Published dashboard multi-page view | Do not assume datasets on inactive pages encountered |
| LIE05-32 | Scheduled dashboard refresh configured | Opportunity only until refresh execution evidenced |
| LIE05-33 | Scheduled refresh query executed | Refresh encounter established, human view separate |
| LIE05-34 | Snapshot sent by email | Delivery established, reading/reliance unknown |
| LIE05-35 | Snapshot sent to Slack/Teams destination | Delivery path, not decision consequence |
| LIE05-36 | Tableau query executes through warehouse | Databricks platform read supported, Tableau view unknown |
| LIE05-37 | BI extract later served offline | Databricks read can seed copy; later report exposure needs extract/view evidence |
| LIE05-38 | JDBC application reads table | Platform encounter supported; app display/process remains external |
| LIE05-39 | Job run lineage reads source | Run-level encounter supported; exact version separate |
| LIE05-40 | Query definitely read table near bad commit | Do not assign latest table version by timestamp proximity |
| LIE05-41 | Query explicitly `VERSION AS OF 42` and evidence retained | Exact-version encounter conditionally supported |
| LIE05-42 | Time-travel SQL text truncated | Exact version unresolved |
| LIE05-43 | Query parameter selects snapshot ID and retained | Exact state can bind when snapshot mapping retained |
| LIE05-44 | Materialized view refresh succeeds | Refresh execution, not human encounter or exact source version by success alone |
| LIE05-45 | A→B→C lineage all captured | No transitive A-suspect exposure to C without state propagation evidence |
| LIE05-46 | B output proven to carry affected state and C reads it | Multi-hop exposure can be established with per-hop evidence |
| LIE05-47 | Consumer has query + cache alternate paths | Global result requires both material paths |
| LIE05-48 | Safe cache path only known | Cannot conclude globally not exposed if query path unresolved |
| LIE05-49 | One qualifying affected-version read | Positive bounded exposure established |
| LIE05-50 | Object read known, version unknown | Encounter established; exposure version unresolved |
| LIE05-51 | No query records during query-history outage/gap | Not evidence of non-exposure |
| LIE05-52 | No lineage after object rename | Not evidence of no downstream use |
| LIE05-53 | Exposed consumer remains healthy | Exposure without downstream monitored effect |
| LIE05-54 | Downstream metric degrades but exact exposure unknown | Effect evidence can coexist with unresolved exposure |
| LIE05-55 | Dashboard viewed and KPI differs | Analytical effect requires exact comparison/context; view alone insufficient |
| LIE05-56 | User viewed bad dashboard then made business decision | Decision reliance still requires business provenance |
| LIE05-57 | Customer ticket references wrong output | Consequence candidate; causal attribution remains separate |
| LIE05-58 | Table popularity high | Priority/context only, not exposure count/severity |
| LIE05-59 | Vendor downstream-impact says High | Source-owned candidate/context, not realized Impact |
| LIE05-60 | No complaints, incomplete telemetry | No `no consequence` conclusion |

**Result:** LIE05-01–LIE05-60 PASS.
