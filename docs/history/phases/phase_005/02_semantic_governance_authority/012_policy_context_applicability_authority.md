# AUTH-012 — Policy-Context Applicability Authority

**Status:** Accepted — Phase 005 Group 02

## Purpose

Apply Assertion Authority to Policy Context while distinguishing authority over a policy/reference from authority to assert that the policy applies to a particular subject/use/context.

## Contract

Policy governance may involve separate authority targets for:

- the policy/control-framework reference or authoritative policy text;
- applicability to a subject, environment, jurisdiction, purpose/use, or consumer;
- approved monitoring/handling summary or interpretation at a bounded non-legal level;
- correction/supersession of applicability assertions.

A source authoritative for policy text is not automatically authoritative for every subject-level applicability assertion unless an accepted rule says so.

## Invariants

- Classification may be an applicability input but does not itself prove Policy Context.
- Policy Context does not grant/deny access, prove enforcement, prove compliance, or perform legal interpretation.
- Multiple policies may simultaneously apply without conflict.
- Conflict exists when applicable authoritative assertions disagree for the same policy/applicability target/context/time, not merely because several policies exist.
- Missing policy authority/context remains unknown/unavailable, not unrestricted.
- Responsibility for compliance/security does not automatically confer policy-applicability authority.
- Policy summaries remain traceable to the underlying governed policy/applicability assertions.

## Example

A governance source can be authoritative for a healthcare handling policy while a separate governed process determines whether that policy applies to Table C in a particular production use. A PHI classification can support that applicability decision without becoming the decision itself.