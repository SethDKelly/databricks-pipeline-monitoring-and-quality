# Phase 008 — Business Questioning and Explanation

**Status:** IN PROGRESS — Groups 01–06 accepted; EXPL-001–EXPL-120 accepted; Group 07 next

## Goal

Refine how the accepted Explanation concept receives a bounded business/operational question, selects the correct source-owned propositions, preserves epistemic/temporal/authorization distinctions, composes evidence-grounded statements for an audience, and evolves as evidence matures without becoming an independent truth source.

Phase 008 consumes the completed functional truth model from Phases 002–007. It must not reopen accepted health, causality, Impact, authority, authorization, Lineage, control, execution, or historical-replay semantics by narrative convenience.

## Refinement namespace

Phase 008 uses **`EXPL-###`** refinement contracts.

`EXPL-###` means business-question and Explanation refinement over accepted concepts. It does **not** create a new `Question`, `Answer`, answer-statement, RCA, Impact-summary, control-effectiveness, uncertainty/confidence, audience-projection or governance truth concept by default, does not extend SYN/REF/AUTH/HLTH/OPS ranges, and must not become an umbrella state that absorbs truth owned by other concepts.

Accepted range so far: **EXPL-001–EXPL-120**.

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
**Status:** **Accepted — EXPL-050–EXPL-080; ICG04-01–ICG04-48 pass.**

Defines inferential/governance shorthand decomposition; Investigation lifecycle/leads/localization; causal proposition/role/status/competition/root-cause/negative semantics; Impact candidate/exposure/effect/consequence/aggregation; Safeguard/Gate enforcement/prevention/release/overlap/control-effect questions; and responsibility/meaning/Classification/Policy Context/Capability Authorization/Assertion Authority questions.

No new concept is required. The existing concepts retain truth ownership; Explanation composes their bounded projections without inventing RCA, affected, control-effectiveness, blame, compliance or authority shortcuts.

See [`04_investigation_causality_impact_control_governance_question_semantics/README.md`](04_investigation_causality_impact_control_governance_question_semantics/README.md).

### Group 05 — Uncertainty, Conflict, Negative Claims & Epistemic Language
**Status:** **Accepted — EXPL-081–EXPL-100; UNC05-01–UNC05-40 pass.**

Defines proposition-faithful language for unknown/unresolved, unavailable, insufficient/indeterminate, conflicting, restricted/redacted, stale-for-use, non-comparable, not-applicable, not-evidenced/not-known and evidence-backed negative states; preserves causal/Impact/control/governance-specific vocabulary; and rejects confidence/probability/completeness arithmetic.

No new concept is required. Source concepts retain their result/evidence states; Explanation communicates them without reassuring narrative completion.

See [`05_uncertainty_conflict_negative_claims_epistemic_language/README.md`](05_uncertainty_conflict_negative_claims_epistemic_language/README.md).

### Group 06 — Audience, Authorization, Safe Abstraction & Basis Inspection
**Status:** **Accepted — EXPL-101–EXPL-120; AUD06-01–AUD06-44 pass.**

Defines requester/target-audience/purpose/delivery binding; separate conclusion/context/limitation/basis/provenance/detail visibility; epistemically monotone safe abstraction; identity/value/Lineage/inferential/governance abstraction; opaque-existence and material-limitation rules; mixed-authorization derived statements; requester-specific `inspectBasis`; mosaic/repeated-query inference risk; cross-audience consistency; high-consequence communication release; and historical/current authorization separation.

No new concept is required. Capability Authorization and AUTH-044–AUTH-053 own permission/disclosure truth; Explanation owns the composed projection and retained communication only.

See [`06_audience_authorization_safe_abstraction_basis_inspection/README.md`](06_audience_authorization_safe_abstraction_basis_inspection/README.md).

### Group 07 — Progressive Maturity, Partial Answers, Refresh & Retention
**Status:** **Next — not started.**

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
- internal statement-to-basis traceability is mandatory even when visible basis disclosure is restricted;
- answer coverage is subquestion/proposition bound, not a universal completeness/confidence score.

## Accepted Group 03 domain-question discipline

Health/change/execution questions preserve:

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

## Accepted Group 04 inferential/governance discipline

Investigation/causality/Impact/control/governance questions preserve:

