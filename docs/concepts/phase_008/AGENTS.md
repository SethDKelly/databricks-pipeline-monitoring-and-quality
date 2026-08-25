# Phase 008 Agent Handoff

Applies to work under `docs/concepts/phase_008/` and complements the repository root `AGENTS.md`.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 007 is complete with OPS-001–OPS-123 final.
- Phase 008 grouping is accepted.
- **Group 01 is complete with EXPL-001–EXPL-012; BQ01-01–BQ01-24 pass.**
- **Group 02 is complete with EXPL-013–EXPL-028; AS02-01–AS02-30 pass.**
- **Group 03 — Health, Change & Execution Question Semantics is next.**
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
- Observation ≠ Assessment ≠ Change Intent ≠ realized Change ≠ Causal Claim ≠ Impact ≠ Annotation;
- reachability ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- current retrospective Explanation ≠ what was known then;
- retained Explanation snapshot ≠ current source truth;
- progressive maturity ≠ automatic status strengthening;
- no universal Explanation confidence/completeness/quality score.

## Group 03 entry contract

Group 03 consumes EXPL-001–EXPL-028 and applies the accepted question/answer structure to health/change/execution propositions.

It should explicitly test questions such as:

- `Did it run?` versus `Did it succeed?` versus `Did it produce the expected/current output?`;
- `Is it healthy?` across explicit dimensions/profiles without inventing a universal asset health state;
- freshness/currentness versus latest successful execution;
- schema compatibility versus observed realized schema versus statistical comparability;
- `What changed?` versus `What was intended?` versus `What was deployed/activated?`;
- intent-to-realization comparison without turning match/divergence into health or cause;
- `Which version/configuration was used?` from run-specific execution evidence rather than active Deployment by convenience;
- retry/restart/rerun/backfill distinctions;
- actual dependency sequence/waiting/consumption versus expected schedule/dependency;
- current versus historical execution/health questions under event/effective time + knowledge cut;
- partial/missing telemetry producing partial answers rather than negative facts;
- direct health/execution statements versus cross-concept derived answers preserving EXPL-015/021.

Do not reopen HLTH/OPS semantics, select UI/rendering/LLM architecture, or turn domain shorthand into universal scalar status.
