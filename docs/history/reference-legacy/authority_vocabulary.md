# Authority Vocabulary Reference

**Status:** Accepted — Phase 005 Group 01

This reference summarizes the authority vocabulary established by the **Assertion Authority** concept and AUTH-001–AUTH-008. The detailed normative contracts remain in `docs/concepts/phase_005/01_authority_vocabulary_and_conflict/`.

## Core terms

### Assertion Authority
Accepted concept that resolves which source/actor/role/governed process has authoritative standing for a bound assertion category/facet/subject scope/context/time. It is separate from Capability Authorization, Responsibility Assignment, evidence sufficiency, policy applicability, and enforcement.

### Source assertion
A provenance-bearing assertion contributed to its owning concept regardless of authority standing.

### Authority target
The bounded assertion domain for authority resolution: owning concept/category plus relevant facet/scheme/type, subject scope, context, effective interval, and knowledge cut where applicable.

### Authority holder
The source, actor, role, organizational authority, or governed process referenced by an authority rule.

### Authority rule
A provenance-bearing rule establishing holder standing, conditions, and any explicit sole/co-authority/precedence/fallback semantics for an authority target.

### Governing basis
The explicit provenance/trust basis supporting use of an authority rule. An authority rule cannot self-validate merely by asserting authority over itself.

### Authoritative assertion
An applicable source assertion whose source/actor has authoritative standing under the applicable accepted authority rule.

### Advisory assertion
An applicable assertion that may enrich, challenge, or contextualize but cannot displace authoritative state for the bound target.

### Explicitly non-authoritative assertion/source
An assertion/source explicitly excluded from authoritative standing for the target. This does not mean the assertion is deleted or necessarily false.

### Conditional authority
Authority standing that applies only when explicit rule conditions are satisfied.

### Fallback authority
Conditional authority that applies when an explicit fallback condition is satisfied, for example evidenced unavailability of a primary authority. Source availability alone never creates fallback authority.

### Co-authority
An explicit rule granting multiple holders authoritative standing concurrently. Co-authoritative disagreement remains authoritative conflict unless another accepted resolver applies.

### Ordered precedence
An explicit authority rule that orders otherwise eligible holders. Precedence resolves standing/current governed state but does not erase lower-precedence assertions or make the winner factually infallible.

## Conflict terms

### Assertion disagreement
Applicable source assertions materially disagree for the same target/context/time.

### Resolved assertion disagreement
Assertions disagree, but accepted authority rules yield an authoritative resolution. Dissenting assertions remain provenance-bearing.

### Authoritative assertion conflict
Two or more simultaneously authoritative assertions materially disagree and no accepted resolver applies.

### Authority-rule conflict
Applicable authority rules disagree about holder standing, precedence, conditions, scope, or time and no accepted governing rule resolves them.

### Authority unknown
No applicable accepted authority rule can be established.

### Authority unavailable
Required authority-rule/source information cannot currently be obtained. Unavailable does not mean no rule exists and does not promote another source automatically.

## Prohibited hidden precedence

The framework must not infer authority merely from:

- source count / majority;
- recency alone;
- synchronization or ingestion order;
- source availability;
- repository ownership;
- job creator identity;
- administrator or organizational title;
- Responsibility Assignment;
- apparent scope specificity.

Any desired precedence, including specific-over-broad behavior, must be explicit in an accepted authority rule.

## Key separations

**Assertion Authority ≠ Capability Authorization**  
Permission to create/edit an assertion does not make it authoritative; authoritative standing does not grant unrelated permission.

**Assertion Authority ≠ Responsibility Assignment**  
Being responsible/steward/owner does not automatically confer authority for every assertion category.

**Assertion Authority ≠ evidence sufficiency**  
An authoritative source cannot make incomplete/irrelevant evidence sufficient for a runtime, causal, exposure, readiness, or enforcement conclusion.

**Assertion Authority ≠ factual infallibility**  
Authoritative assertions can later be corrected or challenged.

**Assertion Authority ≠ enforcement**  
An authoritative rule/policy does not prove that an external access control, Execution Gate, safeguard, job operation, or other mechanism actually enforced it.

## Historical rule

Authority uses effective time plus recorded/knowledge time. Prospective changes, correction, supersession, retirement, and late discovery remain distinct. A later correction may change current retrospective authority resolution without rewriting what authority was known/used at the earlier cutoff.
