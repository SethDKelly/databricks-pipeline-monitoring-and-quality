# INTG-015 — Retention, Historical Replay & Snapshot Capability

A contract records whether a surface is current-state only, exposes bounded history, exposes append/audit history, exposes reconstructible effective intervals, or relies on externally retained snapshots.

Retention horizon, deletion behavior and historical query semantics are proposition specific.

A current-state API cannot support an exact historical knowledge-cut reconstruction merely because the object has an old creation timestamp.

Historical source replay capability is also distinct from retained actual Explanation communication.