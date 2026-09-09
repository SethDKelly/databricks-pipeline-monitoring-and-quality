# SYN-013 — Runtime Evidence → Realized Change

**Status:** Accepted — Phase 003 Group 03

## Outcome

Describe evidence-established runtime/data differences over time as realized Change without treating every numerical difference as material or every Change as degradation.

## Participating concepts and actions

- **Observation** — before/after facts.
- **Execution History** — runtime sequence/context.
- **Deployment** — active configuration context where relevant.
- **Change** — `derive`, `recordOccurred`, `correct`.

## Trigger / initiating condition

Comparable before/after evidence or an explicit source-reported transition becomes available.

## Preconditions

Comparison semantics are sufficiently meaningful; otherwise Change remains non-comparable/insufficient.

## Coordination semantics

- Derive a Change only when the difference is worth preserving as a realized transition under later-defined significance rules; do not create noise from every floating-point/run-to-run difference.
- Preserve changed facet, before/after evidence, direction/magnitude, context, and timing.
- Deployment may contextualize code/config transitions but does not make downstream data differences causal.
- Execution timing shifts can themselves be Change kinds when meaningfully established.
- An observed Change can coexist with `within Expectation`, `atypical only`, violation, or unresolved Assessment.

## State and evidence effects

Observation/Execution/Deployment retain source truth; Change owns the realized difference description.

## Ambiguity / failure propagation

Non-comparable windows, missing prior evidence, structural breaks, or conflicting sources do not yield fabricated deltas.

## Temporal semantics

Change effective interval/time and discovery/knowledge time remain distinct.

## Provenance / traceability

Derived Change links its exact before/after evidence and comparison meaning.

## Security / authorization

Change magnitude/detail may be abstracted where raw values are restricted.

## Invariants

- difference ≠ meaningful Change record;
- Change ≠ degradation;
- Change ≠ cause;
- planned intent ≠ realized Change;
- run-duration Change ≠ data-quality defect.

## Scenarios

C row count shifts materially; job runtime doubles; schema changes; a minor daily volume fluctuation stays ordinary Baseline variation and need not become a material Change record.

## Non-goals

Significance algorithm selection, anomaly detection implementation, health judgment, or RCA.
