# Decision Records — Phase 007 Grouping and Entry

Continues after D-405.

### D-406 — Phase 007 uses nine logical design groups
**Status:** Accepted — Phase 007 planning
Phase 007 will be reviewed as: (1) Lineage relationship taxonomy/historical topology, (2) Change Intent/Deployment/realized Change, (3) prospective blast radius/change-aware review, (4) execution reconstruction/dependency sequence, (5) Investigation/localization/causal handoff, (6) Impact/consumer encounter/exposure/consequence, (7) Propagation Safeguard operations, (8) Execution Gate/control effects, and (9) historical replay/consolidation/exit.

### D-407 — Phase 007 uses the OPS-### refinement namespace
**Status:** Accepted
Phase 007 operational/topology/change/impact/control refinement contracts will use `OPS-###`, beginning with OPS-001 when Group 01 starts. OPS identifiers do not create an Operations concept or extend SYN/REF/AUTH/HLTH ranges.

### D-408 — Historical Lineage topology is refined before change, Impact or control behavior
**Status:** Accepted
Operational reasoning must first establish relationship class, relevance, effective interval and evidence limitations. Current/planned topology cannot substitute for incident-time topology, and Lineage remains below causality and status propagation.

### D-409 — Change realization and prospective blast radius are separate groups
**Status:** Accepted
Change Intent→Deployment→realized Change answers whether intended state actually became active. Prospective blast radius reasons over proposed change and topology before activation. Planned risk/reachability must not be confused with realized exposure/Impact.

### D-410 — Execution reconstruction precedes Investigation localization
**Status:** Accepted
Investigation should consume evidenced actual run/dependency/version sequence rather than treating intended schedules or static Lineage as runtime history. Missing/late/duplicate telemetry remains explicit under Phase 004 evidence rules.

### D-411 — First-deviation localization remains below causal claim status
**Status:** Accepted
Investigation can localize a first relevant deviation and organize competing hypotheses, but Lineage, temporal proximity, reconciliation and localization do not themselves establish causality. REF-013–REF-020 continue to govern Causal Claim status.

### D-412 — Impact is refined as candidate, encounter, effect and consequence layers
**Status:** Accepted
Prospective candidate/reachability, actual consumer/version encounter/exposure, observed downstream effect, technical/analytical/business consequence and causal attribution remain distinct. Non-exposure requires bounded opportunity/path coverage.

### D-413 — Propagation Safeguard and Execution Gate receive separate operational groups
**Status:** Accepted
Safeguard protects output/consumption propagation while Gate protects downstream execution start/admission. Their state, enforcement, authority and operational effects may interact but must not be merged into one control abstraction.

### D-414 — Control-induced effects are explicit operational/Impact evidence
**Status:** Accepted
Gate/safeguard behavior may intentionally create delay, skipped execution, stale safe-version serving or non-delivery. Those effects remain observable/assessable and can support Impact/Causal Claim reasoning, but control action alone does not make them defects or establish causality.

### D-415 — Historical operational replay is the final Phase 007 composition test
**Status:** Accepted
Group 09 replays then-effective topology, change, execution, Investigation, Impact, safeguard and gate state under event/effective time plus knowledge cut. Actual historical state, as-known-then reconstruction and present retrospective interpretation remain distinct.

### D-416 — Phase 007 grouping selects no technical architecture
**Status:** Accepted
The grouping does not select graph storage, event persistence, CI/CD ingestion, scheduler/orchestrator, safeguard implementation, gate mechanism, polling/events, cache/streaming strategy, RCA algorithm, source integration or concrete latency/timeout targets.

### D-417 — Phase 007 is planned but Group 01 has not started
**Status:** Accepted
The nine-group plan and OPS namespace are accepted. No OPS contract has yet been accepted. Group 01 — Lineage Relationship Taxonomy, Historical Topology & Operational Relevance is next and must begin only on explicit user direction.
