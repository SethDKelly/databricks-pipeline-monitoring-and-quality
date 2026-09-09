# ARCH-433 — Command Idempotency

**Status:** Accepted

Material mutating commands carry stable command/opportunity identities and idempotency semantics appropriate to the target adapter or canonical write path.

Retries create attempt provenance, not duplicate semantic decisions or communications.