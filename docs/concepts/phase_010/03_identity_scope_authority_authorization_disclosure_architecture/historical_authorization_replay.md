# Phase 010 Group 03 — Historical Authorization & Governance Replay

## Purpose

Support current authorization, historical authorization, actual retained decision history and current disclosure without collapsing them.

## Four states

1. **historical source/policy state** — what identity/membership/scope/authority/authorization state was effective then;
2. **as-known-at-K policy state** — what qualifying policy/membership evidence was available by the requested knowledge cut;
3. **actual retained decision** — evidence that an authorization/authority/disclosure evaluation actually ran and what it returned;
4. **current replay/current disclosure** — a current evaluation over historical inputs and current requester permissions.

They are independently answerable.

## Actual decision record

Where product/control/audit requirements justify retention, preserve:

- decision identity;
- decision time;
- policy revision identities;
- principal and membership inputs;
- subject/action/context;
- source/local IAM evidence consulted where material;
- result and conditions;
- resolver/version;
- correlation to subsequent request/action/enforcement where available.

A decision record proves the evaluation, not subsequent enforcement.

## Replay-derived result

If an actual decision record is missing but historical inputs survive, DMTZ may reconstruct what the retained rules imply. The result is labeled replay-derived and cannot be presented as proof that the actor was actually checked or admitted at the time.

## Missing history

Expired group membership, policy revisions or source IAM history can make historical authorization unresolved. Current state is never substituted as if historical.

## Retention

Policy/rule history is relatively low-volume but still follows Group 02 lifecycle policy. Exact decision/policy inputs are pinned for dependent retained communication, control, causal confirmation, audit or legal/security commitments. Routine low-value decision telemetry may age after its committed horizon.

## Disclosure of history

Historical authorization facts are themselves sensitive. Current requester authorization governs whether current users can inspect old permission/membership states. A person having been the historical actor does not automatically grant them current access to the audit record.