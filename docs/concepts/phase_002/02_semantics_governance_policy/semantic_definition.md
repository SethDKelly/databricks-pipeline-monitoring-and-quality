# Concept: Semantic Definition

**Status:** Accepted — Phase 002 Group 02

## Purpose

Let people understand what an identified entity means and how it should be interpreted in a relevant business or technical context.

## Operational principle

A business analyst sees that a downstream metric changed materially. Before interpreting the change, the system resolves the applicable semantic assertions for the affected entity at the incident time: business definition, grain, unit, population/inclusion rules, calculation meaning, and any relevant technical description. Two definitions from different contexts can legitimately coexist; contradictory assertions remain visible rather than being flattened into one unexplained description.

## Actors

- Business Analyst / Data Consumer
- Data Steward / Governance Steward
- Data Owner
- Data Engineer / Pipeline Maintainer
- Monitoring framework

## State

- identified subject;
- semantic assertions grouped by semantic facet, such as technical description, business definition, grain, unit, population, calculation meaning, domain, or interpretation guidance;
- context in which an assertion is intended to apply when relevant;
- effective interval/version context;
- assertion provenance, actor/source, and authority context;
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
- **Conflict behavior:** resolution does not silently choose among incompatible assertions unless an accepted authority rule exists.

## Invariants / behavioral expectations

- Semantic Definition describes meaning; it does not assert health, quality, freshness, or causal correctness.
- A technical description and a business definition are distinct semantic facets and must not be flattened merely for convenience.
- Multiple context-specific definitions can be simultaneously valid and are not automatically conflicts.
- Current semantics do not silently rewrite historical interpretation.
- A synchronized copy does not become authoritative merely because it was synchronized last.
- Human-readable names, schemas, code, or column labels may provide clues but are not sufficient to invent authoritative business meaning.
- Missing semantic evidence resolves to `unknown`/missing context, not inferred meaning.
- Semantic Definition does not own responsibility, classification, policy applicability, expectations, or authorization.

## Ambiguity and missing evidence

If semantic assertions are absent, the product reports missing context. If assertions disagree within the same relevant facet/context/time, the conflict is retained with provenance. If the authority relationship is not defined, the concept does not manufacture a canonical winner. Restricted semantic details may be replaced by an authorized safe summary or an indication that semantics are unavailable.

## Synchronizations

- **Entity Identity** supplies the subject.
- **Responsibility Assignment** may identify parties responsible for semantic stewardship without making them automatically authoritative for every definition.
- **Change** can represent semantic changes across time without asserting data degradation or causation.
- **Explanation** uses Semantic Definition to translate technical evidence into business meaning.
- A later authority concept or integration contract may establish source precedence by semantic facet; that policy remains separate from the semantic assertions themselves.

## Security / privacy / governance considerations

Definitions, business populations, metric meaning, and technical descriptions can reveal sensitive business or data-domain information even when no row values are exposed. Visibility must therefore respect authorization and data-minimization principles.

## Evidence / provenance considerations

Every semantic assertion should retain its source/actor, semantic facet, relevant context, assertion time, and effective time when known. Corrections and supersession should remain historically reconstructable. Any later selection of an effective definition must be explainable from the underlying assertions and accepted authority rule.

## Representative scenarios

### Happy path
An authoritative business definition, grain, and unit are available for an affected metric and are presented with provenance.

### Partial semantics
A table has a technical description but no business definition. The product reports the missing business context rather than treating the technical description as equivalent.

### Context-specific meaning
A metric has different valid interpretation notes for internal operational use and external reporting. Both remain scoped to their declared contexts rather than being treated as contradiction.

### Conflicting assertions
Two sources provide incompatible business definitions for the same metric/context/time. Both remain visible until an authority rule resolves the conflict.

### Historical replay
A calculation definition changes prospectively. An investigation of an earlier incident resolves the definition that applied then.

### Unauthorized evidence
A user receives a permitted summary of an asset's meaning while restricted population details remain hidden.

## Non-goals

- responsibility assignment;
- classification or policy applicability;
- quality/freshness expectations;
- authorization;
- automatically inferring authoritative semantics from names, code, schemas, or usage;
- forcing every entity to have one canonical text definition.

## Deferred questions

- Which semantic facets are required for MVP business-facing explanations?
- Which contexts justify distinct valid definitions rather than conflicts?
- What source-precedence rules apply by semantic facet?
