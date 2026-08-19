# Group 02 — Semantics, Governance & Policy

**Status:** Review complete — concepts accepted

## Goal

Define how the product represents **meaning**, **named responsibility**, **classification**, and **declared policy applicability/context** as separate provenance-bearing facts attached to identified entities.

## Accepted concepts

- [Semantic Definition](semantic_definition.md)
- [Responsibility Assignment](responsibility_assignment.md)
- [Classification](classification.md)
- [Policy Context](policy_context.md)

## Boundary decisions

### 1. Semantic meaning is facet- and context-aware

Semantic Definition is not a single canonical description string. Business definition, technical description, grain, units, population rules, calculation meaning, and other semantic facets may coexist. Context-specific assertions can both be valid; incompatible assertions in the same relevant context remain conflicts.

### 2. `Ownership` is renamed `Responsibility Assignment`

The candidate behavior covered technical ownership, business accountability, stewardship, and privacy/security responsibility. Calling all of that `Ownership` would overload the term and risk making an "owner" appear universally authoritative.

Responsibility Assignment records **who bears which named responsibility**, at what time, and from what source. Technical owner, business accountable party, steward, policy/security contact, and similar assignments remain distinct.

### 3. Classification is categorical; handling belongs to Policy Context

Classification states category membership in a named scheme/vocabulary. It does not itself grant access, encode handling obligations, or prove compliance.

Policy Context states which declared policies/handling expectations are asserted to apply in a relevant subject/context/time. Classification may support that applicability, but classification and policy remain separate concepts.

### 4. No concept silently manufactures authority precedence

All four concepts preserve assertions, provenance, effective time, and conflict. When two relevant sources disagree, synchronization order is never an authority rule. Until source-precedence/authority semantics are explicitly accepted, conflict remains a valid result.

This repeated need may later justify an independent authority concept or may be realized through integration/metadata-category contracts. Group 02 deliberately does not decide that boundary prematurely.

### 5. Missing governance information is not a safe default

- missing semantic definition ≠ inferred meaning;
- missing responsibility assignment ≠ explicitly unassigned;
- missing classification ≠ non-sensitive/unclassified;
- missing policy context ≠ unrestricted.

Unknown and incomplete governance context are first-class results.

### 6. Governance metadata is itself sensitive

Definitions, classifications, responsibilities, and policy applicability can reveal restricted business/data information without exposing row values. All four concepts therefore support authorization-aware or abstracted disclosure while remaining separate from authorization itself.

## Scenario review

### S-01 — Join-volume degradation

Pass. A, B, and C can carry independent semantics, responsibilities, classifications, and policy context. Semantic grain/join meaning can inform explanation without becoming a health observation; responsibility can route investigation without asserting cause.

### S-02 — Stale upstream with successful downstream execution

Pass. Group 02 supplies contextual meaning/responsibility only and does not conflate semantic or policy metadata with freshness/execution health.

### S-03 — Deployment-correlated shift

Pass. Semantic, responsibility, classification, or policy changes can be historically resolved and later correlated with a deployment without being treated as deployment causation.

### S-04 — Cross-repository dependency

Pass. Responsibility and governance assertions attach to Entity Identity rather than inheriting automatically from repository boundaries.

### S-05 — Conflicting governance metadata

Pass. This is a core group behavior: conflicting definitions, responsibility assignments, classifications, or policy assertions retain provenance and remain unresolved unless an accepted authority rule exists.

### S-06 — Policy-sensitive explanation

Pass. A viewer can receive a safe semantic summary, team-level responsibility contact, or indication that special handling applies without receiving restricted classification/policy details or raw data.

### S-07 — Historical replay

Pass. Effective-time and supersession history preserves the definitions, responsibilities, classifications, and policy context that applied at the incident time.

## Deferred questions

- exact MVP semantic facets and responsibility types;
- authority/source-precedence rules by metadata category;
- whether an independent Assertion Authority concept is justified in a later boundary review;
- which classification vocabularies/crosswalks are required;
- which policy context dimensions and summaries are required for MVP;
- whether criticality should remain a classification scheme/facet or become a separate concept when Impact is reviewed.

## Group exit gate

**Satisfied.** The product can represent meaning, named responsibility, categorical sensitivity/governance metadata, and declared policy applicability as separate provenance-bearing concepts; conflicts and missing context remain explicit; none of the concepts grants access or claims compliance.

The next review group is **Group 03 — Health Evaluation**.
