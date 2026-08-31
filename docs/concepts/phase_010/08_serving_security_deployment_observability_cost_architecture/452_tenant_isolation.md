# ARCH-452 — Tenant Isolation

**Status:** Accepted

Canonical storage, derived projections, caches, search/vector corpora, logs and runtime request contexts preserve tenant isolation at every material boundary.

Cross-tenant identifiers, counts or hidden-basis metadata are not exposed through shared convenience layers.