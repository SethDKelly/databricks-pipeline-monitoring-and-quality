# Phase 004 Group 03 — Scenario Checks

**Status:** Accepted

These scenarios stress REF-013–REF-020 against the accepted Phase 003 ecosystem model.

## C-01 — A+B→C multiple contributors

C materially loses rows. B population declines and join-key nulls rise before C executes; C consumes the affected B state. Both propositions can be `supported` as contributing causes. Neither must be rejected merely because the other is supported, and no percentage attribution is invented.

**Pass condition:** multiple compatible contributors remain independently evaluated; no forced single root cause.

## C-02 — Deployment temporally impossible

A Deployment activates after sufficiently covered evidence establishes that the relevant degradation already existed.

**Pass condition:** the Deployment claim can be materially weakened or rejected depending on the claim/rejection standard; timing coverage must be sufficient before temporal impossibility is asserted.

## C-03 — Leading claim but unresolved alternative

B decline is the strongest observed hypothesis, but a restricted upstream dependency remains a material alternative and the evidence cannot discriminate it.

**Pass condition:** B may remain supported but cannot become confirmed merely because it is leading; the Investigation may remain unresolved.

## C-04 — Planned filter versus unintended completeness failure

A filter Change Intent predicts lower volume and realized volume matches. Completeness also fails.

**Pass condition:** intent consistency can support the volume explanation without confirming that the filter caused the completeness violation.

## C-05 — Direct safeguard-induced delay

An active/enforced safeguard blocks publication until review; delivery occurs late. Control enforcement and timing evidence strongly support `safeguard contributed to delivery delay`.

**Pass condition:** direct mechanism evidence can create strong support quickly, but `confirmed` still requires an applicable confirmation profile and authority. The safeguard state does not prove the quarantined data was defective.

## C-06 — Gate hold versus upstream lateness

Upstream output is late and an enabled gate holds C. C misses a delivery deadline.

**Pass condition:** separate claims may evaluate `upstream lateness contributed to C delay` and `gate hold contributed to C delay`; gate state alone does not decide either claim's epistemic status.

## C-07 — Fast RCA progression

At 07:12 timing/Lineage produce a proposed B claim. At 07:18 B-change and encounter evidence support it. At 07:30 join-key evidence adds another supported contributor. Later post-ops evidence changes the evidence picture.

**Pass condition:** each status is scoped to its knowledge cut; early support is useful but never narrated as confirmation.

## C-08 — Unresolved after substantial review

Several materially plausible claims remain and available evidence cannot discriminate them despite a completed investigation window.

**Pass condition:** claims can be `unresolved`; Investigation closure does not upgrade them.

## C-09 — Rejection is stronger than lack of support

No evidence supports a Deployment claim, but timing coverage is incomplete.

**Pass condition:** the claim is not rejected solely because support is absent. It can remain proposed/unresolved/weakened according to the evidence picture.

## C-10 — Historical confirmation challenged

A claim was legitimately confirmed under a then-applicable profile. Later corrected timing evidence undermines a required confirmation condition.

**Pass condition:** current status is reevaluated and may become weakened/unresolved/rejected while historical confirmation remains reconstructable.

## C-11 — Restricted confirmation basis

The internal evidence set satisfies a confirmation profile and an authorized confirmer acts, but the requesting analyst cannot inspect part of the basis.

**Pass condition:** the analyst may receive the authorized `confirmed` status and safe limitations where permitted; confirmation does not grant access to restricted evidence.

## C-12 — No default automated confirmation

Automated reasoning assembles strong causal evidence but no accepted policy grants the process confirmation capability for that claim class.

**Pass condition:** the system stops at the strongest non-confirmed status justified by evidence; it does not self-authorize confirmation.

## C-13 — Primary cause requires comparative evidence

Two contributors are supported, but no evidence establishes one as dominant.

**Pass condition:** neither is labeled `primary`; contribution role does not imply percentage allocation.

## C-14 — Confirmation can be fast when evidence is direct

A deterministic control mechanism emits direct evidence that an enforced action blocked a named publication boundary and the downstream publication did not occur through that boundary.

**Pass condition:** elapsed time is not itself a barrier to strong causal status; however, `confirmed` still requires the applicable profile and authority rather than a generic fast-path exception.

## Group result

All checks pass without a new concept, universal confidence score, single-root requirement, automated-confirmation default, causal algorithm, or source-authority decision.
