# Phase 005 Group 06 — Disclosure, Explanation & Audience Governance

**Status:** Accepted — AUTH-044–AUTH-053

## Goal

Govern what an authorized audience may learn and how that truth may be communicated without creating separate truth models, weakening evidence/control semantics, or leaking restricted details through abstraction, composition, or high-consequence publication.

## Accepted handoff from Groups 01–05

- Assertion Authority and AUTH-001–AUTH-043 are accepted;
- Capability Authorization and Authorized Analytical Projection own requester/detail permission truth;
- result visibility may differ from basis visibility, and restricted evidence remains restricted rather than absent;
- derived/aggregate metric, schema, Lineage, causal, Impact, control, authority, authorization, and high-consequence action details can themselves be sensitive;
- proposal/request, approval, issuance, enforcement, and outcome remain distinct;
- current requester authorization governs current disclosure, including historical replay;
- Explanation is a projection over authorized concept state, not a truth source.

## Accepted contracts

- **AUTH-044 — Disclosure Target, Audience, Purpose, Context, and Delivery Binding**
- **AUTH-045 — Result, Basis, Provenance, and Detail-Level Disclosure Separation**
- **AUTH-046 — Safe Abstraction, Redaction, Opaque Existence, and Minimization**
- **AUTH-047 — Composite, Mosaic, and Repeated-Query Inference-Leakage Governance**
- **AUTH-048 — Audience Projection Consistency Across Technical, Business, Executive, and Audit Views**
- **AUTH-049 — High-Consequence Communication Review, Approval, Release, Correction, and Retraction**
- **AUTH-050 — Status-Preserving Language and Non-Overstatement in Disclosure**
- **AUTH-051 — Disclosure of Human Attribution, Authority, Authorization, and Control Metadata**
- **AUTH-052 — Historical Disclosure, Retained Explanation, and Current-Authorization Separation**
- **AUTH-053 — Disclosure Conflict, Unknown/Unavailable Review State, and Safe Non-Disclosure**

## Core accepted distinctions

### Disclosure is target- and delivery-specific

A requester may be allowed to inspect a fact privately without being allowed to publish/export it to another audience. Audience labels such as `technical`, `business`, `executive`, `client`, or `auditor` are context, not permission sources.

### Result visibility does not imply basis visibility

An analyst may see `completeness degraded` while exact null rate, threshold, sensitive field, authority basis, confirmer identity, or supporting evidence remains restricted. Hidden basis remains internally traceable and cannot be narrated as absent.

### Safe abstraction preserves meaning

Authorized abstraction may expose exact state, a coarser category/range, redacted detail, opaque existence, or an explicit restriction limitation. It must preserve critical distinctions such as supported versus confirmed, reachable versus exposed, not-exposed versus fresh, decision versus enforcement, and waived versus clean pass.

### Inference leakage is compositional

Individually permitted metrics, counts, path lengths, timestamps, role names, or repeated narrow queries can combine to identify restricted state. Disclosure safety therefore considers material mosaic/differencing risk rather than evaluating each field in isolation.

### Technical and business views remain one truth

Engineering, business, executive, and audit projections can differ in detail and vocabulary, but they cannot intentionally contradict the same underlying state. Technical detail is not a separate truth, and business simplification cannot strengthen uncertainty or remove material conflict.

### High-consequence communication can require separate review

Permission to view a valid fact does not automatically grant permission to publish a client-facing, regulatory/compliance-adjacent, causal-confirmation, break-glass, or other explicitly governed high-consequence statement. Compose/review/approve/release/correct/retract may be separately governed stages. Communication approval does not make the statement true.

### Disclosure language cannot upgrade state

`supported` cannot become `confirmed root cause`; `reachable` cannot become `affected`; `hold decided` cannot become `hold enforced`; `safeguard active` cannot become `prevented exposure`; `released` cannot become `healthy`; `waived` cannot become an underlying clean pass; authoritative standing cannot become factual infallibility; Policy Context cannot become compliance certification.

### Actor/control metadata can itself be sensitive

A requester may be allowed to know that a causal claim is confirmed, a gate was overridden, or break-glass was used while being denied the confirmer/operator identity, approval chain, delegation detail, service-principal identity, or governing rule. Internal provenance remains intact.

### Historical disclosure is non-rewriting

A retained historical Explanation records what was actually communicated. A present `as-known-then` Explanation is reconstructed unless historical evidence proves otherwise. Historical visibility does not grant current access, and present access does not imply historical access.

### Unresolved disclosure state is not permission

Unknown, conflicting, unavailable, or unsafe-to-project disclosure state never becomes permission. A product may safely withhold a response, but that operational refusal does not fabricate an explicit deny decision or imply the hidden fact does not exist.

## Scenario result

[`scenario_checks.md`](scenario_checks.md) passes representative restricted-metric, opaque-Lineage, causal-status, high-consequence publication, break-glass, Annotation, historical replay, and mosaic-inference scenarios.

No new Concept is required. **Capability Authorization + Authorized Analytical Projection govern what may be disclosed; Explanation owns composed/retained communication state; source concepts retain truth. The catalog remains 24 concepts.**

## Boundaries preserved

Group 06 does **not**:

- create a separate business/executive truth model;
- select UI/chat/report templates, LLM/rules composition, redaction, privacy-budget, or policy-engine technology;
- grant access or declassify restricted evidence;
- redefine metric/schema health, causal status, Impact, control, authority, or authorization truth;
- turn communication review into evidence/causal/control authority;
- treat an audience label as a role/permission source;
- begin Phase 006 or Phase 008 implementation/design.

## Exit

**Group 06 is accepted with AUTH-044–AUTH-053. AUTH-001–AUTH-053 are accepted overall. Group 07 — Consolidation / Exit Review is next and has not started.**
