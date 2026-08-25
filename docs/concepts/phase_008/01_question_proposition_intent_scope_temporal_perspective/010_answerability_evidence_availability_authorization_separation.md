# EXPL-010 — Answerability, Evidence Availability & Authorization Separation

**Status:** Accepted — Phase 008 Group 01

## Requirement

Keep the reasons a question cannot be fully answered separate instead of flattening them into one `unknown` or one confidence score.

Relevant axes include:

- semantic applicability — is the requested proposition meaningful for the bound subject/use?;
- source/evidence availability — is relevant evidence present?;
- evidence sufficiency/coverage — is available evidence sufficient for the requested conclusion?;
- conflict — do applicable sources/results disagree?;
- current integration/source support — can the framework currently observe the required category?;
- authorization/disclosure — may this requester receive the conclusion/basis?;
- question ambiguity — is the proposition itself sufficiently bounded?;
- temporal reconstructability — can the requested historical cut be reconstructed?

## Principle

Answerability is conclusion-relative and may be partial. Do not create a universal answerability percentage or confidence score.

Examples:

- a cause can be unresolved while health and exposure are answerable;
- a conclusion can be internally well-supported but unavailable to the requester because disclosure is denied;
- raw evidence can be restricted while an authorized coarse Assessment is answerable;
- a source category can be unsupported by current integrations without implying the real-world condition is false.

## Boundary

Question intent does not grant evidence access, and authorization cannot manufacture evidence sufficiency.
