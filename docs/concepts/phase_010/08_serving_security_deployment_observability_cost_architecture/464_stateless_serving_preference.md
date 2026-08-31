# ARCH-464 — Stateless Serving Preference

**Status:** Accepted

Serving/control API replicas are stateless with respect to canonical domain truth where practical, using durable canonical journals and explicit derived stores for stateful needs.

This supports scaling/failover without making instance-local memory historical truth.