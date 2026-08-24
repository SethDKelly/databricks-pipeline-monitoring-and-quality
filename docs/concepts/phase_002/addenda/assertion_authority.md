# Concept: Assertion Authority

**Status:** Accepted — Phase 002 post-exit addendum discovered during Phase 005 Group 01

## Purpose

Let the ecosystem determine which source, actor, role, or governed process has authoritative standing to establish a particular assertion category/facet for an identified subject/scope, context, and time, without conflating authority with evidence sufficiency, responsibility, Capability Authorization, policy applicability, or enforcement.

## Operational principle

Several systems may assert metadata about the same table. A governance catalog may provide the authoritative business definition, Unity Catalog may provide authoritative technical schema metadata, and a repository file may provide an advisory description. All assertions remain provenance-bearing. Assertion Authority determines which assertions have authoritative standing for the exact category/facet/context/time; it does not erase lower-standing assertions or make an assertion factually correct merely because its source is authoritative.

A principal can also be permitted by Capability Authorization to submit or revise an assertion while that assertion remains advisory because the principal/source does not hold authoritative standing for the targeted category. Conversely, an authoritative source does not gain permission to perform unrelated actions merely from its assertion authority.

## Actors

- Data Steward / Governance Steward
- Data Owner / Business Authority
- Data Engineer / Pipeline Maintainer
- Security / Privacy / Compliance Stakeholder
- Data Platform Administrator
- Monitoring framework
- External governance / metadata source
- Governed automated process

## State

- authority target: owning concept/assertion category and, when relevant, facet, scheme, responsibility type, expectation class, metric/threshold class, or other bounded assertion type;
- subject scope: identified subject, explicit bounded subject set/domain, or another explicitly declared scope;
- context dimensions such as environment, tenant, purpose/use, jurisdiction, business context, or consumer where relevant;
- authority holder: source, actor, role, organizational authority, or governed process reference;
- standing such as authoritative, advisory, explicitly non-authoritative, conditional, unknown, or conflicting as resolved for the target;
- optional explicit resolution semantics such as sole authority, co-authority, ordered precedence, or conditional/fallback standing when an accepted rule defines them;
- conditions under which standing applies;
- rule provenance and governing basis;
- effective interval and recorded/knowledge time;
- rule revision, correction, supersession, retirement, and conflict history;
- visibility restrictions on authority details where applicable.

## Actions

### `establishRule`
Records a provenance-bearing authority rule for a bound authority target, holder, scope, context, conditions, and effective interval.

### `reviseRule`
Prospectively changes an authority rule while preserving the prior rule for historical resolution.

### `correctRule`
Records that a prior authority rule was incorrect for some earlier effective interval. The correction is known only from its real recorded/knowledge time and does not rewrite what the ecosystem knew before the correction.

### `resolveStanding`
Resolves the applicable authority rule(s) for an assertion source/actor and authority target at a given context/time.

Observable result may include authoritative, advisory, explicitly non-authoritative, conditional, unknown, unavailable, or conflicting standing, together with safe provenance/basis where disclosure permits.

### `explainAuthorityBasis`
Returns the authorized rule/basis explaining why an assertion source/actor has the resolved standing. Restricted authority details may remain opaque while the permitted standing result is exposed.

## Invariants / behavioral expectations

- Assertion Authority determines governance standing; it does **not** make an assertion factually true, evidentially sufficient, healthy, compliant, causally correct, or actually enforced.
- Authority is bound to an explicit target/category/facet/scope/context/time. No source, vendor, repository, team, role, or administrator is globally authoritative by default.
- Capability Authorization and Assertion Authority are independent. Permission to submit/revise an assertion does not make it authoritative; authoritative standing does not grant unrelated action permission.
- Responsibility Assignment does not grant Assertion Authority unless an explicit authority rule says that a responsibility holder is authoritative for a bound target.
- Classification and Policy Context do not themselves grant Assertion Authority.
- Monitoring Scope does not grant Assertion Authority.
- Source availability, synchronization order, ingestion order, record recency, source count, repository ownership, job creator identity, administrator status, organizational title, or technical specificity do not create authority by themselves.
- More-specific scope does not automatically outrank broader scope unless an applicable authority rule explicitly defines that precedence.
- Multiple sources can be co-authoritative when an explicit rule permits it. If co-authoritative assertions conflict and no accepted resolver applies, the result is an **authoritative assertion conflict** rather than an arbitrary winner.
- Multiple advisory sources agreeing do not become authoritative by consensus.
- An explicit precedence/fallback rule can select among otherwise eligible holders, but the losing/lower-standing assertions remain provenance-bearing history rather than being erased or rewritten as false.
- Missing authority evidence is `unknown`, not permission for the most available or convenient source to become authoritative.
- An unavailable authoritative source does not automatically promote another source unless an accepted conditional/fallback rule explicitly does so and its conditions are evidenced.
- Authority rules themselves require provenance and a governing basis. Conflicting authority rules remain authority conflict unless an accepted higher-order/explicit governing rule resolves them; rules do not self-validate by claiming authority over themselves.
- Current authority does not overwrite historical authority. Effective time and recorded/knowledge time remain distinct where material.
- A rule correction can alter current retrospective resolution for an earlier interval without backdating when the correction became known.
- Authority resolution does not waive Phase 004 evidence applicability, coverage, sufficiency, causal-confirmation, exposure, readiness, or control-enforcement standards.

