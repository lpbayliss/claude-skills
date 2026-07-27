# Audience and Story

Use this reference to choose the message, reveal order, language, and emotional/analytical shape for a specific audience.

## Contents

- Audience model
- Audience change
- Governing idea and promise
- Story as reasoning
- Common narrative patterns
- Openings and landings
- Mixed and resistant audiences
- Adaptation matrix

## Audience model

Build an audience model from evidence, not stereotypes:

| Dimension | Questions |
|---|---|
| Role and authority | Who can decide, fund, approve, implement, challenge, or block? |
| Prior knowledge | What concepts, history, data forms, symbols, and jargon can they decode quickly? |
| Stakes | What outcome, risk, cost, identity, or obligation matters to them? |
| Current belief | What do they already believe about the problem and proposed change? |
| Resistance | What legitimate objections, competing priorities, or trust gaps exist? |
| Evidence standard | What would count as credible: data, precedent, mechanism, expert review, demo, customer evidence? |
| Context | Why are they here, what happened immediately before, and what happens after? |
| Attention | How much time and cognitive bandwidth will they realistically give? |
| Accessibility | What language, sensory, cultural, or participation barriers must the plan account for? |

Separate the primary audience from secondary audiences. Optimize the main story for the people whose understanding or action determines success; provide bridges and backup for others.

Avoid demographic caricatures. Tailoring means changing relevance, prerequisites, evidence, and action—not changing truth.

## Audience change

Define the before/after state:

```text
From: [what the audience currently understands, believes, feels, or does]
To:   [what they should understand, believe, decide, or do]
Because: [the governing evidence or insight]
```

A useful objective is observable. Replace `inform them about the migration` with `enable the architecture board to decide whether the staged migration controls operational risk well enough to approve phase one`.

Distinguish:

- **Understanding** — can explain the model, mechanism, or implication.
- **Belief** — accepts a claim as credible.
- **Decision** — chooses among options or approves a scope.
- **Action** — commits to a next step.
- **Skill** — can perform or transfer a procedure.
- **Memory** — can recall the central idea later.

A presentation can pursue more than one, but one should govern.

## Governing idea and promise

The governing idea is the shortest defensible statement that unifies the presentation. It should contain a meaningful claim, not a topic.

Weak:

- `Our platform migration`
- `Three findings from the research`
- `An overview of observability`

Stronger:

- `A compatibility-first migration removes the scaling bottleneck without forcing a high-risk cutover.`
- `The apparent accuracy gain disappears under real production drift, so deployment should wait for targeted data collection.`
- `Teams can reduce incident diagnosis time by standardising context propagation before buying another observability tool.`

The presentation promise translates the idea into audience value: `By the end, you will be able to judge whether phase one is reversible and what evidence should gate phase two.`

## Story as reasoning

A story is a controlled sequence of change and causality:

1. Establish a relevant state.
2. Introduce a gap, question, conflict, trade-off, or opportunity.
3. Develop attempts, evidence, or alternatives.
4. Resolve or reframe the tension.
5. Show the consequence for this audience.

This does not require characters or drama. In technical work, the protagonist may be a user journey, system, hypothesis, operational constraint, or decision.

Use emotion ethically. Concern, surprise, relief, ambition, and curiosity can arise from real stakes; do not manufacture fear, certainty, or sentiment that the evidence does not support.

A narrative improves selection: evidence belongs when it changes the audience’s model of the tension or resolution.

## Common narrative patterns

### Executive decision

```text
Recommendation → why now → evidence → alternatives/trade-offs → risk controls → decision/commitment
```

Lead with the conclusion because senior decision-makers need to know what they are evaluating. Keep implementation detail subordinate to consequences and confidence.

### Proposal or change story

```text
Current reality → cost/tension → achievable future → barrier → proposed path → proof → ask
```

Contrast clarifies why change is needed. Do not exaggerate the current failure or future benefit.

### Explanatory or educational talk

```text
Important question → intuitive model → worked example → complication → refined model → transfer/application
```

Sequence prerequisites before dependent ideas and include retrieval, prediction, or application checks.

### Research story

```text
Motivating problem → knowledge gap → claim/hypothesis → evidence → interpretation → limitation → significance
```

The paper’s section order is not mandatory. Methods receive only the time needed to trust and interpret the result.

### Technical design review

```text
User/system need → constraints → failure of status quo → proposed design → alternatives/trade-offs → validation → rollout decision
```

Orient the audience in the system before changing abstraction levels.

### Demonstration

```text
User goal → current friction → promised capability → critical path demo → evidence of outcome → limits/failure recovery → next action
```

A demo proves a claim; it is not a tour of every feature.

### Status/update

```text
Outcome sought → what changed → evidence → variance/risk → decision or help needed → next commitment
```

Do not narrate work chronologically unless chronology explains cause.

## Openings and landings

### Opening functions

A strong opening should perform most of these quickly:

- create relevance;
- establish the question or tension;
- earn attention;
- indicate the governing direction;
- calibrate credibility and scope.

Useful forms:

- a concrete consequential situation;
- a surprising but verified contrast;
- a question the audience genuinely needs answered;
- a concise recommendation;
- a relatable example that maps directly to the idea;
- a demonstration of the problem.

Avoid defaulting to speaker biography, throat-clearing, a generic agenda, a dictionary definition, a forced joke, or a barrage of uncontextualized statistics.

### Landing functions

The landing should:

- resolve the opening tension;
- restate the governing idea with earned force;
- translate evidence into implication;
- make the decision, action, or changed model explicit;
- end on language the speaker can deliver naturally.

Do not end the actual presentation with `Any questions?`. Land the idea, pause, then invite discussion.

## Mixed and resistant audiences

For mixed expertise:

1. Begin with a shared problem and common vocabulary.
2. introduce a simple system/model that remains true at deeper levels.
3. Add technical detail only when it answers a trust or decision question.
4. Use layered visuals and backup material rather than parallel monologues for each group.
5. State what specialists should inspect later.

For resistance:

- articulate the strongest legitimate objection fairly;
- distinguish values conflict from factual disagreement;
- show what evidence could change the recommendation;
- preserve agency where the audience owns the decision;
- avoid labelling scepticism as ignorance;
- do not bury cost, migration, security, or operational consequences.

## Adaptation matrix

When adapting the same subject, change these deliberately:

| Audience | Lead with | Depth | Evidence | Ask |
|---|---|---|---|---|
| Executives | decision, consequence, risk | system-level | outcomes, scenarios, confidence | approve/prioritize/resource |
| Engineers | constraints, mechanism, trade-offs | implementation-relevant | architecture, data, failure modes | review/choose/implement |
| Researchers | question, gap, claim | method needed for validity | data, uncertainty, alternatives | assess/challenge/extend |
| Customers/users | problem and changed experience | conceptual | examples, outcomes, trust | adopt/try/feedback |
| General public | relevance and intuitive model | minimum viable concepts | concrete evidence and scale | understand/support/act |
| Learners | outcome and prerequisite model | staged | examples, practice, feedback | demonstrate/transfer |

This matrix is a starting point. The real audience model overrides it.
