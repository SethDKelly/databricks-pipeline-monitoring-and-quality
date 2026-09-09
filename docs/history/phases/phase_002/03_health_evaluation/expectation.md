# Concept: Expectation

**Status:** Accepted — Phase 002 Group 03; synchronization refined by Group 04; authority refined by Phase 005 Group 03

## Purpose

Let an authorized actor or source state what behavior or condition should be considered acceptable for an identified subject in a defined context and time.

## Operational principle

A pipeline maintainer registers a Change Intent to add a filter that will intentionally reduce Table C's population. If the business requirement is that post-change C should contain 13–15 million rows, an authorized actor explicitly establishes/revises the volume Expectation effective from the realized activation boundary. The Change Intent can prompt this review, but its anticipated effect does not become a normative criterion automatically.

The same concept can represent structural/schema compatibility Expectations: for example, a consumer may require a named column, accepted type/nullability, key/grain condition, or a bounded compatibility rule. Governed schema meaning remains Semantic Definition; realized schema remains Observation/Change.

## Actors

- Data Owner / accountable business party
- Data Steward / Governance Steward
- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Monitoring framework
- Authoritative external source

## State

- identified subject;
- expectation dimension/property;
- normative criterion or acceptable condition;
- applicability context;
- effective interval and lifecycle state;
- assertion provenance, actor/source, and Assertion Authority context;
- bounded exception/suspension context when explicitly adopted;
- supersession/correction history;
- unresolved or conflicting expectation assertions.

## Actions

### `establish`
Records a provenance-bearing normative criterion for a subject/context.

### `revise`
Changes future normative behavior while retaining earlier versions for historical interpretation.

### `exceptFor`
Records a bounded context/time in which the expectation is suspended/non-applicable without mutating evidence.

### `retire`
Ends future applicability while preserving historical state.

### `resolveApplicable`
Returns applicable expectation assertion(s), none known, conflicting, unauthorized, or unavailable.

## Invariants / behavioral expectations

- Expectation is normative: it describes what **should** be true or acceptable.
- Historical/common behavior does not become an Expectation merely because it is frequent.
- A Change Intent's anticipated effect is descriptive planned context unless an authoritative actor/source explicitly establishes it as an Expectation.
- An intended structural change may require a prospective Expectation revision, but that revision remains an explicit normative action with its own authority/provenance.
- The effective post-change Expectation should align to evidence that the change became active rather than silently applying from plan-registration time unless organizational semantics explicitly say otherwise.
- Expectation does not measure actual state or decide whether its criterion was met; Assessment does.
- Multiple Expectations can apply across different dimensions/contexts.
- Conflicting Expectations remain conflicts until accepted Assertion Authority/precedence semantics resolve them.
- Missing applicable Expectation does not mean healthy/acceptable.
- Current Expectations do not rewrite historical Assessments.
- Baseline-derived ranges remain descriptive unless an authoritative Expectation explicitly adopts a normative criterion.
- A bounded waiver/exception changes normative applicability or required response; it does not mutate Observation, Baseline, structural state, or create a false `pass`.
- Technical schema-definition authority does not automatically grant authority to define structural compatibility Expectations.
- Business criticality, Responsibility Assignment, Classification, Policy Context, metric computation ownership, or source availability do not automatically grant Expectation authority.
- Expectation remains implementation-neutral and is not defined by DQX, SQL, scheduler, ticket, CI/CD, Unity Catalog, or GitHub syntax.

## Phase 005 Group 03 authority boundary

AUTH-016–AUTH-023 refine normative governance while leaving Expectation as the truth owner for normative criteria.

Independently governable layers can include:

- Expectation class/dimension authority;
- metric/check profile selection;
- threshold and warning/failure margin authority;
- severity authority;
- structural/schema compatibility Expectation authority;
- bounded exception/waiver/suspension/retirement authority;
- high-consequence-use eligibility.

