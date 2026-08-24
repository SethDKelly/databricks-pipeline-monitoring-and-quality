# AUTH-023 — High-Consequence Metric / Expectation Use Eligibility

**Status:** Accepted — Phase 005 Group 03

## Purpose

Require explicit normative governance before a metric, schema condition, or Expectation is eligible to participate in an Execution Gate, Propagation Safeguard policy, automated escalation, or other high-consequence decision, without granting the authority to configure/operate that control or proving its evidence is timely/sufficient.

## Contract

A high-consequence-use eligibility assertion should bind:

- exact metric/check/Expectation and version/profile;
- subject, consumer/control target, environment, and use context;
- permitted high-consequence use class;
- applicable threshold/schema rule and lifecycle state;
- authority/provenance for the eligibility decision;
- effective interval and any review/expiry condition.

## Invariants

- Being in a metric profile does not automatically make a metric control-eligible.
- Being business-critical does not automatically make a metric suitable for an Execution Gate.
- An authoritative Expectation does not automatically authorize its use as an active control predicate.
- Control-use eligibility does not grant gate/safeguard configuration, activation, release, override, or job-operation capability; Group 05 owns those authorities.
- Control-use eligibility does not prove the metric/check is currently available, fresh, sufficiently covered, or correctly enforced. REF-001–REF-030 and later Phase 006/009 timing semantics still apply.
- If required evidence is unavailable, an eligible criterion may still resolve readiness/control evidence as unknown and invoke only the explicitly governed fallback behavior.
- CI validation eligibility and runtime gate eligibility can be separately governed because they have different consequences and availability needs.
- Removing control-use eligibility prospectively does not rewrite historical gate/safeguard decisions that legitimately used the rule while it was eligible.

## Example

A completeness metric may be approved for monitoring and business reporting but not for blocking production. A separately governed decision can make a versioned completeness Expectation eligible for a specific downstream Execution Gate; Group 05 must still authorize who can configure/enable/override the gate, and Phase 004/006/009 must still establish evidence readiness.