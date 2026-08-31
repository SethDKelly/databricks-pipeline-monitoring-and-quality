# Group 08 — Backup, DR, Residency & Lifecycle Operations

## Protected state

Disaster recovery protects canonical evidence/provenance journals, identity/governance/policy revisions, Investigation/Causal Claim state and promised retained Explanation/control/basis records according to deployment-specific retention/RPO/RTO commitments.

Derived graph/search/cache/read models are rebuilt from canonical state where possible.

## Restore semantics

Restore provenance records what was recovered, from which retained snapshot/archive and what gaps remain. Recovery today does not rewrite yesterday’s missing evidence or availability-by-K.

## RPO/RTO by service class

SC-01/SC-06 may require tighter recovery than cold SC-04/SC-05 history. Numeric targets remain deployment ADRs, but architecture must state the promises separately.

## Residency

Canonical data and processing are sharded/located according to tenant/residency policy. Cross-region/Geo backup or centralized metadata is used only where the policy explicitly permits it.

## Testing

A backup that has never been restoration-tested does not establish an operational recovery guarantee.