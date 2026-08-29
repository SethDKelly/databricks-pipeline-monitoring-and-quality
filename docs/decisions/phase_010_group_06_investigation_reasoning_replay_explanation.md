# Phase 010 Group 06 — Investigation, Reasoning, Historical Replay & Explanation Architecture Decisions

**Status:** COMPLETE / ACCEPTED

### D-1491 — Reasoning is derived and cannot become a truth owner
**Status:** Accepted

Reasoning evaluates canonical evidence and accepted rules; it does not create source truth, authority, permission, Impact, causality or historical communication.

### D-1492 — Investigation receives a durable canonical identity
**Status:** Accepted

Investigation identity is independent from alert, ticket, model session, chat or UI identity.

### D-1493 — Investigation scope is revisioned and non-rewriting
**Status:** Accepted

Question, subject, population, event window, knowledge cut and purpose changes produce explicit revisions.

### D-1494 — Investigation lifecycle is a non-rewriting journal
**Status:** Accepted

Open, active, paused, closed, reopened and superseded history remains reconstructable.

### D-1495 — Leads remain inquiry/workflow state
**Status:** Accepted

A lead is not a Causal Claim and does not gain truth from prioritization.

### D-1496 — Lead origin does not create authority
**Status:** Accepted

Human, rule, graph, search, anomaly or model origin changes provenance only.

### D-1497 — Lead exclusion is evidence-bearing
**Status:** Accepted

Exclusion requires proposition-specific contradiction/exclusion evidence and adequate coverage; lack of support is not exclusion.

### D-1498 — Investigation annotations remain commentary unless separately evidenced
**Status:** Accepted

Annotation authorship does not create source truth.

### D-1499 — Investigation evidence links retain statement-relative roles
**Status:** Accepted

Supporting, contradicting, limiting, contextual and searched-with-no-match roles remain explicit.

### D-1500 — Late evidence can reopen without rewriting history
**Status:** Accepted

Current retrospective Investigation state may change while earlier knowledge and actions remain historical facts.

### D-1501 — Reasoning graph is rebuildable projection
**Status:** Accepted

Canonical evidence remains in Group 02 journals.

### D-1502 — Reasoning edges are semantically typed
**Status:** Accepted

Lineage, consumed, produced, measured, encounter, exposure, effect, basis and temporal edges cannot be interchanged.

### D-1503 — Derived edges retain exact provenance
**Status:** Accepted

Every reasoning edge resolves to canonical evidence or a versioned derivation rule.

### D-1504 — Graph traversal is bounded
**Status:** Accepted

Traversal binds proposition, identity/scope, time, relationship types, depth/path, authorization and evidence availability.

### D-1505 — Graph proximity is not causal rank
**Status:** Accepted

Distance, centrality, descendant count and path count may guide navigation only.

### D-1506 — Delta node/edge projection is the MVP graph realization
**Status:** Accepted

No dedicated graph database is required for the MVP.

### D-1507 — Dedicated graph technology requires measured need
**Status:** Accepted

A graph engine may be added for demonstrated scale/latency needs but remains derived.

### D-1508 — Exact structured retrieval precedes semantic retrieval
**Status:** Accepted

Canonical ID/proposition/time/scope retrieval is truth-bearing.

### D-1509 — Semantic/vector retrieval is candidate recall only
**Status:** Accepted

Similarity cannot create relevance, authority, evidence status, causal status or completeness.

### D-1510 — Retrieval authorization precedes sensitive model exposure
**Status:** Accepted

Tenant, residency, authorization and disclosure constraints apply before sensitive corpus/index/model access where metadata can leak.

### D-1511 — Derived indexes retain rebuild and model provenance
**Status:** Accepted

Canonical source IDs, projection revision, source watermark and embedding revision are retained where applicable.

### D-1512 — Search/vector failure degrades discovery, not truth
**Status:** Accepted

Exact retrieval remains available where canonical evidence is available.

### D-1513 — Reasoning executions use explicit plans
**Status:** Accepted

Plans bind requested propositions, evidence families, temporal perspective, negative-coverage requirements and allowed derivations.

### D-1514 — Reasoning runs have durable identity and provenance
**Status:** Accepted

Rule/code revisions, source watermark, knowledge cut and authorization context are retained.

### D-1515 — Accepted evidence/status transitions are deterministic and versioned
**Status:** Accepted

Models cannot replace source-status/evidence/authority rules.

### D-1516 — Cross-concept derived statements require explicit derivation rules
**Status:** Accepted

Juxtaposition or prose adjacency is not a semantic join.

### D-1517 — Causal Claims are canonical proposition records
**Status:** Accepted

Cause, effect, role, mechanism/context, scope/time, status, evidence and authority are explicit.

