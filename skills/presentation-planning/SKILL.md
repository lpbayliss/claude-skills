---
name: presentation-planning
description: Plans and writes the underlying content for high-quality presentations without defaulting to slide-file production. Use whenever the user needs a presentation, deck, talk, keynote, pitch, conference session, technical deep dive, architecture/design review, research presentation, executive briefing, training session, demo narrative, or wants an existing presentation made clearer or more persuasive. Produces audience strategy, central message, story architecture, evidence-backed talk/slide plan, speaker intent, transitions, timing, Q&A preparation, and a production brief. Also use before physically creating a PPTX or slides, unless the task is strictly mechanical formatting of already-approved content.
license: MIT
compatibility: Designed for Claude Code and compatible Agent Skills clients; source-grounded work may require file/search and current web research tools.
metadata:
  author: lpbayliss
  version: "0.1.0"
---

# Presentation Planning

Design the communication before designing slides. Produce a production-ready content plan that helps a specific audience understand, believe, decide, or act—not a generic deck outline.

The normal deliverable is the **underlying presentation content and production brief**, not a `.pptx`. If the user also requests a slide file, finish and validate the narrative first, then hand the approved brief to the relevant document-production workflow.

## Non-negotiables

- Start from the audience, occasion, decision, and desired change—not from a slide template.
- Give the presentation one governing idea or throughline. Supporting points must advance it.
- Use story as a reasoning structure, not decoration. Anecdotes and emotion serve the idea; they are not substitutes for evidence.
- Ground factual, numerical, technical, and historical claims in supplied evidence or reputable sources. Mark gaps instead of fabricating support.
- Prefer peer-reviewed, university, standards-body, government, professional-society, or primary-source evidence. Use practitioner presentation advice only when it does not conflict with stronger evidence.
- Preserve uncertainty, counter-evidence, trade-offs, and limitations. Narrative simplicity must not create technical falsehood.
- Plan what the speaker says separately from what the audience sees. Slides support attention and evidence; they are not the script.
- Cut material that does not change understanding, belief, decision, or action.
- Respect the allotted time. Leave room for transitions, pauses, demos, interaction, and questions.

## Choose mode and presentation type

Choose one primary work mode:

| Mode | Use when | Default result |
|---|---|---|
| **Create** | Starting from a topic, goal, notes, research, or source documents | New presentation brief and content plan |
| **Transform** | A report, paper, RFC, or rough outline must become a presentation | Audience-shaped narrative, not a compressed document |
| **Review** | The user wants critique of an outline, script, or deck | Prioritized findings and repaired structure where requested |
| **Adapt** | Existing content must work for a new audience, purpose, or duration | Revised message, depth, evidence, and beat plan |

Identify the presentation type because it changes the story logic:

- **Executive decision / proposal** — recommendation, stakes, evidence, trade-offs, risk, explicit ask.
- **Technical design / architecture review** — problem, constraints, system model, decision, alternatives, evidence, failure modes, rollout.
- **Research / conference talk** — motivating question, gap, claim, method only as needed, evidence, interpretation, limits, significance.
- **Keynote / thought-leadership talk** — compelling idea, tension, reframing, evidence, implications, memorable landing.
- **Pitch / advocacy** — audience problem, opportunity, credible mechanism, proof, objections, ask.
- **Training / teaching** — learner outcome, prior knowledge, conceptual sequence, examples, practice, checks for understanding.
- **Project update / demo** — outcome and decision first, evidence of progress, demo story, risks/blockers, next commitment.

Do not force these patterns when the occasion requires something else.

## Load only what the task needs

- Read [audience and story](references/audience-and-story.md) for Create, Adapt, persuasion, keynote, pitch, or mixed audiences.
- Read [technical presentations](references/technical-presentations.md) for engineering, scientific, architecture, design-review, research, data, or demo-heavy work.
- Read [production brief](references/production-brief.md) whenever producing a complete handoff for a speaker, designer, or slide-production agent.
- Read [review checklist](references/review-checklist.md) for Review mode and before finalizing any substantial presentation plan.

## Planning loop

Track multi-step work, but report the presentation rather than narrating the process:

