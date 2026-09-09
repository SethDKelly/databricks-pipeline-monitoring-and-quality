# Group 04 — Adapter Contract

## Required adapter inputs

- tenant/environment profile;
- capability instance and verified surface;
- acquisition plan revision;
- integration principal/credential reference;
- Monitoring Scope materialization or explicit bounded query population;
- service class;
- requested mode/window;
- prior checkpoint/cursor;
- source-specific quota/retry policy;
- minimization/capture class.

## Required adapter outputs

### Acquisition run manifest

Contains durable run/attempt identity, plan/surface/capability identity, timing, requested scope/window, mode and terminal state.

### Request/page manifest

Captures safe request shape, source request ID, response status, page/partition identity, continuation state, item count when safe, and completion/failure.

### Source envelope

Preserves permitted source-local identity, source timestamps, payload/reference/digest and collection coordinates.

### Normalized evidence

Uses durable evidence IDs and parser revision, linking every normalized record to source envelope + acquisition run.

### Coverage manifest

Binds expected population/window to successfully queried/returned/failed/unresolved segments.

### Integration-health update

Emits dimension-specific state for authn/authz/reachability/quota/lag/checkpoint/pagination/schema/parser/persistence/coverage/freshness.

## Forbidden adapter behavior

An adapter must not:

- create ecosystem identity from name/path/time similarity;
- decide Monitoring Scope from discoverability;
- promote source roles to Assertion Authority;
- convert service-principal access into requester disclosure permission;
- infer negative domain truth from empty data while coverage/lag/health is insufficient;
- silently skip failed pages/partitions;
- advance checkpoints before durable evidence commit;
- turn duplicate transports into independent corroboration;
- silently discard parse failures that can affect coverage;
- rewrite historical evidence on parser/schema change;
- silently switch to a lower-authority source;
- continue aggressive polling through explicit throttle guidance.

## Adapter certification

A new adapter is not production-ready merely because it can call the vendor API. It must pass source-specific scenario replay for identity, pagination, checkpoints, retries, lag, permission loss, quota, schema drift, retention expiry and optional/degraded operation.
