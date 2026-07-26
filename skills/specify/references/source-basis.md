# Evidence Basis

This skill synthesises open, high-trust engineering guidance. Use these sources when the spec needs citations or deeper domain checks.

## Requirements rigor

- NASA Software Engineering Handbook — requirements should be clear, unambiguous, complete, consistent, individually verifiable, and traceable: https://swehb.nasa.gov/plugins/viewsource/viewpagesrc.action?pageId=32604503
- NASA NPR 7150.2D Chapter 4 — establish, approve, maintain, analyse, validate, architect, design, and test software requirements: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4
- INCOSE Guide to Writing Requirements V4 summary — characteristics and writing rules: https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf
- ISO/IEC/IEEE 29148 official scope — requirements-engineering processes and information items (full normative standard is not open): https://www.iso.org/standard/72089.html
- IETF RFC 2119 and RFC 8174 — MUST/SHOULD/MAY semantics: https://datatracker.ietf.org/doc/html/rfc2119 and https://datatracker.ietf.org/doc/html/rfc8174

## Writing and design docs

- Google Technical Writing — scope, non-scope, audience, summary-first organisation: https://developers.google.com/tech-writing/one/documents
- Software Engineering at Google, Documentation — focused purpose, audience, ownership, docs-as-code: https://abseil.io/resources/swe-book/html/ch10.html
- Malte Ubl, Design Docs at Google — goals/non-goals, trade-offs, alternatives, cross-cutting concerns, lifecycle (practitioner account, not official policy): https://www.industrialempathy.com/posts/design-docs-at-google/
- GitLab Architecture Design Workflow — iterative, version-controlled design with DRI and specialist review: https://handbook.gitlab.com/handbook/engineering/architecture/workflow/
- Rust RFC template — motivation, guide/reference explanation, drawbacks, alternatives, prior art, unresolved questions: https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md
- Kubernetes KEP template — test plan, graduation, rollback, monitoring, dependencies, scalability, and production readiness: https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md

## Architecture and decisions

- arc42 overview and quality scenarios: https://arc42.org/overview and https://docs.arc42.org/section-10/
- C4 model diagrams — context/container first; add detail only when valuable: https://c4model.com/diagrams
- Michael Nygard, ADRs — context, decision, status, consequences, immutable history: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Microsoft Azure, maintain an architecture decision record — problem, options, outcome, trade-offs, confidence, implications, append-only supersession: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- AWS Prescriptive Guidance, ADR process — owner, lifecycle, review, rejection rationale, and immutable accepted/rejected records: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

## Production and quality

- Google SRE Launch Coordination Checklist: https://sre.google/sre-book/launch-checklist/
- Google SRE Implementing SLOs: https://sre.google/workbook/implementing-slos/
- Google SRE Non-Abstract Large System Design — feasibility, resilience, concrete resource estimates, assumptions, and failure domains: https://sre.google/workbook/non-abstract-design/
- Google SRE Production Service Best Practices: https://sre.google/sre-book/service-best-practices/
- AWS Operational Readiness Reviews: https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html
- Microsoft Azure Well-Architected reliability checklist: https://learn.microsoft.com/en-us/azure/well-architected/reliability/checklist

## Security

- NIST Secure Software Development Framework / SP 800-218: https://csrc.nist.gov/projects/ssdf
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/

## Agentic development

- GitLab public Spec-Driven Development design — context gathering, agent plans, decision logs, downstream execution and validation: https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/spec_driven_development/

The workflow is intentionally self-contained; the sources above provide the public evidence basis for deeper review.
