# EXPL-004 — Question Scope Dimensions & Boundary

**Status:** Accepted — Phase 008 Group 01

## Requirement

Bind the scope needed for the requested conclusion instead of answering asset-wide or enterprise-wide by convenience.

Material scope dimensions can include:

- environment/workspace/region;
- entity/component/field/key/metric;
- version/revision/configuration/schema/transformation facet;
- execution/run/attempt/opportunity/cycle;
- consumer/use/interface;
- cohort/population/partition;
- health dimension/profile/criterion;
- Lineage relationship/path semantics;
- Investigation/claim/Impact/control instance;
- event/effective-time window;
- knowledge cut.

## Principle

Scope is proposition specific. Different subquestions in the same user request may require different valid scopes.

Examples:

- `Is C healthy?` may require a bound health profile/use/dimension before a clean answer exists.
- `Were all consumers safe?` is consumer/path/version/time scoped; one safe report cannot answer a consumer-wide proposition.
- `Did the Gate block D?` must bind a specific Gate configuration/opportunity/interval rather than a timeless job-wide Gate state.

## Boundary

Broad wording does not authorize broad inference. If evidence only supports a narrower proposition, Explanation should answer narrowly and state the scope limitation.
