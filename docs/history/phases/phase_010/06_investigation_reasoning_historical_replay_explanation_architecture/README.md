# Phase 010 Group 06 — Investigation, Reasoning, Historical Replay & Explanation Architecture

**Status:** COMPLETE / ACCEPTED

## Goal

Realize Investigation/Causal Claim persistence, deterministic evidence-bound reasoning, derived graph/retrieval traversal, historical/as-known replay, statement-to-basis Explanation composition, `inspectBasis`, authentic retained communication, and bounded model assistance without allowing a reasoning engine or LLM to become a source of truth.

## Accepted result

- **ARCH-275–ARCH-350 accepted.**
- Cumulative Phase 010 architecture range: **ARCH-001–ARCH-350**.
- **IRE06-01–IRE06-120 pass.**
- **D-1491–D-1544 accepted.**
- No new product concept is required.

The selected logical chain is:

**bounded question / Investigation scope → exact structured retrieval + bounded derived-graph traversal → time/coverage/authority/evidence evaluation → Investigation lead or Causal Claim evaluation → structured Statement IR + exact basis/limitations → authorized projection → deterministic or model-assisted rendering → retained Explanation snapshot / communication evidence**.

No stage automatically creates the next stage's truth.

## Core architecture decision

The reasoning system is **deterministic-first and evidence-bound**.

DMTZ does not ask an LLM to inspect an unrestricted data lake and decide what is true. The framework first resolves proposition identity, subject, scope, time, knowledge cut, evidence-owner families, coverage burden, authority and authorization through versioned deterministic logic. It then produces structured Statement IR / Answer IR. A model may optionally help with ambiguous language, lead generation, semantic candidate recall or prose rendering, but cannot change the bounded source-owned proposition.

A model outage must therefore leave the framework able to return a semantically faithful structured/template answer.

## Investigation persistence

Investigation is persisted in canonical Group 02 journals with durable identity, scope revisions, lifecycle events, leads, evidence-role links, annotations, dispositions, closure and reopen history.

A ticket, alert, chat session, model trace or UI page may reference an Investigation but cannot substitute for its identity.

Leads remain inquiry/workflow state. They retain generation provenance and limitations whether created by an analyst, deterministic rule, graph traversal, anomaly detector, search query or model. Lead ordering may improve workflow, but no universal hypothesis probability/rank is accepted.

Lead exclusion is evidence-bearing. `No support found` is not the same as `excluded` or `rejected`.

## Derived reasoning graph

The MVP uses **Delta-backed rebuildable node and edge projection tables** over the canonical evidence plane.

Nodes reference canonical IDs for entities, runs, deployments, measurements, evidence, Investigations, Causal Claims and Explanation statements. Edges are typed and provenance-bearing, including source-basis, actual temporal precedence, Lineage, consumed, produced, measured, encountered, exposed, effect, claim-role and statement-basis relationships.

A dedicated graph database is **not required for the MVP**. It may be introduced later only if measured traversal depth, latency, concurrency or scale justifies another operational technology. Any graph database remains a derived projection and cannot become the historical system of record.

Graph distance, centrality, descendant count, recency or path count may assist navigation. They do not create causal probability, Impact, authority or evidence strength.

## Retrieval architecture

Truth-bearing evaluation starts with exact structured retrieval by canonical ID, proposition, entity/scope, event/effective time, knowledge cut and typed relationship.

Semantic/vector retrieval is optional candidate recall. It can suggest potentially relevant evidence or Investigation leads, but similarity cannot prove relevance, authority, causal status, absence, completeness or corroboration.

Derived indexes retain canonical source IDs, projection/embedding revisions and rebuild watermarks. Search/vector failure therefore degrades discovery convenience rather than rewriting source truth.

Tenant, residency, authorization, disclosure and time constraints apply before sensitive content is exposed to a retrieval/model layer. A post-retrieval filter is not sufficient if the index query or metadata itself can reveal restricted existence.

## Reasoning runs and rules

Every reasoning execution has a durable `Reasoning Run` identity bound to:

- exact question/subquestions and proposition identities;
- subject/scope/population;
- event/effective window and knowledge cut;
- plan/rule/code revisions;
- source/evidence watermarks;
- required evidence families and negative-coverage conditions;
- authorization/disclosure context;
- retrieval/graph projection revisions used;
- material limitations and unresolved inputs.

Where Phases 004–009 define exact status transitions or evidence burdens, Group 06 implements them through versioned deterministic rules. Cross-concept derived statements require explicit versioned derivation rules and exact input proposition IDs; juxtaposed prose is never a semantic join.

## Causal Claim architecture

Causal Claims remain canonical proposition records, not model conclusions.

The persisted claim binds cause, effect, causal role, mechanism/transmission assumptions, subject/scope, event window, status, evidence roles, limitations and Assertion Authority context.

Allowed statuses remain:

`proposed / supported / weakened / unresolved / rejected / confirmed`.

