# Runtime Provenance Model

## Canonical chain

**Change Intent → CI execution → deployment attempt → target activation → run → task/attempt → implementation manifest → input consumption → output production**.

Every arrow requires explicit evidence; timestamps/names are candidate correlation only.

## Canonical records

### `deployment_manifest`

Minimum fields:

- `deployment_manifest_id`
- tenant/environment/target IDs
- source repository + commit when Git-backed
- artifact/bundle/content digest
- deploy workflow/run/attempt IDs where applicable
- deploy attempt/result
- target resource IDs
- correlation ID
- effective configuration revision
- event/effective/availability/persistence times
- source/acquisition provenance

### `run_manifest`

- canonical/source run IDs
- job/pipeline/workflow/task identities
- attempt/repair/retry lineage
- trigger/parent relation
- deployment/correlation references
- start/end/lifecycle evidence
- implementation-manifest ID
- acquisition coverage/limitations

### `implementation_manifest`

Facets are independently optional/known:

- code revision/content
- job/task config revision
- parameters
- runtime/compute
- libraries/packages
- environment/capability profile
- external config/secret references

Completeness is explicit. Missing facets are never inherited from current state.

## Direct Git versus workspace/bundle source

For qualifying Databricks remote-Git jobs, `git_snapshot.used_commit` is run-owned source evidence.

For workspace/Git-folder/bundle source, exact Git revision requires deployment/content attestation plus run-specific binding where the product promises exact provenance. A deployment manifest alone proves deployment identity, not that every later run consumed an unchanged source unless the run binding is established.

## Cross-system correlation

Preferred correlation key is a DMTZ-generated opaque ID carried across CI/deployment/runtime records where controllable.

When unavailable, correlation can still be established from source-native immutable IDs/attestations. Name/time-only correlation remains partial/unresolved.

## Retry/repair semantics

Retries/repair attempts remain distinct execution records linked to original attempt/run according to the source. A logical rollup is derived and cannot erase attempt-level evidence.
