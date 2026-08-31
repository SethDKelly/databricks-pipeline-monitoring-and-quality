# Group 08 — Optional Integration & Capability Degradation

## Capability inventory

Every deployment maintains revisioned target-environment capability facts for enabled core/optional integrations, including material plan/version/region/permission/reachability/limit information and verification freshness.

## Optional sources

Collibra, Immuta, external BI/application telemetry, incident/business/financial systems and model/search providers remain optional unless a deployment explicitly makes a feature depend on them.

If an optional capability disappears:

- preserve unrelated canonical monitoring;
- mark dependent propositions/features unavailable/partial;
- surface missing coverage/authority/context;
- do not fabricate platform defaults or substitute unrelated sources;
- do not rewrite historical periods when the integration was available.

## Feature flags

Feature enablement is capability-aware and tenant/deployment scoped. UI hiding is not the only enforcement boundary; backend routes/retrieval also enforce capability and authorization constraints.