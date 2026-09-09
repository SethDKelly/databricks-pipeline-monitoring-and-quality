# INTG-062 — Bundle Deployment Attempt, Apply Outcome & Target Binding

**Status:** Accepted — Phase 009 Group 03

A bundle validation/deploy command or CI step may establish that an attempt was issued with a bounded target and source checkout. Command success establishes that bounded client/workflow result only.

Target activation requires target-side evidence that the intended resource/configuration became effective. If the process needs commit-level provenance, the deployment must explicitly retain and propagate an immutable revision/manifest; branch/origin metadata is insufficient.
