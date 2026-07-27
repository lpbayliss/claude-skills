# Presentation-planning evidence basis

This note records the reputable sources and design decisions behind the `presentation-planning` skill. It is maintainer evidence, not runtime context required for normal use.

## Source hierarchy

The skill prioritizes:

1. peer-reviewed or academic-press evidence about comprehension and multimedia learning;
2. university technical-communication guidance;
3. official professional-society guidance for technical talks;
4. government and standards-body communication/accessibility guidance;
5. established practitioner guidance where it is directly relevant and does not overrule stronger evidence.

The result is not a single branded storytelling formula. Presentation form depends on audience, purpose, evidence, duration, and decision context.

## Audience, purpose, and message

MIT Communication Lab guidance starts technical presentation planning by identifying the presenter's message, purpose, and audience. It notes that a talk seeking experimental feedback should allocate content differently from one communicating a result, and that engineers, scientists, investors, and clinicians attend to different implications. It also recommends outlining the full presentation before designing slides because spoken presentations are linear and cannot be browsed like papers.

Sources:

- [MIT Mechanical Engineering Communication Lab: Technical Presentation](https://mitcommlab.mit.edu/meche/commkit/technical-presentation/)
- [MIT EECS Communication Lab: Slide Presentation](https://mitcommlab.mit.edu/eecs/commkit/slideshow/)

The CDC Clear Communication Index is a research-based planning and assessment tool. It requires communicators to know audience characteristics, define the communication objective, and identify the main message before assessing language, visuals, numbers, and recommendations. The skill generalizes that audience/objective/main-message discipline beyond public health.

Sources:

- [CDC Clear Communication Index](https://www.cdc.gov/ccindex/index.html)
- [CDC Clear Communication Index User Guide](https://www.cdc.gov/ccindex/tool/index.html)

The U.S. plain-language guidance also treats writing for a specific audience as a prerequisite for clear communication.

Source:

- [Digital.gov plain-language audience guidance](https://www.plainlanguage.gov/guidelines/audience/)

## Story as a structure for reasoning

MIT's 2025 scientific-storytelling guidance describes problem, challenge, and resolution as a durable structure, while adapting focus for hypothesis testing, improving known outcomes, or developing systems. It emphasizes a three-sentence story, audience/format adaptation, supporting and counter-evidence, explicit limitations, and iterative feedback.

Source:

- [MIT Biological Engineering Communication Lab: Storytelling in Biological Engineering](https://mitcommlab.mit.edu/be/2025/01/30/storytelling-in-biological-engineering/)

The TEDx Speaker Guide is a reputable practitioner source for short idea-led talks. It distinguishes an idea from a story or fact list, requires evidence and fact-checking, suggests making the audience care before explaining the idea and evidence, and warns that story and emotion are tools rather than the primary objective. It also recommends cutting material based on prerequisite order and talk integrity.

Sources:

- [TEDx Speaker Guide](https://storage.ted.com/tedx/manuals/tedx_speaker_guide.pdf)
- [TED: Create and prepare slides](https://www.ted.com/participate/organize-a-local-tedx-event/tedx-organizer-guide/speakers-program/prepare-your-speaker/create-prepare-slides)

The skill therefore treats story as a sequence of relevance, tension, evidence, resolution, and implication. It explicitly rejects forced anecdotes, emotional manipulation, and a universal hero's-journey template.

## Technical claims and evidence

MIT recommends connecting each result to the broader motivating question, introducing data before showing it, simplifying presentation figures, and using one message per slide. Its scientific-storytelling guidance treats claims as reasoned arguments that need supporting evidence and honest treatment of counter-evidence and ambiguity.

IEEE's Author Center advises conference speakers to identify one key message, prioritize why the work matters and its main contribution, and accept that a 10–20 minute talk cannot explain a paper fully. The objective is to make the audience interested in the work rather than orally reproducing every detail.

Source:

- [IEEE Author Center: Present Your Paper](https://conferences.ieeeauthorcenter.ieee.org/become-an-ieee-conference-author/present-your-paper)

The technical reference in the skill applies these principles to architecture reviews, research talks, incidents, migrations, tutorials, data, diagrams, equations, code, demos, uncertainty, and Q&A.

## Assertion-evidence structure

The assertion-evidence approach replaces topic labels and bullet lists with a succinct assertion supported by visual evidence. A study of 110 engineering students compared assertion-evidence slides that integrated multimedia-learning principles with common PowerPoint-style slides. The assertion-evidence group showed better comprehension, fewer misconceptions, lower perceived cognitive load, and stronger delayed recall.

Sources:

- [Garner and Alley (2013), *How the Design of Presentation Slides Affects Audience Comprehension*](https://writing.engr.psu.edu/ae_comprehension.pdf)
- [Penn State publication record](https://pure.psu.edu/en/publications/how-the-design-of-presentation-slides-affects-audience-comprehens/)
- [Assertion-Evidence project](https://www.assertion-evidence.com/)

The skill uses assertion-style titles and claim/evidence planning, but does not require one slide for every assertion or claim that the approach is universally optimal for every presentation form.

## Cognitive load and multimedia learning

The Cambridge Handbook of Multimedia Learning summarizes experimental support for:

- **coherence** — remove extraneous material;
- **signaling** — cue the organization and essential content;
- **redundancy** — avoid combining graphics, narration, and duplicate on-screen prose;
- **spatial contiguity** — place corresponding words and visuals together;
- **temporal contiguity** — present corresponding narration and animation together.

Source:

- [Cambridge Handbook chapter on reducing extraneous processing](https://www.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/CD5B7AE1279A9AB81F8EEBB53DBEC86E)

The skill translates these findings into content-planning constraints: one principal point at a time, remove nonessential material, direct attention, coordinate explanation with visual evidence, avoid slide-as-transcript redundancy, and segment complex builds.

These principles come primarily from multimedia-learning contexts. The skill applies them proportionately rather than claiming every finding transfers unchanged to every meeting or live performance.

## Accessibility

W3C's Web Accessibility Initiative advises adapting presentation material to audience goals and knowledge, being transparent about expertise, and using accessible presentation guidance. The skill includes production-stage requirements for captions/transcripts, colour-independent encoding, legibility, verbal description of essential visuals, accessible interaction, and honest handling of unknown questions.

Source:

- [W3C WAI: Developing Accessibility Presentations and Training](https://www.w3.org/WAI/teach-advocate/accessibility-training)

Accessibility is included during planning because a story that depends on inaccessible evidence cannot be repaired solely through visual polish later.

## Skill-specific design decisions

- **Content before file production:** narrative, evidence, timing, and speaker/visual roles are settled before generating a deck artifact.
- **Audience change over generic intent:** `inform` is replaced with an observable understanding, belief, decision, action, skill, or memory outcome.
- **One governing idea:** supporting beats form a hierarchy rather than competing as unrelated key messages.
- **Beat planning:** one communicative beat may use no slide, one slide, or several; arbitrary slide-count rules are avoided.
- **Speaker/visual separation:** the production brief states what the audience sees, what the speaker says, and what a producer builds.
- **Truth boundary:** tailoring may change relevance, order, language, and depth but not accepted facts, uncertainty, or material risk.
- **Purpose-specific story patterns:** executive, technical, research, keynote, pitch, training, and demo presentations use different reveal orders.
- **Production-readiness verdict:** physical production should not begin when audience, governing idea, evidence, timing, or high-impact claims remain unresolved.
- **Review and rehearsal:** review checks the title/assertion sequence, evidence, timing, and audience fit before visual polish; rehearsal includes argument, audience, evidence, timing, delivery, Q&A, and technical setup passes.

## Evaluation scope

The checked-in evaluations cover:

- an executive/technical architecture decision;
- a research conference talk with bounded evidence;
- a sensitive all-hands change narrative;
- review and repair of a document-shaped technical deck;
- genuine adaptation for executive and engineering audiences;
- interactive technical training;
- a failure-prone live product demo;
- correction of an unsupported AI-productivity claim;
- a general-public heat-adaptation keynote with causal and anti-cliché traps;
- a data-heavy product review requiring denominator, cohort, and causal discipline.

Trigger negatives separate content strategy from mechanical PPTX production, visual theming, extraction, stage-fright coaching, asynchronous RFC writing, meeting summaries, social-video scripts, chart generation, and grammar-only proofreading.
