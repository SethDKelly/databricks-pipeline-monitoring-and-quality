# ARCH-146 — Acquisition Run Identity

**Status:** Accepted

Every collection attempt receives a durable acquisition-run identity bound to tenant, capability instance, source surface, plan revision, mode, requested scope/window and execution time.

Retries and resumptions remain distinguishable attempts linked to the same logical collection objective where applicable.
