# Authority Vocabulary

**Canonical key:** `authority.vocabulary`

**Kind:** AUTHORITY

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `reference.authority_vocabulary`

**Owns current question:** What shared terms distinguish assertion standing, authority rules and authority conflicts from permission, responsibility, evidence sufficiency and enforcement?

**Stable IDs:** AUTH-001–AUTH-008 provide the governing contract semantics.

## Current semantics

- **source assertion** — provenance-bearing assertion in its owning concept regardless of standing;
- **authority target** — bounded assertion concept/category/facet/scheme/type plus subject scope, context and time;
- **authority holder** — source, actor, role, organizational authority or governed process referenced by a rule;
- **authority rule** — provenance-bearing rule establishing holder standing, conditions and explicit sole/co-authority/precedence/fallback behavior;
- **governing basis** — trust/provenance basis supporting use of the authority rule; a rule cannot self-validate;
- **authoritative assertion** — applicable assertion whose source/actor has authoritative standing for the target;
- **advisory assertion** — usable context that cannot displace authoritative state;
- **explicitly non-authoritative** — deliberately excluded from authoritative standing without implying falsehood or deletion;
- **conditional/fallback authority** — standing available only when explicit conditions are satisfied; availability alone never creates fallback;
- **co-authority** — explicit concurrent authoritative standing for multiple holders;
- **ordered precedence** — explicit ordering of otherwise eligible holders; lower-standing assertions remain retained.

### Conflict vocabulary

- **assertion disagreement** — applicable assertions materially disagree;
- **resolved assertion disagreement** — disagreement remains recorded but accepted authority rules yield an authoritative resolution;
- **authoritative assertion conflict** — simultaneously authoritative assertions disagree with no accepted resolver;
- **authority-rule conflict** — applicable authority rules disagree with no governing resolver;
- **authority unknown** — no applicable accepted rule can be established;
- **authority unavailable** — required authority-rule/source information cannot currently be obtained.

## Invariants / boundaries

Authority is never inferred from source count, majority, recency, synchronization/ingestion order, availability, repository ownership, job creator, administrator/title, Responsibility Assignment or apparent specificity. Specific-over-broad precedence also requires an explicit rule.

Assertion Authority ≠ Capability Authorization ≠ Responsibility Assignment ≠ evidence sufficiency ≠ factual infallibility ≠ enforcement. Authority uses effective and knowledge time; later correction may alter current retrospective resolution without rewriting what was known/used earlier.

## Synchronizations / related canonical resources

See canonical Assertion Authority and Capability Authorization concepts; AUTH-001–AUTH-008 define the detailed rule semantics.

## Provenance

- `docs/reference/authority_vocabulary.md`
- `docs/concepts/phase_005/01_authority_vocabulary_and_conflict/README.md`
