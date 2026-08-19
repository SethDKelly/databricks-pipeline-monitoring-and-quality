# Concept: Classification

**Status:** Accepted — Phase 002 Group 02

## Purpose

Let the ecosystem state that an identified subject belongs to one or more categories in a named governance or sensitivity vocabulary without turning category membership into policy, authorization, or compliance conclusions.

## Operational principle

A table involved in an investigation is classified as PHI and PII by an authoritative governance source. Another system supplies a separate internal confidentiality tier. The product preserves each classification in its original vocabulary and provenance. Those categories can inform Policy Context, but the classification itself does not decide who may access the table or whether any legal/control requirement has been satisfied.

## Actors

- Data Steward / Governance Steward
- Security / Privacy / Compliance Stakeholder
- Data Engineer / Pipeline Maintainer
- Business Analyst / Data Consumer
- Monitoring framework

## State

- identified subject and optional classified facet/context;
- classification scheme/vocabulary;
- category/label as asserted by the source;
- source meaning or scheme reference when available;
- effective interval;
- assertion provenance, actor/source, and authority context;
- optional normalization/crosswalk evidence without replacing the source label;
- supersession/correction history;
- unresolved or conflicting classification assertions.

## Actions

### `classify`
- **Intent:** record or synchronize a classification assertion under a named scheme.
- **State effect:** preserves the source category, scheme, provenance, and relevant effective time.

### `reclassify`
- **Intent:** prospectively supersede a classification assertion while preserving history.

### `resolveAt`
- **Intent:** return classifications applicable to a subject/facet, scheme/context, and time.
- **Observable result:** applicable classification assertion(s), unknown, explicitly unclassified under a scheme when such an assertion exists, conflicting, unauthorized, or unavailable.
- **Conflict behavior:** synchronization order does not choose a winner when assertions conflict.

## Invariants / behavioral expectations

- Classification is categorical metadata; it is not authorization.
- Classification is not Policy Context and does not itself encode handling requirements.
- PII, PHI, confidentiality, criticality, or other labels are assertions within a defined vocabulary; their meaning must not be assumed universal across organizations/sources.
- A source label is retained even when a normalization/crosswalk is also available.
- Multiple classifications from independent schemes can simultaneously apply without conflict.
- Missing classification evidence is `unknown`, not `non-sensitive` or `unclassified`.
- `Unclassified` is meaningful only when explicitly asserted within a relevant scheme.
- Current classification does not overwrite historical classification.
- Classification does not prove legal compliance or the operation of any control.

## Ambiguity and missing evidence

If classification is absent, the product does not infer safety from names, schemas, or lack of labels. Conflicts within a relevant scheme/context remain visible until an accepted authority rule resolves them. Restricted classification details may be withheld while still allowing a safe indication that special handling or restricted context exists.

## Synchronizations

- **Entity Identity** supplies the classified subject.
- **Responsibility Assignment** may identify stewardship or privacy/security responsibility without making that assignment itself a classification.
- **Policy Context** may use classification assertions as evidence or applicability inputs, but policy applicability is independently asserted/resolved.
- **Explanation** may use authorized classification context to communicate sensitivity without exposing restricted values.
- **Change** can represent classification changes across time without treating the change as a data-quality event.

## Security / privacy / governance considerations

Classification metadata can reveal the presence of sensitive information and may itself require restricted visibility. The concept must support safe disclosure at an allowed abstraction level.

## Evidence / provenance considerations

Classification assertions retain the original scheme, category, source/actor, assertion time, effective time, and any crosswalk/normalization evidence. Any later effective-selection rule must remain explainable from the assertions and authority policy.

## Representative scenarios

### Happy path
A table is consistently classified as PHI/PII by the applicable governance authority and retains those labels with provenance.

### Multiple vocabularies
The same asset is `PHI` in one scheme and `Restricted` in an internal confidentiality scheme. Both apply and are not treated as contradictory merely because the labels differ.

### Missing classification
An important asset has no known classification assertion. The result is `unknown`, not `non-sensitive`.

### Conflicting classification
Two sources using the same applicable classification scheme assign incompatible sensitivity categories. The conflict remains explicit.

### Historical replay
A table is reclassified after a business-use change. Earlier incident analysis resolves the classification that applied at that earlier time.

### Unauthorized evidence
A user may be told that restricted handling context exists without being shown a classification label that would reveal sensitive subject matter.

## Non-goals

- enforcing access;
- defining or applying policy requirements;
- legal interpretation or compliance determination;
- defining business semantics;
- deciding which source is authoritative by synchronization order;
- treating absence of classification as evidence of non-sensitivity.

## Deferred questions

- Which classification schemes/categories are required for MVP?
- Which entity/facet kinds need classification in MVP, including columns or metrics if they receive Entity Identity?
- Which source vocabularies should be crosswalked for comparison while preserving original labels?
- What source-precedence rules apply within each scheme/context?
