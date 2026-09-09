# INTG-007 — Subject Identity & Join Contract

Every capability identifies the source-local subject identifiers and the evidence required to reconcile them to accepted Entity Identity or another bounded product subject such as run, deployment, version, consumer, path, control instance or principal.

Join semantics preserve namespace, environment, workspace/account, version and validity interval when material.

Name equality, display-label equality and temporal proximity are not identity evidence by themselves.

If a required reconciliation key is unavailable or ambiguous, the integration result is partial/unknown for propositions that depend on that join rather than silently guessing identity.