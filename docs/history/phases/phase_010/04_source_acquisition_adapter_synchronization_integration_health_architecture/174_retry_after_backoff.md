# ARCH-174 — Retry-After / Backoff Discipline

**Status:** Accepted

Adapters honor vendor retry-after/reset guidance and use bounded exponential backoff with jitter where appropriate.

Continuing aggressive requests through a known throttle is prohibited because it can worsen coverage and integration availability.
