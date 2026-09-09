# Decision Records — Phase 004 Group 02 Event/Effective Time, Knowledge Cut & Correction

This file continues the durable decision sequence after D-097 in [`phase_004_group_01_evidence_sufficiency_and_coverage.md`](phase_004_group_01_evidence_sufficiency_and_coverage.md).

### D-098 — Temporal evidence coordinates remain distinct when they affect truth

**Status:** Accepted — Phase 004 Group 02

Event/effective time, source production/observation time, source availability time, framework collection/retrieval time, framework recorded/knowledge time, derived evaluation time, and correction/supersession time are distinct where their difference changes historical or operational interpretation. Not every source must expose every timestamp, but missing coordinates cannot be silently substituted with another timestamp.

### D-099 — Source availability is not framework knowledge

**Status:** Accepted — Phase 004 Group 02

A fact may exist and be queryable at a source before the monitoring framework has collected/recorded it. `As-known` framework replay uses framework recorded/knowledge time. Source availability may be analyzed separately when sufficiently evidenced, but it does not backdate framework knowledge.

### D-100 — Historical knowledge-cut eligibility requires knowledge by the cutoff

**Status:** Accepted — Phase 004 Group 02

For event/window `T` and knowledge cutoff `K`, evidence can contribute to the framework's `as-known` cut only when it is applicable to `T` and its framework knowledge time is at or before `K`; correction/supersession state used in the cut must also be known by `K`. Current retrieval of an old fact does not make it historical framework knowledge.

### D-101 — `Known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` are separate claims

**Status:** Accepted — Phase 004 Group 02

These claims have different evidence requirements. In particular, `not known by K` is a negative epistemic claim requiring sufficient coverage of the relevant framework knowledge/retention opportunities. Absence from the retained record alone is insufficient when collection or retention coverage is incomplete.

### D-102 — Monitoring analysis may mature progressively as evidence becomes available

**Status:** Accepted — Phase 004 Group 02

The framework should produce the narrowest trustworthy result as soon as the evidence required for that conclusion is available rather than forcing quick operational validation to wait for every slower health/RCA/post-ops evidence source. Early results remain explicitly scoped to their proposition, knowledge cutoff, and limitations.

### D-103 — Fast-path availability may not promote a narrower fact into a broader health conclusion

**Status:** Accepted — Phase 004 Group 02

An immediately available `job succeeded` fact is not `pipeline healthy` while freshness/quality evidence is pending. Likewise, latency objectives cannot waive evidence standards for gate admission, safeguard actions, causal confirmation, or other high-consequence conclusions.

### D-104 — Functional analytical horizons are accepted; concrete latency targets remain deferred

**Status:** Accepted — Phase 004 Group 02

The project recognizes immediate operational validation, enriched health evaluation, investigative/RCA reasoning, and retrospective/post-operations review as useful functional horizons. These are not architecture/service tiers or fixed SLAs. Phase 006 will define health-result timing needs; Phase 009 will evaluate source availability characteristics; Phase 010 will set architectural performance budgets; Phase 011 will turn accepted targets into MVP acceptance criteria.

### D-105 — Late evidence, source correction, independent conflict, reinterpretation, and later authority resolution are distinct

**Status:** Accepted — Phase 004 Group 02

A newer fact is not automatically a correction. Explicit source correction/supersession preserves the prior source state. Independent disagreement remains conflict until resolved. A changed Assessment or causal interpretation does not mutate its underlying source evidence. Later source-authority resolution has its own time and is not backdated.

### D-106 — Correction and reevaluation are non-rewriting

**Status:** Accepted — Phase 004 Group 02

Late/corrected evidence may change the current retrospective conclusion with a later knowledge/evaluation time. It does not rewrite earlier framework knowledge, actual historical gate/safeguard actions, prospective knowledge, or retained historical communications.

### D-107 — Dependent re-evaluation is basis- and materiality-driven

**Status:** Accepted — Phase 004 Group 02

New/corrected evidence triggers reevaluation only where it bears materially on a retained conclusion's basis, applicability, contradiction set, or coverage. Unrelated evidence does not force global reprocessing. A basis can be affected while a conclusion remains demonstrably unchanged; that distinction remains traceable.

### D-108 — Closed Investigations may become review/reopen candidates but are not automatically reopened

**Status:** Accepted — Phase 004 Group 02

Material evidence that undermines a closed Investigation's core outcome, causal basis, Impact conclusion, or other high-consequence statement can create a review/reopen candidate. Closure does not immunize conclusions from evidence, but authority/workflow for reopening remains later refinement.

### D-109 — Actual historical state requires evidence that the state/action/communication existed then

**Status:** Accepted — Phase 004 Group 02

A historical Assessment, Causal Claim status, Investigation closure, gate/safeguard action, authorization state, or Explanation is called actual historical state only when provenance-bearing evidence establishes it existed at the relevant knowledge time. Otherwise a current replay may reconstruct the view but must label it replay-derived/reconstructed.

### D-110 — Group 02 exit gate satisfied; Group 03 is next

**Status:** Accepted

REF-006–REF-012 establish temporal coordinates, exact knowledge-cut eligibility, historical epistemic negatives, progressive analytical availability, correction classification, dependent reevaluation/reopen semantics, and actual-versus-reconstructible state. No new Concept or Phase 003 synchronization is required.

**Phase 004 remains active. Group 03 — Causal Epistemics, Confirmation & Multiple Contributors is next and has not started.**
