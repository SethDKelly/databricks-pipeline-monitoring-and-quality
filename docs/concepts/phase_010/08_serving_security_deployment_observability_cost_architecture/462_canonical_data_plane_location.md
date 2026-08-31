# ARCH-462 — Canonical Data Plane Location

**Status:** Accepted

Canonical structured state remains in the Group 02 Delta-first governed data plane; external application/service databases may store transient sessions, queues or derived projections but not become parallel canonical truth stores.

Portability to governed external Delta/object storage remains valid where Unity Catalog realization is unavailable.