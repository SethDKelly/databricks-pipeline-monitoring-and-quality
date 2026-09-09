# Concept: Classification

**Status:** Accepted — Phase 002 Group 02; authority/criticality refined by Phase 005 Group 02

## Purpose

Let the ecosystem state that an identified subject belongs to one or more categories in a named governance, sensitivity, or criticality vocabulary without turning category membership into policy, authorization, health, Impact, or compliance conclusions.

## Operational principle

A table involved in an investigation is classified as PHI and PII under one governed scheme, `Restricted` under an internal confidentiality scheme, and `Tier 1` under an operational-criticality scheme. The product preserves each classification in its original vocabulary, context, authority standing, and provenance. Those categories can inform Policy Context or prioritization, but classification itself does not decide who may access the table, whether a policy applies, whether a control operated, or whether actual downstream Impact occurred.

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
- assertion provenance, actor/source, and Assertion Authority context;
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
- **Conflict behavior:** authority is resolved within the named scheme/context; synchronization order does not choose a winner.

## Invariants / behavioral expectations

- Classification is categorical metadata; it is not authorization.
- Classification is not Policy Context and does not itself encode handling requirements.
- PII, PHI, confidentiality, business criticality, operational criticality, delivery criticality, or other labels are assertions within a defined vocabulary; their meaning must not be assumed universal across organizations/sources.
- Authority for one classification scheme does not automatically transfer to another scheme.
- A source label is retained even when a normalization/crosswalk is also available.
- A crosswalk/normalization is itself a governed provenance-bearing assertion with separately resolvable authority.
- Multiple classifications from independent schemes can simultaneously apply without conflict.
- Business, operational, consumer, and delivery criticality may legitimately differ by named scheme/context.
- Criticality influences priority/context but is not evidence of actual exposure, downstream effect, business consequence, causal severity, or health failure.
- Missing classification evidence is `unknown`, not `non-sensitive`, `unclassified`, or low criticality.
- `Unclassified` is meaningful only when explicitly asserted within a relevant scheme.
- Current classification does not overwrite historical classification.
- Classification does not prove legal compliance or the operation of any control.
- Lineage, schema similarity, tag similarity, repository/container membership, or parent-domain classification does not automatically propagate a classification to another subject; derived/inherited assertions require explicit provenance and standing.

## Ambiguity and missing evidence

If classification is absent, the product does not infer safety or criticality from names, schemas, downstream use, or lack of labels. Conflicts within a relevant scheme/context remain visible until accepted Assertion Authority rules resolve them. Restricted classification details may be withheld while still allowing a safe indication that special handling or high-priority context exists.

## Synchronizations

- **Entity Identity** supplies the classified subject.
- **Assertion Authority** determines standing within a named scheme/context/time without owning the classification assertion.
- **Responsibility Assignment** may identify stewardship or privacy/security responsibility without making that assignment itself a classification or authority grant.
- **Policy Context** may use classification assertions as evidence or applicability inputs, but policy applicability is independently asserted/resolved.
- **Impact** may use criticality as prioritization/context but cannot convert criticality into exposure/effect/consequence evidence.
- **Explanation** may use authorized classification/criticality context to communicate sensitivity or importance without exposing restricted values.
- **Change** can represent classification/criticality changes across time without treating the change as a data-quality event.

## Security / privacy / governance considerations

Classification and criticality metadata can reveal the presence of sensitive information, important business processes, or client-delivery priorities and may itself require restricted visibility. The concept must support safe disclosure at an allowed abstraction level.

## Evidence / provenance considerations

Classification assertions retain the original scheme, category, source/actor, assertion time, effective time, and any crosswalk/normalization evidence. Any effective-selection rule must remain explainable from the assertions and Assertion Authority rules.

## Representative scenarios

### Happy path
A table is consistently classified as PHI/PII by the applicable authority and retains those labels with provenance.

### Multiple vocabularies
The same asset is `PHI` in one scheme, `Restricted` in an internal confidentiality scheme, and `Tier 1` in operational criticality. All can apply without conflict.

### Context-specific criticality
A dataset is ordinary for internal analytics but `Client Critical` for a named external-reporting consumer. The criticality assertion remains context-scoped instead of becoming a universal label.

### Crosswalk
A governed crosswalk maps a source sensitivity label to an internal handling tier. The original source label and the crosswalk provenance are retained.

### Missing classification
An important asset has no known classification assertion. The result is `unknown`, not `non-sensitive` or low priority.

### Conflicting classification
Two co-authoritative sources using the same applicable scheme assign incompatible categories. The authoritative conflict remains explicit.

### Historical replay
A table is reclassified after a business-use change. Earlier incident analysis resolves the classification that applied at that earlier time.

### Unauthorized evidence
A user may be told that restricted/high-priority handling context exists without being shown a label that would reveal sensitive subject matter.

## Non-goals

- enforcing access;
- defining or applying policy requirements;
- legal interpretation or compliance determination;
- defining business semantics;
- proving health or Impact;
- deciding source authority by synchronization order;
- treating absence of classification as evidence of non-sensitivity/low criticality;
- creating a universal criticality score.

## Deferred questions

- Which classification and criticality schemes/categories are required for MVP?
- Which entity/facet kinds need classification in MVP, including columns or metrics if they receive Entity Identity?
- Which source vocabularies should be crosswalked for comparison while preserving original labels?
- Which concrete sources/actors are authoritative within each scheme/context in the deployment environment?
