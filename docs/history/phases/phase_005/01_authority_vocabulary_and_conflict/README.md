# Phase 005 Group 01 — Authority Vocabulary, Source Assertions & Conflict Resolution

**Status:** Review complete — accepted

## Goal

Define the shared authority vocabulary and conflict/supersession semantics that later Phase 005 groups will apply to governance, normative, capability, control, and disclosure categories.

## Group result

Group 01 exposes one genuine missing truth boundary and accepts a narrow post-Phase-002 concept addendum:

- **Assertion Authority** — resolves which source/actor/role/governed process has authoritative standing to establish a particular assertion category/facet/subject scope/context/time.

The accepted concept catalog therefore moves from **23 to 24 concepts**.

Assertion Authority is distinct from:

- **Capability Authorization** — whether a principal may perform an action;
- **Responsibility Assignment** — who bears a named responsibility;
- **evidence sufficiency** — whether evidence supports a conclusion;
- **Policy Context / Classification** — applicability/category state;
- **enforcement evidence** — whether an external control actually operated.

A principal can be permitted to submit an assertion that remains advisory. A source can be authoritative for one facet and advisory for another. An authoritative source can still be wrong and later corrected.

## Accepted authority contracts — AUTH-001–AUTH-008

1. [`001_authority_target_and_vocabulary.md`](001_authority_target_and_vocabulary.md) — authority target binding and common vocabulary.
2. [`002_authority_rule_provenance_and_governing_basis.md`](002_authority_rule_provenance_and_governing_basis.md) — rule provenance, governing basis, and meta-conflict behavior.
3. [`003_assertion_standing_and_conditional_authority.md`](003_assertion_standing_and_conditional_authority.md) — authoritative/advisory/non-authoritative/conditional/unknown/conflicting standing.
4. [`004_assertion_disagreement_and_authority_conflict.md`](004_assertion_disagreement_and_authority_conflict.md) — assertion disagreement, authoritative conflict, and authority-rule conflict.
5. [`005_explicit_precedence_coauthority_and_fallback.md`](005_explicit_precedence_coauthority_and_fallback.md) — sole/co-authority, explicit precedence, and evidenced conditional fallback.
6. [`006_authority_revision_correction_supersession_and_time.md`](006_authority_revision_correction_supersession_and_time.md) — prospective revision, correction, supersession, and bitemporal authority history.
7. [`007_unknown_unavailable_and_resolution_limits.md`](007_unknown_unavailable_and_resolution_limits.md) — explicit unknown/unavailable authority states and no convenient default.
8. [`008_authority_separation_from_evidence_permission_and_enforcement.md`](008_authority_separation_from_evidence_permission_and_enforcement.md) — separation from evidence sufficiency, Capability Authorization, responsibility, policy, and enforcement.

## Common authority vocabulary

### Source assertion
A provenance-bearing assertion contributed to its owning concept regardless of standing.

### Authority target
The bounded concept/category/facet/scheme/responsibility/expectation/metric class plus subject scope/context/time for which standing is resolved.

### Authority rule
A provenance-bearing rule establishing standing, conditions, and any explicit precedence/fallback behavior for an authority target.

### Authoritative assertion
An applicable assertion from a source/actor with authoritative standing for the bound target.

### Advisory assertion
An applicable assertion that may enrich/challenge/contextualize but cannot displace authoritative state.

### Resolved assertion disagreement
Assertions disagree, but an accepted authority rule yields authoritative resolution while preserving the dissenting assertions.

### Authoritative assertion conflict
Two or more simultaneously authoritative assertions disagree and no accepted resolver applies.

### Authority-rule conflict
Applicable authority rules themselves disagree and no accepted governing rule resolves them.

### Authority unknown/unavailable
No applicable accepted rule can be established, or required authority-rule evidence is unavailable. Neither state permits the framework to choose the most convenient source.

## No hidden precedence

The following do **not** create authority unless an explicit applicable rule says so:

- source count / majority;
- recency alone;
- synchronization or ingestion order;
- source availability;
- repository ownership;
- job creator identity;
- platform administrator status;
- organizational title;
- Responsibility Assignment;
- apparent source specificity;
- a source asserting that it is authoritative.

More-specific rules also do not automatically override broader rules. Specificity precedence must itself be explicit.

## Governing-basis rule

Authority rules require provenance and an accepted governing basis or trust root appropriate to the deployment context. A rule cannot validate itself merely by claiming authority over authority.

When authority rules conflict and no accepted governing resolver exists, the result remains authority conflict. Phase 005 defines this functional behavior without selecting the technical trust-root implementation.

## Historical behavior

Authority is effective-time and knowledge-time aware.

- prospective authority changes do not rewrite earlier authority;
- later authority-rule corrections may revise current retrospective resolution for an earlier interval;
- `as-known-then` views use authority state actually known at the cutoff;
- resolving a conflict later does not imply the conflict was resolved earlier;
- historical Explanations/actions that used the then-known authority state remain actual historical artifacts.

## Boundaries retained

Group 01 does not:

- decide concrete Databricks/Collibra/Immuta/GitHub/Unity Catalog authority assignments;
- define semantic, metric, threshold, capability, gate, safeguard, or confirmation authority in detail;
- choose IAM, rule engine, workflow, storage, or architecture;
- change REF-001–REF-030 evidence semantics;
- treat authoritative standing as factual infallibility or enforcement proof.

## Scenario result

[`scenario_checks.md`](scenario_checks.md) passes the representative authority/conflict cases, including co-authoritative disagreement, explicit fallback, rule conflict, capability-versus-standing, responsibility-versus-standing, historical transfer/correction, restricted authority basis, and evidence-sufficiency separation.

## Exit decision

**Accepted. Phase 005 Group 01 is complete. Assertion Authority is accepted as the 24th concept and AUTH-001–AUTH-008 are accepted. Phase 005 Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance is next and has not started.**
