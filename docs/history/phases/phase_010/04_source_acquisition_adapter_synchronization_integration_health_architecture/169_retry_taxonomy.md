# ARCH-169 — Retry Taxonomy

**Status:** Accepted

Retry policy distinguishes transient transport/throttle/unavailability failures from deterministic authentication, authorization, request-shape and semantic errors.

There is no universal retry-everything policy; idempotency and source guidance govern retries.
