# Level 1 Capstone Self-Assessment

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 1 | Significant gaps. This section needs substantial rework. |
| 2 | Below expectations. The intent is there but execution needs improvement. |
| 3 | Meets expectations. Solid work with room for refinement. |
| 4 | Exceeds expectations. Clear, thorough, and well-reasoned. |
| 5 | Exceptional. Could serve as an example for others to learn from. |

---

### 1. Problem Clarity

**Your score:** 4

**Justification:** The problem statement is specific, avoids solution language, and is backed by 5 distinct evidence sources. The "What Happens If We Don't Solve It" section includes concrete ARR numbers. I docked a point because my falsifiable hypothesis could be more precise about the leading indicator — "begins declining" is slightly vague.

---

### 2. Requirements Precision

**Your score:** 4

**Justification:** Most requirements are testable and specific. I used measurable thresholds (70% similarity, 30-second performance budget) rather than vague language. The "single click" interaction requirement is concrete. I think requirement #8 (learning from confirmations) could be more specific about what "improve accuracy" means in measurable terms.

---

### 3. Constraint Completeness

**Your score:** 3

**Justification:** I captured the key constraints (schema freeze, no ML team, performance budget, privacy). However, I could have been more specific about the privacy constraint — what exactly does "respect project-level permissions" mean in the dependency context? If Task A in Project 1 depends on Task B in Project 2, and the PM only has access to Project 1, what do they see? I flagged this as an open question in discovery but didn't fully resolve it in the spec.

---

### 4. Success Criteria Testability

**Your score:** 4

**Justification:** Every criterion has a specific metric, target number, measurement source, and timeline. I included both adoption (activation rate) and outcome (blocked task reduction) metrics. The NPS criterion is the weakest — a 5-point increase is specific but NPS surveys have significant variance and 90 days might not be enough signal.

---

### 5. Non-Goals Clarity

**Your score:** 5

**Justification:** The Won't Have section lists 4 items that stakeholders would reasonably expect (especially graph-based ML and cross-workspace). Each has a clear rationale explaining why it's excluded for v1 specifically, not dismissed permanently. The mobile exclusion is the kind of thing that would come up in a review and having it pre-addressed saves time.

---

### 6. Overall Spec Coherence

**Your score:** 4

**Justification:** The spec tells a clear story from problem → evidence → constraints → requirements → success criteria. The requirements map back to the problem statement evidence (e.g., the 40% activation target connects to the multi-project segment identified in the problem). The constraint about no ML team directly explains the Won't Have on graph-based detection. One gap: the discovery doc identified the permissions question as open, and the spec doesn't fully close it.

---

## Total Score: 24 / 30

## Reflection

If I had one more hour, I'd fully resolve the cross-project permissions question. The spec acknowledges it as a constraint but doesn't specify the exact behavior — should we show a generic "dependency detected in another project" message, or should we show the task title but not the details? This is the kind of ambiguity that would force an engineering conversation mid-sprint, which is exactly what a good spec should prevent.
