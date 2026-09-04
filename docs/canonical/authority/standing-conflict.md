# Assertion Standing, Rules & Conflict

**Canonical key:** `auth.standing-conflict`

**Kind:** AUTHORITY

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.AUTH`

**Owns current question:** How is authoritative standing resolved for source assertions without hidden precedence or conflation with evidence, permission or enforcement?

**Stable IDs:** AUTH-001–AUTH-008

## Current semantics

### AUTH-001 — Authority Target Binding and Vocabulary
Authority resolves for an exact assertion target: owning concept/category, relevant facet/scheme/type, subject scope, context and time. No source is globally authoritative by default.

### AUTH-002 — Authority Rule Provenance and Governing Basis
Authority rules retain provenance and accepted governing basis. A rule cannot establish its own legitimacy merely by asserting authority over authority.

### AUTH-003 — Assertion Standing and Conditional Authority
Standing distinguishes authoritative, advisory, explicitly non-authoritative, conditional, unknown, unavailable and conflicting states. Conditional standing requires its rule conditions to be evidenced.

### AUTH-004 — Assertion Disagreement and Authority Conflict
Assertion disagreement, resolved disagreement, authoritative assertion conflict and authority-rule conflict are distinct. Conflict is not erased merely to produce one answer.

### AUTH-005 — Explicit Precedence, Co-Authority, and Fallback
Sole authority, co-authority, ordered precedence and fallback are valid only when explicitly governed. Fallback requires both a rule and evidence its activation condition holds.

### AUTH-006 — Authority Revision, Correction, Supersession, and Time
Authority is bitemporal. Prospective revision, correction, supersession and retirement preserve historical/as-known authority and rule-conflict state.

### AUTH-007 — Unknown, Unavailable, and Resolution Limits
Unknown/unavailable standing never authorizes use of the most convenient, newest or currently reachable source as authoritative.

### AUTH-008 — Authority Separation from Evidence, Permission, Responsibility, Policy, and Enforcement
Authoritative standing does not manufacture factual correctness, REF sufficiency, Capability Authorization, responsibility, policy applicability, compliance or enforcement.

## Invariants / boundaries

No hidden precedence from majority, recency, ingestion/synchronization order, availability, repository ownership, job creator, title/admin, Responsibility Assignment or specificity. Co-authoritative conflict remains conflict absent an explicit resolver.

## Provenance

- `docs/concepts/phase_005/01_authority_vocabulary_and_conflict/README.md`
- canonical `authority/vocabulary.md` is the compact term reference.
