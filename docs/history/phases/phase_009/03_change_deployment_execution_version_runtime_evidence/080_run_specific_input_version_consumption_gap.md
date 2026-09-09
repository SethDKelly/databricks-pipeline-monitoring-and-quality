# INTG-080 — Run-Specific Input-Version Consumption Gap

**Status:** Accepted — Phase 009 Group 03

For generic multi-input Spark/SQL workloads, the evaluated out-of-box sources do not provide a universal exact manifest of every input entity/version consumed by a run.

Exact consumption is therefore **unsupported out of the box / conditional** on workload-specific telemetry, query/transaction evidence, explicit version parameters, source snapshots, manifests or other accepted instrumentation. `Latest upstream output` and temporal proximity remain invalid substitutes.
