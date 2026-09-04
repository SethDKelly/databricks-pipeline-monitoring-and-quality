# Assertion Authority

**Canonical key:** `concept.assertion_authority`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.assertion_authority`

**Owns current question:** Which source/actor/role/governed process has authoritative standing for a bounded assertion target/facet/scope/context/time?

**Stable IDs:** N/A

## Current semantics

Assertion Authority owns authority target/category/facet/scheme/responsibility/expectation class; subject scope/context; holder; standing (`authoritative`, `advisory`, explicitly non-authoritative, conditional, unknown, conflicting); explicit sole/co-authority/precedence/fallback semantics when governed; conditions; provenance/basis; effective interval/knowledge time; rule correction/supersession/retirement; conflict and visibility.

## Actions

- `establishRule` — record a bounded provenance-bearing authority rule.
- `reviseRule` — prospectively change the rule while preserving history.
- `correctRule` — correct earlier effective rule state without backdating when the correction became known.
- `resolveStanding` — return standing/conditions/conflict/unknown/unavailable for exact target/context/time.
- `explainAuthorityBasis` — expose allowed governing basis.

## Invariants / boundaries

- Assertion Authority determines governance standing; it does not make an assertion factually true, evidentially sufficient, healthy, compliant, causal, or enforced.
- Assertion Authority ≠ Capability Authorization ≠ Responsibility Assignment ≠ evidence sufficiency ≠ enforcement.
- No source/vendor/repository/team/role/administrator is globally authoritative by default; standing is target/scope/context/time bound.
- Availability, synchronization/ingestion order, recency, source count, title, repository ownership, creator identity, technical specificity, or scope specificity do not create authority unless an explicit accepted rule says so.
- Multiple advisory sources do not become authoritative by consensus.
- Co-authoritative disagreement without accepted resolver remains authoritative assertion conflict.
- Fallback/precedence requires explicit governed rule plus evidence its conditions apply; unavailable primary authority does not promote another source automatically.
- Authority rules themselves need provenance and can conflict; they do not self-validate by claiming authority.
- Current authority does not overwrite historical authority; effective and knowledge time remain separate.

## Ambiguity / evidence

Preserve distinct states: assertion disagreement, resolved disagreement, authoritative assertion conflict, authority-rule conflict, and authority unknown. Available assertion with unknown standing remains contextual/advisory, not authoritative by convenience.

## Synchronizations / related canonical resources

Semantic Definition, Responsibility Assignment, Classification, Policy Context, Expectation and later governed assertion families consume standing without transferring assertion truth here. Capability Authorization separately governs who may create/revise rules/assertions. Explanation may expose safe authority context.

## Non-goals

Factual correctness, evidence sufficiency, IAM permission/enforcement, responsibility, policy applicability/compliance, vendor selection, or source availability/reliability scoring.

## Provenance

- `docs/concepts/phase_002/addenda/assertion_authority.md`
- `docs/concepts/phase_005/`
