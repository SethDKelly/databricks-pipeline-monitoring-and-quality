# ARCH-178 — Conditional-Request Optimization

**Status:** Accepted

When supported, ETag/Last-Modified or equivalent conditional requests reduce unnecessary polling while retaining request/checkpoint provenance.

A `304 Not Modified` is bounded to the exact representation/request semantics and is not a universal no-change claim.
