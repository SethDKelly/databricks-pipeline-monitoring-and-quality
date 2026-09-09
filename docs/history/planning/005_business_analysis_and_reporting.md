# 005 — Business Analysis, Question Answering, and Reporting

**Status:** Discovery input — refined/superseded where necessary by the accepted Phase 002 Explanation, Impact, Causal Claim, Assessment, Semantic Definition, Responsibility Assignment, Classification, and Policy Context concepts.

## Goal

Make pipeline/data-quality state understandable to business audiences while preserving enough evidence and epistemic detail for engineering follow-through.

## Primary interaction model

The product should answer questions such as:

- Is this asset healthy or stale according to applicable Expectations?
- Is behavior atypical versus Baseline even if no normative failure exists?
- What changed and was it planned?
- Which Deployment became active and what actually ran?
- Which causal explanations are supported, contradicted, confirmed under a standard, or unresolved?
- Which downstream consumers are reachable, actually exposed, visibly affected, or tied to evidenced business consequence?
- Who bears relevant responsibility?
- What Classification/Policy Context applies?
- What evidence supports each material statement?
- What was known during the incident versus what later evidence establishes?

## Explanation model

**Explanation** is the accepted foundational concept. A dashboard, chat answer, report, daily digest, or exported artifact is a possible presentation realization.

Different audiences may receive different authorized detail, but material conclusions must remain evidence-consistent.

### Business-facing layer

May emphasize:

- what changed/violated an Expectation;
- intended versus unintended context;
- known downstream exposure/consequence;
- current causal confidence/uncertainty;
- responsible party;
- safe business meaning/policy context.

### Analytical/engineering layer

May expose deeper Observation/Assessment basis, Change Intent, Deployment/execution sequence, Lineage paths, Causal Claim support/contradiction, Impact evidence, and historical knowledge state.

## Trust requirements

Statements must preserve their epistemic kind. For example:

- **Observed:** C produced 14M rows.
- **Assessment:** 14M satisfies the revised post-change volume Expectation but is non-comparable to the pre-change Baseline.
- **Observed:** completeness also fell and violates its Expectation.
- **Causal Claim — supported:** B population reduction contributed to C loss.
- **Causal Claim — unresolved:** join-key quality may also contribute.
- **Impact — exposed:** Report 1 refreshed from affected C.
- **Impact — candidate only:** Report 2 is downstream but has not refreshed.

The exact UI wording is deferred; these semantic distinctions are not.

## Historical explanation

The product should support both a contemporaneous knowledge view (`what was known then`) and retrospective view (`what we know now`) when later evidence changes the conclusion.

## Security

Explanation operates over an authorized evidence view. Restricted evidence, entities, claims, downstream consumers, or annotations cannot be retrieved merely to leak their substance through prose.

This planning note is not the authoritative concept definition; accepted Phase 002 specifications are.
