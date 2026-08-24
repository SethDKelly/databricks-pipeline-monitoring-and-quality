# AUTH-025 — Authorization State, Conditions, and Resolution Semantics

**Status:** Accepted — Phase 005 Group 04

## Purpose

Define authorization-result semantics without converting missing/conflicting evidence into permission or inventing a universal `deny wins` rule that erases the underlying authorization truth.

## Accepted states

At minimum, resolution can yield:

- **allowed** — an applicable authoritative authorization permits the exact capability target;
- **denied** — an applicable authoritative authorization explicitly prohibits the exact capability target;
- **conditional** — permission depends on one or more explicit conditions that are not yet fully resolved for the request;
- **unknown** — no sufficient applicable authorization resolution can be established;
- **conflicting** — applicable authoritative authorization assertions disagree and no accepted resolver applies;
- **unavailable** — required authorization evidence/source cannot currently be evaluated.

## Conditional authorization

Conditions may reference purpose, environment, tenant, subject set, consumer, time window, incident state, approval, or other explicitly modeled context. A conditional grant becomes usable only when the applicable condition is evidenced as satisfied. Missing condition evidence does not become `allowed`.

## Conflict and fail-safe behavior

Authorization truth and runtime fallback remain separate:

- `unknown` is not `denied` and never means allowed;
- `conflicting` is not `denied` and never means allowed;
- `unavailable` is not `denied` and never means allowed;
- an implementation may later conservatively refuse an action unless a positive applicable allow is resolved, but that fail-safe behavior must not rewrite the underlying state to `denied`;
- `deny wins`, `direct decision wins`, `latest wins`, or `most specific wins` are valid only when an explicit accepted authorization-combination rule says so.

## Invariants

- Capability Authorization is proposition-specific to principal + action + subject + context + time.
- Missing authorization evidence is never permission.
- Source availability or synchronization order is not authorization precedence.
- Authorization conflict remains visible until an accepted authority/combination rule resolves it.
- A positive authorization result does not prove external enforcement or successful action.
