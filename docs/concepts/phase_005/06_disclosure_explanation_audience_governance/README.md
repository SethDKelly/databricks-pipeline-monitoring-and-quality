# Phase 005 Group 06 — Disclosure, Explanation & Audience Governance

**Status:** Next review group — not yet started

## Goal

Govern what authorized audiences may learn from otherwise valid ecosystem truth without creating different truth models for technical and business users, and without exposing sensitive high-consequence control/authorization detail merely because the underlying action or conclusion is valid.

## Accepted handoff from Groups 01–05

- Assertion Authority and AUTH-001–AUTH-043 are accepted;
- Authorized Analytical Projection is a requester-capability-filtered view, not declassification or a new truth concept;
- result visibility may differ from basis visibility, and hidden evidence must remain represented as restricted rather than absent;
- derived/aggregate metric, schema, Lineage, causal, Impact, control, authority, and authorization details can themselves be sensitive;
- proposal/request, approval, execution, enforcement, and outcome are distinct high-consequence facts;
- causal confirmation can be visible without disclosing restricted confirmer identity, evidence, or profile detail when authorization requires opacity;
- gate/safeguard/job/break-glass/delegation state may reveal sensitive operational controls or incident posture;
- current requester authorization governs present disclosure even for historical replay.

## Primary review questions

- disclosure of metric values versus health summaries, thresholds/Baselines, schema details, Policy Context, Lineage, Causal Claims, Impact, safeguards, gates, Annotations, and business consequences;
- disclosure of high-consequence approval/override/break-glass/delegation/automation state and whether actor identity or control details may be opaque;
- acknowledgment of restricted entities/paths while keeping identities/details hidden;
- technical diagnostic views versus business semantic health projections over the same truth;
- which high-consequence statements require additional review before business/client-facing Explanation;
- safe redaction/abstraction without inference leakage, false precision, or false absence;
- communicating `confirmed`, `overridden`, `held`, `released`, or `break-glass` without implying broader health/safety/compliance conclusions;
- historical authorization/disclosure detail and current requester limits;
- disclosure of unresolved/conflicting authority or authorization without exposing restricted rule/source details.

## Boundaries

This group governs disclosure/review constraints, not the underlying permission truth already defined in Group 04 or high-consequence action authority defined in Group 05. Phase 006 defines health/metric semantics and Phase 008 defines detailed Explanation/question UX. Explanation remains a projection over authorized truth, not an independent truth source.

Do not select redaction/declassification technology, UI architecture, LLM behavior, report templates, or vendor-specific policy engine.

## Exit direction

Group 06 exits when disclosure rules can support detailed engineering analysis and appropriately abstracted business/client communication while preserving exact epistemic/control status, current authorization, opacity, and inference-leakage constraints.

**Group 06 has not started.**
