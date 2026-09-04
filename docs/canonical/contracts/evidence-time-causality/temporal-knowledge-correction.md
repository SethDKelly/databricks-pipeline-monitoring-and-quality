# Temporal Knowledge, Historical Cuts & Correction

**Canonical key:** `ref.temporal-knowledge-correction`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.REF`

**Owns current question:** Which evidence and interpretations are eligible at a historical knowledge cut, and how do late/corrected facts revise current retrospective understanding without rewriting history?

**Stable IDs:** REF-006–REF-012

## Current semantics

### REF-006 — Temporal Coordinates and Evidence Availability
Where material, distinguish event/effective time, source observation/production time, source availability, collection/retrieval, framework recorded/knowledge time, derived evaluation time and correction/supersession time. Coincidence does not make them interchangeable.

### REF-007 — Historical Knowledge-Cut Eligibility
For event/window T and knowledge cutoff K, evidence contributes to an `as-known` view only when applicable to T and recorded/known by the framework at or before K. Later retrieval of old source facts does not backdate framework knowledge.

### REF-008 — Known By, Learned After, and Not Known By Claims
`known by K`, `learned after K`, `not recorded by K`, `not known by K`, and `not available by K` are distinct propositions. Negative epistemic claims require sufficient record/opportunity/retention coverage.

### REF-009 — Progressive Evidence Availability and Analytical Maturity
The system may emit the narrowest trustworthy result as soon as that result's evidence burden is met. Faster availability never upgrades scope: execution success can be known while freshness/quality remain pending; proposed/supportable RCA can mature later without status inflation.

### REF-010 — Late Evidence, Correction, Conflict, and Reinterpretation
Late arrival, source correction/supersession, independent conflict, semantic reinterpretation/reassessment and later authority resolution remain distinct. Only accepted correction semantics supersede earlier source state for current use.

### REF-011 — Dependent Re-evaluation and Investigation Reopen Materiality
New/corrected evidence triggers reevaluation only when it materially bears on a retained conclusion's basis, applicability, contradiction set or coverage. Material challenges can create review/reopen candidates; closure does not immunize prior conclusions.

### REF-012 — Actual Retained State versus Reconstructible Historical State
Historical Assessment, claim, Investigation, authorization/control action or Explanation is `actual historical state` only when evidence establishes it existed then. Otherwise replay is a current reconstruction over the historical cut and must be labeled accordingly.

## Invariants / boundaries

- event/effective time ≠ knowledge/record time;
- source availability ≠ framework knowledge;
- historically known inputs ≠ historically produced interpretation;
- later evidence/correction cannot rewrite what was known, decided, enforced or communicated then;
- current retrospective truth and as-known-at-K truth may legitimately differ.

## Synchronizations / related canonical resources

Applies across all temporal concept histories and SYN historical replay. Later AUTH rules also use effective and knowledge time but do not alter REF temporal eligibility.

## Provenance

- `docs/concepts/phase_004/02_event_time_knowledge_cut_and_correction/README.md`
- Phase 004 Group 02 accepted REF-006–REF-012.