An authoritative Expectation or business-critical metric does not automatically become eligible for an Execution Gate or safeguard. Even when high-consequence-use eligibility exists, control configuration/override capability and evidence readiness/enforcement remain separate.

## Ambiguity and missing evidence

A planned change may identify a need to revise an Expectation before exact post-change acceptable values are known. That state remains unresolved rather than converting the Change Intent into a threshold. If activation timing is uncertain, post-change applicability remains tied to evidence/accepted effective semantics rather than guessed deployment time.

If two co-authoritative Expectations conflict for the same bound subject/dimension/context/time and no accepted resolver applies, preserve authoritative normative conflict. Do not silently use strictest/latest/business/technical/highest-severity precedence.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Assertion Authority** determines which Expectation assertions/lifecycle actions have authoritative standing for a bound dimension/context/time.
- **Capability Authorization** separately determines whether a principal may perform an establish/revise/except/retire action where permission is required.
- **Responsibility Assignment** may identify parties responsible for maintaining/approving Expectations without granting universal authority.
- **Semantic Definition** provides interpretation such as grain/business-calendar/schema/key semantics.
- **Observation** provides evidence relevant to the criterion.
- **Assessment** compares authorized Observations with the applicable Expectation.
- **Baseline** remains descriptive and cannot silently become an Expectation.
- **Change Intent** can trigger explicit review/establishment/revision of a prospective post-change Expectation.
- **Deployment/Change** can establish the realized activation/change boundary relevant to effective applicability.
- **Execution Gate/Propagation Safeguard** may later consume an explicitly control-eligible Expectation, but normative authority does not grant control capability or prove enforcement.

## Security / privacy / governance considerations

Expectations, thresholds, schema compatibility rules, severity, waivers, and Change Intents can reveal sensitive business rules, schedules, filters, operating assumptions, or control criteria. Maintenance/authority, action permission, and viewer disclosure remain separate.

## Evidence / provenance considerations

Every Expectation retains source/actor, assertion time, effective interval, context, authority standing, and revision/exception/retirement history. If a revision is related to Change Intent, that relationship should be traceable without making intent itself the normative source unless explicitly authorized.

Historical replay preserves the normative rule and waiver/exception state that was applicable/known at the relevant cutoff; later corrections do not rewrite earlier Assessments or control decisions.

## Representative scenarios

### Planned filter with prospective criterion
A filter is planned and expected to lower C. An authoritative business/data authority explicitly revises C's acceptable post-change range effective from activation. The first post-change Observation can be assessed immediately even before a new Baseline exists.

### Planned effect without approved criterion
A Change Intent predicts lower volume but no authoritative party sets an acceptable range. The first post-change result may be compared with historical/planned context but cannot receive a normative volume pass/fail solely from the intent.

### Successful run, failed post-change expectation
The filter deploys and lowers volume as intended, but completeness violates a separate Expectation. Planned change does not suppress the violation.

### Structural compatibility
A downstream export requires a fixed schema while another consumer permits additive optional columns. The same realized schema addition can satisfy one consumer-specific Expectation and violate the other.

### Bounded waiver
A migration window has an authorized temporary exception to a volume Expectation. The low volume Observation remains evidence; the rule is represented as excepted for that bounded window rather than as a false pass.

### Historical revision
A threshold changes at a realized deployment boundary. Incidents before that boundary continue to resolve the old criterion.

## Non-goals

- measuring actual conditions;
- deriving Baselines;
- treating planned effects as automatic normative requirements;
- producing health status;
- defining root cause;
- metric/statistical/schema-diff algorithm design;
- encoding vendor-specific quality-rule syntax;
- granting production-control capability.

## Deferred questions

- first-MVP Expectation dimensions/lifecycle states and rule classes — Phase 006/011;
- detailed threshold/margin/statistical semantics — Phase 006;
- evidence/timing required for control-eligible conditions — Phases 004/006/009;
- concrete authoritative sources/actors by target environment — Phase 009;
- consequence/severity display and audience communication — Phase 008.