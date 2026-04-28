# Problem Statement: Smart Dependencies

**Author:** Test Student
**Date:** 2026-04-28

---

## The Problem

Project managers at companies running multiple concurrent projects frequently discover cross-project dependencies only after work is already blocked, causing cascading delays and rework. At Relay, this manifests as missed deadlines, frustrated teams, and growing churn risk among our most valuable customer segment.

---

## Who It Affects

- **Primary:** Project managers managing 3+ concurrent projects (~2,400 accounts, representing 74% of ARR)
- **Secondary:** Individual contributors whose tasks get blocked by invisible cross-project dependencies, leading to context-switching and wasted sprint capacity
- **Stakeholder:** Engineering leads who currently coordinate dependencies through ad-hoc Slack messages and manual status meetings

---

## Evidence It's a Problem

| Evidence Type | Source | Detail |
|---------------|--------|--------|
| Survey data | Q3 NPS survey, n=1,200 | 67% of multi-project teams report 1+ missed deadline per quarter from invisible dependencies |
| Support tickets | Zendesk, last 90 days | 34 tickets tagged "dependency" or "blocked by other project," up 40% QoQ |
| Usage data | Product analytics | Teams with 5+ projects have 2.3x higher rate of tasks marked "blocked" vs. single-project teams |
| Competitive signal | G2 reviews | Competitor X launched dependency detection in September; 12 Relay customers mentioned it in feedback |
| Feature requests | CS quarterly report | Dependency visibility is #3 most-requested feature |

---

## What Happens If We Don't Solve It

- **Customer impact:** Multi-project teams will continue to experience preventable delays. Our power users — the ones managing the most complex work — are the ones feeling the most pain. That's exactly the segment we can't afford to lose.
- **Business impact:** 14 enterprise accounts representing $2.4M in ARR show early churn signals, with "coordination overhead" cited as a top-3 reason in exit interviews. If we lose 30-40% of these in the next 2 renewal cycles, that's $720K-$960K at risk.
- **Competitive risk:** Competitor X's dependency feature is basic, but it ships the narrative that modern PM tools should handle this natively. Every month we wait, that narrative hardens and we shift from "leading" to "responding."

---

## Falsifiable Hypothesis

**We believe that** surfacing auto-detected cross-project dependencies in the project timeline view

**for** project managers managing 3+ concurrent projects

**will result in** a 25% reduction in cross-project blocked tasks within 60 days of launch

**We'll know we're right when** 40% of multi-project teams activate the feature within 30 days and the "blocked by other project" task rate begins declining within 2 weeks of activation.

---

## Next Step

- [ ] Schedule discovery session using discovery-template.md — target date: next Tuesday
- [ ] Share with Maya (Engineering Lead) for feasibility gut-check
- [ ] Present at next product review for prioritization decision
