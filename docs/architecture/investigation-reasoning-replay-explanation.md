# Investigation, Reasoning, Historical Replay & Explanation Architecture

**Canonical key:** `architecture.investigation_reasoning_replay_explanation`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.investigation_reasoning_replay_explanation`

**Stable IDs:** ARCH-275–ARCH-350

**Stable ID index:** `ARCH-275`, `ARCH-276`, `ARCH-277`, `ARCH-278`, `ARCH-279`, `ARCH-280`, `ARCH-281`, `ARCH-282`, `ARCH-283`, `ARCH-284`, `ARCH-285`, `ARCH-286`, `ARCH-287`, `ARCH-288`, `ARCH-289`, `ARCH-290`, `ARCH-291`, `ARCH-292`, `ARCH-293`, `ARCH-294`, `ARCH-295`, `ARCH-296`, `ARCH-297`, `ARCH-298`, `ARCH-299`, `ARCH-300`, `ARCH-301`, `ARCH-302`, `ARCH-303`, `ARCH-304`, `ARCH-305`, `ARCH-306`, `ARCH-307`, `ARCH-308`, `ARCH-309`, `ARCH-310`, `ARCH-311`, `ARCH-312`, `ARCH-313`, `ARCH-314`, `ARCH-315`, `ARCH-316`, `ARCH-317`, `ARCH-318`, `ARCH-319`, `ARCH-320`, `ARCH-321`, `ARCH-322`, `ARCH-323`, `ARCH-324`, `ARCH-325`, `ARCH-326`, `ARCH-327`, `ARCH-328`, `ARCH-329`, `ARCH-330`, `ARCH-331`, `ARCH-332`, `ARCH-333`, `ARCH-334`, `ARCH-335`, `ARCH-336`, `ARCH-337`, `ARCH-338`, `ARCH-339`, `ARCH-340`, `ARCH-341`, `ARCH-342`, `ARCH-343`, `ARCH-344`, `ARCH-345`, `ARCH-346`, `ARCH-347`, `ARCH-348`, `ARCH-349`, `ARCH-350`

**Owns current question after cutover:** How does DMTZ persist Investigation/Causal Claim state, reason deterministically over evidence, replay historical knowledge, compose Statement/Answer IR and optionally use graph/search/models without delegating truth?

## Canonical contract

The reasoning chain is:

**bounded question / Investigation scope → exact structured retrieval + bounded derived-graph traversal → time/coverage/authority/evidence evaluation → Investigation lead or Causal Claim evaluation → structured Statement IR + exact basis/limitations → authorized projection → deterministic or model-assisted rendering → retained Explanation snapshot / communication evidence**.

No stage automatically creates the next stage's truth.

## Deterministic-first reasoning

DMTZ resolves proposition identity, subject, scope, time/knowledge cut, evidence-owner families, coverage burden, authority and authorization through versioned deterministic logic before rendering. An LLM is never asked to inspect unrestricted evidence and decide truth.

Model assistance may help ambiguous-language handling, lead generation, semantic candidate recall or prose rendering. It cannot change the bounded source-owned proposition, evidence status, authority, causal status or control state. Model outage must leave a semantically faithful deterministic structured/template path.

## Investigation and Causal Claim persistence

Investigation is durable canonical workflow state with identity, scope revisions, lifecycle events, leads, evidence-role links, annotations, dispositions, closure and reopen history. Tickets, alerts, chats, traces and UI sessions may reference it but do not substitute for it.

Leads remain inquiry state with generation provenance and limitations. Lead ordering does not create probability or causal confidence. `No support found` is not `excluded` or `rejected`.

Causal Claims bind cause, effect, role/mechanism assumptions, subject/scope/window, status, evidence roles, limitations and authority context. Status remains `proposed / supported / weakened / unresolved / rejected / confirmed`. `confirmed` requires REF-017 evidence plus AUTH-034 authority; Investigation closure, analyst agreement, remediation success, graph position, timing or model confidence cannot bypass that gate.

## Derived graph and retrieval

The MVP uses Delta-backed rebuildable node/edge projection tables over the canonical evidence plane. A dedicated graph database is optional and, if later justified by measured traversal needs, remains a derived projection rather than historical truth.

Graph distance, centrality, path count, descendant count and recency may aid navigation; they do not establish cause, Impact, authority or evidence strength.

Exact structured retrieval by canonical ID/proposition/entity/scope/time/knowledge cut/typed relationship is truth-bearing. Semantic/vector retrieval is optional candidate recall and cannot prove relevance, authority, causality, absence, completeness or corroboration.

Tenant, residency, authorization and disclosure constraints apply before sensitive retrieval/model exposure. Post-retrieval filtering is insufficient when query/index metadata can itself leak restricted existence.

## Historical replay

Historical reasoning uses canonical temporal/evidence-availability journals, not Delta time travel, current graph state, current policy or current source state. As-known-at-`K` admits only evidence available by `K`. Later evidence may change current retrospective reasoning while preserving the earlier as-known result.

Replay retains eligible/excluded-after-K basis, rule revisions, coverage and limitations. Expired or never-retained material remains unavailable. A reconstructed historical Explanation is labeled reconstruction and never presented as authentic prior communication.

## Statement IR / Answer IR

Statement IR binds exact proposition, subject/scope/time perspective, source-owned epistemic state, supporting/contradicting/limiting/context basis, derivation rule, material limitations and disclosure requirements. Answer IR composes independently evaluated sibling statements, unresolved subquestions, ordering/materiality and authorized projection instructions.

Statement identity is not wording identity. UI cards, templates, APIs and model prose can render one Statement IR without becoming separate truths. Supported siblings do not strengthen unresolved siblings. No universal answer-completeness score exists.

All renderers must be epistemically equivalent to Statement IR. Invalid model prose is rejected, boundedly repaired or replaced with deterministic rendering.

## Basis inspection and retained communication

`inspectBasis` is separately authorized item-by-item. Visible reference, internal resolvability, retained payload and permission are independent states.

Exact historical basis projection requires a retained prior projection/snapshot; current permission cannot reconstruct what a historical requester actually saw.

Material communicated Explanations retain authentic content/snapshot plus statement IDs, limitations, audience/purpose/delivery context, projection decision, communication time and renderer/template/prompt/model revision where applicable. Composition, approval, release, delivery, receipt/read and reliance remain separate propositions.

## Model/tool boundary

Model calls are provider-neutral, deployment-capability gated and provenance-bearing. Mutable aliases are operational selectors; historical invocation identity binds the resolved revision. Models access only bounded tools that enforce tenant/residency, scope/time, authorization/disclosure, evidence/coverage and minimization.

Model/provider agreement is common-derived analysis, not independent corroboration. Model, vector/search or graph outages degrade assistance/discovery, not underlying truth.

## Architecture boundary

This segment does not mandate a graph database, embedding/vector provider, LLM/provider, agent framework, orchestration runtime, UI/API topology, observability stack, secrets product or active-control implementation.

## Provenance

- `docs/concepts/phase_010/06_investigation_reasoning_historical_replay_explanation_architecture/README.md`
- atomic ARCH-275–ARCH-350 files under that Phase 010 group
- Phase 010 decisions D-1491–D-1544 and IRE06-01–IRE06-120 review evidence
