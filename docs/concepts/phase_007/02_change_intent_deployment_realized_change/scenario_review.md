# Phase 007 Group 02 Scenario Review — Change Intent, Deployment Realization & Realized Change

**Status:** Accepted — C02-01–C02-24 pass

This suite tests OPS-010–OPS-020 against ordinary, ambiguous, negative-evidence, phased, rollback and historical cases.

## C02-01 — Planned filter fully realized
Intent I1 says production C will activate filter F2 and population should decrease. Deployment D1 is explicitly linked to I1, F2 activation is established, and comparable evidence establishes the intended population change.

**Pass.** Association, activation, realized Change and intent conformance are separately evidenced. The implementation component/effect can be `matched` without implying health or cause.

## C02-02 — Deployment attempt fails
D1 is linked to I1 but the deployment mechanism reports failure and no activation evidence exists.

**Pass.** Attempt/association remain historical; activation is not established and the intent is not marked realized.

## C02-03 — Workflow success, activation unknown
CI/CD reports success for R2 but target/runtime evidence cannot establish R2 active.

**Pass.** Attempt outcome is known; activation remains unknown/not evidenced. Workflow success does not manufacture active state.

## C02-04 — Activation established, intended effect absent
F2 is proven active, but bounded negative evidence establishes C population did not decrease during the intended evaluation window.

**Pass.** Implementation activation is established while anticipated-effect comparison can be `not realized`/diverged as applicable. Activation does not manufacture effect.

## C02-05 — Activation established, effect not yet evidenced
F2 is active, but downstream Observation evidence is delayed/unavailable.

**Pass.** Implementation state can be matched while effect realization is `not evidenced`/unavailable rather than assumed.

## C02-06 — Intended effect partially realized
Intent requires two target populations P1/P2. P1 conforms; P2 remains on prior state.

**Pass.** Slice-specific results are retained and overall shorthand can be `partially matched` only under explicit composition.

## C02-07 — Realized magnitude diverges
Intent anticipates a modest reduction; evidence establishes a 70% drop outside the bounded intended range.

**Pass.** Realized Change remains valid; comparison is `diverged` without automatically labeling the outcome defective or causal.

## C02-08 — Undeclared side effect
The intended population reduction occurs, while null rate also increases although the intent never mentioned null behavior.

**Pass.** The null-rate Change is `not declared/anticipated in the registered intent`; documentation silence is not proof of humanly unintended behavior. Health remains separate.

## C02-09 — One Deployment realizes several intents
Release D2 contains independent filter I1 and schema I2 components.

**Pass.** Per-intent linkage/comparison remains separate. Schema divergence cannot rewrite a valid filter realization.

## C02-10 — One intent spans several Deployments
I3 requires code deployment, later configuration enablement and regional rollout.

**Pass.** Many-to-one realization is represented across several activation intervals/slices; no single deployment is declared the whole intent by convenience.

## C02-11 — Wrong environment activates
R2 becomes active in development while I1 targets production.

**Pass.** Development activation does not realize the production intent.

## C02-12 — Canary rollout
Ten percent canary cohort activates F2 before the rest of production.

**Pass.** Canary state remains slice-specific. Ten-percent rollout does not globally switch the target context or imply 10% semantic completion unless the intent defines that measure.

## C02-13 — Overlapping intents
I4 and I5 overlap target/time/facet and both are compatible with observed C population shift.

**Pass.** Both can retain realization context while causal attribution remains unresolved. Temporal compatibility does not decide which intent/deployment caused the effect.

## C02-14 — Configuration-only change
Source revision remains R2 while runtime configuration changes K6→K7.

**Pass.** Configuration state is independently versionable; same commit does not mean unchanged operating state.

## C02-15 — Repository commit differs from deployed runtime identity
Repository main points to R3, deployment provenance establishes package built from R2 plus K7 active in production.

**Pass.** Current repository revision is not substituted for active deployment identity.

## C02-16 — Unregistered deployment
D4 activates a configuration with no matching registered intent known.

**Pass.** Deployment remains valid evidence. The result is unregistered/no matching intent known, not automatically unauthorized or unplanned.

## C02-17 — Realized source shift with no Deployment
B distribution/semantics change from source-system behavior without a monitored deployment or registered intent.

**Pass.** Change can be established independently. Missing intent/deployment context is not fabricated.

## C02-18 — Outside declared intent scope
I6 declares a schema addition for interface A; evidence establishes an additional incompatible change to interface B outside that declared target.

**Pass.** B's Change can be marked outside declared intent scope when scope/Change evidence is sufficient; this still does not determine defect or authorization.

## C02-19 — Rollback reactivates prior revision
R2 is active from 10:00–11:00; rollback D6 activates R1 again at 11:00.

**Pass.** Both activation intervals remain. R2 history is not erased and R1's second interval is not backdated.

## C02-20 — Code rollback does not restore produced data
R1 code is restored, but data written by R2 remains in C.

**Pass.** Deployment restoration and data-state restoration are separate propositions. Data Change/health require their own evidence.

## C02-21 — Revision label restored, configuration differs
R1 is reactivated with configuration K8 rather than historical K4.

**Pass.** Same code revision does not prove restoration of the former composite operating state.

## C02-22 — Late activation correction
At incident time activation was unknown. Later evidence proves R2 activated at 09:55.

**Pass.** Retrospective active-state history uses 09:55 while the contemporaneous knowledge cut preserves activation unknown.

## C02-23 — Conflicting active-state sources
One source says R2 active; another applicable source says R1 active and evidence/authority does not resolve the conflict.

**Pass.** Active state remains conflicting. Neither recency nor source convenience silently wins.

## C02-24 — Planned topology becomes effective only after relationship evidence
Intent proposes new D→C input; deployment activates code intended to use D. Lineage evidence later establishes D→C effective for the relevant population/version.

**Pass.** Planned topology, deployment activation, effective Lineage and realized topology Change remain separate. Deployment activation alone does not create the edge.

## Exit result

All C02-01–C02-24 pass without:

- a new realization concept;
- a universal deployment/version identifier;
- workflow-success activation shortcuts;
- one scalar realization/completion score;
- treating missing registration as humanly unplanned/unauthorized;
- treating rollback as historical erasure or universal downstream restoration;
- causal/health inference from intent conformance;
- architecture/source-integration selection.
