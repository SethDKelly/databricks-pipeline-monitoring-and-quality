# Explanation Statement and Basis Architecture

## Statement IR

Every material answer statement is represented before prose as Statement IR with:

- statement/proposition identity;
- subject/population/scope;
- event/effective and knowledge perspective;
- source-owned result/status vocabulary;
- direct-projection or explicit derivation-rule identity;
- supporting/contradicting/limiting/contextual basis IDs;
- material limitations;
- disclosure requirements;
- presentation materiality metadata.

## Answer IR

Answer IR is a deterministic composition of Statement IR records plus sibling/subquestion relationships, unresolved areas, ordering and authorized projection instructions.

It is not a global truth object and has no global confidence/completeness score.

## Direct versus derived

A direct statement projects an accepted source-owned proposition. A cross-concept derived statement requires an explicit versioned derivation rule and exact input proposition IDs.

Two facts placed next to each other in prose do not create a third fact.

## Basis roles

Basis roles are statement-relative. One evidence item may support one statement and limit or contradict another.

Common-derived evidence remains marked so cardinality cannot masquerade as corroboration.

## Limitations

Material coverage, source-health, historical, authorization or evidence-sufficiency limitations travel with Statement IR and constrain headline, summary and detail renderings.

## Partial answers

Sibling statements are independently answerable. One unresolved subquestion does not suppress supported siblings, and one answered sibling does not fill an unresolved one.

## Rendering

Template, API, UI and model-assisted rendering consume the same Statement/Answer IR. Renderers may vary language/detail but cannot alter status, polarity, scope, basis or material limitations.

A render validator checks factual clauses against Statement IR and rejects unsupported additions or strengthening.