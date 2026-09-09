# ARCH-437 — Authorization-Context Cache Keying

**Status:** Accepted

Any cache containing authorization/disclosure-sensitive results is partitioned/keyed by the material policy context needed to prevent cross-principal, cross-purpose, cross-tenant or cross-detail reuse.

A broader cached projection cannot be reused for a narrower requester by post-hoc UI hiding.