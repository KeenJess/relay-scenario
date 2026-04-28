# Discovery Document: Smart Dependencies

**Author:** Test Student
**Date:** 2026-04-28

---

## Discovery Goals

1. Validate that cross-project dependency visibility is the right problem to solve (vs. better project templates, manual linking, etc.)
2. Understand how teams currently work around invisible dependencies
3. Identify technical feasibility constraints for auto-detection
4. Size the opportunity relative to other roadmap candidates

---

## User Research

### Interviews Conducted

| Who | Role | Key Insight |
|-----|------|-------------|
| Sarah K. | PM, Enterprise account (200+ users) | "I spend 3 hours every Monday manually checking if my team's work is blocked by other projects. I open 4 different project views and cross-reference timelines in a spreadsheet." |
| James T. | Engineering Lead, Mid-market | "Dependencies bite us mid-sprint. We plan assuming our work is independent, then discover on day 3 that another team's API change breaks our integration." |
| Priya M. | CSM | "Dependency issues come up in almost every QBR with multi-project accounts. They don't always say 'dependency' — they say 'we keep getting surprised by things we didn't know about.'" |

### Patterns Observed

- **Workarounds are manual and fragile.** Most teams use Slack channels, weekly sync meetings, or shared spreadsheets. None of these are connected to the project data.
- **The pain scales with project count.** Single-project teams rarely mention dependencies. At 3+ projects, it becomes a weekly frustration. At 5+, it's cited as the #1 coordination challenge.
- **Detection matters more than management.** Users don't need help managing known dependencies — they need help discovering the ones they don't know about.

---

## Technical Feasibility

### Data Available
- Task titles, descriptions, and comments (text similarity potential)
- Project timelines and date overlaps
- Historical "blocked" status transitions
- Team membership overlaps across projects

### Approach Options

| Approach | Complexity | Accuracy Potential | Timeline |
|----------|-----------|-------------------|----------|
| Keyword matching (titles/descriptions) | Low | Medium — high false positive rate | 4 weeks |
| NLP-based semantic similarity | Medium | Medium-high | 8 weeks |
| Graph-based (team overlaps + timeline proximity + text) | High | Highest | 12 weeks |

### Recommendation
Start with keyword matching + timeline overlap as v1. It's shippable in 4-6 weeks and gives us real user data to train the more sophisticated model later.

---

## Competitive Landscape

- **Competitor X:** Launched basic dependency view (manual linking only, no auto-detection). Early reviews are mixed — users appreciate the visibility but say manual linking is tedious.
- **Competitor Y:** No dependency features. Focused on reporting and analytics.
- **Opportunity:** Auto-detection is the differentiator. Nobody in our space is doing it well yet. First-mover advantage is real but time-limited — probably 6-9 months before someone else ships it.

---

## Open Questions

1. What's the acceptable false positive rate? (Need to test with users — hypothesis: under 15% is tolerable, over 25% causes feature abandonment)
2. Should we show detected dependencies as suggestions or as confirmed links?
3. How do we handle cross-project permissions? A PM on Project A might not have access to Project B's details.