`confirmed` remains strictly gated by **REF-017 evidence sufficiency + AUTH-034 eligible Assertion Authority** for the exact claim. Investigation closure, incident ownership, analyst agreement, remediation success, model confidence, repeated model agreement, graph position or timing cannot bypass that gate.

`rejected` requires evidence that contradicts or excludes the bounded claim. Lack of support remains lack of support.

## Historical replay

Historical reasoning is performed from canonical bitemporal/evidence-availability journals, not from Delta transaction-log time travel, current graph state, current policy state or current source state.

An as-known-at-`K` replay admits only evidence known/available by `K`, even if later evidence describes an event that occurred before `K`.

Current retrospective reasoning may incorporate late evidence and corrections, but it remains a different perspective from the historical as-known result.

Replay retains a basis manifest identifying eligible basis, excluded-after-`K` material, rule revisions, source coverage and material limitations. If required evidence expired or was never retained, the replay remains limited rather than reconstructing missing payload from a provenance stub.

A reconstructed historical Explanation is explicitly labeled reconstruction. It is never presented as the exact communication that occurred then.

## Statement IR and Answer IR

Explanation composition is separated from prose rendering through two structured layers.

**Statement IR** binds:

- exact proposition identity;
- subject/scope/time perspective;
- source-owned status/epistemic vocabulary;
- supporting, contradicting, limiting and contextual basis IDs;
- derivation-rule ID where applicable;
- material limitations;
- disclosure requirements.

**Answer IR** contains the selected Statement IR set, sibling relationships, unresolved subquestions, ordering/materiality metadata and authorized projection instructions.

Statement identity is not wording identity. A template, UI card, API response and model-written paragraph can represent the same Statement IR without becoming different truths.

Partial answers are valid: supported sibling statements may be returned while other subquestions remain unresolved. No universal answer-completeness percentage is introduced.

## Rendering and validation

A deterministic template renderer is the minimum viable rendering path.

Model-assisted rendering is optional. Every renderer must be epistemically equivalent to the underlying Statement IR: it may shorten, expand or rephrase but cannot strengthen status, broaden scope, omit a material limitation or add an unsupported factual clause.

Rendered output is validated against Statement IR. Invalid model output is rejected, repaired through bounded regeneration, or replaced by deterministic rendering.

## `inspectBasis`

`inspectBasis` is a separately authorized operation over a specific statement. Current requester, purpose, delivery context and disclosure policy determine whether each basis item is shown exactly, coarsely, redacted, as an opaque reference or withheld.

Internal statement-to-basis traceability remains complete regardless of visible projection.

Visible reference, source resolvability, payload availability and authorization to inspect the payload are independent states.

The exact basis projection shown historically can be recovered only if that projection or authentic Explanation snapshot was retained. Current permission expansion cannot reconstruct what a prior requester actually saw.

## Explanation communication retention

Material communicated Explanations retain an immutable snapshot or canonical serialized representation bound to:

- Explanation/statement IDs;
- exact rendered content or content digest plus recoverable canonical content;
- material limitations;
- audience/requester/purpose/delivery context;
- authorization/projection decision identity;
- communication time;
- rendering/template/prompt/model version where applicable;
- current-preferred/supersession relationships.

Composition, approval, release, delivery, receipt/read and reliance remain separate evidence propositions.

Retention follows Group 02 policy: Explanation snapshots and dependent exact basis are pinned for the promised product/audit/policy horizon, not automatically forever. Age alone neither forces deletion nor indefinite retention.

## Model architecture

Model invocation is provider-neutral.

Where the deployment verifies it, Databricks Unity AI Gateway/model services are a preferred conditional realization because they provide governed model access and an OpenAI-compatible interface. External providers or other gateways remain valid when organization policy, residency, capability and cost permit.

Every model call records model/provider/service identity, model and prompt/template/tool revisions, bounded input Statement/candidate IDs, output digest, timestamps, usage/cost where available and trace references.

Mutable model or prompt aliases are operational selectors only. Historical invocation identity binds the resolved immutable model/prompt/template revision.

MLflow Prompt Registry may be used when the deployment verifies that capability, but DMTZ does not depend on it for prompt identity. MLflow Tracing may enrich observability of model/retrieval execution, but traces do not become canonical source evidence or authentic Explanation snapshots by themselves.

Databricks AI Search/Vector Search may serve an authorized derived semantic index. It remains optional and rebuildable.

## Tool-mediated model assistance

A model cannot receive unrestricted canonical-store access.

Models may call bounded reasoning/search tools whose implementation enforces:

- tenant/residency;
- proposition/scope/time limits;
- authorization/disclosure;
- evidence/coverage rules;
- canonical provenance;
- result-size/detail minimization.

For final prose rendering, the preferred grounding packet is the authorized Statement IR / basis projection required by the answer, not a raw dump of source evidence.

Model-generated lead suggestions, candidate classifications or renderings are analytical artifacts. Multiple model runs or model/provider agreement are common-derived and are not independent corroboration.

