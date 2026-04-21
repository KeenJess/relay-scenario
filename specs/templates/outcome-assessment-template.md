# Outcome Assessment: [Feature Name]

**Author:** [Your name]
**Date:** [Date]
**Spec Version Assessed:** [Link to the spec and version number]
**Release Date:** [When the feature shipped]
**Assessment Date:** [When you're writing this -- ideally 30-60 days post-launch]

---

## Spec Fidelity Score

Rate how faithfully the shipped feature matched the original spec. This isn't about whether the spec was "right" -- it's about whether the spec was a reliable guide during development.

**Score: [1-5]**

| Score | Description |
|-------|-------------|
| 1 | **Spec was largely abandoned.** The team stopped referencing it early in development. The shipped feature bears little resemblance to what was written. |
| 2 | **Significant deviations.** Multiple Must Have requirements changed or were dropped. The spec described a different feature than what shipped. |
| 3 | **Moderate fidelity.** Core intent was preserved but several requirements changed during development. The spec was useful but required significant real-time negotiation. |
| 4 | **High fidelity.** Most requirements shipped as written. Changes were minor and well-documented. The spec served as a reliable guide. |
| 5 | **Near-perfect fidelity.** The shipped feature matches the spec closely. Changes were minimal and made through the spec's change process. |

**Rationale for score:** [Explain your rating. What stayed? What changed? Why?]

---

## What the Spec Got Right

[List the specific things your spec handled well. Be concrete -- not "the requirements were good" but "the requirement to show dependency confidence scores prevented three weeks of design debate."]

1. [e.g., The constraint about not requiring a database migration kept the project on track when the timeline compressed by 2 weeks.]
2. [e.g., The Won't Have section explicitly excluded cross-workspace dependencies, which prevented scope creep when the enterprise team asked for it mid-sprint.]
3. [e.g., The success criteria gave the team a clear target -- we could objectively say "this is working" at the 30-day check-in.]

---

## What to Write Differently

[List the specific things you'd change about the spec if you were writing it again. These are lessons for your next spec, not criticisms of your past self.]

1. [e.g., The UX/Design Intent section was too vague. I wrote "should feel lightweight" but didn't define what that meant in terms of interaction patterns. This caused 4 days of design iteration that a more specific intent statement could have prevented.]
2. [e.g., I missed a critical edge case: what happens when a detected dependency spans a project the user can't access. This became a 2-week detour. My discovery template's edge case section should have caught this.]
3. [e.g., The requirements used ambiguous language ("quickly," "easily") in two places. Next time, every requirement gets a concrete threshold.]

---

## Customer Outcome Assessment

[Evaluate whether the feature achieved its intended outcome for customers. Reference the success criteria from the original spec.]

| Success Criterion (from spec) | Target | Actual | Status |
|------------------------------|--------|--------|--------|
| [e.g., 40% of multi-project teams activate within 30 days] | [40%] | [e.g., 34%] | [Met / Partially Met / Not Met] |
| [e.g., Cross-project blocked tasks decrease by 25% within 60 days] | [25%] | [e.g., 18%] | [Status] |
| [e.g., NPS for multi-project accounts improves by 5+ points] | [+5] | [e.g., +3] | [Status] |

**Qualitative feedback:**
- [Summarize what customers are saying. Include both positive signals and concerns.]

**Overall customer outcome:** [Is the feature solving the problem you set out to solve? What's working and what isn't?]

---

## Lessons for Next Spec

[Distill the most important takeaways. These should be actionable changes to how you write specs, not generic reflections.]

### Process Lessons
- [e.g., I should share the draft spec with engineering 2 days before the formal review. The in-meeting feedback was less useful than the async comments I got when I tried this informally.]

### Content Lessons
- [e.g., My edge cases section needs a forcing function. Next time I'll use the "what if the user has 0? 1? 1,000? 1,000,000?" framework for every data-dependent feature.]

### Collaboration Lessons
- [e.g., The spec's Open Questions table worked well as a living document. But I should have assigned owners earlier -- 3 questions sat unresolved for 2 weeks because nobody felt responsible.]

---

## Follow-Up Actions

- [ ] [e.g., File spec amendment to address the permissions edge case for Phase 2]
- [ ] [e.g., Schedule 90-day check-in to re-evaluate success criteria that were "Partially Met"]
- [ ] [e.g., Share lessons learned with the broader product team at next product review]
- [ ] [e.g., Update spec template based on content lessons above]
