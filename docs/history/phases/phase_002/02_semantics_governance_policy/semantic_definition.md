# Concept: Semantic Definition

**Status:** Accepted — Phase 002 Group 02; authority refined by Phase 005 Group 02

## Purpose

Let people understand what an identified entity means and how it should be interpreted in a relevant business or technical context.

## Operational principle

A business analyst sees that a downstream metric changed materially. Before interpreting the change, the system resolves the applicable semantic assertions for the affected entity at the incident time: business definition, grain, unit, population/inclusion rules, calculation meaning, technical description, and—where relevant—field/key/schema meaning. Two definitions from different contexts can legitimately coexist; contradictory assertions remain visible rather than being flattened into one unexplained description.

A governed schema declaration may describe field roles, grain, identifiers, or structural meaning. That declaration is distinct from both the physical schema actually observed in production and any normative structural Expectation requiring compatibility.

## Actors

- Business Analyst / Data Consumer
- Data Steward / Governance Steward
- Data Owner
- Data Engineer / Pipeline Maintainer
- Monitoring framework

## State

- identified subject;
- semantic assertions grouped by semantic facet, such as technical description, business definition, grain, unit, population, calculation meaning, domain, interpretation guidance, column/field role, identifier/key role, or governed schema/schema-contract meaning;
- context in which an assertion is intended to apply when relevant;
- effective interval/version context;
- assertion provenance, actor/source, and Assertion Authority context;
- supersession/correction history;
- unresolved or conflicting semantic assertions.

## Actions

### `define`
- **Intent:** record or synchronize a semantic assertion for an identified subject/facet/context.
- **State effect:** preserves the assertion with provenance and applicable effective time.

### `revise`
- **Intent:** prospectively supersede a semantic assertion while preserving historical interpretation.
- **State effect:** closes/supersedes the prior assertion and records the revision without rewriting the past.

### `resolveAt`
- **Intent:** return semantic assertions applicable to a subject, context, and time.
- **Observable result:** applicable assertion(s), unknown, conflicting, unauthorized, or unavailable, with provenance where disclosure is allowed.
- **Conflict behavior:** resolution does not silently choose among incompatible assertions unless accepted Assertion Authority rules resolve their standing.

## Invariants / behavioral expectations

- Semantic Definition describes meaning; it does not assert health, quality, freshness, causal correctness, or realized physical state.
- A technical description and a business definition are distinct semantic facets and must not be flattened merely for convenience.
- Business definition, technical schema declaration, grain, units, population, calculation meaning, field role, and key role may have different authority holders.
- Multiple context-specific definitions can be simultaneously valid and are not automatically conflicts.
- Current semantics do not silently rewrite historical interpretation.
- A synchronized copy does not become authoritative merely because it was synchronized last.
- Human-readable names, DDL, schemas, code, SQL usage, or column labels may provide clues/assertions but are not sufficient to invent authoritative business meaning.
- A declared primary/business-key role does not prove observed uniqueness or nullability health.
- A column disappearance plus a new similarly typed/name column does not by itself prove a semantic rename; Change Intent, identity, semantic, or other evidence is required.
- Governed/declared schema meaning ≠ normative schema Expectation ≠ realized schema Observation/Change.
- Missing semantic evidence resolves to `unknown`/missing context, not inferred meaning.
- Semantic Definition does not own responsibility, classification, policy applicability, expectations, authorization, or realized schema conformance.

## Ambiguity and missing evidence

If semantic assertions are absent, the product reports missing context. If assertions disagree within the same relevant facet/context/time, the conflict is retained with provenance. If authority standing is unresolved, the concept does not manufacture a canonical winner. Restricted semantic/schema details may be replaced by an authorized safe summary or an indication that semantics are unavailable.

## Synchronizations

- **Entity Identity** supplies the subject and can support stable identity across renamed/migrated entities where evidence exists.
- **Assertion Authority** determines authoritative/advisory/conflicting standing per semantic facet/context/time without owning the semantic assertion.
- **Responsibility Assignment** may identify parties responsible for semantic stewardship without making them automatically authoritative for every definition.
- **Expectation** may define normative schema/field/key/grain compatibility separately from semantic meaning.
- **Observation/Change** provide evidence of realized physical schema and structural transitions without replacing semantic authority.
- **Change Intent** may declare a planned rename/schema/grain/key change without proving realization.
- **Change** can represent semantic or schema changes across time without asserting data degradation or causation.
- **Baseline/Assessment** may use semantic/grain/key context to determine metric comparability and health.
- **Explanation** uses Semantic Definition to translate technical evidence into business meaning.

## Security / privacy / governance considerations

Definitions, business populations, schema details, key roles, metric meaning, and technical descriptions can reveal sensitive business or data-domain information even when no row values are exposed. Visibility must therefore respect authorization and data-minimization principles.

## Evidence / provenance considerations

Every semantic assertion should retain its source/actor, semantic facet, relevant context, assertion time, effective time, and authority standing/basis when known. Corrections and supersession should remain historically reconstructable. Any selection of an effective authoritative definition must be explainable from the underlying assertions and Assertion Authority rules.

## Representative scenarios

### Happy path
An authoritative business definition, grain, and unit are available for an affected metric and are presented with provenance.

### Partial semantics
A table has a technical description/schema declaration but no business definition. The product reports the missing business context rather than treating the technical description as equivalent.

### Schema declaration versus realized state
A governed declaration says `customer_id` is required and is the business key. Runtime evidence shows the field is absent or non-unique. Semantic Definition retains the declared meaning; Observation/Change and Assessment describe the realized mismatch/health.

### Context-specific meaning
A metric has different valid interpretation notes for internal operational use and external reporting. Both remain scoped to their declared contexts rather than being treated as contradiction.

### Conflicting assertions
Two authoritative sources provide incompatible business definitions for the same metric/context/time. The authoritative conflict remains visible until an accepted resolver applies.

### Historical replay
A calculation or schema meaning changes prospectively. An investigation of an earlier incident resolves the definition that applied then.

### Unauthorized evidence
A user receives a permitted summary of an asset's meaning while restricted population/schema details remain hidden.

## Non-goals

- responsibility assignment;
- classification or policy applicability;
- quality/freshness/schema-health expectations;
- authorization;
- realized physical schema observation;
- automatically inferring authoritative semantics from names, code, DDL, schemas, or usage;
- forcing every entity to have one canonical text definition.

## Deferred questions

- Which semantic/schema facets are required for MVP business-facing and technical explanations?
- Which contexts justify distinct valid definitions rather than conflicts?
- Which concrete sources hold authority for each semantic facet in the deployment environment?
- Which column/field entities require explicit Entity Identity for rename/history tracking in MVP?
