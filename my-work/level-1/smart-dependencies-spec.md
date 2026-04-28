# Product Spec: Smart Dependencies v1.0

**Author:** Test Student
**Date:** 2026-04-28
**Status:** Approved
**Version:** 1.0

> **Summary:** Smart Dependencies automatically detects and surfaces cross-project task relationships for multi-project teams, reducing invisible blockers by giving PMs visibility into dependencies they didn't know existed.

---

## Problem

Project managers managing 3+ concurrent projects at Relay frequently discover cross-project dependencies only after work is blocked. This causes cascading delays, missed deadlines, and growing churn risk among our highest-value customer segment ($2.4M ARR at risk across 14 enterprise accounts).

---

## Requirements

### Must Have

1. The system shall scan task titles and descriptions across projects within the same workspace and flag potential dependencies when text similarity exceeds a configurable threshold (default: 70%).
2. The system shall detect timeline-based dependency candidates when tasks in different projects have overlapping date ranges AND share team member assignments.
3. Detected dependencies shall appear as a "Suggested Dependency" badge on the task card in both list and timeline views.
4. Users shall be able to confirm, dismiss, or snooze a suggested dependency with a single click.
5. Confirmed dependencies shall create a visible link between the two tasks, shown in both project timelines.
6. The system shall send a notification to affected task owners when a new dependency is detected on their task.
7. A "Dependencies Dashboard" shall show all detected, confirmed, and dismissed dependencies for a workspace, filterable by project and status.

### Should Have

8. The system shall learn from confirmed and dismissed suggestions to improve detection accuracy over time (per-workspace model tuning).
9. Users shall be able to manually create dependencies between any two tasks across projects, using the same UI as confirmed auto-detected ones.
10. The Dependencies Dashboard shall include a "risk score" for each dependency based on timeline proximity and task priority.

### Won't Have (This Release)

- **Full graph-based ML detection.** v1 uses keyword matching + timeline overlap. Graph-based analysis is a v2 investment pending v1 usage data.
- **Cross-workspace dependencies.** Scope is within a single workspace. Cross-workspace adds significant permission and data isolation complexity.
- **Automated dependency resolution.** We detect and surface, we don't auto-adjust timelines or reassign tasks. That's a different product decision.
- **Mobile support.** Dependencies Dashboard and suggestion interactions are desktop/web only for v1.

---

## Constraints

- **Schema freeze:** The platform team has a schema freeze starting March 15. Any new database tables must be approved by February 28.
- **No dedicated ML team:** Detection must work with rule-based approaches (keyword + timeline). We can't depend on a trained model for v1.
- **Performance budget:** Dependency scanning must complete within 30 seconds for workspaces with up to 10,000 active tasks. Scanning runs asynchronously — it must not block user interactions.
- **Privacy:** Dependency suggestions must respect existing project-level permissions. A user should never see dependency details for a project they don't have access to.

---

## Success Criteria

| Metric | Target | Measurement | Timeline |
|--------|--------|-------------|----------|
| Feature activation | 40% of multi-project teams (3+ projects) | Product analytics: "Smart Dependencies" toggle enabled | 30 days post-launch |
| Blocked task reduction | 25% decrease in "blocked by other project" tasks | Product analytics: blocked status transitions | 60 days post-launch |
| Suggestion acceptance rate | >50% of suggestions confirmed or snoozed (vs. dismissed) | Dependencies Dashboard analytics | 60 days post-launch |
| NPS improvement | 5-point increase among multi-project PMs | Targeted NPS survey to multi-project segment | 90 days post-launch |
| False positive rate | <20% of suggestions dismissed as irrelevant | Dismiss rate tracking | 30 days post-launch |

---

## Dependencies

- Design: Dependency badge component and Dashboard wireframes (due: 2 weeks before eng start)
- Platform: Schema approval for dependency tables (due: February 28)
- Notifications: Integration with existing notification system (parallel workstream)
