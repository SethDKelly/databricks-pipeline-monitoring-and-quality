# Group 08 — Serving Reference Architecture

## Principle

Serving is a governed projection/orchestration layer over canonical journals and policies, never an alternative truth store.

## Selected request chain

**authenticated request → canonical Principal/context binding → Capability Authorization + disclosure evaluation → exact canonical/derived retrieval → deterministic reasoning where required → Statement/Answer IR → authorized projection → response epistemic envelope → optional retained communication**.

Historical replay and `inspectBasis` remain distinct paths because they carry different time/disclosure obligations.

## Logical runtime planes

1. **Canonical data plane** — Group 02 Delta-first evidence, policy, Investigation, Explanation/control journals.
2. **Acquisition/processing plane** — Group 04 reconciliation/incremental workers and Group 05 normalization/measurement/lineage processing.
3. **Derived query plane** — rebuildable serving tables, operational graph, search/vector indexes and caches.
4. **Serving/reasoning plane** — stateless APIs, exact query, deterministic reasoning, replay, basis inspection and rendering.
5. **Active-control plane** — latency/security-isolated Gate/Safeguard decision/delivery adapters.
6. **Operations plane** — observability, lifecycle/archive, capacity/quota and cost telemetry.

The planes are logical boundaries, not one-microservice-per-plane requirements.

## MVP topology

The selected MVP is Databricks-centered for canonical Delta persistence and durable batch/reconciliation work. A thin stateless API/service façade is preferred for user-facing serving, and externally reachable edge/control adapters may be deployed when GitHub callbacks or pre-start brokers require them.

UI clients do not receive unrestricted direct canonical-table access. They consume authorization-aware API projections.

## Cache discipline

Caches bind tenant, material authorization/disclosure context, projection revision, canonical/source watermark and applicability horizon. Stale or differently authorized entries are not reused by convenience.

## Degradation

Loss of a cache/index may reduce latency or semantic candidate recall but canonical exact queries remain the recovery basis. Loss of a required canonical/evidence dependency produces explicit partial/unavailable state; supported sibling propositions remain serviceable.