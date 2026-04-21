# Level 1 Capstone Rubric: The Complete Spec

Use this rubric to self-assess your completed Smart Dependencies spec. Score each criterion 1-5 and write a brief justification. Be honest -- a 3 with clear self-awareness is more valuable than an inflated 5.

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 1 | Significant gaps. This section needs substantial rework. |
| 2 | Below expectations. The intent is there but execution needs improvement. |
| 3 | Meets expectations. Solid work with room for refinement. |
| 4 | Exceeds expectations. Clear, thorough, and well-reasoned. |
| 5 | Exceptional. Could serve as an example for others to learn from. |

---

## Criteria

### 1. Problem Clarity

Does the spec articulate the problem clearly enough that someone who knows nothing about Smart Dependencies would understand the user's pain?

| Score | Description |
|-------|-------------|
| 1 | The problem statement is vague, uses solution language, or could describe many different problems. A reader wouldn't understand why this matters. |
| 3 | The problem is clearly stated and backed by evidence. The reader understands the user's pain and its business impact. Minor gaps in specificity or evidence quality. |
| 5 | The problem is sharp, falsifiable, and backed by multiple evidence types (quantitative and qualitative). The "What Happens If We Don't Solve It" section creates genuine urgency with specific numbers. A skeptical executive would be convinced. |

**Your score:** ___
**Justification:**

---

### 2. Requirements Precision

Are the requirements specific enough that an engineer could build and test each one without asking the PM for clarification?

| Score | Description |
|-------|-------------|
| 1 | Requirements are vague, use subjective language (quickly, easily, intuitive), or describe goals rather than behaviors. An engineer would need extensive conversation before starting. |
| 3 | Most requirements are testable and specific. A few use ambiguous language or combine multiple concerns into one requirement. An engineer could start work but would need 2-3 clarifying conversations. |
| 5 | Every requirement passes the Precision Test: specific, measurable, and independently testable. No vague qualifiers. Requirements with "and" have been split. An engineer could write test cases directly from the spec. |

**Your score:** ___
**Justification:**

---

### 3. Constraint Completeness

Does the spec honestly capture the technical, business, timeline, and legal constraints that shape the solution space?

| Score | Description |
|-------|-------------|
| 1 | Constraints are missing or generic ("we need to ship fast"). No connection between constraints and requirements. |
| 3 | Key constraints are identified (technical, timeline, business) and are specific enough to be actionable. Most constraints are reflected in the requirements. One or two constraints may be missing or vague. |
| 5 | Constraints are comprehensive, specific, and directly traceable to requirements decisions. The reader understands exactly why certain choices were made and what boundaries the team is working within. Includes constraints the team might wish weren't there. |

**Your score:** ___
**Justification:**

---

### 4. Success Criteria Testability

Could you look at data 30-60 days after launch and objectively determine whether each success criterion was met?

| Score | Description |
|-------|-------------|
| 1 | Success criteria are vague ("users like it," "adoption is good") or missing. No specific metrics or targets. |
| 3 | Success criteria include specific metrics and targets. Most are measurable with existing tools. Mix of leading and lagging indicators, though one or two may be hard to measure in practice. |
| 5 | Every success criterion has a specific metric, a quantitative target, a measurement method, and a timeline. Includes both adoption metrics (did people use it?) and outcome metrics (did it help?). Criteria are ambitious but realistic based on the evidence in the problem statement. |

**Your score:** ___
**Justification:**

---

### 5. Non-Goals Clarity

Does the Won't Have section explicitly exclude features that a reasonable stakeholder might expect, with clear rationale?

| Score | Description |
|-------|-------------|
| 1 | Won't Have section is missing or contains only obviously irrelevant items (e.g., "Won't Have: a mobile game"). Doesn't protect the team from scope creep. |
| 3 | Won't Have section lists 2-3 items that are genuinely tempting or that stakeholders have asked about. Rationale is present but could be stronger. |
| 5 | Won't Have section lists 3+ items that a reasonable person might expect to be included. Each has a clear rationale explaining why it's excluded *for this release* (not forever). The section reads as a deliberate scoping choice, not an afterthought. |

**Your score:** ___
**Justification:**

---

### 6. Overall Spec Coherence

Does the spec tell a coherent story from problem to solution to success? Do the sections reinforce each other, or do they feel disconnected?

| Score | Description |
|-------|-------------|
| 1 | Sections feel like they were written independently. The requirements don't clearly solve the problem. Success criteria don't map to requirements. Constraints aren't reflected in the approach. |
| 3 | The spec tells a mostly coherent story. The requirements address the problem, success criteria are relevant, and constraints are reflected. A few disconnects or gaps in the logic chain. |
| 5 | The spec reads as a single, coherent argument: here's the problem, here's the evidence, here are the constraints, here's what we'll build, here's how we'll know it worked. Every section reinforces the others. A new reader could follow the logic without any additional context. |

**Your score:** ___
**Justification:**

---

## Total Score: ___ / 30

| Range | Interpretation |
|-------|---------------|
| 25-30 | Strong spec. You could hand this to an engineering team with high confidence. |
| 19-24 | Solid spec. Ready for review with minor revisions expected. |
| 13-18 | Developing. The structure is there but significant sections need strengthening. |
| 6-12 | Early stage. Revisit the module exercises to strengthen weak areas before moving on. |

## Reflection

What's the one thing you'd improve about this spec if you had one more hour?

**Your answer:**
