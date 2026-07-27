# Technical Presentations

Use this reference for scientific, engineering, software, data, architecture, design-review, research, and demo-heavy presentations.

## Contents

- Technical communication contract
- Claim-evidence architecture
- Technical narrative patterns
- Managing depth and abstraction
- Data, diagrams, equations, and code
- Demos
- Uncertainty and intellectual honesty
- Technical Q&A and backup

## Technical communication contract

Technical audiences do not need every detail; they need the details that let them understand, trust, challenge, and act on the central claim.

Before planning, state:

- the technical question or decision;
- audience expertise and disciplinary mix;
- accepted prerequisites;
- system/research boundary;
- key claim and confidence level;
- evidence standard;
- decision, feedback, or follow-up sought;
- details that belong in a paper, RFC, appendix, repository, or backup rather than the main talk.

For conference talks, the objective is often to make the audience understand and care about the contribution enough to engage with the full work—not to reproduce the paper orally. For reviews, the objective is to make a decision with sufficient evidence, not to display how much work occurred.

## Claim-evidence architecture

Build the main line as claims supported by evidence:

| Claim | Why it matters | Evidence | Counter-evidence/limit | Audience implication |
|---|---|---|---|---|

A claim should be specific, contestable, and no stronger than its evidence. Useful evidence includes:

- measured results with uncertainty and baseline;
- mechanism or derivation;
- controlled comparison;
- architecture and failure analysis;
- operational or user evidence;
- reproducible demonstration;
- established external work with clear provenance.

Use assertion-style titles to expose the reasoning. The audience should be able to read the title sequence and recover the argument.

Do not hide negative or ambiguous results that materially affect the claim. Address credible alternatives and explain what evidence would distinguish them.

## Technical narrative patterns

### Architecture or design review

```text
Decision and scope
→ user/system need
→ constraints and invariants
→ current failure or gap
→ proposed system model
→ key flows and boundaries
→ alternatives and trade-offs
→ failure/recovery/security
→ validation evidence
→ rollout and decision requested
```

Lead with the recommendation when the reviewers are deciding. If the proposal is exploratory, lead with the unresolved decision and evidence needed.

### Research or scientific talk

```text
Motivating problem
→ what is unknown or inadequate
→ precise claim/hypothesis
→ approach at the level needed for validity
→ decisive evidence
→ interpretation and alternatives
→ limitations
→ significance and next question
```

Avoid the paper-shaped sequence of lengthy literature review, all methods, every result, then a rushed conclusion. Context and method earn only the time needed to interpret the claim.

### Engineering incident or learning review

```text
Impact and stakes
→ expected system behaviour
→ observed divergence
→ causal chain and contributing conditions
→ response and evidence
→ systemic changes
→ residual risk and verification
```

Avoid suspense about the cause. The audience needs an accurate model, not a mystery reveal. Keep blame out of the causal explanation.

### Technical proposal or migration

```text
Recommendation
→ why change/why now
→ fixed constraints
→ compatibility and risk boundaries
→ staged path
→ evidence and rollback/roll-forward
→ costs and alternatives
→ approval/gate
```

### Technical tutorial

```text
Task learners will perform
→ mental model and prerequisites
→ smallest working example
→ explanation of mechanism
→ common failure
→ guided practice
→ independent application
```

### Demo

```text
Claim the demo will prove
→ starting state
→ critical user/system path
→ visible result
→ meaning of result
→ boundary/failure behaviour
→ implication
```

## Managing depth and abstraction

A technical talk fails when it changes abstraction levels without orientation. Use a stable map:

1. Show the system or problem boundary.
2. Identify the component or relationship under discussion.
3. Zoom in for mechanism or evidence.
4. Return to the system-level implication.

Signal every zoom. Keep names and visual encoding consistent across levels.

Decide whether each detail is:

- **Required to understand** — main story.
- **Required to trust** — main story or concise evidence.
- **Required to implement** — include for implementation audiences; otherwise reference.
- **Required only to answer likely challenge** — backup.
- **Interesting but nonessential** — cut.

When expertise is mixed, define a shared model with plain language, then retain precise technical names so experts can map it to the real system. Do not replace accuracy with analogy.

## Data, diagrams, equations, and code

### Data

Before showing data, tell the audience:

- the question the data answers;
- population/sample and baseline;
- axes, unit, scale, and encoding;
- expected pattern or comparison;
- uncertainty and material exclusions.

Then reveal the evidence and state the interpretation. Simplify paper figures for presentation time: remove irrelevant series and labels, emphasize the decisive feature, and retain provenance. Never crop or re-scale in a way that changes the conclusion.

Contextualize numbers with a meaningful denominator, baseline, range, or consequence. Avoid decorative statistics.

### Diagrams

A diagram should answer one question. Define boundary, actors/components, relationships, data/control direction, ownership, trust or failure boundaries where relevant. Introduce complex diagrams in stages and preserve spatial consistency.

Do not use an architecture diagram as wallpaper while discussing unrelated claims.

### Equations

State what the equation helps decide or predict. Define variables before manipulation. Show only derivation steps necessary for trust or learning; use visual emphasis to connect terms to physical/system meaning.

### Code

Use code only when syntax or implementation shape is evidence. Keep snippets short, enlarge the relevant lines, remove incidental scaffolding, and explain behaviour before detail. For most audiences, a flow, interface, invariant, or before/after diff communicates better than a full source listing.

Do not live-code a critical path without a tested fallback.

## Demos

A demo needs a contract:

- claim being demonstrated;
- known starting state and data;
- exact critical path;
- visible success criterion;
- time budget;
- network/service/dependency assumptions;
- failure contingency: recording, screenshots, logs, or static walkthrough;
- transition back to the argument.

Rehearse the demo under presentation conditions. Avoid unbounded exploration, setup narration, and feature tourism. If a demo fails, explain what was supposed to happen and use the fallback without consuming the entire talk.

## Uncertainty and intellectual honesty

Distinguish:

- observed result;
- interpretation;
- causal claim;
- assumption;
- modelled or simulated result;
- projected benefit;
- accepted requirement;
- open question.

State material uncertainty where the claim appears, not only in a final limitations slide. Use precise language such as `consistent with`, `estimated`, `under these assumptions`, and `not yet measured` when appropriate.

Do not:

- imply causality from correlation;
- present a benchmark as production performance;
- generalize beyond the sample/population;
- hide failed cases or incompatible evidence;
- compare metrics with different definitions;
- present planned validation as a passing result;
- claim consensus from one source.

A clear limitation often increases credibility because it shows the audience where confidence should stop.

## Technical Q&A and backup

Prepare questions by category:

- premise and problem importance;
- method or design validity;
- alternatives and prior work;
- edge cases and failure modes;
- security, privacy, operations, and cost;
- scale and generalizability;
- implementation/rollout;
- contradictory evidence;
- ownership and next decision.

For each likely challenge, prepare:

```text
Short answer → evidence/reason → limit → follow-up or backup
```

Use backup material for detailed derivations, extended benchmarks, schemas, alternative architectures, methodology, threat models, rollout data, and source tables. Backup is not a dumping ground; title each item with the question it answers.

If the answer is unknown, say so and state what would establish it. Do not improvise certainty under pressure.
