# Progressive Maturity, Partial Answers, Refresh & Retention

**Canonical key:** `experience.progressive-maturity-retention`

**Kind:** EXPERIENCE CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.EXPL`

**Owns current question:** How may Explanation evolve as evidence, source status, authorization or materiality changes while preserving stable identity and actual prior communication?

**Stable IDs:** EXPL-121–EXPL-140

## Current semantics

### EXPL-121 — Trustworthy Partial-Answer Eligibility
A narrow partial answer is valid when its bounded statements are sufficiently supported and authorized; unresolved sibling subquestions remain explicit rather than delaying all communication.

### EXPL-122 — Evidence Maturity vs Elapsed Time
Explanation maturity follows material evidence/source/authorization/context change; elapsed time, repeated rendering or analyst attention does not strengthen truth.

### EXPL-123 — Stable Statement Identity Across Refresh
Preserve statement proposition identity across wording, detail and basis-visibility changes when subject, predicate, scope, event target and knowledge perspective remain materially the same.

### EXPL-124 — Material Refresh Trigger
Refresh when a material dependency changes, including source truth/status, evidence availability, authorization, materiality, scope or relevant context; recomputation alone is not necessarily material.

### EXPL-125 — No-Op Recomposition & Presentation Delta
Repeated recomposition with unchanged proposition/status/basis meaning is a presentation-only/no-op delta and must not be described as epistemic maturation.

### EXPL-126 — Basis Enrichment Without Automatic Strengthening
New basis can enrich traceability or support detail while leaving statement status unchanged; more evidence items do not automatically strengthen a conclusion.

### EXPL-127 — Contradiction & Conflict Refresh
New contradiction/conflict changes the current Explanation only through source-owned proposition re-evaluation and must preserve unresolved/conflicting states when they remain material.

### EXPL-128 — Correction & Supersession Refresh
Source correction/supersession updates current preferred interpretation prospectively while preserving prior source state, knowledge and communication history.

### EXPL-129 — Derived-Statement Dependency Re-Evaluation
A derived statement re-evaluates its exact dependencies and semantic join logic; upstream change never causes blind transitive status flipping.

### EXPL-130 — Typed Statement Delta Classification
Classify Explanation changes at least as presentation-only, basis, status, scope, materiality or authorization/detail changes so `the answer changed` is not treated as one undifferentiated truth event.

### EXPL-131 — Statement Addition, Removal & Materiality Change
Addition/removal from the current composition reflects current materiality/coverage/projection; removal does not imply false, retracted, resolved or nonexistent unless source semantics establish that.

### EXPL-132 — Authorization-Driven Projection Change
Authorization broadening or narrowing changes visible projection, not internal truth; a newly visible statement is not newly true and a newly hidden one is not false.

### EXPL-133 — Question Lineage & Scope Boundary
Changed subject, conclusion, material scope, event/effective target or knowledge cut creates a different proposition/question lineage rather than a silent refresh of the original statement.

### EXPL-134 — Retained Actual Communication Snapshot
A retained Explanation snapshot is evidence of what was actually communicated for an audience/context/time; it is not timeless source truth.

### EXPL-135 — Non-Overwriting Refresh & Supersession Linkage
Current Explanation may supersede an earlier communication for present use, but predecessor/successor linkage preserves the earlier snapshot rather than overwriting history.

### EXPL-136 — Prior Snapshot vs Current Truth
An authentic prior snapshot can be outdated, restricted or unsuitable for current use while remaining accurate evidence of prior communication.

### EXPL-137 — Partial-Coverage Evolution
Track which bounded subquestions/material statements are answered, unresolved or newly material across refresh without converting coverage into a universal percentage/confidence score.

### EXPL-138 — Explanation Change-Summary Semantics
A change summary may describe exact source/status/basis/scope/authorization transitions but cannot invent generic `confidence improved`, `maturity increased` or causal wording beyond accepted source semantics.

### EXPL-139 — Retained vs Reconstructible Historical Explanation
If an actual prior snapshot is unavailable, retain that absence; a reconstructed as-known-at-cut Explanation must be labeled reconstruction rather than presented as exact prior communication.

### EXPL-140 — Historical/Comparative Handoff
Provide Group 08 stable propositions, retained snapshots, refresh lineage and typed deltas so historical comparison can separate source truth, knowledge, communication and retrospective interpretation.

## Invariants / boundaries

- partial answer validity is proposition bound;
- elapsed time ≠ evidence;
- wording change ≠ semantic maturation;
- basis enrichment ≠ automatic status strengthening;
- derived refresh follows exact dependencies, not transitive propagation;
- removed from current projection ≠ false/retracted;
- authorization change ≠ truth change;
- retained snapshot ≠ timeless truth;
- current correction does not rewrite prior communication;
- reconstructed historical Explanation ≠ actual prior communication;
- no universal maturity/confidence/completeness score.

## Architecture boundary

This contract does not choose persistence stores, snapshot schemas, event buses, refresh schedulers, notifications, retention periods, cache invalidation, streaming/batch architecture, LLM regeneration triggers or UI diff rendering.

## Provenance

- `docs/concepts/phase_008/07_progressive_maturity_partial_answers_refresh_retention/README.md`
- Phase 008 Group 07 accepted EXPL-121–EXPL-140.
