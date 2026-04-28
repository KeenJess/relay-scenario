# Initial Reactions: Smart Dependencies

The CEO wants us to build "Smart Dependencies" — an AI feature that auto-detects task relationships across projects. My first thoughts:

**What excites me:**
- This could genuinely solve the coordination pain I've heard from CS. Multi-project teams are drowning in invisible blockers.
- AI-powered detection means we're not asking PMs to manually link every dependency — that's the approach competitors are taking and it doesn't scale.

**What worries me:**
- "Smart" is dangerously vague. What does the CEO actually mean? Auto-detection? Suggestions? Full automation?
- False positives could be worse than no feature at all — if we flag dependencies that don't exist, PMs will stop trusting the system within a week.
- We don't have a data science team. Where's the ML expertise coming from?

**Questions I need answered before I can spec this:**
1. What's the actual business urgency? Is this about churn risk, competitive pressure, or a board commitment?
2. How much engineering capacity can we allocate? This feels like a 2-quarter effort minimum.
3. Do we have enough historical data to train a useful model, or are we starting from scratch?
