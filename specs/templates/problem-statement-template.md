# Problem Statement: [Feature or Initiative Name]

**Author:** [Your name]
**Date:** [Date]

---

## The Problem

[Describe the problem in plain language. Avoid solution language -- don't say "we need to build X." Instead, describe what's going wrong for the user or the business. One to three sentences.]

<!-- EXAMPLE:
Project managers at companies running multiple concurrent projects frequently discover cross-project dependencies only after work is already blocked, causing cascading delays and rework.
-->

---

## Who It Affects

[Identify the specific users or segments who experience this problem. Be precise -- "all users" is almost never accurate. Include the approximate size or revenue weight of this segment if you can.]

- **Primary:** [e.g., Project managers managing 3+ concurrent projects (~2,400 accounts, representing 74% of ARR)]
- **Secondary:** [e.g., Individual contributors whose tasks get blocked by invisible cross-project dependencies]
- **Stakeholder:** [e.g., Engineering leads who currently coordinate dependencies through ad-hoc Slack messages]

---

## Evidence It's a Problem

[List the concrete evidence you have. Include quantitative data, qualitative signals, or both. Be specific about sources and dates. If you're extrapolating, say so.]

| Evidence Type | Source | Detail |
|---------------|--------|--------|
| Survey data | [e.g., Q3 NPS survey, n=1,200] | [e.g., 67% of multi-project teams report 1+ missed deadline per quarter from invisible dependencies] |
| Support tickets | [e.g., Zendesk, last 90 days] | [e.g., 34 tickets tagged "dependency" or "blocked by other project," up 40% QoQ] |
| Churn interviews | [e.g., CS team exit interviews, Q2-Q3] | [e.g., 3 of 8 churned enterprise accounts cited "coordination overhead" as a top-3 reason] |
| Usage data | [e.g., Product analytics] | [e.g., Teams with 5+ projects have 2.3x higher rate of tasks marked "blocked" vs. single-project teams] |
| Competitive signal | [e.g., G2 reviews, social media] | [e.g., Competitor X launched dependency detection in September; 12 Relay customers mentioned it in feedback] |

---

## What Happens If We Don't Solve It

[Describe the cost of inaction. Think about customer impact, business impact, and competitive risk. Make it concrete -- "we might lose customers" is weak. "We risk $2.4M in ARR from multi-project accounts showing early churn signals" is strong.]

- **Customer impact:** [e.g., Multi-project teams will continue to experience preventable delays, eroding trust in Relay as their "source of truth" for project coordination.]
- **Business impact:** [e.g., The 14 enterprise accounts ($2.4M ARR) showing early churn signals cite coordination overhead. Without improvement, we estimate 30-40% churn risk in the next 2 renewal cycles.]
- **Competitive risk:** [e.g., Competitor X's dependency feature is basic but ships the narrative that "modern PM tools should handle this." If we wait 2+ quarters, we're responding instead of leading.]

---

## Falsifiable Hypothesis

[Write a clear, testable hypothesis that connects solving this problem to a measurable outcome. This is your "bet." If this hypothesis turns out to be wrong, you've still learned something valuable.]

**We believe that** [description of the solution direction -- keep it high-level]

**for** [target user segment]

**will result in** [measurable outcome with specific target]

**We'll know we're right when** [leading indicator you can measure within 30-60 days of launch]

<!-- EXAMPLE:
We believe that surfacing auto-detected cross-project dependencies in the project timeline view for project managers managing 3+ concurrent projects will result in a 25% reduction in cross-project blocked tasks within 60 days. We'll know we're right when 40% of multi-project teams activate the feature within 30 days and the "blocked by other project" task rate begins declining within 2 weeks of activation.
-->

---

## Next Step

[What happens with this problem statement? Does it feed into a discovery session? A spec? A prioritization discussion? Be explicit so this document has a clear "what now."]

- [ ] [e.g., Schedule discovery session using discovery-template.md -- target date: ____]
- [ ] [e.g., Share with engineering lead for feasibility gut-check]
- [ ] [e.g., Present at next product review for prioritization decision]