### D-1518 — Causal status uses the accepted six-state vocabulary
**Status:** Accepted

`proposed`, `supported`, `weakened`, `unresolved`, `rejected`, and `confirmed` are retained exactly.

### D-1519 — Causal support is claim-relative
**Status:** Accepted

Timing, Lineage, remediation, reconciliation, graph position or basis count cannot substitute for claim-specific evaluation.

### D-1520 — Rejection requires contradiction or exclusion evidence
**Status:** Accepted

Unsupported is not rejected.

### D-1521 — Confirmation remains REF-017 + AUTH-034 gated
**Status:** Accepted

No model, Investigation owner, remediation result or consensus shortcut exists.

### D-1522 — Localization remains separate from causality
**Status:** Accepted

First observed, earliest evidenced, boundary mismatch and first consumer effect are not root-cause truth.

### D-1523 — Counterfactual reasoning is analytical, not realized history
**Status:** Accepted

What-if output retains assumptions and cannot be recorded as an actual event.

### D-1524 — Historical replay binds an explicit knowledge cut
**Status:** Accepted

Event/effective window, K, proposition, requester/purpose and perspective are explicit.

### D-1525 — Availability-by-K governs as-known evidence eligibility
**Status:** Accepted

Event time before K is insufficient when the evidence became available later.

### D-1526 — Historical replay selects historical definition/governance revisions
**Status:** Accepted

Current definitions/policies cannot be projected backward by convenience.

### D-1527 — Late evidence is excluded from earlier as-known results
**Status:** Accepted

It may participate in current retrospective analysis only.

### D-1528 — Corrections/supersessions are non-rewriting
**Status:** Accepted

Current preferred interpretation can change without falsifying what was known or communicated earlier.

### D-1529 — Reconstructed historical Explanation is not authentic communication
**Status:** Accepted

Authenticity requires retained communication evidence.

### D-1530 — Historical replay retains a basis manifest
**Status:** Accepted

Eligible/excluded basis, rule revisions, source coverage and material limitations remain inspectable.

### D-1531 — Product replay uses canonical journals, not Delta time travel
**Status:** Accepted

Graph/index history and current-state projection are also insufficient substitutes.

### D-1532 — Expired basis constrains replay rather than being reconstructed
**Status:** Accepted

Provenance stubs cannot manufacture missing payload detail.

### D-1533 — Explanation uses Statement IR
**Status:** Accepted

Proposition identity, scope/time, source-owned status, basis roles, derivation and material limitations exist before prose.

### D-1534 — Answer IR composes statements without creating global truth
**Status:** Accepted

Partial sibling answers remain valid and no global completeness/confidence score is introduced.

### D-1535 — Deterministic template rendering is mandatory
**Status:** Accepted

Truthful basic answers cannot depend on LLM availability.

### D-1536 — All renderers preserve epistemic equivalence
**Status:** Accepted

Wording/detail may change but status, scope, basis and material limitations may not.

### D-1537 — Rendered output is validated against Statement IR
**Status:** Accepted

Unsupported clauses, strengthened polarity/status, broadened scope and omitted material limitations are rejected or replaced.

### D-1538 — `inspectBasis` is separately authorized
**Status:** Accepted

Conclusion visibility does not imply basis/detail/export visibility.

### D-1539 — Authentic Explanation communication is retained explicitly where promised
**Status:** Accepted

Snapshot/content, Statement IDs, limitations, audience/purpose/delivery and communication time are bound together.

### D-1540 — Reasoning/Explanation retention follows explicit value and promise
**Status:** Accepted

Released snapshots/exact dependent basis may be pinned; routine traces, candidates and drafts do not accumulate forever by default.

### D-1541 — Model invocation is provider-neutral; Databricks is conditional realization
**Status:** Accepted

Unity AI Gateway/model services are preferred where deployment capability/policy supports them, but no vendor model service owns DMTZ truth.

### D-1542 — Model, prompt, template and tool revisions are immutable invocation identity
**Status:** Accepted

Mutable aliases cannot be the sole historical identity.

### D-1543 — Model/tool/search degradation has deterministic fallback
**Status:** Accepted

Outage/refusal/quota/unsupported deployment does not change source truth and cannot block a basic semantically valid answer when canonical evidence is available.

### D-1544 — Group 06 accepts ARCH-275–ARCH-350 and promotes Group 07
**Status:** Accepted — Group 06 closure

IRE06-01–IRE06-120 pass. Group 06 closes with canonical Investigation/Causal Claim persistence, Delta-backed derived graph traversal, exact-first retrieval, availability-by-K replay, Statement/Answer IR, itemwise basis inspection, authentic Explanation snapshots and optional non-authoritative model assistance. Group 07 — Execution Gate, Propagation Safeguard & Active-Control Architecture is next.
