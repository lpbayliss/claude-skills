# Transform Existing Artifacts into Effective Specifications

Use this process for existing specifications, PRDs, RFCs, ADRs, tickets, plans, diagrams, screenshots, transcripts, or mixed source material.

## Preserve before improving

1. Keep the original artifact unchanged unless the user explicitly requests in-place editing.
2. Record each source by path, URL, title, date, revision, or other stable identifier.
3. Separate explicit source statements from your interpretation.
4. Correct factual claims when stronger evidence disproves them. Supersede an accepted requirement, constraint, policy, or decision only through its governing source or acceptance authority; current implementation behavior alone has no such authority.
5. Scope a supersession to the exact accepted claim being replaced. Preserve adjacent sequencing, timing, thresholds, and safety constraints unless the authority explicitly changes them. A later source stating a weaker minimum does not silently relax an earlier stronger constraint. Keep the timing of an activity separate from the timing of its passing result or approval: “perform before A” plus “pass before B” does not mean “pass before A.”
6. Surface contradictions rather than choosing an answer without authority.

## Build a conversion map

For consequential source statements, record:

| Source statement | Source | Classification | Evidence/confidence | Disposition |
|---|---|---|---|---|
| Quoted or faithfully summarized claim | path/page/section | fact, requirement, constraint, decision, assumption, risk, question, example | basis | preserve, rewrite, split, challenge, defer, remove |

Use the map to prevent accidental loss and to make rewrites auditable. A short map is enough for small artifacts; use an appendix for large conversions.

## Normalize without changing intent

- Rewrite solution-first requests as outcomes while retaining the proposed mechanism as an option.
- Split compound requirements that can fail independently.
- Convert vague adjectives into measurable placeholders and resolution methods.
- Distinguish examples from exhaustive behavior.
- Distinguish current-state evidence from desired future state.
- Turn implied exclusions into explicit non-goals only when the source supports them; otherwise mark them as proposed.
- Preserve fixed compatibility or policy obligations verbatim where wording is authoritative.
- Record accepted decisions in or link them to ADRs rather than burying them in prose.
- Mark every material obligation added during review as **derived/proposed**, record the risk or evidence that motivates it, and name the authority required to accept it. Do not present reviewer-added safeguards as already accepted source intent.

## Handle visual artifacts

For diagrams, screenshots, whiteboards, and mockups:

1. Extract visible labels, actors, components, stores, arrows, states, annotations, and boundaries.
2. Record spatial or visual interpretation separately from explicit text.
3. Treat unlabeled arrows, ambiguous direction, colour-only meaning, and missing legends as unresolved.
4. Do not infer protocol, cardinality, ownership, trust, ordering, or persistence unless shown or corroborated.
5. Create accessible prose describing the visual.
6. Ask for owner confirmation when different interpretations materially change behaviour or design.

## Reconcile multiple artifacts

Establish precedence from explicit governance first: accepted decisions, current contracts, approved product requirements, then drafts and notes. If precedence is not defined:

- report contradictions with source references;
- identify the decision owner;
- keep the output `Not ready` when the conflict affects mandatory behaviour;
- do not use recency alone as proof of authority.

## Correct weak existing specs

Look for:

- missing problem evidence or decision owner;
- unvalidated mechanisms presented as mandatory;
- requirements without actors, conditions, limits, or pass criteria;
- missing non-goals and boundary definitions;
- absent failure, cancellation, recovery, migration, or abuse scenarios;
- unsupported numeric targets;
- tests that do not map to requirements;
- implementation tasks that still require product invention;
- rollout without containment, telemetry, or rollback;
- contradictory or stale sections;
- no maintenance or supersession path.

## Transformation output

After the corrected artifact, include:

```markdown
## Source transformation summary
### Preserved
### Corrected or clarified
### Reclassified
### Removed or superseded
### Unresolved conflicts and owner decisions
```

For material changes, include the conversion map or a link to it. Explain why a change was made; do not merely say that text was "improved."