- [ ] Frame the communication contract
- [ ] Inspect and classify source material
- [ ] Define the audience change and governing idea
- [ ] Build the story spine and evidence chain
- [ ] Allocate beats, timing, visuals, and spoken content
- [ ] Prepare opening, transitions, landing, Q&A, and rehearsal
- [ ] Review, cut, repair, and issue the production brief

### 1. Frame the communication contract

Capture or infer:

- occasion, format, venue, and delivery medium;
- time limit, Q&A allocation, interaction, and demo constraints;
- primary and secondary audiences;
- what they already know, believe, value, fear, and can decide;
- speaker credibility and relationship to the audience;
- desired audience change: what they should **understand, remember, believe, decide, feel, or do**;
- evidence available, evidence missing, and claims requiring verification;
- downstream deliverable: outline, script, slide-by-slide brief, speaker notes, or production handoff.

Ask only when a missing answer would materially change the governing idea, audience strategy, factual integrity, or call to action. Otherwise state a bounded assumption and proceed.

Do not treat “inform” as a sufficient objective. Name what the audience should be able to explain, evaluate, or do differently afterward.

### 2. Inspect and classify sources

Read all supplied notes, reports, papers, data, diagrams, prior decks, and local context before selecting the story. Separate:

- claims and conclusions;
- supporting and contradicting evidence;
- examples and human consequences;
- constraints and accepted decisions;
- uncertainty and open questions;
- material that belongs in the main story, backup, handout, or nowhere.

A presentation is linear and time-bound; do not preserve document order by default. Reorder material around audience comprehension and the desired decision.

For consequential claims that depend on current facts or external authorities, verify them when tools permit. Keep a compact source/evidence map so a designer or speaker can trace each claim.

### 3. Define the governing idea

Write these before outlining slides:

- **Audience change:** `From [current state] to [desired state].`
- **Governing idea:** one clear sentence the audience should remember and be able to repeat.
- **Presentation promise:** why listening will be worth their time.
- **Credibility basis:** why this speaker/evidence deserves attention.
- **Decision or action:** what should happen after the presentation, if applicable.

Test the governing idea:

- Is it specific enough to disagree with or act on?
- Can the evidence reasonably support it?
- Is it relevant to this audience now?
- Does every major section help establish it?

If the material supports several unrelated ideas, narrow the scope or define a hierarchy. For a complex briefing with multiple decisions, define one master idea and subordinate decision questions rather than flattening them into unrelated key messages.

### 4. Build the story spine

Choose a reasoning arc appropriate to the purpose. Useful starting structures include:

```text
Problem → complication → insight → evidence → resolution → implication
Current state → desired state → obstacle → path → proof → ask
Question → gap → claim → evidence → interpretation → significance
Decision → options → recommendation → rationale → risks → commitment
System need → constraints → design → trade-offs → validation → rollout
Learner need → model → example → practice → feedback → transfer
```

Use tension as the unresolved question, conflict, trade-off, or gap that makes the next beat necessary. Each beat should create or answer a question in the audience’s mind.

The structure may be conclusion-first for decision-makers or process-led for audiences who need to evaluate scientific reasoning. Read the audience reference rather than applying one universal reveal order.

Write the story first as:

1. a one-sentence governing idea;
2. a three-sentence version: problem, insight, implication;
3. a sequence of claim-level beats.

If those do not cohere, slides will not repair the presentation.

### 5. Design the opening and landing

The opening should quickly establish relevance, tension, and direction. Prefer a consequential situation, question, contrast, concrete example, or clear recommendation over biography, housekeeping, a string of statistics, or a generic agenda.

Reveal enough structure to orient the audience. A formal roadmap helps long or technical talks; a short persuasive talk often works better when the structure is felt rather than announced.

The landing should resolve the opening tension and make the governing idea memorable. End with implication, decision, commitment, or next action—not merely “Questions?” or a recap list. Transition into Q&A only after the landing has completed the talk.

### 6. Allocate beats and content

Plan by **beats**, not by an arbitrary slide count. A beat is one audience-facing claim, question, demonstration, comparison, or transition. It may use zero, one, or several slides.

For every beat, define:

- audience question being answered;
- takeaway assertion;
- speaker content and level of detail;
- evidence or example;
- visual purpose, if a visual genuinely helps;
- transition from the previous beat;
- timing and cut priority;
- source, caveat, or backup material.

