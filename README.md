# Databricks Pipeline Monitoring and Quality

DMTZ is an evidence-grounded monitoring, reasoning, and operational-control framework for Databricks and Spark data ecosystems.

The project is designed to answer questions that ordinary job-status monitoring cannot answer reliably: what happened, whether the resulting data is healthy and current, what changed, which downstream consumers may have encountered an affected state, what evidence supports a causal explanation, which assertions are authoritative, and when protective or execution controls may legitimately act.

DMTZ treats those questions as related but distinct. A successful job is not automatically a healthy pipeline; lineage is not proof of exposure; missing evidence is not proof that an event did not occur; authorization is not assertion authority; and a control decision is not proof that enforcement occurred.

> **Project documentation starts at [`docs/index.md`](docs/index.md).** It is the current discovery and routing entry point for semantic, architectural, operational, implementation, and historical material.

## What the framework models

DMTZ maintains explicit boundaries between the major kinds of knowledge needed to reason about a production data ecosystem:

- **scope, identity, semantics, responsibility, classification, and policy** — what is being monitored, what entities mean, who is responsible, and which rules apply;
- **expectations, baselines, observations, and assessments** — what should happen, what normally happens, what was actually observed, and what can be concluded from the available evidence;
- **change intent, execution, deployment, lineage, and realized change** — what was intended, what ran, what was deployed, how systems relate, and what materially changed;
- **investigation, causal claims, impact, annotations, and explanations** — how incidents are reconstructed, how causal confidence is bounded, what downstream consequences are evidenced, and how findings are communicated;
- **propagation safeguards, capability authorization, execution gates, and assertion authority** — how protective action, operator permissions, execution admission, and source/actor standing remain independently governed.

The canonical concept catalog contains 24 independently motivated concepts. See [Concepts](docs/concepts/README.md) for the current catalog and ownership boundaries.

## Design principles

DMTZ is built around a small set of durable reasoning rules:

- **Evidence is conclusion-specific.** The evidence sufficient to support one proposition may be insufficient for another, especially for negative claims such as “no exposure occurred.”
- **Observed facts remain separate from derived judgments.** Observation, assessment, readiness, causal explanation, and control state are not interchangeable.
- **Authority is explicit and scoped.** Source standing, operator authorization, semantic ownership, policy authority, and confirmation authority are modeled separately rather than inferred from titles, recency, source count, or platform ownership.
- **Time matters.** Event time, source availability, framework knowledge time, corrections, supersession, and retrospective knowledge are retained distinctly where material.
- **Concepts synchronize without collapsing.** Cross-concept behavior is defined through explicit contracts instead of creating ambiguous shared state.
- **Analysis may mature progressively.** Narrow trustworthy answers can be returned before slower evidence is available; later evidence may enrich or revise the result without rewriting what was known earlier.
- **Controls cannot manufacture truth.** A safeguard or gate may govern action, but it cannot convert missing or insufficient evidence into a positive health, readiness, causality, or enforcement claim.

The current cross-cutting contracts and invariants are maintained under [Contracts](docs/contracts/README.md) and [Invariants](docs/invariants/README.md).

## Technical architecture

The architecture separates evidence acquisition and persistence from identity, authority, health reasoning, lineage and impact analysis, investigation and explanation, active controls, and serving/security/deployment concerns.

Current architecture documentation is organized under [Architecture](docs/architecture/README.md), with a composed reference architecture covering the accepted technical contract. Architecture documentation describes the intended system design; it should not be interpreted as evidence that a particular Databricks workspace, integration, deployment target, or production capability has already been implemented or verified.

Related current documentation:

| Area | Documentation |
|---|---|
| Project documentation entry point | [`docs/index.md`](docs/index.md) |
| Concepts | [`docs/concepts/`](docs/concepts/README.md) |
| Architecture | [`docs/architecture/`](docs/architecture/README.md) |
| Authority | [`docs/authority/`](docs/authority/README.md) |
| Contracts | [`docs/contracts/`](docs/contracts/README.md) |
| Experience and explanations | [`docs/experience/`](docs/experience/README.md) |
| Invariants | [`docs/invariants/`](docs/invariants/README.md) |
| Policies | [`docs/policies/`](docs/policies/README.md) |
| Reference material | [`docs/reference/`](docs/reference/README.md) |
| Implementation program | [`docs/implementation/`](docs/implementation/README.md) |
| Historical design and provenance | [`docs/history/`](docs/history/README.md) |

## Current project state

The semantic model, cross-cutting contracts, authority model, and technical architecture are established in the current documentation tree. Repository documentation has been normalized so current semantic authority lives in first-class domain paths while historical design material is kept separately as provenance.

**Implementation 001-A is NEXT / READY / NOT STARTED.** The project should therefore still be treated as design- and architecture-led until implementation work and corresponding runtime evidence exist. See the [Implementation Program](docs/implementation/README.md) for the current implementation boundary and execution status.

## Working with the repository

For human or agent work, begin with [`docs/index.md`](docs/index.md) when the correct documentation location is unknown. Known stable contract identifiers should be resolved through the repository's stable-ID tooling rather than by search order or first occurrence.

Repository-level agent and development rules are defined in [`AGENTS.md`](AGENTS.md). Those rules preserve documentation authority, semantic boundaries, context discipline, security expectations, and the requirement that implementation work begin only when explicitly selected.

The top-level `knowledge/` directory is a generated OKF v0.2 compatibility projection. It is useful for tools that consume OKF-shaped knowledge, but it is not an independent semantic authority and should not be hand-edited. The authored project documentation remains under `docs/`.

## Contributing

Contributions should preserve the distinction between current semantic authority, implementation state, and historical provenance. Start with [`AGENTS.md`](AGENTS.md) and [`docs/index.md`](docs/index.md), then work from the smallest current owner for the concept, contract, architecture segment, policy, or implementation package being changed.

When changing accepted semantics, preserve explicit ownership and provenance rather than silently rewriting historical rationale. When changing implementation, do not claim runtime, Databricks-provider, deployment, or production support without corresponding evidence.

Historical design progression, prior decisions, completed reviews, and superseded material remain available under [`docs/history/`](docs/history/README.md) for audit and rationale; they do not need to be restated in this README.
