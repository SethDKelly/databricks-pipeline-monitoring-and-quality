# AUTH-043 — Action, Approval, Enforcement, Outcome, and Historical Audit Separation

**Status:** Accepted — Phase 005 Group 05

## Purpose

Preserve a complete high-consequence audit chain without conflating authorization, approval, action issuance, external enforcement, operational outcome, health, or causal truth.

## Contract

Where material, retain distinct provenance-bearing records/references for:

1. requested/proposed action;
2. authorization/approval resolution and conditions;
3. action issuance/execution attempt by the authorized principal;
4. delivery/acceptance by an external control plane where applicable;
5. enforcement/effect evidence;
6. resulting execution/publication/consumption/claim state;
7. downstream operational/business outcome;
8. later correction/review/revocation state.

These stages may have different event, recorded/knowledge, and evaluation times.

## Invariants

- Approved ≠ executed.
- Executed/issued ≠ externally accepted.
- Accepted by a control plane ≠ enforced.
- Enforced ≠ desired outcome achieved.
- Desired operational outcome ≠ healthy data or correct causal conclusion.
- Gate override action ≠ prerequisite ready.
- Safeguard release action ≠ output healthy.
- Job retry action ≠ successful run.
- Causal confirmation authorization ≠ confirmation action; confirmation action still requires the accepted evidence profile and provenance.
- Historical replay preserves the exact authorization/approval/action/enforcement state known then; later correction does not rewrite prior action history.
- Current authorization governs present review/disclosure even when reconstructing historical high-consequence activity.

## Example

An override receives the required approvals at 07:10, an operator issues it at 07:12, the external scheduler accepts it at 07:13, C starts at 07:14, and a stale-output Assessment appears at 07:20. Each state remains separately represented; the earlier approvals do not prove the downstream outcome was safe.