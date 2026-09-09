# SYN-015 — Runtime Risk Context → Propagation Safeguard

**Status:** Accepted — Phase 003 Group 03

## Outcome

Allow proactive or reactive protection of downstream consumers when an authorized decision concludes that continued propagation is too risky, while separating evidence/health judgment from the protective control itself.

## Participating concepts and actions

- **Propagation Safeguard** — `propose`, `activate`, `release`, `resolveAt`.
- **Assessment** — reactive health evidence.
- **Investigation** — optional human review context.
- **Impact** and **Lineage** — downstream candidate/placement context.
- **Change Intent** — prospective planned-change context.
- **Responsibility Assignment** / **Policy Context** — optional governance/routing context.

## Trigger / initiating condition

An authorized human decision or later-accepted response rule determines that a planned or observed condition warrants protective propagation control.

## Preconditions

The protected subject/boundary is identified; proposal versus active enforcement remains distinguishable; activation authority is established under applicable semantics.

## Coordination semantics

1. Gather the relevant evidence/risk context without converting it into an automatic quarantine decision.
2. Use Lineage/Impact to evaluate candidate placement: origin output, publication boundary, specific consumer/region/cohort, or another supported boundary.
3. Prefer the least disruptive effective protection scope consistent with the accepted decision; do not assume source-level quarantine is always correct.
4. Record `propose` when protection is recommended but not yet enforced.
5. Record `activate` only when authority and enforcement evidence support active protection.
6. If no output exists, safeguard downstream advancement/current-cycle publication instead of inventing a quarantined data object.
7. Record release explicitly when authorized evidence/decision ends the protected interval.
8. Observe any operational delay/non-delivery created by the safeguard as separate runtime evidence.

## State and evidence effects

Source evidence/Assessments/Impact remain unchanged. Propagation Safeguard owns the protective lifecycle.

## Ambiguity / failure propagation

Unknown enforcement remains proposed/activation-unknown. Incomplete Lineage may limit confidence in placement coverage. A high-risk unknown can justify a proposal under policy/human judgment without being mislabeled a confirmed defect.

## Temporal semantics

Proposal, active protected interval, release, and knowledge/correction times remain distinct.

## Provenance / traceability

Every active safeguard traces to authority, enforcement evidence, protected boundary, and the evidence/context that motivated it.

## Security / authorization

Monitoring visibility does not grant production-control authority. Restricted client/consumer detail may be abstracted while safeguard scope remains enforceable by authorized systems.

## Invariants

- Assessment ≠ safeguard;
- proposed ≠ active;
- quarantine ≠ proof of defect;
- release ≠ proof of health;
- no output ≠ quarantined object;
- safeguard placement ≠ Lineage truth;
- safeguard-induced delay remains observable;
- automatic quarantine requires explicit accepted authority/rule.

## Scenarios

Completeness failure on C triggers an authorized quarantine at C publication; missing C output holds downstream current-cycle delivery; planned high-blast-radius A change proposes a temporary first-run safeguard; client-specific boundary is held while internal consumers continue.

## Non-goals

Defining the organization's response policy, implementing storage/quarantine mechanics, deleting data, automatic rollback, or causal attribution.
