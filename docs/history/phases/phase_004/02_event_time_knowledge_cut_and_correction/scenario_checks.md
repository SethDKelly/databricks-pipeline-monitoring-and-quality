# Phase 004 Group 02 — Scenario Checks

**Status:** Accepted

| Scenario | Required distinction | Result |
|---|---|---|
| Run completes before monitoring ingest | event/source-availability time differs from framework knowledge time | Pass |
| Current query discovers an old run | old event time does not backdate current knowledge | Pass |
| Source record existed but was never collected | source-available may be true while framework-known is false/unknown | Pass |
| Missing retained evidence around a monitoring outage | cannot claim `not known by cutoff` from absence alone | Pass |
| Late consumption log proves historical exposure | incident-time exposure remains unknown; later retrospective view becomes exposed | Pass |
| Source explicitly corrects a row count | correction supersedes current use while prior state remains reconstructable | Pass |
| Independent source disagrees with row count | conflict remains conflict rather than automatic correction | Pass |
| Baseline correction changes Assessment | source Observation remains unchanged; new Assessment is reassessment | Pass |
| Closed Investigation receives immaterial late evidence | no automatic reopen | Pass |
| Closed Investigation receives evidence undermining core cause | becomes review/reopen candidate without erasing historical closure | Pass |
| 07:04 job success, 07:08 Metric View quality failure | fast execution answer remains valid but never implied overall health | Pass |
| RCA evidence arrives after operational validation | later RCA enriches/changes causal interpretation with new knowledge time | Pass |
| Post-ops review adds downstream usage evidence next day | retrospective Impact changes while incident-time knowledge remains preserved | Pass |
| High-consequence gate decision lacks required slow evidence | latency objective cannot waive the gate's evidence standard | Pass |
| No retained incident Explanation | current `as-known-then` answer is labeled reconstructed | Pass |
| Historical actor had wider data access | historical authorization remains evidence; current requester disclosure remains current | Pass |

## Progressive-availability reference sequence

A representative healthy product sequence may legitimately look like:

- **07:04:10** — `Job C execution succeeded` from run evidence;
- **07:05:00** — `current output exists and meets freshness criterion` from output/freshness evidence;
- **07:08:00** — `completeness criterion violated` from Metric View/DQ evidence;
- **07:15:00** — `upstream B degradation is a supported causal hypothesis` from Lineage/change/RCA evidence;
- **next day** — `Report R was exposed and used in a client process` from late consumption/consequence evidence.

The sequence is not a required implementation schedule. It demonstrates that later evidence can increase analytical maturity without making the early narrowly scoped statements historically false.
