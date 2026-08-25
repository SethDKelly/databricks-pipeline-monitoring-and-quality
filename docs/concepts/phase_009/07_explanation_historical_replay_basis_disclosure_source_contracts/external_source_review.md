# External Source Review — Phase 009 Group 07

**Verified:** 2026-08-25

This review records current public source facts used by Group 07. It does not substitute for environment-specific discovery of enabled source history, external log retention, source permissions, communication channels, redaction policy or historical authorization records.

## Databricks system/history surfaces

- [System tables reference](https://docs.databricks.com/aws/en/admin/system-tables/) — many material account/system surfaces currently have a **365-day free retention period**, including `system.access.audit`, `system.query.history`, table/column lineage, job/run/task history and the new alert system tables. Other surfaces have different retention, including shorter, longer or indefinite horizons. System-table identity therefore does not imply one universal replay period.
- The same reference documents that system-table data is not real-time; updates occur throughout the day. A recently missing event can therefore be a lag condition rather than absence.
- [Jobs system table reference](https://docs.databricks.com/aws/en/admin/system-tables/jobs) — job/job-task/pipeline configuration tables use SCD2-style history and retain the latest record for an entity even when older intermediate history falls outside the 365-day window. Surviving latest state is not equivalent to complete older configuration history.
- [Query history system table](https://docs.databricks.com/aws/en/admin/system-tables/query-history) — `system.query.history` is currently Public Preview and captures covered SQL warehouse/serverless notebook/job statements account-wide within a region. By default only admins have access; Databricks recommends dynamic views when sharing subsets.
- Query history exposes `statement_id`, execution/actor context, `statement_text`, error detail, parameters, query source and other telemetry. Documentation states `statement_text` and `error_message` are empty when customer-managed keys are configured; long statement text can hit a character limit, and parameter structures expose an `is_truncated` indicator. Exact basis inspection therefore cannot assume complete query payloads.
- [Alert system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/alerts) — `system.alert.alerts` is an SCD2 configuration history and `system.alert.alert_evaluation_history` records one row per evaluation with evaluated state, result values, notification delivery status and error details. Both are currently Public Preview and the system-table reference lists a 365-day free retention period.
- Alert notification delivery status is useful evidence that the source attempted/completed a delivery according to its own semantics. The source does not, by that fact alone, prove the exact Explanation text rendered to the recipient, human reading or decision reliance.
- Databricks audit/query/lineage/alert/user information can contain sensitive actor identifiers, object names, SQL text, parameters and errors. Internal administrative visibility is not treated as requester disclosure authorization.

## GitHub history, comments and audit

- [Audit log for an enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/security-and-compliance/audit-log-for-an-enterprise) — GitHub Enterprise Cloud currently lists events affecting the enterprise for the last **180 days** and retains Git events for **seven days**.
- [Exporting audit log activity](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/exporting-audit-log-activity-for-your-enterprise) — audit/Git events can be exported for offline analysis; export size/time limits apply.
- [Streaming the audit log](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise) — enterprise audit streaming can retain events externally for longer periods. GitHub describes at-least-once delivery, so duplicate streamed records retain common derivation and are not independent corroboration.
- [REST API issue comments](https://docs.github.com/en/rest/issues/comments) — comment records expose stable IDs, current body, creator and created/updated timestamps and can be edited through the API. Current body therefore does not itself prove prior bodies.
- [Tracking changes in a comment](https://docs.github.com/en/communities/moderating-comments-and-conversations/tracking-changes-in-a-comment) — GitHub UI exposes edit history for issues/comments/review comments/commit comments. Authorized users can delete sensitive revision content. GitHub currently retains a maximum of **100 edits** per content item, preserving original content plus the most recent 99 edits while removing older intermediate edits beyond the limit.
- GitHub comments/issues/reviews can therefore be useful retained-communication sources, but they are mutable governed records rather than an automatically immutable Explanation archive.

## Collibra history and visibility

- [About history](https://productresources.collibra.com/docs/collibra/latest/Content/History/ref_history-pages.htm) — Collibra automatically keeps history for users/resources such as assets, domains and communities and records many create/edit/delete, characteristic, status, classification, comments/tags/ratings, workflow, responsibility and view-permission changes with actor/time context.
- The history documentation notes that some edits are represented as delete + create rather than a simple update and that changes to inherited responsibilities are not shown in resource history.
- [Release 2026.08](https://productresources.collibra.com/docs/collibra/latest/Content/ReleaseNotes/Archive/ref_release-202608.htm) — current releases allow administrators to disable history logging for selected attribute assignments by setting `History Enabled` to false. History remains enabled by default, but configured suppression means attribute history is not universal.
- [Permissions](https://productresources.collibra.com/docs/collibra/latest/Content/Settings/RolesAndPermissions/Permissions/co_permissions.htm) and [operating model](https://productresources.collibra.com/docs/collibra/latest/Content/to_operating-model.htm) — Collibra visibility/actions are permission-driven; without View permission a resource can be hidden from the user. Non-visible resource/history is therefore observer-relative rather than evidence of absence.

## Immuta audit, query context and retention

- [Databricks Spark Query Audit Logs](https://documentation.immuta.com/saas/governance/detect-your-data/audit/reference-guides/query-audit-logs/databricks) — for covered registered Immuta users/data sources, audit can include executed Spark/query context and policy information enforced during execution. Current documentation states these Databricks audit logs expire after **90 days** by default and recommends exporting UAM logs to S3 or ADLS Gen2 for long-term retention.
- [Databricks Unity Catalog Query Audit Logs](https://documentation.immuta.com/SaaS/governance/detect-your-data/audit/reference-guides/query-audit-logs/databricks-uc) — the Unity Catalog audit integration uses Databricks system query-history/lineage data and has different scope semantics, including configurable workspace ingestion and filtering of transformation-query patterns. Integration/version therefore matters to completeness.
- [Extracting Insights from Immuta Audit Logs](https://documentation.immuta.com/SaaS/knowledge-base/implementation/audit-and-monitor/extracting-insights-from-immuta-audit-logs) — current SaaS guidance again states 90-day default retention and recommends secure exports for long-term analysis. Policy, permission, tag, attribute and query events can support historical access/policy explanations when retained.
- Query/audit payloads may include query text, users, entitlements, policies, object names and security-profile context. These can be materially sensitive basis details; current availability to an Immuta auditor does not imply Explanation disclosure permission.

## Retained communication and delivery sources

- The evaluated vendor sources contain multiple **delivery/activity** records but no universal product-native store of the exact DMTZ Explanation content and authorized projection that was shown to each audience.
- Databricks alert notification status and dashboard snapshot/audit events can establish bounded delivery facts; GitHub comments/issues can store actual text but remain mutable; other email/Slack/Teams/ticket systems may retain exact messages depending on environment.
- Therefore any requirement to prove exact prior Explanation wording/detail/basis visibility remains environment-specific unless the architecture deliberately retains authentic Explanation snapshots or channel-native immutable history.

## Environment-specific unknowns retained

- which Databricks system tables are enabled and which historical rows are accessible to the monitoring service;
- whether system-table exports/materializations extend retention beyond vendor-native windows and retain availability timestamps;
- whether query text/parameters/error detail are available under the target encryption/security configuration;
- exact alert notification destinations and whether channel-native content is retained;
- GitHub plan/audit streaming configuration and repository/comment retention/moderation practices;
- Collibra history-enabled settings for every material governed attribute/facet and current/historical resource visibility;
- Immuta deployment/integration version, query-audit coverage and configured long-term UAM export;
- organization-owned Explanation snapshot/communication retention and immutable content identity;
- historical authorization/permission archives sufficient to reconstruct actor access at old knowledge cuts;
- present disclosure/minimization policy for raw query text, parameters, errors, actors, consumer identities, source existence/counts and provenance details;
- how long internal basis provenance must remain resolvable after the underlying vendor source expires;
- whether any external ticketing/email/chat/reporting system will be treated as an authoritative retained-communication surface.

These remain `unknown / not yet verified`, conditional or partial support rather than assumptions.
