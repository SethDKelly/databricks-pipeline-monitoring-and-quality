# Phase 004 Group 02 — Event/Effective Time, Knowledge Cut & Correction

**Status:** Accepted

## Goal

Specialize the Group 01 evidence-applicability/coverage/sufficiency framework for exact historical and correction semantics: what evidence is eligible for an `as-known` view, what can legitimately be said to have been known or not known by a cutoff, how results can mature progressively as evidence arrives, and how late/corrected evidence propagates into reevaluation without rewriting contemporaneous history.

## Accepted refinements

1. [`REF-006 — Temporal Coordinates and Evidence Availability`](006_temporal_coordinates_and_evidence_availability.md)
2. [`REF-007 — Historical Knowledge-Cut Eligibility`](007_historical_knowledge_cut_eligibility.md)
3. [`REF-008 — Known By, Learned After, and Not Known By Claims`](008_known_by_learned_after_not_known_by.md)
4. [`REF-009 — Progressive Evidence Availability and Analytical Maturity`](009_progressive_evidence_availability_and_analytical_maturity.md)
5. [`REF-010 — Late Evidence, Correction, Conflict, and Reinterpretation`](010_late_evidence_correction_conflict_reinterpretation.md)
6. [`REF-011 — Dependent Re-evaluation and Investigation Reopen Materiality`](011_dependent_reevaluation_and_reopen_materiality.md)
7. [`REF-012 — Actual Retained State versus Reconstructible Historical State`](012_actual_retained_vs_reconstructible_state.md)

See [`scenario_checks.md`](scenario_checks.md) for accepted timing/correction/progressive-availability scenarios.

## Core temporal model

Where material, the framework distinguishes:

**event/effective time → source production/observation time → source availability time → collection/retrieval time → framework recorded/knowledge time → derived evaluation time**

plus explicit correction/supersession time when later source state changes.

These times may coincide, but they are not semantically interchangeable.

### Source availability is not framework knowledge
A fact can exist and even be queryable in Databricks before the monitoring framework has retrieved it. That fact may support a later retrospective view, but it is not silently inserted into an earlier `as-known` framework cut.

### Framework knowledge is not derived interpretation
Inputs may be known before an Assessment, RCA claim, Impact conclusion, or Explanation is actually produced. A replay-derived interpretation over historically known inputs is still a current reconstruction unless historical state proves the interpretation existed then.

## Exact `as-known` eligibility

For event/window `T` and knowledge cutoff `K`, evidence contributes only when it is applicable to `T` and its framework recorded/knowledge time is at or before `K`. Corrections/supersessions used in the cut must also have been known by `K`.

A current retrieval of an old source record gives the framework current knowledge. It does not backdate the framework's historical knowledge merely because the source record's event time is old.

## Historical epistemic claims

Group 02 distinguishes:

- **known by K** — retained evidence establishes framework knowledge at/before K;
- **learned after K** — relevant evidence entered framework knowledge after K;
- **not recorded by K** — a narrower retained-record statement requiring sufficient record coverage;
- **not known by K** — a stronger negative epistemic statement requiring sufficient opportunity-to-observe/retention coverage;
- **not available by K** — a separate source-availability statement requiring source availability evidence.

Absence from a historical record does not automatically prove absence of knowledge.

## Progressive analytical availability

Monitoring results are allowed to mature in stages as evidence becomes available. The framework should produce the narrowest trustworthy result as soon as that result's evidence standard is satisfied rather than waiting for every slower evidence source.

Provisional functional horizons are:

1. **Immediate operational validation** — run lifecycle, queue/duration, direct dependency/output facts that are already available;
2. **Enriched health evaluation** — freshness, Metric View/DQ, Baseline/Expectation and richer semantic evidence;
3. **Investigative / RCA reasoning** — Lineage, deployment/change, competing Causal Claims, consumption evidence and analyst research;
4. **Retrospective / post-operations review** — late/corrected evidence, completed incident windows and later downstream/consequence evidence.

These horizons are not architecture tiers or fixed latency SLAs. Their exact performance objectives are handed to Phases 006, 009, 010 and 011.

### Critical invariant
`Job succeeded` available immediately must never be promoted into `pipeline healthy` merely because quality evidence has not arrived yet. The correct early state can be `execution succeeded; quality/freshness evidence pending or incomplete`.

Likewise, a high-consequence gate/safeguard/causal decision cannot weaken its evidence standard merely to meet a low-latency objective.

## Later-information classification

Group 02 distinguishes:

- late-arriving evidence;
- source correction/supersession;
- independent conflicting evidence;
- semantic reinterpretation/reassessment;
- later source-authority resolution.

Only explicit accepted correction semantics allow a prior source state to be superseded for current use; independent disagreement remains conflict until resolved.

## Dependent re-evaluation

New/corrected evidence causes reevaluation only where it bears materially on a retained conclusion's basis, applicability, contradiction set, or coverage.

Possible outcomes include:

- no relevant dependency;
- basis affected but conclusion demonstrably unchanged;
- conclusion may change and requires reevaluation;
- high-consequence historical conclusion materially challenged and becomes a review/reopen candidate.

A closed Investigation is not automatically reopened for every late event, but closure never makes its conclusions immune to materially new evidence.

## Retained versus reconstructed historical state

A historical Assessment, claim status, Investigation closure, gate/safeguard action, authorization state, or Explanation may be called **actual historical state** only when provenance-bearing evidence establishes that it existed then.

Otherwise the system may produce a **reconstructed/replay-derived** view from the historical evidence cut, clearly labeled with its current evaluation/generation time.

This distinction allows later architecture to choose selective retention and on-demand replay without pretending reconstructed conclusions were actual historical actions or communications.

## Execution/monitoring timing consideration accepted for later phases

The product must eventually define expected result-availability characteristics for different monitoring products. Group 02 establishes the semantic foundation but does not choose concrete targets.

The handoff is:

- **Phase 006:** define which health dimensions/results need immediate, near-real-time, delayed, or post-ops evaluation and what evidence freshness/latency expectations apply;
- **Phase 009:** evaluate actual source/integration availability characteristics for Databricks jobs, Metric Views, DQX, GitHub/deployment, Lineage, governance, consumption, and other evidence;
- **Phase 010:** select architecture/performance budgets for fast-path versus asynchronous/deeper reasoning while keeping passive monitoring off the ungated production critical path;
- **Phase 011:** translate the selected targets into MVP acceptance criteria.

## Group 02 exit gate

**Satisfied.** REF-006–REF-012 make historical cuts, evidence arrival, progressive analysis, late/corrected evidence, dependent re-evaluation, and retained-versus-reconstructed state explicit without creating a new concept or selecting temporal/storage/performance architecture.

## Handoff to Group 03

Group 03 — **Causal Epistemics, Confirmation & Multiple Contributors** must apply REF-001–REF-012 to:

- exact Causal Claim status vocabulary and transitions;
- what support/contradiction means under coverage/conflict rules;
- what evidence is required before `confirmed` is permissible;
- review/authority boundaries for confirmation;
- multiple contributors/alternatives;
- how later evidence challenges a previously confirmed claim;
- how causal status can mature progressively without early RCA results being overstated.
