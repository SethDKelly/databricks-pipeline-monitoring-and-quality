# SYN-027 — Originating Condition + Downstream Outcome → Explicit Causal Attribution

**Status:** Accepted — Phase 003 Group 05

## Outcome

Ensure any assertion that an originating condition caused, contributed to, enabled, or prevented a downstream effect/consequence becomes an explicit Causal Claim rather than being implied by Impact layering or Explanation wording.

## Participating concepts and actions

- **Impact** — candidate, exposure, effect, and consequence state/evidence.
- **Causal Claim** — `propose`, `support`, `contradict`, and later status evolution under Group 04 semantics.
- **Investigation** — contextualizes the inquiry where present.
- **Lineage**, **Execution History**, **Observation**, **Assessment**, **Change**, **Deployment**, **Change Intent**, and **Propagation Safeguard** may supply evidence without owning the causal proposition.

## Trigger / initiating condition

An actor/system proposes a statement connecting an originating condition to a downstream effect or consequence, such as `C's bad output caused Report R's metric failure`.

## Preconditions

The proposed cause condition and downstream outcome are defined. Impact evidence and relevant historical relationship/evidence are traceable enough to evaluate the proposition.

## Coordination semantics

1. Preserve Impact's current reachability/exposure/effect/consequence states without upgrading them.
2. Form the causal proposition explicitly as a Causal Claim with defined cause, effect, time context, and contribution role where useful.
3. Link Impact exposure/effect/consequence evidence as support or contradiction only according to Group 04 causal-evidence semantics.
4. Where the claimed mechanism requires consumption of an affected state, missing exposure evidence is a material gap; reachability alone is insufficient.
5. Reliable evidence that the downstream effect predates the proposed cause or that the consumer did not encounter the relevant state can materially contradict the claim where coverage is sufficient.
6. Multiple downstream claims and multiple contributing upstream conditions can coexist.
7. Explanation must render the claim's actual epistemic status rather than converting `supported` into `caused` or `confirmed`.

## State and evidence effects

Impact state remains downstream evidence. Causal Claim owns attribution proposition/status. Investigation may link both but owns neither truth.

## Ambiguity / failure propagation

Unknown exposure, incomplete Lineage, conflicting timing, restricted evidence, or alternative explanations can leave the claim proposed/supported/unresolved. Lack of known alternatives is not confirmation.

## Temporal semantics

Claim evidence is evaluated against incident-time relationships and events. Later evidence may revise claim support while preserving earlier knowledge-time status.

## Provenance / traceability

Every support/contradiction link remains traceable to Impact and source evidence.

## Security / authorization

The downstream causal conclusion may itself be sensitive. A safe projection can expose a coarse claim status only when independently authorized and must not reveal hidden evidence through rationale.

## Invariants

- Impact candidate ≠ causal claim;
- exposure ≠ cause;
- downstream effect ≠ origin caused effect;
- consequence ≠ causal attribution;
- Lineage path ≠ cause;
- supported ≠ confirmed;
- Explanation wording cannot promote Causal Claim status.

## Scenarios

**Exposed and degraded report:** exposure plus temporal/mechanism evidence supports a claim that C contributed to Report R's metric failure, but confirmation remains gated.

**Effect predates C condition:** the attribution claim is weakened/contradicted while the downstream effect remains valid.

**Two contributors:** C's stale state and an independent report configuration change remain separate contributing claims.

## Non-goals

New causal algorithm, numerical confidence, automatic confirmation, or modifying Impact state to encode causal truth.

## Deferred questions

Later evidence/authority standard for confirmed downstream attribution and whether claim-to-claim causal chains need additional structured relationships.

## Later refinement — Phase 007 Groups 05–06

OPS-060/061 and OPS-082 make the handoff exact: Investigation/localization never substitutes for the causal proposition; causation/contribution/enabling/triggering/prevention/material-influence language requires a Causal Claim; Impact layers remain evidence/context; sufficient non-exposure can contradict encounter-dependent mechanisms while unknown exposure remains a gap; confirmed upstream causality does not automatically confirm downstream consumer exposure or origin→effect/consequence attribution; multiple origins/contributors remain valid; and `confirmed` remains REF-017 + AUTH-034 gated.
