# INTG-027 — IAM Principal Source & Projection

**Status:** Accepted — Phase 009 Group 02

Where Databricks or Immuta synchronizes users/groups/attributes from an external identity provider, the synchronized platform identity is a projection of that upstream identity for the supported fields.

The upstream IAM remains the candidate authority for attributes/group membership it actually sources; locally-created platform identities/attributes remain distinct. Group source, external ID and synchronization mode are material.
