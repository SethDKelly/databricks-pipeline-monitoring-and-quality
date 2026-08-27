# ARCH-107 — Authorization States and Conflict

**Status:** Accepted

The resolver preserves AUTH-025 states: allowed, denied, conditional, unknown, conflicting and unavailable.

Missing policy or membership evidence never matures into allow.

Runtime fail-safe behavior is operational handling and does not rewrite an unresolved authorization proposition into fabricated historical truth.