# AUTH-030 — Authorized Analytical Projection, Opacity, and Evidence Minimization

**Status:** Accepted — Phase 005 Group 04

## Purpose

Define Authorized Analytical Projection as a capability-filtered view over existing concept truth so restricted-data analysis remains useful without inventing a sanitized truth concept or retrieving hidden details merely to narrate them.

## Contract

For a requester/question, projection should resolve authorization independently for material result/basis/detail classes and may expose:

- exact permitted state;
- an authorized abstraction/summary;
- an opaque reference indicating relevant restricted state exists;
- an explicit limitation that evidence/detail is restricted;
- nothing, when even existence is not permitted to be disclosed.

## Invariants

- Authorized Analytical Projection is a synchronization/view, not a new truth-owning concept and not declassification.
- Projection does not mutate Observation, Assessment, Lineage, Causal Claim, Impact, governance, or control state.
- Permission to see a conclusion does not imply permission to see every basis item.
- Hidden evidence is never described as absent merely because the requester cannot see it.
- An opaque node may preserve path/reasoning continuity only when acknowledging its existence is authorized.
- Exact hidden-node counts, path lengths, labels, thresholds, metric values, or other seemingly aggregated details may still leak restricted information and require authorization.
- Explanation later consumes this projection; it must not fetch requester-hidden raw evidence merely to produce a more detailed narrative.

## Internal evidence distinction

The framework may internally hold sufficient restricted evidence while the requester receives only an authorized result/limitation. That is valid only when the framework/service principal itself is authorized to access/process the required evidence. If the framework lacks access, the evidence is unavailable and cannot be counted as internally present.
