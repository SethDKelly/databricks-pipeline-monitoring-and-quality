# EXPL-001 — Question Request Proposition & Identity

**Status:** Accepted — Phase 008 Group 01

## Requirement

Treat a business/operational question as a bounded request proposition attached to Explanation composition, not as an independent truth-owning concept.

A material question request should bind enough context to identify what answer is being requested, including as applicable:

- requester/principal and requested purpose/context;
- requested conclusion or information need;
- subject/entity target(s);
- environment/slice/version/run/consumer/population scope where material;
- event/effective-time target or window;
- recorded/knowledge-time perspective where historical reasoning matters;
- intended audience or projection context when already known;
- request/composition time and provenance.

## Identity discipline

Natural-language wording is not itself question identity. Two differently worded requests can ask the same bounded proposition, while identical wording can denote different questions under different subject/time/context bindings.

Question identity is therefore proposition/context based rather than string based.

Examples:

- `Is C healthy?` for production current-cycle completeness is not the same question as `Is C healthy?` for development schema compatibility.
- `Did report R use version V?` and `Was R exposed to V?` may overlap but are not automatically identical; exposure additionally depends on the applicable encounter proposition.

## Boundaries

- question request ≠ source truth;
- question request ≠ authorization;
- question request ≠ evidence collection permission;
- question wording ≠ truth-owner selection by itself;
- question identity ≠ UI conversation/thread identity.

A retained Explanation may preserve the initiating question/request identity, but retaining the request does not create a new canonical state owner.
