# Phase 008 — Business Questioning and Explanation

**Status:** IN PROGRESS — Groups 01–03 accepted; EXPL-001–EXPL-049 accepted; Group 04 next

## Goal

Refine how the accepted Explanation concept receives a bounded business/operational question, selects the correct source-owned propositions, preserves epistemic/temporal/authorization distinctions, composes evidence-grounded statements for an audience, and evolves as evidence matures without becoming an independent truth source.

Phase 008 consumes the completed functional truth model from Phases 002–007. It must not reopen accepted health, causality, Impact, authority, authorization, Lineage, control, execution, or historical-replay semantics by narrative convenience.

## Refinement namespace

Phase 008 uses **`EXPL-###`** refinement contracts.

`EXPL-###` means business-question and Explanation refinement over accepted concepts. It does **not** create a new `Question`, `Answer`, or answer-statement truth concept by default, does not extend SYN/REF/AUTH/HLTH/OPS ranges, and must not become an umbrella state that absorbs the truth owned by other concepts.

Accepted range so far: **EXPL-001–EXPL-049**.

## Logical delivery grouping

Phase 008 is reviewed in eight dependency-ordered functional groups. The sequence is a reasoning/review strategy, not an implementation decomposition.

### Group 01 — Question Proposition, Intent, Scope & Temporal Perspective
**Status:** **Accepted — EXPL-001–EXPL-012; BQ01-01–BQ01-24 pass.**

Defines the bounded question request, requested conclusion type, subject/entity resolution, scope dimensions, event/effective-time and knowledge-cut semantics, current-versus-historical-versus-retrospective perspective, compound-question decomposition, truth-owner routing, ambiguity handling, answerability/evidence/authorization separation, and negative-question evidence burdens.

No new concept is required. The question remains initiating request context for Explanation rather than a new truth-owning concept.

See [`01_question_proposition_intent_scope_temporal_perspective/README.md`](01_question_proposition_intent_scope_temporal_perspective/README.md).

### Group 02 — Answer Structure, Statement Selection & Basis Traceability
**Status:** **Accepted — EXPL-013–EXPL-028; AS02-01–AS02-30 pass.**

Defines material answer-statement proposition identity, source/epistemic preservation, direct projection versus cross-concept derivation, question-relative statement materiality, answer/context/limitation roles, statement-relative support/contradiction/limitation basis, conclusion-relative sufficiency, duplicate/common-derived evidence discipline, explicit semantic join logic, summary/detail equivalence, safe omission/compression, sibling independence, primary-answer ordering, internal basis inspection, and bounded answer coverage.

No new concept is required. Explanation owns the composed communication only; answer statements remain projections of source-owned or explicitly derived propositions.

See [`02_answer_structure_statement_selection_basis_traceability/README.md`](02_answer_structure_statement_selection_basis_traceability/README.md).

### Group 03 — Health, Change & Execution Question Semantics
**Status:** **Accepted — EXPL-029–EXPL-049; HCE03-01–HCE03-36 pass.**

Defines how operational shorthand resolves into exact execution occurrence/lifecycle/output/currentness/health/structure/comparability/quality/reconciliation/change/intent/deployment/version/sequence/timing/historical propositions without collapsing accepted Phase 006/007 distinctions.

No new concept is required. Explanation translates question wording; Assessment, Observation, Change Intent, Deployment, Change and Execution History retain source truth.

See [`03_health_change_execution_question_semantics/README.md`](03_health_change_execution_question_semantics/README.md).

### Group 04 — Investigation, Causality, Impact, Control & Governance Question Semantics
**Status:** **Next — not started.**

Will refine `why`, root-cause, downstream Impact, consumer exposure, Safeguard, Gate, responsibility, policy/meaning and capability-oriented questions while preserving Investigation/Causal Claim/Impact/control/governance ownership boundaries.

See [`04_investigation_causality_impact_control_governance_question_semantics/README.md`](04_investigation_causality_impact_control_governance_question_semantics/README.md).

### Group 05 — Uncertainty, Conflict, Negative Claims & Epistemic Language
**Status:** Not started.

Will refine answer language for unknown, conflicting, unavailable, restricted, insufficient, not-applicable, negative-evidence and competing-claim states; calibrate uncertainty without inventing universal confidence scores; and prevent narrative wording from strengthening evidence.

See [`05_uncertainty_conflict_negative_claims_epistemic_language/README.md`](05_uncertainty_conflict_negative_claims_epistemic_language/README.md).

### Group 06 — Audience, Authorization, Safe Abstraction & Basis Inspection
**Status:** Not started.

Will refine role/purpose-specific analytical projection, safe abstraction, redaction/omission semantics, cross-audience consistency, authorized basis inspection and inference-risk boundaries without treating audience or presentation as authority.

See [`06_audience_authorization_safe_abstraction_basis_inspection/README.md`](06_audience_authorization_safe_abstraction_basis_inspection/README.md).

### Group 07 — Progressive Maturity, Partial Answers, Refresh & Retention
**Status:** Not started.

Will refine narrow early answers versus broader later answers, partial answer completeness, maturity/change notifications, Explanation refresh, retained snapshots, supersession/linkage and stable facts versus revised derived conclusions.

See [`07_progressive_maturity_partial_answers_refresh_retention/README.md`](07_progressive_maturity_partial_answers_refresh_retention/README.md).

### Group 08 — Historical/Comparative Explanation & Consolidation / Exit Review
**Status:** Not started.

