# INTG-061 — Databricks External-Deployment / Bundle Provenance

**Status:** Accepted — Phase 009 Group 03

Databricks job deployment metadata can identify externally managed/BUNDLE resources and associated metadata-file context. Bundle Git metadata can carry repository origin/branch context.

These fields establish management/provenance context only. They do not by themselves attest an immutable Git commit for every deployed workspace-source resource or every later run.
