# Layer 2 — Execution Planning

## docs/mvp_plan.md

**Purpose**: Turn scope into an ordered execution plan. Defines milestones, sequencing, and what "done" looks like at each stage.

**Template structure**:

1. MVP goal — the single question v1 must answer
2. Core features — broken down by capability
3. Explicit exclusions — temporary "not yet" items
4. Tech stack reference — directional, detailed decisions live in technical_design.md
5. Page structure sketch — rough layout of key screens
6. Acceptance criteria — the minimum checklist for MVP closure
7. Development sequence — ordered list of implementation steps
8. Blocking dependencies — what must come before what
9. Product risks

**Relationship to other docs**: Formal scope is in project_scope.md. If this document contradicts scope, this document is corrected. Technical details are in technical_design.md.

**Antipode example**:

- Core question: Can a user see their antipode and get a light experience with geographic facts and emotional expression — through a simple webpage?
- Dev sequence: (1) scaffold project, (2) coordinate input, (3) antipode calculation + tests, (4) map display, (5) reverse geocoding, (6) result UI, (7) template copy generation, (8) share card, (9) browser geolocation, (10) city search evaluation
- Blocking chain: calculation must pass tests before map is connected; map must be usable before geocoding is added
- Risk: adding too many features in v1 dilutes focus

