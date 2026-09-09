# LLM, Retrieval and Rendering Architecture

## Principle

The LLM is an optional assistant around an evidence-bound reasoning system, not the reasoning system's source of truth.

## Allowed model roles

A model may assist with:

- parsing ambiguous natural-language questions into candidate bounded subquestions for deterministic validation;
- suggesting Investigation leads/candidate relations;
- semantic candidate retrieval;
- proposing presentation ordering;
- rendering authorized Statement IR into natural language.

A model may not determine Assertion Authority, evidence sufficiency, negative coverage, Causal Claim confirmation, Impact, authorization or historical truth by model confidence.

## Provider-neutral gateway

DMTZ defines a provider-neutral model invocation contract. A deployment may route it through Databricks Unity AI Gateway/model services, an external-provider gateway or another approved service.

Model/provider availability remains a Group 01 capability instance.

## Structured tool use

Models receive bounded tools rather than unrestricted database credentials. Tool calls carry exact scope/time/tenant/purpose context and the tool implementation performs authorization and evidence-rule checks.

Structured schemas are required for lead suggestions, query decomposition and render plans. Free-form model assertions never become domain facts directly.

## Grounding packet

Final prose rendering receives Statement IR plus only the authorized basis/context necessary for the output. Raw evidence is not sent merely because the model can accept a large context window.

## Invocation provenance

Retain invocation ID, provider/model/service, resolved model revision where available, prompt/template/tool revisions, input statement/candidate IDs, output digest, timing, token/cost metrics where available, and optional tracing identifiers.

## Prompt versioning

Every invocation binds an immutable prompt/template revision or digest. Mutable aliases may choose a version but are not retained as the sole historical identity.

MLflow Prompt Registry is a useful conditional implementation where verified, but its current Beta status means the product cannot require it universally.

## Databricks AI options

Where deployment capability and policy permit:

- Unity AI Gateway/model services can centralize governed model access;
- Foundation Model/Model Serving APIs provide an OpenAI-compatible invocation interface;
- AI Search/Vector Search can accelerate semantic candidate retrieval;
- MLflow Tracing can observe model/retriever/tool execution;
- MLflow Prompt Registry can assist prompt lifecycle/version management.

Each remains deployment-verified and subordinate to DMTZ's canonical records.

## Fallback

If model invocation fails or is disallowed, deterministic reasoning and template rendering continue. If semantic search is unavailable, exact structured retrieval remains available and the discovery limitation is recorded if material.

## Validation

Model-rendered text is parsed/validated against Statement IR. Unsupported clauses, scope broadening, status strengthening or missing material limitations cause rejection/regeneration or deterministic fallback.

Multiple model outputs or model/provider agreement do not count as independent corroboration.