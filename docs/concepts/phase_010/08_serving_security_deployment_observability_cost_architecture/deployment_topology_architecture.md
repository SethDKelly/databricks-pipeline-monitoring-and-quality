# Group 08 — Deployment Topology Architecture

## Selected logical topology

The reference topology is **Databricks-centered canonical evidence + portable stateless service/edge components**.

- Canonical Delta journals/policies remain in the governed Group 02 data plane.
- Reconciliation, normalization, measurement and heavy replay may run as Databricks-native jobs/compute or equivalent portable workers according to deployment facts.
- Interactive serving uses a stateless API façade rather than exposing raw canonical tables to UI callers.
- GitHub protection callbacks and Databricks pre-start control brokers may use an external reachable service boundary when necessary.
- Derived serving stores/indexes are disposable/rebuildable.

## Failure-domain isolation

SC-06 active control receives sufficient independent capacity, credentials and operational isolation that dashboard/model/replay saturation cannot decide its behavior indirectly.

Optional model/vector/search services are not in the canonical or active-control critical path.

## Environment isolation

Development/test/staging/production use distinct credentials/configuration/callback identities and appropriately isolated data. Production evidence/control cannot be mutated from lower environments.

## Deployment revisions and rollback

Configuration/topology revisions are version-addressed. Rollback changes the running implementation, not canonical historical records produced by the superseded revision.

## Capability verification

Startup and periodic reconciliation verify material capability instances and assumptions. Target environment facts win over public documentation when availability differs.