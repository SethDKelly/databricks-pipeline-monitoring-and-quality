# EXPL-072 — Gate + Safeguard Overlap Question

**Status:** Accepted — Phase 008 Group 04

## Requirement

Questions such as `was the pipeline blocked/protected?` must not merge Execution Gate and Propagation Safeguard.

Gate HOLD controls start/admission; Safeguard controls bounded propagation/publication/consumption surfaces. Gate ADMIT does not release Safeguard; Safeguard release does not ADMIT Gate; override of one does not automatically affect the other.

If both apply, report their separate propositions/enforcement intervals and independently evidenced effects.