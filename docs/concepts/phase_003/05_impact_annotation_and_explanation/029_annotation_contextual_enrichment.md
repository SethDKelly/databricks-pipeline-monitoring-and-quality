# SYN-029 — Human Annotation + Structured State → Contextual Enrichment

**Status:** Accepted — Phase 003 Group 05

## Outcome

Allow human context to enrich Investigation, Impact, Causal Claim, safeguard, and Explanation views without turning free-form commentary into hidden structured truth or authority.

## Participating concepts and actions

- **Annotation** — `add`, `revise`, `withdraw`, `dispute`.
- **Investigation**, **Impact**, **Causal Claim**, **Propagation Safeguard**, and **Explanation** — may reference relevant Annotation.
- **Observation**, **Change**, **Change Intent**, **Expectation**, **Responsibility Assignment**, **Classification**, and **Policy Context** receive statements that actually belong to those structured concepts.
- **Capability Authorization** — resolves Annotation authoring and viewing capabilities independently where applicable.

## Trigger / initiating condition

A human provides contextual information, interpretation, business-use detail, operational commentary, or a disputed/withdrawn note relevant to the monitored ecosystem.

## Preconditions

The Annotation has an attributable author, referent/context, record time, and visibility context. Structured assertions are redirected rather than hidden in commentary.

## Coordination semantics

1. Record human context as Annotation with author/time/referent/visibility provenance.
2. If the content is a reproducible measured fact, establish it through Observation/Change under the appropriate evidence semantics rather than treating the Annotation as the fact itself.
3. If the content proposes causality, create/link a Causal Claim; Annotation may remain supporting human context.
4. If the content declares planned intent, normative expectation, responsibility, classification, or policy applicability, route it to the owning structured concept with its own authority semantics.
5. Impact may reference an Annotation describing a client/business consequence, but the consequence statement preserves that its source is human-authored unless stronger evidence independently establishes it.
6. Dispute, revision, and withdrawal remain visible to downstream reasoning; Explanation cannot present a disputed/withdrawn note as uncontested current fact.
7. Viewing an Annotation and adding/revising one are independent capabilities when authorization semantics distinguish them.

## State and evidence effects

Annotation owns attributed human context and its revision/dispute lifecycle. Other concepts own any structured truth created from separately accepted evidence/assertions.

## Ambiguity / failure propagation

Conflicting human statements coexist. Restricted Annotation content may remain opaque. Absence of Annotation has no evidentiary meaning.

## Temporal semantics

Annotation record time and optional context/effective time remain distinct. Later withdrawal/dispute does not erase the Annotation's earlier role in contemporaneous reasoning.

## Provenance / traceability

Every use of an Annotation retains author/source, referent, version, status, and visibility context.

## Security / authorization

Free-form notes can leak restricted values, client names, policy details, or personal information. Explanation must never use restricted Annotation content to smuggle hidden facts into an otherwise permitted summary.

## Invariants

- Annotation ≠ Observation;
- Annotation ≠ Causal Claim;
- Annotation ≠ Change Intent;
- Annotation ≠ Expectation;
- Annotation ≠ Responsibility Assignment;
- Annotation ≠ Classification/Policy Context;
- author title ≠ universal authority;
- disputed/withdrawn Annotation ≠ uncontested current fact;
- view permission ≠ author/edit permission.

## Scenarios

**Month-end context:** a stakeholder note explains unusual business timing; it informs analysis without modifying the Baseline automatically.

**Client-use statement:** a business owner says a client used an affected report; Impact may record that consequence with human-source provenance while seeking corroborating evidence where needed.

**Incorrect causal note:** timing evidence contradicts a note blaming a Deployment; the note remains attributed while the Causal Claim is weakened.

**Restricted Annotation:** analyst sees `restricted business context exists` without the note text.

## Non-goals

Chat/UI implementation, moderation architecture, replacing structured concepts, or automatic truth promotion from human text.

## Deferred questions

First-MVP Annotation categories, moderation/retention, and whether specific high-consequence consequence statements require review/corroboration before business-facing Explanation.