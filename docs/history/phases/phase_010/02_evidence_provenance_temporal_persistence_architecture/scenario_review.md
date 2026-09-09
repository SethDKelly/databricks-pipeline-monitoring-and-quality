# Phase 010 Group 02 — Evidence / Provenance / Temporal / Persistence Scenario Review

**Suite:** EPT02-01–EPT02-72

All scenarios pass against ARCH-033–ARCH-080.

| ID | Scenario | Expected architecture result |
|---|---|---|
| EPT02-01 | Source fact copied into framework store | retained copy preserves source authority/limitations; framework owns capture history only |
| EPT02-02 | Original source later expires | retained copy can remain evidence with original provenance; no new authority |
| EPT02-03 | Same payload bytes observed twice from same source at different times | distinct logical occurrences may share physical bytes |
| EPT02-04 | Two retained rows derive from one audit export | common derivation retained; not independent corroboration |
| EPT02-05 | Independent sources produce identical payload text | do not merge logical occurrences merely by digest equality |
| EPT02-06 | Payload digest mismatches on restore | integrity failure surfaced; restored material not trusted silently |
| EPT02-07 | Event occurred Monday but source publishes Wednesday | event/effective Monday; availability Wednesday |
| EPT02-08 | Framework collects Thursday | collection/persistence remains Thursday; no backdating |
| EPT02-09 | As-known cutoff Tuesday | late Wednesday evidence excluded from Tuesday view |
| EPT02-10 | Later evidence resolves Tuesday unknown | current retrospective can resolve; historical Tuesday remains unknown |
| EPT02-11 | Source corrects prior record | append linked correction/supersession; prior record preserved |
| EPT02-12 | Source deletes corrected record later | deletion/source unavailability separate from retained history |
| EPT02-13 | Current-state view shows corrected value | convenience view valid; earlier value still reconstructable |
| EPT02-14 | Parser v2 reprocesses old payload differently | new derivation/parser revision; no new source observation |
| EPT02-15 | Schema migration changes physical columns | durable evidence IDs/provenance preserved |
| EPT02-16 | OPTIMIZE/compaction rewrites Delta files | physical rewrite only; semantic record set unchanged |
| EPT02-17 | Delta transaction log older version pruned | DMTZ row-based history still works if canonical records retained |
| EPT02-18 | VACUUM removes old files not needed by current table state | product replay does not depend on that time-travel version |
| EPT02-19 | Unity Catalog managed tables verified | preferred structured realization allowed |
| EPT02-20 | Unity Catalog managed tables unavailable | external Delta/cloud-object realization remains valid |
| EPT02-21 | Managed table lifecycle conflicts with org archive policy | use deployment-approved external/other valid realization |
| EPT02-22 | Unity Catalog volumes available | may govern opaque payload plane |
| EPT02-23 | Volumes unavailable | governed cloud-object payload location used; semantics unchanged |
| EPT02-24 | VARIANT unsupported by target runtime | portable structured/string payload representation used |
| EPT02-25 | FILE type unavailable/Beta disabled | manifest + ordinary object reference remains baseline |
| EPT02-26 | Large source artifact required for audit | object payload plane stores selectively with manifest/digest |
| EPT02-27 | Raw production rows are not needed | do not copy them; metadata/minimized capture only |
| EPT02-28 | Sensitive payload can be represented by digest + metadata | hash/minimized capture class allowed when evidence promise permits |
| EPT02-29 | Graph projection is deleted | rebuild from canonical typed records |
| EPT02-30 | Graph projection is stale | stale traversal cannot overwrite canonical state |
| EPT02-31 | Search index ranks old evidence highly | ranking does not make it material/truthful by itself |
| EPT02-32 | Serving cache loses a correction | canonical store wins; cache must refresh/rebuild |
| EPT02-33 | Report asks only current operational state | retained old history does not automatically flood report |
| EPT02-34 | User explicitly asks last year comparison | warm retained history becomes relevant candidate set |
| EPT02-35 | User asks two-year trend and old metrics were safely rolled up | approved trend aggregates may serve that bounded trend question |
| EPT02-36 | User asks exact old run after detail was downsampled | exact answer unavailable/limited; aggregate cannot substitute |
| EPT02-37 | Three-year-old unreferenced routine telemetry exceeds policy | eligible for expiry rather than indefinite accumulation |
| EPT02-38 | Three-year-old event linked to recurring incident | explicit dependency/relevance can retain/restore it despite age |
| EPT02-39 | Active Investigation references expiring evidence | dependency pin blocks ordinary TTL |
| EPT02-40 | Supported Causal Claim requires exact basis | exact required basis pinned/non-lossy for review promise |
| EPT02-41 | Retained Explanation promises exact prior basis | basis/payload retained for promised horizon or limitation explicit |
| EPT02-42 | Gate enforcement record reaches routine TTL | control-audit dependency can extend retention |
| EPT02-43 | Legal hold applies to subset | scoped hold overrides ordinary TTL only for bound material |
| EPT02-44 | Hold released | reevaluate normal policy; no automatic immediate purge requirement |
| EPT02-45 | New policy shortens ordinary warm window | effective-dated policy may transition eligible existing data; history of policy retained |
| EPT02-46 | Product promise still requires 1-year replay | shorter cost policy cannot delete required evidence |
| EPT02-47 | Cost spike suggests aggressive cleanup | review lifecycle/minimization/tiering; no silent evidence loss |
| EPT02-48 | Metric measurements older than detailed need | eligible for governed daily/weekly/monthly rollup if exact detail not promised |
| EPT02-49 | Exposure negative depends on individual read events | lossy aggregation disallowed if it would break coverage proof |
| EPT02-50 | Causal evidence consists of exact configuration record | summary cannot replace exact basis silently |
| EPT02-51 | Opaque payload expires after ordinary TTL | retain permitted provenance stub and expiry record |
| EPT02-52 | Citation points to expired payload | render basis as payload-expired/not inspectable, not absent |
| EPT02-53 | Payload archived, not expired | reference reports archived/restorable state |
| EPT02-54 | Cold restore succeeds | original evidence ID/provenance retained; no new observation |
| EPT02-55 | Cold restore fails | basis unavailable; not evidence of source absence |
| EPT02-56 | Irreversible purge occurs | lifecycle audit record retains policy/reason without deleted content |
| EPT02-57 | Evidence crosses residency boundary without permission | physical sharding/authorized reference prevents unsafe copy |
| EPT02-58 | Two regions require independent stores | logical identity can remain stable while physical persistence is partitioned |
| EPT02-59 | Backup restored after outage | restored rows retain original IDs/times/provenance |
| EPT02-60 | Backup restoration duplicates files | logical dedup/integrity prevents duplicate evidence occurrences |
| EPT02-61 | Historical source identifier renamed | durable framework evidence/source identity maintains historical linkage where mapping exists |
| EPT02-62 | Source locator itself is sensitive | provenance projection may restrict locator while internal identity remains |
| EPT02-63 | Vendor retains source for 365 days | vendor horizon informs capability; does not automatically become DMTZ TTL |
| EPT02-64 | Delta defaults expose ~30-day log history | infrastructure default does not define DMTZ historical promise |
| EPT02-65 | Routine recent report uses 120-day reference profile | valid configurable default; not universal semantic requirement |
| EPT02-66 | Annual comparison needs ~400-day detailed history | warm policy supports it where adopted; target profile can differ explicitly |
| EPT02-67 | 24-month trend summary is enough for bounded trend | old detailed aggregatable measurements may expire after validated rollup |
| EPT02-68 | Audit requires seven years | explicit audit policy/hold extends scoped material beyond ordinary reference profile |
| EPT02-69 | SC-01 request would require cold archive restore for unrelated old evidence | do not block narrow current fact; old evidence remains outside relevance scope |
| EPT02-70 | SC-04 historical request needs archived evidence | slower restore path valid; correctness dominates immediacy |
| EPT02-71 | SC-06 control history required after incident | retain exact decision/delivery/enforcement evidence for configured audit horizon |
| EPT02-72 | Group 03 begins after persistence acceptance | identity/authority architecture consumes stable canonical IDs/time/history/retention semantics without reopening store roles |

## Result

**EPT02-01–EPT02-72 pass.** The suite validates canonical/derived separation, bitemporal history, retention versus relevance, practical aging, non-lossy exceptions, archive/expiry semantics and deployment portability without selecting later serving/reasoning/control technology.
