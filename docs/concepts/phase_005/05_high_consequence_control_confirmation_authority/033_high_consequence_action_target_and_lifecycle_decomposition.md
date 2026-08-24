# AUTH-033 — High-Consequence Action Target and Lifecycle Decomposition

**Status:** Accepted — Phase 005 Group 05

## Purpose

Bind high-consequence authorization to the exact action, target, context, and lifecycle stage rather than granting a broad `operator` or `administrator` capability.

## Contract

A high-consequence authorization target should identify, where material:

- principal or control/service principal;
- exact action class and lifecycle stage;
- target subject/control/claim/execution opportunity;
- environment, tenant, consumer, incident, or purpose context;
- effective interval and knowledge time;
- required normative/control profile or rule version;
- approval/delegation/emergency conditions;
- provenance and authority for the authorization decision.

Relevant lifecycle stages include **propose/request**, **approve/authorize**, **execute/issue**, **override/cancel/release**, and where applicable **review/close**. These are independently resolvable capabilities.

## Invariants

- Permission to propose an action does not imply permission to approve or execute it.
- Permission to approve does not imply permission to execute.
- Permission to execute does not imply permission to override, cancel, release, retire, or delegate.
- Broad titles such as `admin`, `owner`, `operator`, `on-call`, or `service account` do not create universal high-consequence authority.
- High-consequence-use eligibility from AUTH-023 is a prerequisite-governance fact, not permission to operate the control.
- Authorization to perform a high-consequence action never proves the action was issued, enforced, successful, safe, or causally justified.

## Examples

A responder may be allowed to **propose** a safeguard while activation requires a second authorized approver and a separately authorized executor. A platform operator may be allowed to execute an approved gate override without being allowed to approve their own override request.