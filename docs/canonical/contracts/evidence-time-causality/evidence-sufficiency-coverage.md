# Evidence Sufficiency, Coverage & Negative Evidence

**Canonical key:** `ref.evidence-sufficiency-coverage`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.REF`

**Owns current question:** What evidence may support a bounded proposition, especially strong negative or exclusion conclusions?

**Stable IDs:** REF-001–REF-005

## Current semantics

Evidence evaluation is proposition-relative. Applicability, opportunity/coverage, independence/conflict, and conclusion-specific sufficiency are separate questions; no universal evidence-confidence or trust score is accepted.

### REF-001 — Evidence Applicability and Proposition Binding
Evidence bears on a conclusion only when subject, property, context, event window, grain/version and conclusion scope align sufficiently. A fact applicable to one proposition cannot be reused to prove a broader one by convenience.

### REF-002 — Coverage Profile and Opportunity to Observe
Coverage describes the bounded observation universe: time, population/partition, source/query scope, version/consumer scope, collection success, sampling/estimation and known gaps. `Complete` is meaningful only relative to that declared universe.

### REF-003 — Negative, Absence, and Exclusion Evidence
A negative conclusion requires a mechanism capable of observing the relevant event/state plus sufficient bounded coverage of the opportunities in which it could occur. Missing, failed, restricted or unavailable telemetry is not evidence of absence.

### REF-004 — Corroboration, Conflict, and Evidence Independence
Supporting, contradicting, duplicated, derived and common-source evidence remain distinguishable. Multiple records from one underlying event do not become independent corroboration. Applicable conflict remains explicit until an accepted authority rule resolves standing.

### REF-005 — Conclusion-Specific Evidence Sufficiency Evaluation
Sufficiency is evaluated for the exact conclusion and applicable standard. The same evidence can prove existence while remaining insufficient for exclusivity, absence, cause, prevention or another stronger claim.

## Invariants / boundaries

- evidence sufficiency ≠ Assertion Authority ≠ Capability Authorization ≠ disclosure permission;
- source count, availability or recency do not create authority or independence;
- missing evidence ≠ zero/false/absence;
- stronger claims require stronger proposition-specific coverage;
- restricted requester visibility does not alter internal evidence relationships, while framework inability to access evidence is an availability limitation.

## Synchronizations / related canonical resources

Uses canonical concept truth from Observation, Assessment, Causal Claim, Impact, Execution Gate and Propagation Safeguard. Temporal specialization continues in REF-006–REF-012.

## Provenance

- `docs/concepts/phase_004/01_evidence_sufficiency_and_coverage/README.md`
- Phase 004 Group 01 accepted REF-001–REF-005 and its scenario checks.
