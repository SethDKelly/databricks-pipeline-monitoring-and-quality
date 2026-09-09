# AUTH-037 — Propagation Safeguard Proposal, Activation, Release, and Recovery Authority

**Status:** Accepted — Phase 005 Group 05

## Purpose

Separate safeguard proposal, activation, maintenance, release, cancellation, renewal/expiry, and recovery authority so protective action and restoration of propagation are independently governable.

## Contract

Safeguard capabilities may independently include:

- propose a safeguard for a bound output/consumption boundary;
- approve activation when required;
- activate/issue the protective action;
- extend/renew or alter its bounded scope where explicitly allowed;
- cancel a proposal that never activated;
- release an active safeguard;
- retire or expire a recurring/preconfigured safeguard rule where later represented.

Each capability binds protected subject/boundary, environment/consumer scope, effective interval, reason/incident context where required, approval conditions, and provenance.

## Invariants

- Proposal authority does not imply activation authority.
- Activation authority does not imply release authority; release can be equally or more consequential because it restores exposure/consumption.
- Data ownership, responsibility, or the ability to view an Assessment does not silently grant safeguard authority.
- Safeguard authority does not imply Execution Gate authority.
- Activation permission does not prove the external boundary was actually protected.
- Release permission/action does not prove the output is healthy or that the original concern was resolved.
- An automated response may activate or release only under an explicitly authorized action class and conditions; a monitoring alert alone does not authorize protection.
- Missing or unavailable authorization does not silently activate, maintain, or release a safeguard; any fallback behavior must be explicitly governed.

## Example

An analyst can propose a quarantine based on a severe Assessment. A separately authorized incident approver permits activation, a control service executes it, and release later requires another authorized action after review. None of those stages changes the underlying health evidence.