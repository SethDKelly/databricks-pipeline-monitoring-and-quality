# Phase 008 Agent Handoff

Applies to work under `docs/concepts/phase_008/` and complements the repository root `AGENTS.md`.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 007 is complete with OPS-001–OPS-123 final.
- Phase 008 grouping is accepted.
- **Group 01 is complete with EXPL-001–EXPL-012; BQ01-01–BQ01-24 pass.**
- **Group 02 is complete with EXPL-013–EXPL-028; AS02-01–AS02-30 pass.**
- **Group 03 is complete with EXPL-029–EXPL-049; HCE03-01–HCE03-36 pass.**
- **Group 04 — Investigation, Causality, Impact, Control & Governance Question Semantics is next.**
- Accepted concept count remains 24.

## Accepted Group 01 rules

Preserve:

- no new Question concept is required; the bounded question is initiating request context for Explanation;
- question request identity binds requested conclusion, subject(s), scope, temporal perspective and relevant request/audience/purpose context;
- question family is routing/answer-contract metadata, not a truth state, authority rule or proof standard by itself;
- natural-language wording equality does not define question identity and wording difference does not always imply a different proposition;
- subject resolution uses Entity Identity and keeps environment/version/consumer/run/cohort distinctions explicit;
- unresolved identity ambiguity remains ambiguity rather than guessed target selection;
- event/effective time and recorded/knowledge cut are independent coordinates;
- a historical question with no explicit knowledge cut is current retrospective interpretation and must be labeled as such rather than implied contemporaneous knowledge;
- compound questions decompose into independently answerable subquestions when their truth owners/evidence burdens differ;
- one answered subquestion cannot strengthen an unresolved sibling;
- each requested conclusion routes to the concept(s) that own that proposition; Explanation never becomes the source of health, cause, Impact, control, governance or authorization truth;
- `why`/causal wording requires Causal Claim semantics when the answer asserts causality;
- asking for a fact does not authorize access to it;
- answerability ≠ evidence availability ≠ semantic applicability ≠ authorization/disclosure ≠ source integration support;
- partial answerability is valid and should be explicit;
- materially ambiguous/underspecified questions must preserve ambiguity or bounded interpretations instead of silently choosing the most convenient one;
- broad shorthand such as `healthy`, `okay`, `affected`, `safe`, `blocked`, `owned`, `planned` or `why` must resolve to the accepted underlying proposition before being answered;
- a negative-form question does not lower the REF evidence burden for a negative answer;
- missing evidence cannot become `no run`, `no impact`, `no path`, `no exposure`, `no effect`, `no control action`, `unplanned`, or other strong negative by wording convenience.

See [`01_question_proposition_intent_scope_temporal_perspective/README.md`](01_question_proposition_intent_scope_temporal_perspective/README.md).

## Accepted Group 02 rules

Preserve:

- no new Answer/Statement truth concept is required; material answer statements remain Explanation projections;
- rendered sentence wording ≠ material statement proposition identity;
- statement proposition identity preserves source conclusion, subject, material scope and temporal/knowledge perspective;
- source truth owner and epistemic type survive composition;
- direct source projection and derived cross-concept statement are distinct;
- a derived statement requires explicit accepted join logic and sufficient basis for the derived proposition;
- juxtaposition/prose adjacency does not create causality, exposure, prevention, health or control truth;
- statement materiality is question relative and does not become evidence strength;
- answer-bearing/context/limitation are presentation roles, not new epistemic categories;
- material limitations cannot be omitted when omission would overstate the conclusion;
- supporting, contradicting and limiting basis roles are statement relative;
- evidence sufficiency is conclusion relative;
- duplicate/common-derived basis ≠ independent corroboration;
- basis count ≠ confidence and no arithmetic confidence rule is accepted;
- cross-concept answer composition is not generally transitive;
- headline/summary/detail may differ in detail but not proposition scope, polarity or epistemic strength;
- a summary may say less but cannot imply more;
- omission ≠ evidence of absence;
- sibling answer statements remain independently traceable and one cannot strengthen another;
- no synthetic overall answer/incident/root-cause/Impact/control truth is created for narrative convenience;
- answer ordering/primary-answer selection is question/context specific and creates no hidden authority/score;
- internal statement-to-basis traceability is mandatory;
- visible basis disclosure is separate and belongs to Group 06;
- answer coverage is proposition/subquestion bound rather than a universal completeness/confidence score.

See [`02_answer_structure_statement_selection_basis_traceability/README.md`](02_answer_structure_statement_selection_basis_traceability/README.md).