- Investigation lifecycle/lead/localization ≠ Causal Claim;
- first observed/earliest evidenced/boundary/consumer effect ≠ root cause;
- causal role and status remain explicit; `confirmed` retains REF-017 + AUTH-034 requirements;
- multiple causal claims can remain competing or compatible without one narrative winner;
- `root cause` singular wording does not force singular causal truth;
- candidate/reachable ≠ opportunity ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- `affected` resolves to a specific Impact layer and strong all/none claims retain population/coverage burden;
- Safeguard lifecycle/admin facts ≠ enforcement ≠ REF-028 prevention ≠ post-release recovery;
- readiness ≠ Gate decision ≠ Gate enforcement ≠ execution;
- HOLD ≠ failed execution; ADMIT ≠ run; override/fallback/escalation/degraded control remain distinct;
- Gate and Safeguard remain independent controls;
- broader control-effect statements remain Causal Claims except the accepted narrow prevented-exposure determination;
- Responsibility Assignment ≠ fault/cause/Assertion Authority/Capability Authorization;
- Semantic Definition ≠ realized state/health/policy/authorization;
- Classification ≠ Policy Context/authorization/Impact/compliance;
- Policy Context ≠ enforcement/legal interpretation/compliance;
- Capability Authorization ≠ responsibility/authority/action success;
- Assertion Authority ≠ factual truth/evidence sufficiency/permission/enforcement.

## Accepted Group 05 epistemic-language discipline

Explanation preserves:

- unknown/unresolved ≠ false/absent/safe;
- unavailable source/evidence condition ≠ proposition-level negative truth;
- insufficient evidence/indeterminate ≠ weak positive or weak negative;
- evidence conflict, authoritative assertion conflict, authority-rule conflict, authorization conflict and competing causal claims remain distinct;
- restricted/redacted/opaque ≠ unavailable/absent;
- stale-for-use ≠ violation by default;
- non-comparable ≠ not applicable;
- `not evidenced`, `not recorded`, `not known by cutoff` and evidence-backed absence remain distinct;
- absence of evidence ≠ evidence of absence;
- strong negative conclusions retain conclusion-specific REF/HLTH/OPS/AUTH opportunity/coverage burdens;
- positive conclusions use source status rather than invented confidence/probability adjectives;
- causal statuses remain proposed/supported/weakened/unresolved/rejected/confirmed without promotion;
- Impact unknown/non-exposure/no-effect/no-consequence remain distinct;
- degraded control telemetry does not prove fail-open/fail-closed;
- missing responsibility/classification/policy/authorization/authority context does not silently become a benign/default state;
- competing claims remain multiple absent accepted resolution;
- material limitations constrain headlines as well as detail;
- sibling statements retain independent epistemic states;
- no universal confidence/probability/completeness/RCA/answer-quality score is accepted;
- historical epistemic state remains separate from current retrospective resolution.

## Accepted Group 06 audience/authorization discipline

Explanation projection now preserves:

- audience/purpose/delivery labels as context rather than permission;
- requester visibility ≠ permission to disclose to another target audience;
- private inspection ≠ export/forward/publish/client disclosure;
- conclusion visibility ≠ context/limitation/basis/provenance/exact-detail visibility;
- internal statement-to-basis traceability even when visible basis is restricted;
- safe abstraction as epistemically monotone rather than declassification;
- exact/coarse/redacted/generalized/opaque/withheld projection only when independently authorized and semantically valid;
- alias/generalization without merging materially distinct subject scope;
- value/threshold/schema abstraction without inventing severity/health;
- Lineage abstraction without inventing directness/completeness/exposure;
- causal/Impact/control/governance abstraction without blame/compliance/prevention shortcuts;
- restricted/omitted ≠ absent, with opaque existence itself separately governed;
- material hidden limitations constraining or withholding the visible conclusion;
- no new coarse inference synthesized from otherwise hidden evidence;
- `inspectBasis` as a separately authorized projection whose metadata can itself be sensitive;
- visible citation/reference ≠ permission to inspect source;
- mosaic/differencing/repeated-query risk as compositional;
- cross-audience consistency over one truth without identical detail;
- communication review/release ≠ truth/evidence authority;
- historical actor authorization, retained prior communication and current requester disclosure as separate.

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

**Groups 01–06 are accepted with EXPL-001–EXPL-120. BQ01-01–BQ01-24, AS02-01–AS02-30, HCE03-01–HCE03-36, ICG04-01–ICG04-48, UNC05-01–UNC05-40 and AUD06-01–AUD06-44 pass. Group 07 — Progressive Maturity, Partial Answers, Refresh & Retention is next.**
