# Concept: Expectation

**Status:** Accepted — Phase 002 Group 03; synchronization refined by Group 04

## Purpose

Let an authorized actor or source state what behavior or condition should be considered acceptable for an identified subject in a defined context and time.

## Operational principle

A pipeline maintainer registers a Change Intent to add a filter that will intentionally reduce Table C's population. If the business requirement is that post-change C should contain 13–15 million rows, an authorized actor explicitly establishes/revises the volume Expectation effective from the realized activation boundary. The Change Intent can prompt this review, but its anticipated effect does not become a normative criterion automatically.

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
- assertion provenance, actor/source, and authority context;
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
- A Change Intent's anticipated effect is descriptive planned context unless an authorized actor/source explicitly establishes it as an Expectation.
- An intended structural change may require a prospective Expectation revision, but that revision remains an explicit normative action with its own authority/provenance.
- The effective post-change Expectation should align to evidence that the change became active rather than silently applying from plan-registration time unless organizational semantics explicitly say otherwise.
- Expectation does not measure actual state or decide whether its criterion was met; Assessment does.
- Multiple Expectations can apply across different dimensions/contexts.
- Conflicting Expectations remain conflicts until authority/precedence semantics resolve them.
- Missing applicable Expectation does not mean healthy/acceptable.
- Current Expectations do not rewrite historical Assessments.
- Expectation remains implementation-neutral and is not defined by DQX, SQL, scheduler, ticket, or CI/CD syntax.

## Ambiguity and missing evidence

A planned change may identify a need to revise an Expectation before exact post-change acceptable values are known. That state remains unresolved rather than converting the Change Intent into a threshold. If activation timing is uncertain, post-change applicability remains tied to evidence/accepted effective semantics rather than guessed deployment time.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Responsibility Assignment** may identify parties responsible for maintaining/approving Expectations without granting universal authority.
- **Semantic Definition** provides interpretation such as grain/business-calendar semantics.
- **Observation** provides evidence relevant to the criterion.
- **Assessment** compares authorized Observations with the applicable Expectation.
- **Baseline** remains descriptive and cannot silently become an Expectation.
- **Change Intent** can trigger explicit review/establishment/revision of a prospective post-change Expectation.
- **Deployment/Change** can establish the realized activation/change boundary relevant to effective applicability.

## Security / privacy / governance considerations

Expectations and Change Intents can reveal sensitive thresholds, business rules, schedules, filters, or operating assumptions. Maintenance authority and viewer disclosure remain separate.

## Evidence / provenance considerations

Every Expectation retains source/actor, assertion time, effective interval, context, and revision/exception history. If a revision is related to Change Intent, that relationship should be traceable without making intent itself the normative source unless explicitly authorized.

## Representative scenarios

### Planned filter with prospective criterion
A filter is planned and expected to lower C. An authorized business/data authority explicitly revises C's acceptable post-change range effective from activation. The first post-change Observation can be assessed immediately even before a new Baseline exists.

### Planned effect without approved criterion
A Change Intent predicts lower volume but no authorized party sets an acceptable range. The first post-change result may be compared with historical/planned context but cannot receive a normative volume pass/fail solely from the intent.

### Successful run, failed post-change expectation
The filter deploys and lowers volume as intended, but completeness violates a separate Expectation. Planned change does not suppress the violation.

### Historical revision
A threshold changes at a realized deployment boundary. Incidents before that boundary continue to resolve the old criterion.

## Non-goals

- measuring actual conditions;
- deriving Baselines;
- treating planned effects as automatic normative requirements;
- producing health status;
- defining root cause;
- encoding vendor-specific quality-rule syntax.

## Deferred questions

- first-MVP Expectation dimensions/lifecycle states;
- authority/source precedence for change-driven Expectation revisions;
- semantics when a planned effective time and actual activation time differ;
- consequence/severity policy.