## Accepted Group 03 rules

Preserve:

- operational shorthand resolves to exact accepted propositions rather than a universal status;
- `did it run?` is separate from lifecycle success/failure/cancellation;
- execution success is separate from output existence/qualification;
- output existence is separate from currentness/freshness/health/downstream use;
- freshness/currentness/current-cycle questions bind exact temporal/use rules rather than latest-run shortcuts;
- `is it healthy?` requires explicit dimension/profile/use/context semantics;
- realized structure, compatibility, statistical comparability and normative quality remain separate;
- Baseline typicality does not become Expectation health;
- warning/proximity/severity/priority/waiver do not rewrite criterion truth;
- reconciliation result does not become Causal Claim;
- `what changed?` routes to realized Change;
- `was it planned?` binds exact Change Intent revision/component;
- no matching registered intent does not prove unplanned change;
- Deployment attempt/outcome, activation and downstream effect remain separate;
- intent-to-realization matched/diverged does not establish health or cause;
- run-specific implementation/input/output versions require Execution History binding;
- active Deployment does not automatically establish run-specific version use;
- latest upstream output does not establish consumed input;
- retry/restart/rerun/backfill preserve source-specific continuity semantics;
- dependency, expected order, actual precedence, waiting and consumption remain separate;
- expected work/opportunity/Gate state does not manufacture execution;
- strong no-run/no-output/no-consumption claims retain negative-evidence coverage burden;
- duration, start delay, wait interval, delivery lateness and freshness/currentness are distinct;
- timing/overlap does not establish causality;
- historical health/change/execution answers preserve event/effective time and knowledge cut;
- direct domain statements can support Group 04 but cannot become causality/Impact/control/governance truth by composition.

See [`03_health_change_execution_question_semantics/README.md`](03_health_change_execution_question_semantics/README.md).

## Permanent Phase 008 boundaries

Preserve throughout the phase:

- Explanation ≠ independent truth source;
- question intent ≠ evidence;
- question family ≠ source authority;
- wording ≠ proposition identity;
- answer statement ≠ independent truth state;
- direct projection ≠ derived cross-concept proposition;
- answer materiality/ordering ≠ evidence strength/authority;
- basis count ≠ confidence;
- summary ≠ stronger epistemic status;
- omission/redaction ≠ absence;
- audience ≠ authority;
- authorized abstraction ≠ declassification by inference;
- internal statement basis ≠ visible raw evidence requirement for every audience;
- Observation ≠ Assessment ≠ Change Intent ≠ Deployment ≠ realized Change ≠ Execution History ≠ Causal Claim ≠ Impact ≠ Annotation;
- run success ≠ output existence/currentness/health;
- structural compatibility ≠ statistical comparability ≠ normative health;
- active Deployment ≠ run-specific version use;
- timing/Lineage/reconciliation/change proximity ≠ causality;
- reachability ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- current retrospective Explanation ≠ what was known then;
- retained Explanation snapshot ≠ current source truth;
- progressive maturity ≠ automatic status strengthening;
- no universal Explanation confidence/completeness/quality/operational-status score.

## Group 04 entry contract

Group 04 consumes EXPL-001–EXPL-049 and applies the accepted question/answer/domain structure to Investigation, causality, Impact, control and governance propositions.

It should explicitly test:

- `why did this happen?`, `what is the root cause?`, `what contributed?`, and unresolved-cause questions;
- Investigation lead/localization versus Causal Claim status;
- supported/rejected/confirmed competing causal claims without narrative winner selection;
- downstream candidate/reachability versus actual encounter/exposure/effect/consequence;
- `who was affected?` and strong `nobody was affected` coverage burdens;
- Safeguard proposal/authorization/request/enforcement/prevented-exposure/release/recovery distinctions;
- Gate configuration/readiness/decision/delivery/enforcement/execution/control-effect distinctions;
- `did the control prevent the problem?` versus control overlap;
- responsibility/ownership versus fault/cause/authorization;
- Semantic Definition/Policy Context/Classification versus compliance conclusions;
- Capability Authorization versus responsibility/policy/assertion authority;
- business consequence versus technical/analytical effect;
- causal attribution from control/change/exposure facts only through accepted Causal Claim semantics;
- historical/restricted questions without current-disclosure or retrospective strengthening shortcuts.

Do not reopen Phase 005/007 truth semantics, select UI/rendering/LLM architecture, or create a universal RCA/Impact/control/governance score.
