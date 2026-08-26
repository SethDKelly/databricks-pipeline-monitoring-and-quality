# ARCH-030 — Architecture Failure Semantics

**Status:** Accepted

Source/integration failure states such as authentication failure, permission denial, throttling, timeout, partial pagination, schema drift, parser failure, lag, retention expiry, or optional-source absence must remain distinguishable from domain-negative facts.

Later architecture must make these states observable enough to suppress or narrow unsupported conclusions.
