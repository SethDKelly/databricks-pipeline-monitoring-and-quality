# Phase 008 Agent Handoff

Applies to work under `docs/concepts/phase_008/` and complements the repository root `AGENTS.md`.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 007 is complete with OPS-001–OPS-123 final.
- Phase 008 grouping is accepted.
- **Group 01 is complete with EXPL-001–EXPL-012; BQ01-01–BQ01-24 pass.**
- **Group 02 — Answer Structure, Statement Selection & Basis Traceability is next.**
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

## Permanent Phase 008 boundaries

Preserve throughout the phase:

- Explanation ≠ independent truth source;
- question intent ≠ evidence;
- question family ≠ source authority;
- wording ≠ proposition identity;
- audience ≠ authority;
- requested conclusion ≠ supported conclusion;
- summary ≠ stronger epistemic status;
- omission/redaction ≠ absence;
- authorized abstraction ≠ declassification by inference;
- statement basis ≠ visible raw evidence requirement for every audience;
- Observation ≠ Assessment ≠ Change Intent ≠ realized Change ≠ Causal Claim ≠ Impact ≠ Annotation;
- reachability ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- current retrospective Explanation ≠ what was known then;
- retained Explanation snapshot ≠ current source truth;
- progressive maturity ≠ automatic status strengthening;
- no universal Explanation confidence/completeness/quality score unless a later contract explicitly establishes a bounded non-truth-owned presentation metric without violating accepted score prohibitions.

## Group 02 entry contract

Group 02 consumes EXPL-001–EXPL-012 and should refine how an answer is composed once the bounded question is known.

It should explicitly test:

- material statement identity and type;
- direct source-owned statement versus derived cross-concept statement;
- statement-to-basis linkage and basis multiplicity;
- supporting versus contradicting basis where applicable;
- answer headline/summary versus detail/drill-down without status strengthening;
- what belongs in a minimal answer versus optional context;
- basis inspection when underlying evidence is unavailable/restricted to the requester;
- multiple independent statements in one answer without hidden composite status;
- conflicting or partially answerable statements remaining separate;
- causal/Impact/control statements retaining their source epistemic state;
- machine-generated or human-authored prose origin not becoming authority;
- stable internal proposition identity despite different presentation wording.

Do not choose rendering/UI/citation widgets, LLM/template architecture, prompt format, retrieval store or persistence architecture.
