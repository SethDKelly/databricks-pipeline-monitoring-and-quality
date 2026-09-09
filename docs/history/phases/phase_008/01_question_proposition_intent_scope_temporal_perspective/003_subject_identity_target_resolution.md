# EXPL-003 — Subject Identity & Target Resolution

**Status:** Accepted — Phase 008 Group 01

## Requirement

Resolve the subject of a question through accepted Entity Identity semantics before composing material conclusions.

Question targets may include, as applicable:

- data/pipeline entities;
- logical executions or execution opportunities;
- Change Intent/Deployment revisions;
- versions or implementation-state facets;
- consumers/reports/applications;
- Investigation/Causal Claim/Impact/control instances;
- cohorts/regions/populations/fields/keys/metrics;
- governance/responsibility/policy subjects.

## Ambiguity discipline

Names, aliases, repository names, job names, table names or display labels are not sufficient identity evidence when multiple candidates are plausible.

If `orders` could mean production and development tables, or a historical rename creates two plausible targets, the question remains materially ambiguous until the proposition can be bounded or the answer explicitly presents bounded interpretations.

Explanation must not silently choose the most convenient target merely to produce an answer.

## Boundaries

- name equality ≠ Entity Identity;
- historical rename continuity requires accepted identity evidence;
- current identity/reference state ≠ automatically the identity mapping applicable at an earlier knowledge cut;
- subject resolution ≠ Monitoring Scope;
- subject resolution ≠ authorization to disclose the subject.
