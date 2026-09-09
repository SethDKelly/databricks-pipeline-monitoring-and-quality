# AUTH-048 — Audience Projection Consistency Across Technical, Business, Executive, and Audit Views

**Status:** Accepted — Phase 005 Group 06

## Purpose
Allow different audiences to receive different levels of detail while preserving one underlying truth and the same epistemic/control meaning.

## Contract
Audience projections may emphasize different permitted facets, for example:
- technical: exact metrics, thresholds, schema, timing, evidence, Lineage, and diagnostic detail;
- business: semantic health, freshness/readiness, affected business population, consequence, and responsibility context;
- executive: material status, consequence, uncertainty, decision/control posture, and recovery context;
- audit/review: provenance, authority/authorization, temporal history, approvals, and retained evidence where independently authorized.

## Invariants
- Audience category does not itself grant authorization.
- Different views may differ in vocabulary, granularity, and visible basis but must not intentionally contradict the same underlying state.
- A business summary may say `completeness degraded` while an engineer sees the exact null rate and threshold; both refer to the same Assessment.
- A simpler audience view must preserve material uncertainty, conflict, waiver, causal status, exposure, and control distinctions rather than flatten them for readability.
- Technical detail is not inherently more truthful, and business abstraction is not a separate truth model.
- Phase 008 later chooses concrete question/Explanation structures and UI behavior.
