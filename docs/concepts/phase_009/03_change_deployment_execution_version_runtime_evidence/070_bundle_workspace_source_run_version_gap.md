# INTG-070 — Bundle / Workspace-Source Run-Version Gap

**Status:** Accepted — Phase 009 Group 03

Databricks recommends workspace-source tasks for bundle-deployed code rather than combining bundle source deployment with job-level Git source. Documented bundle metadata exposes repository origin/branch context and external-management state but not a universal immutable commit consumed by each run.

Therefore exact Git revision for a bundle/workspace-source run is **unsupported out of the box / conditional** on explicit deployment/run attestation, immutable content manifest, artifact fingerprint or equivalent evidence.