Will refine comparative and historical Explanation over event/effective time and knowledge cuts, incident-time versus retrospective accounts, explanation-diff semantics, current authorized projection, and end-to-end Phase 008 composition/exit.

See [`08_historical_comparative_explanation_consolidation_exit/README.md`](08_historical_comparative_explanation_consolidation_exit/README.md).

## Why this order

1. **Question contract first** — the framework cannot select evidence or answer structure safely until the requested conclusion, subject, scope and temporal perspective are bounded.
2. **Answer structure second** — statement identity and basis traceability must be stable before domain-specific prose rules are refined.
3. **Direct operational question families before inferential families** — health/change/execution questions provide a simpler test of source ownership before causal/Impact/control/governance composition.
4. **Uncertainty after domain semantics** — uncertainty language must preserve the actual states produced by the source concepts rather than invent generic wording first.
5. **Authorization after proposition semantics** — safe abstraction should project an already-valid answer basis, not influence what the underlying conclusion becomes.
6. **Progressive maturity after basis/audience semantics** — refresh behavior needs stable statement identity, epistemic state and disclosure rules.
7. **Historical/comparative replay last** — time-cut composition is the final test that Explanation remains non-rewriting.

## Accepted answer foundation through Group 02

Phase 008 preserves:

**bounded question/subquestion → candidate source-owned propositions → question-relevant/material statement selection → direct projection or explicit cross-concept derivation → statement-level source/epistemic identity → supporting/contradicting/limiting basis → headline/summary/detail composition → internal basis inspection → bounded answer coverage**.

No arrow creates stronger truth automatically.

For answer composition specifically:

- rendered wording ≠ material statement proposition identity;
- statement role/context ≠ truth ownership;
- direct projection ≠ cross-concept derivation;
- juxtaposition ≠ semantic join;
- materiality/ordering ≠ evidence strength/authority;
- supporting/contradicting/limiting basis is statement-relative;
- basis count ≠ confidence and common-derived basis ≠ independent corroboration;
- headline/summary/detail may vary in detail but not epistemic strength;
- omission cannot remove a material qualification when doing so would overstate the answer;
- sibling statements remain independent and do not create one synthetic global answer truth;
- internal statement-to-basis traceability is mandatory even when visible basis disclosure is later restricted;
- answer coverage is subquestion/proposition bound, not a universal completeness/confidence score.

## Accepted Group 03 domain-question discipline

Health/change/execution questions now preserve:

- `ran` ≠ lifecycle success/failure/cancellation;
- execution success ≠ output existence/qualification;
- output existence ≠ current/fresh/healthy/consumed;
- freshness/currentness/current-cycle semantics are use- and opportunity-bound;
- health is dimension/profile/use/context bound rather than a universal scalar property;
- realized schema ≠ structural compatibility ≠ statistical comparability ≠ normative quality;
- Baseline typicality ≠ Expectation outcome;
- warning/severity/waiver ≠ criterion truth;
- reconciliation mismatch ≠ root cause;
- realized Change ≠ Change Intent ≠ Deployment attempt/activation;
- intent-realization match/divergence ≠ health/cause;
- no matching registered intent ≠ proven unplanned change;
- active Deployment ≠ run-specific implementation state;
- latest upstream output ≠ run-specific consumed input;
- retry/restart/rerun/backfill retain distinct source semantics;
- dependency ≠ actual precedence ≠ waiting ≠ consumption;
- expected work/opportunity/Gate state ≠ execution;
- missing telemetry ≠ no run/output/consumption;
- duration/start delay/wait/lateness/currentness are distinct timing propositions;
- timing or deployment proximity ≠ causal attribution;
- current retrospective operational answer ≠ what was known then.

## Accepted Phase 007 handoff

Preserve at minimum:

- actual retained historical state ≠ as-known-at-cut reconstruction ≠ current retrospective interpretation;
- current authorized projection cannot rewrite internal truth;
- candidate/reachable ≠ encounter opportunity ≠ exposed ≠ downstream effect ≠ consequence ≠ causal attribution;
- Investigation lead/localization ≠ Causal Claim;
- `confirmed` Causal Claim remains REF-017 + AUTH-034 governed;
- health/result outcome ≠ evidence suitability ≠ readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Safeguard enforcement ≠ prevented exposure;
- Gate HOLD ≠ failed execution; ADMIT/override/fallback admission ≠ execution/readiness;
- missing/restricted/unavailable evidence is not a negative fact;
- no universal scalar health/confidence/risk/RCA/Impact/control/replay score is accepted.

## Architecture boundary

Phase 008 defines functional questioning and Explanation semantics only. It does not select:

- chat, dashboard, report or notebook UX;
- LLM, template, rule engine, retrieval engine or deterministic/generative composition architecture;
- prompt format, model provider or agent topology;
- visible citation widget/UI;
- search/index/vector/database architecture;
- persistence or snapshot storage implementation;
- notification/event architecture;
- source integrations owned by Phase 009;
- technical architecture owned by Phase 010.

## Later-phase handoff

Phase 009 will map accepted question/Explanation requirements to real source availability, authority, latency, retention, cost and observability. Phase 010 will select implementation architecture only after those integration facts are known.

## Phase direction

**Groups 01–03 are accepted with EXPL-001–EXPL-049. BQ01-01–BQ01-24, AS02-01–AS02-30 and HCE03-01–HCE03-36 pass. Group 04 — Investigation, Causality, Impact, Control & Governance Question Semantics is next.**
