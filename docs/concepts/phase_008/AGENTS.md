# Phase 008 Agent Handoff

Applies to work under `docs/concepts/phase_008/` and complements the repository root `AGENTS.md`.

## Current status

Canonical repository phase status is maintained in [`../../README.md#current-state`](../../README.md#current-state).

- Phase 007 is complete with OPS-001–OPS-123 final.
- Phase 008 grouping is accepted.
- **Group 01 is complete with EXPL-001–EXPL-012; BQ01-01–BQ01-24 pass.**
- **Group 02 is complete with EXPL-013–EXPL-028; AS02-01–AS02-30 pass.**
- **Group 03 is complete with EXPL-029–EXPL-049; HCE03-01–HCE03-36 pass.**
- **Group 04 is complete with EXPL-050–EXPL-080; ICG04-01–ICG04-48 pass.**
- **Group 05 is complete with EXPL-081–EXPL-100; UNC05-01–UNC05-40 pass.**
- **Group 06 is complete with EXPL-101–EXPL-120; AUD06-01–AUD06-44 pass.**
- **Group 07 is complete with EXPL-121–EXPL-140; PMR07-01–PMR07-44 pass.**
- **Group 08 — Historical/Comparative Explanation & Consolidation / Exit Review is next.**
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

## Accepted Group 04 rules

Preserve:

- inferential/governance shorthand resolves to exact accepted truth-family propositions;
- Investigation lifecycle/lead/localization do not establish Causal Claim status;
- first observed/earliest evidenced/first boundary/consumer effect are distinct and do not become root cause;
- causal answers bind explicit cause→effect proposition, causal role and source status;
- `confirmed` remains REF-017 + AUTH-034 governed;
- compatible/competing Causal Claims can remain multiple; no forced winner or causal ranking;
- singular `root cause` wording does not manufacture a singular cause;
- lack of causal support does not become rejection;
- candidate/reachable, encounter opportunity, exposure, downstream effect, consequence and causal attribution remain separate;
- `affected` must resolve to an explicit Impact layer;
- strong all/none/only Impact claims require bounded population and coverage;
- Safeguard proposal/configuration/authorization/request/acceptance and enforcement remain separate;
- Safeguard active + consumer not exposed does not establish prevented exposure;
- prevented exposure retains REF-028 + OPS-093 requirements and no-opportunity protection receives no prevention credit;
- Safeguard release does not prove healthy/fresh/current recovery;
- exact Gate criterion/evidence suitability/readiness/decision/delivery/enforcement/execution remain separate;
- HOLD does not mean failed execution and ADMIT does not mean run;
- override preserves readiness; fallback/override/escalation/degraded-control remain distinct;
- Execution Gate and Propagation Safeguard remain independent;
- broader control-effect claims use Causal Claim semantics except accepted narrow prevented-exposure determination;
- Responsibility Assignment is type/context/time bound and does not establish fault/cause/authority/permission;
- Semantic Definition answers meaning but not realized state/health/policy/authorization;
- Classification does not create Policy Context, permission, realized Impact or compliance;
- Policy Context does not prove enforcement, legal interpretation, breach or compliance;
- Capability Authorization is principal+capability+subject/context/time permission and does not prove action success;
- Assertion Authority determines bounded standing, not factual truth/evidence sufficiency/permission/enforcement;
- recency/source count/synchronization order/specificity/title do not create hidden authority;
- no universal RCA/Impact/control-effectiveness/governance-confidence score is accepted.

See [`04_investigation_causality_impact_control_governance_question_semantics/README.md`](04_investigation_causality_impact_control_governance_question_semantics/README.md).

## Accepted Group 05 rules

Preserve:

- source epistemic/result vocabulary rather than a generic uncertainty state;
- unknown/unresolved does not mean false, absent, safe or unaffected;
- unavailable source/evidence condition remains separate from the proposition result;
- insufficient evidence/indeterminate is not a weak positive or weak negative;
- evidence conflict, assertion conflict, authority-rule conflict, authorization conflict and competing claims remain distinct;
- restricted/redacted/opaque does not mean unavailable or absent;
- stale-for-use does not rewrite an underlying result or automatically mean violation;
- non-comparable does not mean not applicable;
- not evidenced, not recorded, not known by cutoff and evidence-backed absence remain distinct;
- strong negatives require conclusion-specific opportunity/coverage/authority burdens;
- negative-form wording never lowers those burdens;
- positive statements use source status rather than invented `likely`, `certain`, probability or confidence numbers;
- Causal Claim proposed/supported/weakened/unresolved/rejected/confirmed states remain exact; rejected requires discriminating evidence and confirmed remains REF-017 + AUTH-034 gated;
- Impact candidate/opportunity/exposure/effect/consequence negative and unknown states remain separate;
- missing/degraded control telemetry does not prove fail-open/fail-closed;
- missing Responsibility Assignment is unknown, not unassigned;
- missing Classification is unknown, not non-sensitive;
- missing Policy Context is unknown/incomplete, not unrestricted/compliant;
- unknown Capability Authorization is not permission;
- unknown Assertion Authority does not promote an available source;
- competing claims remain multiple absent accepted resolution;
- material scope/coverage limitations constrain headlines and detail;
- sibling statements retain independent epistemic states;
- no universal Explanation confidence/probability/completeness/RCA/answer-quality score is accepted;
- historical as-known epistemic state remains separate from current retrospective resolution.

See [`05_uncertainty_conflict_negative_claims_epistemic_language/README.md`](05_uncertainty_conflict_negative_claims_epistemic_language/README.md).

## Accepted Group 06 rules

Preserve:

- current projection binds requester, target audience, purpose, subject/context, temporal perspective, delivery and material information/detail class;
- audience labels are context, not permission sources;
- requester visibility does not grant disclosure to another audience;
- private inspect, export, forward and publication may resolve differently;
- conclusion, context, limitation, basis, provenance and exact-detail visibility remain independently governable;
- visible conclusion does not require visible raw evidence, while internal statement-to-basis traceability remains complete;
- safe abstraction may expose exact/coarse/redacted/generalized/opaque/withheld information only when independently authorized and semantically valid;
- safe abstraction is epistemically monotone and cannot strengthen scope, polarity, causal role, status, negative coverage or authority standing;
- aggregation/redaction/generalization is not automatic declassification;
- aliases/generalizations cannot merge materially distinct subjects or change coverage/Impact/causal scope;
- hidden values/thresholds/schema detail cannot be converted into invented severity or health;
- opaque Lineage cannot imply directness, path completeness, exposure or causality;
- causal/Impact/control/governance abstraction retains its exact layer/status and cannot manufacture blame/compliance/prevention/recovery;
- restricted/redacted/omitted does not mean absent;
- acknowledging opaque existence, counts, source class or redaction marker is itself disclosure-governed;
- material hidden limitations constrain/narrow/withhold the visible conclusion;
- Explanation cannot combine otherwise hidden facts into a new coarse inference merely for summarization;
- a separately authorized existing conclusion may remain visible when detailed basis is restricted;
- `inspectBasis` is a requester-specific projection and can expose exact basis, coarse provenance/status, redaction/opaque limitation or safe non-disclosure;
- visible citation/reference does not grant permission to inspect source evidence;
- mosaic/differencing/repeated-query risk remains compositional;
- cross-audience views may differ in detail and visible scope but cannot intentionally contradict the same bounded visible proposition;
- high-consequence communication review/release is separate from fact visibility and cannot strengthen truth;
- historical actor authorization, retained actual prior communication and current requester disclosure remain separate;
- current access expansion/revocation can change current projection without rewriting prior retained Explanation snapshots;
- no universal safe-summary level or separate audience truth model is accepted.

See [`06_audience_authorization_safe_abstraction_basis_inspection/README.md`](06_audience_authorization_safe_abstraction_basis_inspection/README.md).

## Accepted Group 07 rules

Preserve:

- a bounded trustworthy partial answer may be delivered before all sibling subquestions resolve;
- partial coverage remains proposition/subquestion bound rather than a global completeness score;
- progressive maturity requires material source/evidence/authorization/context change;
- elapsed time, polling and repeated recomposition do not strengthen truth;
- statement proposition identity persists across refresh while defining subject/scope/time identity remains unchanged;
- wording/detail/citation/basis-visibility changes can be presentation/projection deltas without a new proposition;
- materially changed subject, scope, event window or knowledge cut is a different proposition, not a silent refresh;
- basis can enrich without changing source status or confidence;
- duplicate/common-derived basis remains non-independent;
- new contradiction/conflict/correction/supersession changes Explanation only through source-owned re-evaluation;
- derived statements re-evaluate exact dependencies and accepted join logic rather than transitively flipping;
- statement delta classes distinguish presentation-only, basis-only, status, scope, materiality and authorization changes;
- removal from the current composition does not automatically mean false, retracted, resolved or nonexistent;
- authorization broadening/narrowing changes visible projection without changing internal truth;
- materially different question/request scope creates distinct Explanation lineage or explicit comparison;
- retained Explanation snapshot is evidence of actual prior communication for its bound context, not timeless source truth;
- refreshed current projections link to predecessors/superseded snapshots rather than silently overwriting them;
- Explanation supersession and source-state supersession remain separate;
- an authentic old snapshot may be unsuitable as the current answer without becoming fictitious;
- current access expansion/revocation does not backfill/erase retained earlier communication;
- missing retained snapshots remain missing; reconstruction cannot be labeled exact prior communication;
- partial answer coverage can broaden or narrow without a scalar maturity/completeness score;
- change summaries preserve exact source transition semantics and cannot invent `confidence improved` from time alone;
- notification/event/persistence architecture remains deferred.

See [`07_progressive_maturity_partial_answers_refresh_retention/README.md`](07_progressive_maturity_partial_answers_refresh_retention/README.md).

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
- result visibility ≠ basis/provenance/detail visibility;
- requester visibility ≠ onward-disclosure permission;
- safe abstraction can reduce detail but cannot strengthen truth;
- opaque existence itself can be sensitive;
- internal traceability survives visible redaction;
- Observation ≠ Assessment ≠ Change Intent ≠ Deployment ≠ realized Change ≠ Execution History ≠ Investigation ≠ Causal Claim ≠ Impact ≠ Annotation;
- run success ≠ output existence/currentness/health;
- structural compatibility ≠ statistical comparability ≠ normative health;
- active Deployment ≠ run-specific version use;
- timing/Lineage/reconciliation/change proximity ≠ causality;
- Investigation lead/localization ≠ causal truth;
- reachability ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- Safeguard enforcement ≠ prevented exposure ≠ recovery;
- readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Execution Gate ≠ Propagation Safeguard;
- responsibility ≠ fault/cause/authority/permission;
- Classification/Policy Context ≠ compliance;
- Assertion Authority ≠ Capability Authorization ≠ evidence sufficiency ≠ enforcement;
- unknown/unavailable/insufficient/conflicting/restricted/stale/non-comparable/not-applicable remain distinguishable;
- absence of evidence ≠ evidence of absence;
- current retrospective Explanation ≠ what was known then;
- retained Explanation snapshot ≠ current source truth;
- retained actual communication ≠ reconstructed historical Explanation;
- Explanation supersession ≠ source-truth supersession;
- removed from current projection ≠ false/absent by default;
- authorization-driven projection change ≠ truth change;
- progressive maturity ≠ automatic status strengthening;
- elapsed time/recomposition ≠ evidence maturity;
- no universal Explanation confidence/completeness/quality/operational-status/RCA/Impact/control-effectiveness/maturity score.

## Group 08 entry contract

Group 08 consumes EXPL-001–EXPL-140 and performs the historical/comparative consolidation of Phase 008.

It should explicitly test:

- comparison of two or more event/effective windows without collapsing scope;
- comparison of two or more knowledge cuts without later-evidence backfill;
- actual retained source state versus as-known-at-cut reconstruction versus current retrospective interpretation;
- actual retained Explanation communication versus reconstructed `what would have been explainable then`;
- current requester authorization over historical material versus historical actor authorization;
- explanation deltas that distinguish source/status/basis changes from materiality/authorization/presentation changes;
- current correction/supersession while prior retained communication remains intact;
- question/statement identity across rename/version/scope/time changes;
- negative claims at historical cuts with exact opportunity/coverage burdens;
- full Phase 008 end-to-end scenario replay and exit review;
- no new Question/Answer/Explanation-truth concept;
- no presentation/LLM/retrieval/persistence architecture selection.

Do not let historical comparison become another truth owner, current authorization become historical permission, or current retrospective knowledge rewrite earlier cuts.
