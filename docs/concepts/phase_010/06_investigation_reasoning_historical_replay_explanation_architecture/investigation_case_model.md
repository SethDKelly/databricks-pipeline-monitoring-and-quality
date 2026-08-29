# Investigation and Case Persistence Model

## Canonical records

Group 06 persists Investigation state in the Group 02 canonical structured evidence plane rather than in a ticketing system or model conversation.

Recommended logical records:

- `investigation` — stable ID and owning tenant;
- `investigation_revision` — question/outcome, subject/population, event window, knowledge cut, purpose and scope;
- `investigation_lifecycle_event` — open/active/paused/closed/reopened/superseded/duplicate history;
- `investigation_lead` — bounded inquiry proposition, origin, generation method/revision and limitations;
- `investigation_lead_disposition` — active/deprioritized/excluded/merged/superseded with rationale and evidence;
- `investigation_evidence_link` — supporting/contradicting/limiting/contextual/searched-no-match role to canonical evidence;
- `investigation_annotation` — commentary/procedure with author/origin and time;
- `causal_claim` / `causal_claim_status_event` — exact causal proposition and non-rewriting status history.

## Lead generation

Leads may originate from analysts, deterministic rules, Lineage traversal, health/reconciliation boundaries, runtime contrasts, semantic search or models. Origin changes workflow provenance only.

There is no universal numeric hypothesis score. If a UI orders leads, ordering factors must be separately explainable and cannot be presented as causal probability.

## Exclusion

Lead exclusion is a strong bounded conclusion. The record should bind the exact exclusion proposition, searched scope, evidence/coverage mechanism and rule revision.

Missing support, restricted evidence, search-index failure or unavailable source state cannot become exclusion.

## Localization

Investigation can record first observed deviation, earliest evidenced state change, first localized reconciliation/transformation boundary and first downstream consumer effect independently. These positions may differ.

## Closure and reopen

Closure records an operational disposition; it does not transition linked Causal Claims by implication. Late evidence may reopen an Investigation and change current retrospective localization without rewriting earlier lifecycle events or the earlier knowledge cut.

## Integration with external case systems

Incident/ticket/case systems may be referenced by external ID and synchronized as optional workflow integrations. Their status is not canonical Investigation or Causal Claim truth unless an accepted source contract explicitly says so.