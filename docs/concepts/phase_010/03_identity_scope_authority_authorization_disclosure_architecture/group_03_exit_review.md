# Phase 010 Group 03 — Exit Review

**Status:** COMPLETE / ACCEPTED

## Accepted range

- ARCH-081–ARCH-132 accepted.
- Cumulative Phase 010 architecture range: ARCH-001–ARCH-132.
- IAD03-01–IAD03-84 pass.
- D-1337–D-1382 accepted.

## Exit conclusion

Identity, scope, authority, authorization and disclosure now have concrete canonical architecture without treating IAM products as the product truth model.

The selected logical architecture is:

**tenant-scoped canonical Entity/Principal registries + evidence-bearing source identity bindings + versioned Monitoring Scope + versioned Assertion Authority + versioned Capability Authorization + retained material decision manifests + current disclosure projection over the Group 02 canonical persistence plane**.

## Gap treatment

- **GAP-009-01 Monitoring Scope:** architecture resolved by organization-owned versioned scope registry/materialization.
- **GAP-009-02 Assertion Authority:** architecture resolved by organization-owned policy-as-data authority registry.
- **GAP-009-03 cross-system Entity Identity:** architecture resolved by canonical entity/principal registry plus evidence-bearing source bindings; actual mappings remain deployment data.
- **GAP-009-20 causal confirmation authority:** architecture resolved by explicit causal authority profile; confirmation still requires REF-017 + AUTH-034 at runtime/workflow.
- **GAP-009-29 historical authorization:** architecture materially resolved through versioned policy/membership inputs plus actual decision journal/replay distinction; source-native historical gaps remain environment-specific.
- **GAP-009-31 sensitive basis disclosure:** architecture resolved through disclosure-dimensional authorization, safe projection, itemwise basis filtering and metadata/mosaic protection.

## Durable safeguards

1. Entity Identity is not name/path/timestamp similarity.
2. Source identity remains source-owned after canonical mapping.
3. Monitoring Scope is not source presence/access or authorization.
4. Unknown scope membership is not exclusion.
5. Vendor role/ownership is not automatic Assertion Authority.
6. Assertion Authority is not evidence sufficiency or Capability Authorization.
7. Authorization is not action occurrence or enforcement.
8. Historical authorization is not current permission.
9. Actual retained decision is not replay-derived authorization.
10. Service-principal processing permission is not requester visibility.
11. Conclusion visibility is not basis/detail/export permission.
12. Safe abstraction cannot strengthen or broaden a proposition.
13. Hidden basis existence/count/provenance can itself be sensitive.
14. Retained/archived evidence is not automatically disclosable.
15. Cross-residency authorization does not justify centralizing restricted payloads.
16. Vendor-documented IAM capability is still deployment-bound under Group 01.

## Technology decisions intentionally not made

Group 03 does not select an external policy engine, IAM/IdP vendor, authoring UI, secret store, service/API topology, event bus or connector synchronization mechanism. The canonical rule/data model is selected; runtime packaging remains later architecture work.

## Group 04 entry

Group 04 may design source acquisition/adapters/integration health over ARCH-001–ARCH-132. Adapters must preserve source-local identity, map through canonical identity primitives, evaluate collection permissions without treating denial as domain absence, respect Monitoring Scope, and emit coverage/health facts needed for later authorization/negative-evidence reasoning.