## Conflict vocabulary

### Assertion disagreement
Two or more applicable source assertions materially disagree for the same target/context/time.

### Resolved assertion disagreement
Applicable assertions disagree, but an accepted authority rule yields an authoritative resolution while preserving the disagreement and all source assertions.

### Authoritative assertion conflict
Two or more assertions with simultaneously authoritative standing materially disagree and no accepted resolution rule selects among them.

### Authority-rule conflict
Two or more applicable authority rules disagree about holder standing, precedence, conditions, or scope and no accepted governing rule resolves the rule conflict.

### Authority unknown
No applicable accepted authority rule can be established for the requested target/context/time.

These states are distinct from Phase 004 evidence conflict/insufficiency and from Capability Authorization conflict.

## Ambiguity and missing evidence

If an assertion is available but authority standing is unknown, the assertion remains usable as provenance-bearing context where appropriate but must not be presented as authoritative state. If an authority source/rule is unavailable, the framework reports unavailable/unknown authority unless an explicit fallback rule applies.

Overlapping rules do not implicitly use recency, scope specificity, source priority, or majority vote. If overlap cannot be resolved through accepted rule semantics, the result remains authority-rule conflict.

## Synchronizations

- **Entity Identity** supplies the identified subject when authority scope targets a specific entity.
- **Semantic Definition**, **Responsibility Assignment**, **Classification**, **Policy Context**, **Expectation**, and later metric/threshold governance use Assertion Authority to determine which assertions have authoritative standing without moving their assertion truth into this concept.
- **Capability Authorization** determines whether a principal may create/revise authority rules or assertions where such permission is required; it remains separate from the standing those assertions receive.
- **Historical replay** resolves the authority rules known/applicable at the relevant effective time and knowledge cutoff rather than projecting current precedence backward.
- **Explanation** may communicate authorized source/authority context and unresolved authority conflict without revealing restricted governance details.
- Phase 009 may identify concrete source-specific authority contracts (for example Databricks, Collibra, Immuta, GitHub, human stewards), but availability/integration does not create Assertion Authority by itself.

## Security / privacy / governance considerations

Authority metadata can reveal internal governance hierarchy, privileged roles, security ownership, sensitive domains, or control structures. Authority-rule visibility must therefore be independently governed; a requester may receive an authorized result such as `authoritative business definition` while the authority-holder identity/basis remains partially opaque.

## Evidence / provenance considerations

Every material authority rule should retain its authority target, holder, scope/context, conditions, provenance/governing basis, effective interval, recorded/knowledge time, and correction/supersession history. Any resolved authoritative state must be explainable from the underlying assertions plus the applicable authority rule(s), without treating resolution order as authority.

## Representative scenarios

### Authoritative plus advisory definition
Collibra is explicitly authoritative for the business-definition facet; a repository document supplies a conflicting advisory definition. The authoritative business definition resolves from Collibra while the repository disagreement remains visible/provenance-bearing.

### Different facets, no conflict
Unity Catalog is authoritative for a technical schema facet while a business steward is authoritative for a business population definition. Different facets legitimately use different authorities.

### Co-authoritative conflict
Two explicitly co-authoritative business stewards provide incompatible definitions. The result remains authoritative conflict until an accepted resolver applies.

### No implicit consensus
Three advisory systems agree on a classification but the authoritative classification source is unknown. Agreement does not manufacture authoritative classification.

### Explicit conditional fallback
A rule states that Source B is authoritative only when Source A is unavailable for a defined context. If A unavailability is evidenced and the rule applies, B can resolve as authoritative for that context. Without the explicit rule, B does not inherit authority merely because A is offline.

### Capability versus authority
An engineer is permitted to edit a semantic description but holds advisory standing for the business-definition facet. The edit is accepted as an assertion but does not replace the authoritative business definition.

### Responsibility versus authority
A team is the technical owner of Table C but no rule grants that team authority over business criticality. Responsibility remains separate.

### Prospective authority change
Authority for a classification scheme moves from Source A to Source B effective next month. Historical replay before the transition uses A; later state uses B.

### Rule correction
A governance office later corrects an authority rule and establishes that Source B, not A, should have governed an earlier period. Current retrospective resolution may change, while an `as-known-then` view still reflects the rule known at the time.

### Authority-rule conflict
Two governing sources claim incompatible precedence rules for the same semantic facet and scope. With no accepted higher-order resolver, authority remains conflicting rather than choosing the newest or most specific rule.

### Restricted authority basis
An analyst may see that a business definition is authoritative while the identity of the restricted governance source is hidden.

## Non-goals

- proving factual correctness of an assertion;
- evidence sufficiency or source-measurement reliability scoring;
- Capability Authorization or IAM enforcement;
- Responsibility Assignment;
- policy applicability or compliance determination;
- choosing Databricks, GitHub, Collibra, Immuta, Unity Catalog, or any vendor as universally authoritative;
- deciding concrete source-integration availability/latency;
- selecting storage, rule engine, workflow, or technical architecture.

## Deferred questions

- Which authority-target categories/facets are required for MVP?
- Which explicit precedence/conditional/fallback rule forms are required beyond the common semantics?
- Which authority-rule changes require multi-party approval or additional Capability Authorization?
- Which concrete sources/actors are authoritative for each target in the deployment environment?
- Which authority details can be safely disclosed to each audience?
