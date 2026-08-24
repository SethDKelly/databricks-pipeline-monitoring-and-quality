# REF-016 — Material Alternatives and Causal Discrimination

**Status:** Accepted — Phase 004 Group 03

## Purpose

Require stronger causal statuses to account for material competing explanations without demanding proof against every imaginable alternative or forcing mutually compatible contributors into a single winner.

## Material alternative set

An alternative is material when, within the bounded Investigation scope and evidence known at the relevant cutoff, it is plausible enough and relevant enough that ignoring it would materially overstate the focal claim.

Materiality can arise from:

- historical Lineage/dependency structure;
- observed Changes/Assessments;
- timing;
- known Deployments/Change Intent;
- mechanism compatibility;
- analyst evidence/context;
- prior comparable incidents;
- other provenance-bearing evidence.

## Rules

- Stronger causal status requires a documented bounded alternative set appropriate to the claim and Investigation scope.
- The framework does not require enumeration or exclusion of every conceivable cause.
- Mutually compatible contributors are not treated as competitors merely because more than one claim exists.
- Evidence supporting one claim does not automatically contradict another claim that could coexist causally.
- For materially competing or mutually exclusive claims, inability to discriminate can justify `unresolved` even when each claim has some support.
- A claim cannot become `confirmed` merely because it is the best-ranked available story while other material alternatives remain comparably supported and unresolved under the applicable confirmation profile.
- Alternative exclusion relies on REF-001–REF-005: negative evidence requires applicable opportunity-to-observe and sufficient bounded coverage.
- Restricted or unavailable evidence can leave a material alternative opaque; that limitation remains explicit rather than being treated as exclusion.
- The bounded alternative set can evolve as later evidence reveals previously unknown candidates; earlier evaluations remain historically reconstructable.

## Example

C loses rows. B population decline and increased join-key nulls can both contribute and need not compete. A recent Deployment is a separate claim. If C's degradation is sufficiently established to predate the Deployment, that can discriminate against the Deployment claim. If evidence cannot distinguish whether B population decline or join-key degradation contributed, both can remain supported contributors without forcing one root cause.

## Non-goals

- exhaustive causal universe enumeration;
- ranking algorithm selection;
- Bayesian probability assignment;
- single-root-cause enforcement.
