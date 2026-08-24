# REF-001 — Evidence Applicability and Proposition Binding

**Status:** Accepted — Phase 004 Group 01

## Outcome

Before evidence can support, contradict, exclude, or contextualize a conclusion, bind it to the exact proposition being evaluated and determine whether the evidence is applicable enough to bear on that proposition.

## Proposition binding

A proposition should identify, where material:

- subject / Entity Identity;
- property, event, relationship, or outcome being asserted;
- event/effective time or bounded interval;
- environment/context/cohort;
- grain, version, output, execution, or consumer identity;
- direction/strength of conclusion, such as `exists`, `did not occur`, `exposed`, `not exposed`, `ready`, `caused`, or `contradicts`;
- any declared comparison/reference or causal window relevant to the proposition.

Evidence cannot be evaluated meaningfully against an unbounded statement such as `the pipeline is fine` or `nothing changed`.

## Applicability dimensions

An evidence item is evaluated for:

- **subject alignment** — whether it refers to the same identified subject or a justified related subject;
- **semantic/property alignment** — whether the measured/retrieved property actually bears on the proposition;
- **temporal alignment** — whether the evidence applies to the relevant event time/window;
- **grain/version alignment** — whether run/output/version/partition/cohort/consumer scope is compatible;
- **derivation alignment** — whether an aggregate/derived item can legitimately bear on the proposition and its derivation is traceable;
- **relationship alignment** — when reasoning across Lineage or dependencies, whether the relationship was applicable for the relevant time/context;
- **knowledge-cut eligibility** — for historical replay, whether the evidence was recorded/known by the requested cutoff; exact semantics are refined in Group 02.

## Applicability outcomes

A refinement evaluation may describe evidence as:

- applicable;
- partially applicable / scope-limited;
- not applicable;
- temporally non-applicable;
- non-comparable;
- ambiguous/conflicting identity or version;
- unavailable;
- unknown.

These are evidence-relationship results, not health conclusions.

## Invariants

- Evidence that is nearby in time but about the wrong subject/version is not applicable by proximity alone.
- Lineage reachability can make evidence worth inspecting but does not automatically make every upstream fact applicable to every downstream proposition.
- A Deployment record is applicable to a causal proposition only as Deployment evidence; it does not become data-change evidence merely because activation was nearby.
- An aggregate Observation can be applicable without exposing raw rows when its derivation/grain are sufficient for the proposition.
- Restricted disclosure does not make applicable evidence semantically non-applicable; the requester may receive only an authorized abstraction.
- Evidence applicability does not determine source authority, truth priority, or conclusion sufficiency by itself.

## Examples

### Correct version
A row-count Observation for C output V42 is applicable to a proposition about V42 completeness. A count from V41 may be useful comparison context but is not direct evidence about V42's count.

### Wrong grain
A monthly aggregate is insufficiently aligned to prove that one specific daily partition was empty unless its derivation permits that inference.

### Causal timing
B's population reduction before C's loss is temporally relevant to a causal claim. A B reduction first observed after C's loss may still be related historically but cannot support the same temporal-order proposition without additional evidence.

## Non-goals

- selecting authoritative sources;
- assigning a universal evidence score;
- deciding conclusion sufficiency;
- causal confirmation;
- access-control implementation.
