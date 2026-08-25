# Phase 007 Group 07 — Propagation Safeguard Scope, Enforcement, Release & Recovery

**Status:** Next — not started

## Goal

Refine how Propagation Safeguard protects specific suspect states and consumer paths, how enforcement/effectiveness is evidenced, and how release/recovery interact with downstream freshness, delivery and Impact.

## Accepted input from Groups 01–06

Group 07 consumes:

- OPS-001–OPS-009 historical Lineage, publication/consumption paths and bounded alternate-path completeness;
- OPS-010–OPS-020 exact suspect/affected realized state and deployment/change intervals;
- OPS-021–OPS-033 prospective path/review context without treating planned paths as actual protection surfaces;
- OPS-034–OPS-049 actual execution/output/version and negative-consumption evidence;
- OPS-050–OPS-066 Investigation/Causal Claim context without using causal status as control-enforcement proof;
- OPS-067–OPS-085 exact consumer encounter modes/opportunities, exposed/not-exposed/safe/unknown path results, alternate paths, downstream effects and consequence evidence.

Impact state is evidence for safeguard evaluation, not Safeguard truth. In particular:

- a consumer being `not exposed` does not prove a Safeguard prevented exposure;
- a Safeguard being active does not prove it controlled the material encounter path;
- a protected path with an uncovered alternate path cannot support global prevention;
- prevented exposure requires an applicable encounter opportunity or other counterfactual-relevant opportunity plus material enforcement and adequate negative path/version evidence;
- safe/stale serving after a Safeguard may represent successful protection with a separate freshness/delivery consequence.

## Primary questions

- What exactly is protected: suspect output/version, publication channel, consumer path, table/view interface, refresh opportunity, population/cohort or another bounded propagation surface?
- How should proposed/configured/active/enforced/partially enforced/failed/expired/released safeguard state remain distinct?
- What evidence establishes material control over a relevant encounter path/opportunity?
- How should alternate paths and bypasses affect protection/prevention conclusions?
- What supports `prevented exposure` versus merely `Safeguard active + no observed exposure`?
- How should safe prior-state serving, hold/non-delivery and freshness loss be represented during protection?
- How should extension, expiry, release and recovery be represented without implying health/currentness?
- How should safeguard-induced delay, stale serving or non-delivery become separate operational/Impact evidence?

## Group 07 entry scenarios

Explicitly test:

- Safeguard active but no evidence of opportunity-specific enforcement;
- suspect V blocked on primary path while alternate API path remains open;
- suspect V blocked and safe V-1 served, causing staleness;
- hold prevents publication with a real consumer refresh opportunity;
- no consumer opportunity during the hold;
- partial enforcement across consumers/regions/cohorts;
- enforcement telemetry conflict/unavailability;
- expiry before suspect state is cleared;
- release followed by consumer encounter with recovered/suspect/unknown state;
- release with no proof of health/currentness;
- sufficient prevented-exposure claim under complete alternate-path coverage;
- restricted enforcement/path evidence;
- safeguard-induced missed delivery consequence requiring separate Impact/Causal Claim evidence.

## Required boundaries

Preserve:

- proposal/configuration/request ≠ active safeguard;
- active safeguard ≠ enforcement proof;
- enforcement ≠ prevented exposure by itself;
- prevented exposure requires material control plus applicable opportunity and adequate negative/path coverage;
- `not exposed` ≠ `prevented by Safeguard`;
- safeguard release ≠ healthy/current output;
- blocked suspect state ≠ fresh/current downstream delivery;
- safeguard authority ≠ actual enforcement;
- safeguard-induced delay/non-delivery ≠ automatic defect or causal conclusion.

## Handoff to Group 08

Group 08 should preserve Safeguard as output/consumption protection while refining Execution Gate as start/admission control. It should then analyze interactions and control-induced effects without merging the two concepts.

## Deferred

Do not select quarantine tables, views, aliases, ACL mechanisms, publication routing, storage locations, enforcement services or concrete control integrations in this group.
