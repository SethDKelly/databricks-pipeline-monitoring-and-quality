# Integration Contract Vocabulary, Source Roles & Capability Matrix

**Canonical key:** `integration.group-01`

**Kind:** INTEGRATION CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.INTG`

**Stable IDs:** INTG-001–INTG-022

**Owns current question:** What can an exact source surface actually evidence for a bounded accepted proposition, under what authority, join, temporal, coverage, replay, disclosure and operational constraints?

## Canonical contract

Every source review preserves the chain:

**exact source surface + semantic/version context → bounded accepted proposition → evidence role → authority applicability → identity/join contract → temporal coordinates → grain/context → positive capability → negative/opportunity/coverage capability → availability/latency → retention/replay → mutation/correction → disclosure → derivation/independence → quota/cost → integration observability → support classification + residual gaps**.

No arrow creates stronger truth automatically.

Preserve:

- product/vendor name ≠ exact source surface;
- source availability ≠ relevance ≠ eligibility ≠ authority ≠ sufficiency ≠ disclosure authorization;
- source role ≠ Assertion Authority or standing;
- source-local identity/name ≠ ecosystem Entity Identity;
- timestamp proximity ≠ exact cross-system association;
- event/effective time ≠ recorded time ≠ first reliable availability/knowledge time ≠ retrieval time;
- aggregate/asset grain ≠ narrower proposition grain;
- positive-event support ≠ negative-evidence capability;
- no returned record ≠ absence without opportunity, sufficient coverage and source health;
- one path/population/mode coverage ≠ global completeness;
- current-state availability ≠ historical replay capability;
- late/backfilled evidence now ≠ evidence available at an earlier knowledge cut;
- destructive mutation or missing history may make replay unsupported rather than reconstructible by assumption;
- multiple endpoints ≠ independent corroboration when commonly derived;
- fallback availability ≠ inherited authority;
- source conflict ≠ hidden winner;
- quota/cost may constrain feasible coverage but cannot rewrite truth;
- integration failure ≠ monitored-product negative.

Accepted support classes are `supported`, `partially supported`, `unsupported`, `unknown / not yet verified`, and `not applicable`. They are integration-feasibility outcomes, not truth, confidence, completeness, health or quality states. No vendor-wide support/completeness score exists.

## Stable contracts

### INTG-001 — Source Surface Capability Identity & Version Context
Bind capability claims to the exact API/table/event/query/export/object surface and material edition/version/semantic context; a product name alone is never sufficient source identity.

### INTG-002 — Proposition Binding & Truth-Owner Boundary
Every capability row binds a source to a specific accepted proposition while the accepted concept remains truth owner; integration convenience cannot create a new truth model.

### INTG-003 — Evidence Role Taxonomy & Source Assertion Type
Classify observational, declarative, normative/reference, operational-action, relationship, authorization, contextual and derived/projection roles without treating the role as authority or sufficiency.

### INTG-004 — Authority Applicability & Standing Boundary
Determine authority for the exact proposition/category/context/time under accepted AUTH rules; source prominence, recency, count or availability creates no standing.

### INTG-005 — Relevance, Sufficiency, Eligibility & Authorization Separation
Evaluate relevance, conclusion-specific sufficiency, knowledge-cut eligibility, authority and disclosure authorization independently.

### INTG-006 — Access, Retrieval & Disclosure Capability
Distinguish whether evidence exists, can be retrieved internally and may be disclosed to the current requester/audience/purpose; one does not imply the others.

### INTG-007 — Subject Identity & Join Contract
Bind source-local subjects to accepted Entity Identity using explicit identifiers/crosswalk evidence and preserve unresolved identity where exact mapping is unavailable.

### INTG-008 — Cross-System Association Strength & Join Evidence
Require explicit association evidence for deployment↔run, run↔version, consumer↔state and decision↔enforcement joins; names, actors and timestamp proximity are insufficient.

### INTG-009 — Temporal Coordinate Contract
Keep event/effective, source-recorded/committed, correction/supersession, reliable availability and retrieval times distinct, including precision, timezone and skew limits when ordering matters.

### INTG-010 — Granularity, Cardinality & Context Binding
Preserve source grain, cardinality and material context; asset-level evidence cannot silently answer field-, run-, consumer-, path- or version-specific propositions.

### INTG-011 — Positive Evidence Capability
Record exactly which positive propositions the source can establish and under what coverage/context, without extrapolating to stronger sibling conclusions.

### INTG-012 — Negative Evidence Capability & Opportunity Coverage
Strong negatives require bounded opportunity/population/path/window plus sufficient collection/query coverage and source health; `no record` alone is not absence evidence.

### INTG-013 — Coverage, Completeness & Observable Population Boundary
State the actual observable population/mode/path/workspace/time/event class and never convert bounded coverage into universal completeness.

### INTG-014 — Availability, Latency, Freshness & Knowledge Eligibility
Treat source publication/collection latency as evidence-availability and knowledge-cut eligibility, not as a change to event/effective truth.

### INTG-015 — Retention, Historical Replay & Snapshot Capability
Evaluate historical replay from actual retained history/snapshots and retention horizons; current state is not automatically historical state.

### INTG-016 — Mutation, Correction, Backfill, Deletion & Supersession
Preserve source mutation/correction/backfill/deletion semantics so current retrospective evidence does not rewrite what existed or was knowable earlier.

### INTG-017 — Duplicate, Common Derivation & Independence
Track common derivation across APIs/exports/replicas so duplication does not become independent corroboration.

### INTG-018 — Conflict, Fallback & Source-Precedence Boundary
Keep source conflict explicit absent accepted evidence/authority resolution; fallback or later synchronization does not create precedence or inherited authority.

### INTG-019 — Support Classification & Residual Gap Taxonomy
Classify integration feasibility proposition-by-proposition and record residual gaps explicitly; unsupported/unknown is a valid finding and never permission to weaken accepted semantics.

### INTG-020 — Quota, Rate, Cost & Operational Constraints
Record quotas, rates, volumes and cost where they affect feasible coverage/latency while keeping them separate from evidence authority and truth.

### INTG-021 — Integration Observability & Failure-State Evidence
Distinguish source absence from authentication failure, permission denial, throttling, pagination failure, API/schema drift, parser failure, delayed indexing, retention expiry and source outage.

### INTG-022 — Capability Matrix Composition & Group 02 Handoff
Compose source capability only from explicit proposition-bound rows and residual gaps; later source families inherit this matrix discipline rather than vendor reputation or convenience.

## Architecture boundary

This contract selects no adapter interfaces, SDKs, ingestion jobs, schemas, queues, polling/streaming, caches, credentials, persistence or deployment topology.

## Provenance

- `docs/concepts/phase_009/01_integration_contract_vocabulary_source_roles_capability_matrix/README.md`
- Phase 009 Group 01 accepted INTG-001–INTG-022.