Use assertion-style titles where slides are planned: a title should state the point, not merely name the topic. Prefer visual evidence, diagrams, demonstrations, and simplified data over bullet lists. Introduce how to read unfamiliar data before asking the audience to interpret it.

Apply cognitive-load discipline:

- one principal point at a time;
- remove extraneous content;
- signal where attention should go;
- keep related explanation and visual evidence together;
- do not duplicate full spoken narration as on-screen prose;
- segment complex builds and reveal them in a controlled sequence.

Do not convert every spoken sentence into a slide. Some beats need only the speaker.

### 7. Tailor depth and language

Adjust content to the audience’s prior knowledge and stakes:

- explain enough prerequisite context to enter the argument;
- translate specialist terms, symbols, diagrams, units, and scales that the audience cannot decode quickly;
- use analogies only when their mapping and limits are clear;
- connect numbers to a meaningful baseline, comparison, consequence, or decision;
- preserve the detail experts need to trust the argument, but move nonessential derivations and edge cases to backup;
- anticipate mixed audiences by establishing a shared model before branching into specialist evidence.

Never “simplify” by making a stronger causal, safety, performance, or certainty claim than the evidence supports.

### 8. Prepare delivery, questions, and production

Plan:

- exact intent of the opening and closing;
- transitions that explain why the next beat follows;
- demonstrations, failure contingencies, and fallback evidence;
- likely objections, skeptical questions, and short evidence-backed answers;
- backup material for questions that matter but do not belong in the main line;
- interaction or comprehension checks where appropriate;
- rehearsal passes for story, timing, language, visuals/demo, and hostile/friendly audience feedback.

Write scripts only when useful. Prefer full scripting for high-stakes short talks, precise openings/closings, sensitive claims, or timed narration. Prefer structured speaker notes for technical reviews and interactive sessions where verbatim delivery would be brittle.

### 9. Review and cut

Use the [review checklist](references/review-checklist.md). Repair the plan until:

- the title/assertion sequence alone tells a coherent story;
- every major claim has support or an explicit evidence gap;
- the audience can follow the prerequisites and transitions;
- content fits the real time budget with breathing room;
- technical nuance and counter-evidence are honest;
- the ask or landing is earned by the argument;
- the production team knows what the audience should see and what the speaker should say.

Cut from lowest decision value first: ornamental context, repeated claims, method detail that does not affect trust, secondary examples, and nice-to-know background. Preserve the logic and evidence that make the governing idea credible.

## Output rules

Scale the deliverable to the request. For a quick or early-stage task, use the minimum viable brief in [production brief](references/production-brief.md); do not emit every possible section merely because the template exists.

For a complete production handoff, default to this order unless the user requests another format:

1. Presentation strategy
2. Audience change and governing idea
3. Three-sentence story
4. Beat and timing plan
5. Evidence/source map
6. Opening and landing
7. Q&A and backup
8. Production and rehearsal notes
9. Assumptions and open gaps

- Lead with the presentation strategy and governing idea, not generic advice about public speaking.
- Produce a concrete story and content plan using the supplied subject matter.
- Separate **speaker content**, **visual intent**, and **evidence/source**.
- Give meaningful beat/slide titles that assert conclusions or pose purposeful questions; avoid repeated labels such as `Background`, `Solution`, `Results`, and `Conclusion`.
- Include timing by section or beat and identify safe cuts for shorter delivery.
- State assumptions and unresolved evidence explicitly.
- Do not physically produce slides unless separately requested.
- Do not pad with stock phrases, fake anecdotes, rhetorical questions the speaker would never say, or inspirational clichés.

## Gotchas

- A report is not a presentation script; a script is not slide copy; slides are not a handout.
- Storytelling does not require a personal anecdote, chronological reveal, hero’s journey, or emotional manipulation.
- “Tell them what you’ll tell them” can help long instruction but can flatten a short persuasive talk; orient proportionately.
- An executive audience usually wants recommendation and consequence early; a technical review still needs enough reasoning to trust it.
- Dense source material creates a selection problem, not permission for dense slides.
- A live demo needs a narrative purpose and a failure plan; feature tourism is not a story.
- Q&A preparation cannot compensate for a main argument that hides a known objection.
