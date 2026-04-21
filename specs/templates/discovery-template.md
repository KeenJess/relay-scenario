# Discovery Session: [Feature or Initiative Name]

**Author:** [Your name]
**Date:** [Date]
**Participants:** [List people involved in this discovery]
**Related Problem Statement:** [Link to problem statement if one exists]

---

## Feature Context

[Provide a brief summary of what you're exploring and why. This should orient someone who wasn't in the problem statement discussion. Two to four sentences.]

<!-- EXAMPLE:
We're exploring how to surface cross-project task dependencies automatically within Relay. Our CEO flagged this as a strategic priority, and our problem statement confirms the pain: 67% of multi-project teams report missed deadlines from invisible dependencies. This discovery session aims to validate our assumptions, understand the user's current workflow, and identify constraints before we write the spec.
-->

---

## Assumptions to Validate

[List your team's assumptions about the problem and potential solution. Be honest about what you think you know vs. what you've proven. Mark each as Validated, Invalidated, or Needs More Data by the end of discovery.]

| # | Assumption | Confidence (Pre-Discovery) | Status (Post-Discovery) | Evidence |
|---|-----------|---------------------------|------------------------|----------|
| 1 | [e.g., PMs want dependencies detected automatically rather than entering them manually] | [High / Medium / Low] | [Validated / Invalidated / Needs Data] | [Fill after discovery] |
| 2 | [e.g., Cross-project dependencies are the primary source of blocked work, not within-project dependencies] | [High / Medium / Low] | [Status] | [Evidence] |
| 3 | [e.g., Users trust AI-generated dependency suggestions enough to act on them] | [High / Medium / Low] | [Status] | [Evidence] |
| 4 | [e.g., Existing task data contains enough signal to detect dependencies without requiring new user input] | [High / Medium / Low] | [Status] | [Evidence] |

---

## User Jobs

[Describe what users are trying to accomplish (not what they want the software to do). Use the Jobs-to-be-Done format: "When [situation], I want to [motivation], so I can [expected outcome]."]

| # | Job Statement | Frequency | Current Solution | Pain Level (1-5) |
|---|--------------|-----------|-----------------|-------------------|
| 1 | [e.g., When I'm planning next sprint's work, I want to see which tasks depend on other teams' deliverables, so I can sequence work correctly and avoid blocks.] | [Daily / Weekly / etc.] | [e.g., Manually asking in Slack, scanning other projects' boards] | [1-5] |
| 2 | [e.g., When a task gets blocked, I want to quickly understand the full chain of what's waiting on what, so I can escalate to the right person.] | [Frequency] | [Current workaround] | [Pain] |
| 3 | [e.g., When I'm reporting project status to leadership, I want to show dependency-related risks proactively, so I'm not surprised by delays in the review meeting.] | [Frequency] | [Current workaround] | [Pain] |

---

## Edge Cases

[Think about the scenarios that will break your feature or complicate the design. These are the cases your spec needs to address explicitly.]

| # | Edge Case | Likelihood | Impact | Notes |
|---|-----------|-----------|--------|-------|
| 1 | [e.g., User doesn't have access to the project that contains the dependency] | [High / Medium / Low] | [High / Medium / Low] | [e.g., Permissions model -- do we show the dependency exists without revealing task details?] |
| 2 | [e.g., Circular dependencies (A depends on B depends on A)] | [Likelihood] | [Impact] | [Notes] |
| 3 | [e.g., Stale dependencies -- the relationship was valid last month but the upstream task shipped] | [Likelihood] | [Impact] | [Notes] |
| 4 | [e.g., AI detects a false dependency that causes a team to delay work unnecessarily] | [Likelihood] | [Impact] | [Notes] |

---

## Technical Constraints

[Capture what engineering and data science have told you (or what you need to ask them). This shapes the solution space.]

- **Data availability:** [e.g., What signals exist in our current data model? Task titles, descriptions, assignees, project membership, activity logs?]
- **Model readiness:** [e.g., Data science has a proof-of-concept at 83% precision. What's the path to production? What's the latency?]
- **Infrastructure:** [e.g., Can we run inference in real-time, or does this need to be a batch job? Any cost implications?]
- **Integration points:** [e.g., Does this need to work with our existing notification system? Calendar sync? Slack integration?]
- **Scale:** [e.g., Largest customer has 12,000 tasks across 40 projects. Can the detection model handle that volume?]

---

## Competitive Landscape

[What are others doing in this space? Not to copy them, but to understand user expectations and identify opportunities to differentiate.]

| Competitor | What They Offer | Strengths | Gaps |
|-----------|----------------|-----------|------|
| [e.g., Competitor X] | [e.g., Manual dependency linking with a visual timeline] | [e.g., Clean UI, fast adoption] | [e.g., No auto-detection, only works within a single project] |
| [e.g., Competitor Y] | [e.g., AI-suggested links, beta] | [e.g., First mover on AI angle] | [e.g., High false positive rate based on user reviews, no cross-project support] |
| [e.g., Internal workaround] | [e.g., Slack channels + spreadsheets for cross-team coordination] | [e.g., Familiar, flexible] | [e.g., Doesn't scale, information gets lost, no audit trail] |

---

## Open Questions

[Capture everything you still don't know. These feed directly into the spec's Open Questions section or become follow-up research tasks.]

| # | Question | Who Can Answer | Priority | Status |
|---|----------|---------------|----------|--------|
| 1 | [e.g., What false positive rate is acceptable to users before they stop trusting the feature?] | [e.g., UX research] | [High / Medium / Low] | [Open / Answered] |
| 2 | [e.g., Do enterprise customers need admin controls to enable/disable AI detection per project?] | [e.g., Enterprise CS team] | [Priority] | [Status] |
| 3 | [e.g., How do competitors handle the permissions problem for cross-project dependencies?] | [e.g., Competitive research] | [Priority] | [Status] |

---

## Discovery Summary

[Fill this in after the session. What did you learn? What changed? What's the recommended next step?]

**Key findings:**
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

**Assumptions that changed:**
- [Which assumptions were validated or invalidated, and what does that mean for the approach?]

**Recommended next step:**
- [ ] [e.g., Proceed to spec writing using spec-template.md]
- [ ] [e.g., Run follow-up discovery on [specific open question]]
- [ ] [e.g., Pause -- the problem isn't validated enough to invest in a spec]
