# Phase 010 Group 06 — External Source Review

**Verified:** 2026-08-28

This review records current public vendor capabilities relevant to reasoning/retrieval/model architecture. Per ARCH-001–ARCH-032, public documentation is not proof that a specific enterprise deployment exposes the capability.

## Databricks Unity AI Gateway / model APIs

Current Databricks documentation describes Unity AI Gateway/model services as governed model APIs represented through Unity Catalog. They can route to Databricks-hosted or external model destinations and apply access control, rate limits, guardrails and auditing. Databricks model APIs and Model Serving expose OpenAI-compatible interfaces.

Architecture interpretation:

- useful conditional implementation for DMTZ's provider-neutral model gateway;
- model-service availability/region/plan/permissions remain capability-instance facts;
- gateway authorization does not replace DMTZ Assertion Authority, evidence sufficiency or disclosure semantics;
- model invocation/audit evidence does not become domain truth.

References:

- https://docs.databricks.com/aws/en/ai-gateway/
- https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview
- https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis
- https://docs.databricks.com/api/ai-gateway/v1/model-service

## Function calling

Databricks documents OpenAI-compatible function calling for supported model-serving paths. The model emits structured function arguments; application code remains responsible for executing tools.

Architecture interpretation: this is compatible with ARCH-342–ARCH-343 because the model can request bounded tools while DMTZ-controlled code performs authorization, retrieval and evidence evaluation.

Reference: https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling

## Databricks AI Search / Vector Search

Current Databricks APIs expose managed AI Search/Vector Search endpoints and indexes, including standard and storage-optimized endpoints and Delta-sync/direct-access index forms.

Architecture interpretation:

- suitable optional derived candidate-retrieval/index layer;
- no vector index is a canonical evidence store;
- similarity does not establish evidence status, authority or completeness;
- embedding/index revision and source IDs must be retained for retrieval provenance;
- exact tenant capability, cost, scale and endpoint availability remain environment facts.

References:

- https://docs.databricks.com/api/vector-search/v1
- https://docs.databricks.com/aws/en/ai-search/filtering-guide
- https://docs.databricks.com/aws/en/ai-search/best-practices

## MLflow Tracing

Databricks documents MLflow Tracing for GenAI applications as capturing inputs, outputs, intermediate operations and metadata across model/retriever/tool flows, with Unity Catalog recommended for production trace storage.

Architecture interpretation:

- useful optional operational observability for reasoning/model execution;
- trace absence does not erase DMTZ's canonical reasoning/model invocation record;
- trace existence does not prove an Explanation was actually communicated;
- trace inputs/outputs remain disclosure/retention governed.

References:

- https://docs.databricks.com/aws/en/mlflow3/genai/tracing
- https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101

## MLflow Prompt Registry

Current Databricks documentation describes Prompt Registry as a Unity-Catalog-integrated prompt lifecycle system with immutable versions and mutable aliases. The feature is currently documented as **Beta** and may require preview enablement/permissions.

Architecture interpretation:

- useful conditional prompt-authoring/version-management integration;
- never a universal Phase 010 dependency;
- DMTZ model invocation must retain the resolved immutable prompt/template identity even when an alias selects it;
- current alias state cannot reconstruct historical invocation identity.

References:

- https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/
- https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/use-prompts-in-deployed-apps

## Conclusion

Current vendor capabilities support the selected architecture but do not define it. DMTZ remains able to run deterministic reasoning/template rendering without any LLM, Vector Search, Prompt Registry or MLflow Tracing dependency. Optional Databricks AI facilities are accelerators/governance/observability integrations whose exact usability is deployment verified.