## Graceful degradation

- Model unavailable → deterministic reasoning and template rendering continue.
- Vector/search unavailable → exact structured retrieval and bounded graph traversal continue; candidate recall may narrow and the limitation is recorded where material.
- Graph projection stale/unavailable → canonical structured evidence remains authoritative; traversal may fall back to direct typed queries or report degraded discovery.
- Historical basis expired → replay explicitly limited; no reconstruction of missing payload detail.
- Restricted basis → authorized projection narrows; restricted is not absent.
- Partial runtime/Impact evidence from Group 05 → reasoning remains partial/unknown; it cannot manufacture a complete causal/Impact narrative.

## Phase 009 gap treatment

- **GAP-009-19:** durable Investigation/lead/annotation/claim-state persistence is architecturally resolved.
- **GAP-009-20:** causal confirmation evaluation now combines REF-017 with Group 03 Assertion Authority; actual organization authority data remains deployment policy.
- **GAP-009-25:** long-horizon replay uses Group 02 retained journals/archive rather than vendor-native retention alone.
- **GAP-009-26:** availability-by-`K` is a first-class replay filter/manifest input.
- **GAP-009-27:** authentic retained Explanation snapshots/communication are explicitly product-owned where promised.
- **GAP-009-28:** exact prior `inspectBasis` requires retained prior projection/snapshot; otherwise it remains unavailable rather than reconstructed.
- **GAP-009-29:** historical authorization consumes Group 03 retained decisions/evidence while current disclosure remains separate.
- **GAP-009-30:** basis durability consumes Group 02 lifecycle/pinning/provenance-stub semantics and exposes expiration limitations.
- **GAP-009-31:** sensitive-basis disclosure consumes Group 03 itemwise authorization and safe projection.
- **GAP-009-17/18 implications:** business consequence and strong multi-hop negatives remain limited by Group 05 source/path/population evidence; reasoning cannot close those gaps by inference convenience.

## Current vendor capability review

Current Databricks documentation supports several useful conditional implementation options:

- Unity AI Gateway/model services provide governed access to Databricks-hosted or external models and an OpenAI-compatible interface.
- Foundation Model APIs and serving capabilities remain region/compute/capability dependent and therefore subject to Group 01 environment verification.
- Function calling can produce structured tool arguments, but application code still executes the tool; this aligns with DMTZ's tool-mediated boundary.
- AI Search/Vector Search provides managed semantic/vector indexes and can accelerate candidate retrieval.
- MLflow Tracing can capture model, retriever and tool execution for GenAI observability.
- MLflow Prompt Registry supports immutable prompt versions and mutable aliases but is currently documented as Beta, so it is never a universal dependency.

See `external_source_review.md` for exact references and architecture interpretation.

## Scenario validation

`scenario_review.md` passes **IRE06-01–IRE06-120**, including Investigation lifecycle/reopen, conflicting leads, evidence-bearing exclusion, stale graph/search projections, semantic false positives, Causal Claim confirmation boundaries, late evidence and historical cuts, corrections, expired basis, mixed authorization, authentic-vs-reconstructed communication, model hallucination, prompt/model drift, vector/model outages and deterministic fallback.

## Durable rejection rules added by Group 06

Reject any later architecture that:

- makes an LLM/agent the source of domain truth;
- treats a model's confidence/probability as DMTZ evidence strength;
- lets model/provider agreement become corroboration;
- treats graph distance or semantic similarity as causal ranking;
- stores a derived graph/search/vector index as the only historical truth;
- allows semantic retrieval to bypass tenant/disclosure filtering;
- allows free-form model output to become a domain fact without accepted evidence/rule evaluation;
- uses current evidence/policy/source state to backfill an as-known historical result;
- labels reconstructed Explanation as authentic prior communication;
- drops Statement-to-basis links during rendering;
- permits summary prose to strengthen the underlying Statement IR;
- treats `inspectBasis` permission as inherited from conclusion visibility;
- makes model/vector availability a prerequisite for truthful basic answers;
- forces indefinite retention of all reasoning traces simply because they exist.

## Technology decisions intentionally not made

Group 06 does **not** select a final:

- dedicated graph database/product;
- embedding model/provider;
- vector-search vendor outside the conditional Databricks option;
- LLM/model/provider;
- prompt-authoring product as a universal dependency;
- agent framework;
- orchestration/worker runtime;
- UI/API/service topology;
- observability stack beyond the optional MLflow capability;
- secrets implementation;
- active-control implementation.

Group 08 will own final deployment/service/observability/cost packaging.

## Group 07 handoff

Group 07 may now design Execution Gate and Propagation Safeguard over **ARCH-001–ARCH-350**.

It may use reasoning/Explanation outputs as criterion/evidence inputs only through their exact Statement/Assessment/proposition identities. A model-generated recommendation, Investigation lead, rendered sentence or cached answer cannot itself become a Gate decision, Safeguard authorization or enforcement action.
