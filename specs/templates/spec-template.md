# Product Spec: [Feature Name]

**Author:** [Your name]
**Date:** [Date]
**Status:** [Draft | In Review | Approved | Shipped]
**Version:** [1.0]

---

## Problem Statement

[Write a clear, falsifiable statement of the problem this feature solves. Who experiences the problem? What evidence do you have that it's real? What happens if you don't solve it?]

<!-- EXAMPLE:
Project managers using Relay cannot see cross-project task dependencies until work is already blocked. In our Q3 customer survey, 67% of teams with 3+ active projects reported at least one missed deadline per quarter due to invisible dependencies. If we don't solve this, churn risk increases for our multi-project accounts, which represent 74% of ARR.
-->

---

## Context

[Describe the broader situation. Why now? What has changed in the market, in customer feedback, or in your product strategy that makes this the right problem to solve at this moment? Include links to supporting data, research, or prior discussions.]

<!-- EXAMPLE:
Three factors converge: (1) Our Q3 NPS dropped 8 points among teams managing 5+ projects, with "coordination overhead" as the #1 open-text theme. (2) Competitor X shipped a basic dependency view last month, generating significant social media discussion. (3) Our data science team shipped an internal proof-of-concept showing we can detect implicit task relationships with 83% precision using existing activity data.
-->

---

## Requirements

### Must Have

- [Requirement 1: Be specific and testable. A developer should be able to read this and know when it's done.]
- [Requirement 2]
- [Requirement 3]

### Should Have

- [Requirement 1: Important but not blocking for initial release.]
- [Requirement 2]

### Won't Have (This Release)

- [Explicitly call out what you're NOT building. This is as important as what you are building.]
- [Include things stakeholders might expect but that you've intentionally scoped out.]

---

## Constraints

[List the technical, business, timeline, legal, or resource constraints that shape the solution space. Be honest -- constraints aren't weaknesses, they're design inputs.]

- **Technical:** [e.g., Must work within existing task data model. Cannot require a database migration before Q2.]
- **Timeline:** [e.g., Must ship MVP in 6 weeks to align with Q1 board commitment.]
- **Business:** [e.g., Cannot change pricing for existing customers. Must work for both free and paid tiers.]
- **Legal/Compliance:** [e.g., AI-generated suggestions must be clearly labeled as automated.]

---

## Success Criteria

[Define how you'll know this worked. Each criterion should be measurable and have a target. Include both leading indicators (did people use it?) and lagging indicators (did it improve outcomes?).]

- [ ] [Metric 1: e.g., 40% of multi-project teams activate Smart Dependencies within 30 days of release]
- [ ] [Metric 2: e.g., Cross-project blocked tasks decrease by 25% within 60 days]
- [ ] [Metric 3: e.g., NPS for multi-project accounts improves by 5+ points in next quarterly survey]

---

## UX/Design Intent

[Describe the intended user experience at a high level. You're not designing the UI -- you're communicating the experience you want users to have. What should it feel like? Where does the user encounter this feature? What's the "aha" moment?]

[If you have wireframes, mockups, or design references, link them here.]

---

## Open Questions

[List unresolved questions that need answers before or during development. Assign an owner and target date for each.]

| # | Question | Owner | Target Date | Resolution |
|---|----------|-------|-------------|------------|
| 1 | [e.g., How do we handle dependencies between projects the user doesn't have access to?] | [Name] | [Date] | [Pending] |
| 2 | [e.g., What's the acceptable false positive rate for auto-detected dependencies?] | [Name] | [Date] | [Pending] |

---

## Appendix

[Include supporting materials: user research summaries, data analysis, competitive screenshots, technical architecture notes, or anything that supports the decisions in this spec without cluttering the main sections.]
