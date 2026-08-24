# REF-015 — Causal Support, Contradiction, and Evidence-Dimension Evaluation

**Status:** Accepted — Phase 004 Group 03

## Purpose

Refine how applicable evidence supports or contradicts a Causal Claim across causal reasoning dimensions without collapsing the result into one opaque score.

## Evidence dimensions

Evaluate only dimensions material to the claim, including:

1. **Cause occurrence** — did the proposed cause condition actually occur?
2. **Effect occurrence** — did the defined outcome actually occur?
3. **Temporal ordering** — did the cause occur early enough to influence the effect under the relevant event semantics?
4. **Relationship/mechanism applicability** — did the required dependency, join, control, or other mechanism exist and make the influence plausible at the relevant time?
5. **Encounter/transmission** — where transmission requires a version/state/output to be encountered, is that encounter evidenced?
6. **Directional/semantic compatibility** — is the observed change capable of producing the defined outcome in the proposed direction?
7. **Contrast/intervention evidence** — rollback, retry, restored input, unaffected peers/cohorts, or other sufficiently comparable contrasts where available.
8. **Alternative-explanation evidence** — does evidence support, contradict, or fail to discriminate material competing explanations?
9. **Coverage/exclusion evidence** — are negative or unchanged findings supported by enough opportunity-to-observe and bounded coverage to be meaningful?

## Rules

- Evidence links state which dimension(s) they bear on and whether they support, contradict, constrain, or are non-discriminating.
- One item can legitimately bear on several dimensions, but it is not counted as several independent observations.
- Duplicated/common-derived telemetry does not gain artificial causal weight.
- Lack of contradicting evidence is not support by itself.
- Temporal ordering is normally necessary for ordinary forward causation but is not sufficient for causation.
- Strong temporal contradiction can justify weakening or rejection only when timing/applicability coverage is sufficient.
- Mechanism compatibility supports plausibility; mechanism evidence plus encounter/state evidence may provide stronger support depending on the claim class.
- An Assessment or Baseline deviation is evidence about an outcome/condition, not causal proof by itself.
- Restricted evidence can materially affect internal status while remaining hidden from an unauthorized audience; visible limitations must not misstate hidden evidence as absent.

## Non-goals

- a fixed weighted causal score;
- requiring every claim to have evidence in every listed dimension;
- statistical causal-inference method selection.
