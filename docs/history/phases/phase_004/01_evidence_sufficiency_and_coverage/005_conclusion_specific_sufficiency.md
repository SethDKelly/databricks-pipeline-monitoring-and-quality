# REF-005 — Conclusion-Specific Evidence Sufficiency Evaluation

**Status:** Accepted — Phase 004 Group 01

## Outcome

Determine whether an applicable evidence set is adequate to support a **specific conclusion for a specific purpose** under an explicit evidence standard, while preserving limitations and avoiding universal confidence scoring.

## Sufficiency target

A sufficiency evaluation binds:

- target proposition/conclusion;
- subject/context/time/grain/version scope;
- intended conclusion strength;
- applicable evidence set;
- Coverage Profile and known gaps;
- corroboration/conflict/common-derivation relationships;
- explicit evidence standard/rule version where defined;
- material limitations, restrictions, and unresolved dependencies;
- evaluation event/knowledge-time context when relevant.

## Sufficiency outcomes

A refinement may resolve as:

- **sufficient for the stated conclusion**;
- **insufficient**;
- **conflicting / indeterminate**;
- **non-applicable / non-comparable**;
- **unavailable**;
- **unknown**.

These outcomes do not become a new source fact and do not silently change the owning concept's state. They are the evidence-standard basis used by the applicable concept action or synchronization.

## Conclusion specificity

Sufficiency is always named with the conclusion.

Examples:

- sufficient to establish `at least one qualifying run occurred`;
- insufficient to establish `no qualifying run occurred`;
- sufficient to establish `consumer refreshed after version V existed` but insufficient to establish `consumer consumed V`;
- sufficient to establish `upstream job completed` but insufficient for a gate requiring `current qualifying output available`;
- sufficient to contradict `Deployment D initiated the degradation` but insufficient to identify the actual cause.

The framework should avoid generic labels such as `high confidence evidence` when they obscure what conclusion is actually justified.

## Evidence standards

A conclusion standard may specify required combinations of:

- applicability dimensions;
- bounded coverage expectations;
- opportunity-to-observe requirements;
- tolerated gaps;
- corroboration or complementary evidence requirements;
- conflict handling;
- measurement/derivation uncertainty;
- temporal ordering/knowledge-cut conditions;
- review/authority requirements for high-consequence status where separately defined.

Group 01 defines this structure, not every domain-specific threshold. Later Phase 004 groups specialize standards for temporal knowledge, causal confirmation, exposure/non-exposure, gate readiness/enforcement, and safeguard prevention.

## Invariants

- Sufficiency is not an intrinsic permanent property of an evidence item.
- Stronger or broader conclusions may require more coverage than narrower conclusions.
- `Insufficient` does not mean the proposition is false.
- `Sufficient` does not mean every related proposition is true.
- Lack of contradiction does not itself make a causal claim sufficient for confirmation.
- More evidence items do not automatically make evidence sufficient if they duplicate the same observation or fail to cover the required proposition dimensions.
- A sufficiency evaluation must expose material limitations even when the conclusion threshold is met.
- Sufficiency does not grant Capability Authorization, source authority, safeguard/gate authority, or action permission.
- A requester can receive an authorized safe sufficiency/result summary while restricted basis details remain hidden.
- If required evidence is inaccessible to the framework itself, the evaluation cannot treat that evidence as present merely because it may exist elsewhere.

## Relationship to accepted concepts

- **Observation** uses coverage/sufficiency to distinguish observed absence from missing telemetry.
- **Assessment** requires sufficient Observation/reference evidence for its basis-specific result.
- **Causal Claim** uses later specialized standards for support, contradiction, rejection, and confirmation.
- **Impact** uses later specialized standards for exposure/non-exposure and consequence evidence.
- **Execution Gate** uses later specialized standards for prerequisite readiness and enforcement evidence.
- **Propagation Safeguard** uses later specialized standards for activation/enforcement/prevented-exposure evidence.
- **Historical replay** uses Group 02 standards for eligibility under knowledge cutoffs and `not known by cutoff` claims.
- **Explanation** communicates the owning concept result and authorized limitations; it does not create sufficiency by rhetoric.

## Non-goals

- universal confidence/trust score;
- selecting statistical models;
- deciding every domain-specific threshold in Group 01;
- source authority;
- user authorization;
- architecture or persistence design.
