# SYN-031 — Authorized Analytical Projection → Evidence-Grounded Explanation

**Status:** Accepted — Phase 003 Group 05

## Outcome

Compose an audience-appropriate Explanation that combines permitted health, execution, governance, responsibility, Lineage, investigation, causality, Impact, safeguard, Annotation, and capability context while preserving epistemic status, statement-to-basis traceability, redaction limits, and temporal perspective.

## Participating concepts and actions

- **Explanation** — `compose`, `composeAt`, `inspectBasis`, `refresh`.
- **Capability Authorization** — authorization decisions supporting the analytical projection and basis inspection.
- The authorized projections of **Semantic Definition**, **Responsibility Assignment**, **Classification**, **Policy Context**, **Expectation**, **Baseline**, **Observation**, **Assessment**, **Change Intent**, **Deployment**, **Execution History**, **Lineage**, **Change**, **Investigation**, **Causal Claim**, **Impact**, **Propagation Safeguard**, and **Annotation**.

## Trigger / initiating condition

An actor requests an explanation/report/answer about subject health, runtime state, governance/policy context, root cause, downstream Impact, safeguards, or historical state.

## Preconditions

The question/audience/time context is defined and SYN-030 has produced a sufficiently authorized analytical projection or explicit limitations.

## Coordination semantics

1. Compose only from the authorized projection; Explanation does not query hidden raw evidence merely to make the answer more complete.
2. Preserve statement type/epistemic label: observed fact, normative/comparative Assessment, registered intent, realized Change, Causal Claim status, Impact candidate/exposure/effect/consequence, safeguard state, human Annotation, governance/policy context, authorization limitation, unknown/conflict, etc.
3. Present policies/restrictions, responsibility, pipeline/table health, execution timing, Lineage, causal evidence, downstream Impact, and safeguard state side-by-side where useful without converting one category into another.
4. Preserve Impact layering explicitly: reachable candidate, exposed/not-exposed/unknown, observed downstream effect, consequence evidence, and causal attribution remain distinct.
5. Preserve causal status: `supported contributor` remains supported; multiple claims remain multiple; unresolved remains unresolved; no narrative simplification can create `confirmed`.
6. `inspectBasis` returns the authorized basis available to the requester. If a coarse statement is authorized while exact underlying evidence is not, the basis view may expose a provenance/status class and redaction indicator rather than hidden values.
7. If the requester lacks authorization even for the coarse conclusion, Explanation reports an allowed limitation/omission rather than using hidden evidence to state it indirectly.
8. Safe omission cannot be worded as evidence of absence. `Additional restricted downstream context exists` and `downstream consumers not found` are materially different statements.
9. Audience detail may vary, but projections over the same underlying state must not intentionally contradict one another for presentation convenience.
10. Where relevant, Explanation may state available operational capabilities separately, such as `job retry permitted` or `safeguard activation not permitted`; it does not perform the action.
11. `composeAt` preserves the requested evidence/knowledge-time perspective. Historical authorization can be described as evidence where permitted, but the current requester still receives only currently authorized disclosure.
12. `refresh` after new evidence/Impact/claim/authorization state creates an updated view while retained prior explanations remain reconstructable.

## State and evidence effects

Explanation owns only the composed communication/snapshot if retained. It does not create or alter underlying truth, Impact, causal status, authorization, or operational state.

## Ambiguity / failure propagation

Missing, conflicting, restricted, stale, or insufficient evidence remains visible at an appropriate abstraction. A partial authorized view can support a narrower Explanation; it never licenses plausible narrative completion.

## Temporal semantics

Explanation retains generation time, requested event-time perspective, requested knowledge-time cut, and relevant authorization/redaction context. Group 06 will consolidate end-to-end replay semantics.

## Provenance / traceability

Every material statement has an internal statement-to-basis link to the projected source concept state and its epistemic/authorization context. Visible citation UI is deferred, but internal traceability is mandatory.

## Security / authorization

Explanation is a high-risk cross-source inference surface. It must not reveal restricted identities, thresholds, policy text, Annotation content, consumer names, or causal details through summarization, comparison, omission patterns, or generated prose beyond authorized abstraction.

## Invariants

- Explanation ≠ independent truth source;
- authorized projection ≠ unrestricted evidence;
- restricted basis cannot be smuggled through prose;
- reachability ≠ exposure ≠ downstream effect ≠ consequence;
- downstream effect ≠ causal attribution;
- supported ≠ confirmed;
- Annotation remains human context;
- Policy Context ≠ compliance conclusion;
- Responsibility Assignment ≠ authorization;
- action capability display ≠ action execution;
- redacted/omitted ≠ nonexistent;
- historical view ≠ authorization bypass.

## Scenarios

**Business analyst without raw access:** Explanation shows that C completeness failed, execution duration was acceptable, a restricted upstream contributor is supported but unconfirmed, one downstream report was exposed/affected, another was protected by safeguard, relevant handling restrictions apply, and the responsible team is visible—without rows, sensitive thresholds, restricted identities, or policy text.

**Engineering detail:** an engineer with broader capability inspects the same underlying conclusions with version/execution evidence and detailed Lineage while causal status remains identical.

**Reachable but not exposed:** Explanation says a critical report is downstream but reliable evidence shows it did not consume the affected version; it does not call the report affected.

**Multiple causes:** two supported contributors remain visible rather than being collapsed to a single root cause.

**Historical correction:** retained incident-time Explanation remains reconstructable; refreshed retrospective Explanation includes later evidence and states the changed knowledge context.

## Non-goals

UI/chat/dashboard implementation, LLM/template selection, granting authorization, generating new evidence, changing Impact/Causal Claim state, or executing operational actions.

## Deferred questions

Audience-specific minimum explanation schemas, visible evidence citation requirements, deterministic versus generative rules for high-consequence statements, retained snapshot policy, and safe-answer behavior for deeply mixed authorization paths.