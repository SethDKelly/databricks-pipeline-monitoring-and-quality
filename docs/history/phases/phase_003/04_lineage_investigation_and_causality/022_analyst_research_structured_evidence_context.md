# SYN-022 — Analyst Research → Structured Evidence / Claim / Context

**Status:** Accepted — Phase 003 Group 04

## Outcome

Make analyst investigation a first-class contributor to the evidence model by routing research results into the concept that owns their meaning instead of storing every human finding as an Annotation.

## Participating concepts and actions

- **Investigation** — `linkEvidence`, `linkClaim`, `refineScope`.
- **Observation** — `record` for reproducible/measured facts.
- **Change** — `derive` / `recordOccurred` where analyst-supported evidence establishes a realized difference/event.
- **Causal Claim** — `propose`, `support`, `contradict` for causal propositions/evaluation.
- **Annotation** — `add` for attributed contextual commentary.
- **Change Intent**, **Expectation**, **Responsibility Assignment**, **Classification**, **Policy Context** — receive structured human assertions when the analyst/stakeholder is actually establishing those respective truths under applicable authority.

## Trigger / initiating condition

An analyst or other authorized human performs research, supplies evidence, or adds context during an Investigation.

## Coordination semantics

1. Determine what kind of statement/result the human is contributing.
2. A reproducible query/measurement with evidence basis becomes an **Observation**.
3. A supported before/after or source-event difference may become **Change** under Change semantics.
4. A proposition about why an outcome occurred becomes a **Causal Claim**, not merely an Annotation.
5. Business/operational commentary that is useful but not independently structured fact remains **Annotation**.
6. Planned intent, normative criteria, responsibility, classification, or policy assertions are redirected to their owning concepts with their own authority/provenance requirements.
7. Link the resulting structured record/context back to the Investigation.
8. Human title alone does not make a claim confirmed or an assertion universally authoritative.

## State and evidence effects

Each concept owns the structured state appropriate to its purpose. Investigation links it; analyst activity itself does not create a separate shadow truth store.

## Ambiguity / failure propagation

A human-provided statement without sufficient evidence for a structured fact can remain Annotation or a proposed Causal Claim. Disputed/withdrawn context remains attributed rather than being silently promoted.

## Temporal semantics

Record when the analyst learned/recorded the result separately from the event/effective time described by underlying evidence.

## Provenance / traceability

Human identity, method/query/source references where applicable, and Investigation context remain traceable.

## Security / authorization

Analyst research must operate within existing access rights. Free-form Annotation must not become a path for copying restricted raw values into broadly visible context.

## Invariants

- human research ≠ Annotation by default;
- reproducible fact → Observation semantics;
- causal interpretation → Causal Claim semantics;
- structured plan/norm/governance truth → owning concept;
- human authority ≠ universal authority;
- analyst intervention does not bypass evidence provenance.

## Scenarios

An analyst queries B and establishes a timestamped row-count drop: record an Observation and derived Change. An analyst proposes that join-key nulls contributed to C loss: create a Causal Claim. A stakeholder notes a one-time month-end event: Annotation unless stronger structured evidence is supplied.

## Non-goals

Notebook/query tool selection, analyst workspace UX, universal approval authority, or automatic trust in human assertions.
