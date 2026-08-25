# OPS-015 — Intent-to-Realization Comparison Layers & Vocabulary

**Status:** Accepted — Phase 007 Group 02

## Purpose

Answer `what became of this intent?` without creating a fourth truth-owning lifecycle concept or hiding evidence gaps behind a single convenient `deployed`/`realized` flag.

## Derived comparison

Intent-to-realization comparison is a **derived synchronization result** over:

- exact Change Intent revision/component from OPS-010;
- associated Deployment evidence from OPS-013;
- activation/active-state evidence from OPS-012;
- realized Change from OPS-014;
- applicable temporal/evidence rules from REF-001–REF-012.

It owns no independent historical truth. Every result remains traceable to the underlying concepts and selected knowledge cut.

## Comparison layers

At minimum preserve separately:

1. **association layer** — is this intent component linked to a deployment attempt/activation?;
2. **activation layer** — did the intended implementation state become active for this target/slice?;
3. **realized-state layer** — what implementation/data/schema/topology/behavior Change is actually evidenced?;
4. **intent-conformance layer** — how does that realized state compare with the bounded intended proposition/anticipated effect?;
5. **limitations layer** — what evidence, coverage, conflict or restriction limits the comparison?

Success at one layer never manufactures the next.

## Conformance vocabulary

For one exact intent component/effect comparison, use as applicable:

- `matched` — sufficient evidence establishes the realized state/effect conforms to the bounded intended proposition;
- `partially matched` — some explicitly required components/slices conform while others are divergent, unresolved or not realized;
- `diverged` — sufficient evidence establishes material incompatibility with the bounded intended proposition;
- `not realized` — sufficient negative evidence establishes the intended state/effect did not occur within the bounded realization opportunity/window;
- `not evidenced` — positive realization evidence is not currently established, without claiming non-realization;
- `indeterminate` — applicable evidence is insufficient/non-comparable to decide;
- `conflicting` — applicable evidence supports incompatible results;
- `unavailable` — required evidence cannot currently be obtained.

There is no universal numeric percent-complete or realization confidence score.

## Anticipated-effect discipline

Implementation activation may be `matched` while an anticipated downstream effect is `not evidenced`, `diverged`, or independently satisfied for another reason. Conformance is not causality.

## Invariants

- intent realization comparison ≠ new Concept;
- associated ≠ activated ≠ realized effect ≠ matched intent;
- `not evidenced` ≠ `not realized`;
- `matched` ≠ healthy/acceptable;
- `diverged` ≠ defective/unauthorized;
- anticipated-effect match ≠ proof the deployment caused the effect;
- comparison uses the exact intent revision effective for the question, not the latest revision by convenience.

## Handoff

OPS-016 defines how comparison behaves across partial/phased/multi-target and overlapping realization.