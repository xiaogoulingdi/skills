# Layer 1 — Product Definition

## docs/product_idea.md

**Purpose**: The raw idea dump. Not a spec, not a commitment. A place to capture where the project came from, what it might become, and what creative possibilities exist.

**Template structure**:

1. Product origin — where the idea came from
2. One-line description
3. Core positioning — the irreducible value proposition
4. Target users — who might care
5. Core user flow — the happy path
6. Core logic — the defining algorithm or mental model
7. Creative feature ideas — a list of "maybe later" features
8. UI style gut-check — what it should feel like
9. AI/copy principles — guardrails for generated content
10. Commercialization notes — optional, early thoughts

**Relationship to other docs**: For the official scope, see project_scope.md. For execution order, see mvp_plan.md. Ideas here only become commitments when promoted into scope or an issue.

**Antipode example**:

- Origin: the antipode concept — the point on Earth exactly opposite you
- Core positioning: antipode calculation + geographic explanation + restrained copy + shareable card
- Target users: map lovers, small-web-app appreciators, people who resonate with "the farthest place from me"
- Core flow: enter location → calculate antipode → show on map → explain where it is → generate emotional copy → shareable card
- Core logic: latitude negated, longitude ±180°, normalized to [-180, 180]
- Creative pool: day/night states, escape index, letters from the other side, two-person antipode relationships
- UI gut-check: quiet, clear, restrained, not dark-AI-template, light palette with sea blues and mist grays

## docs/project_scope.md

**Purpose**: The formal boundary. Answers "what does v1 do, what does it NOT do, and how do we know it's done".

**Template structure**:

1. Project goal — restated cleanly
2. MVP target — the question v1 must answer
3. Target users
4. In-scope capabilities — with acceptance criteria per capability
5. Out-of-scope — explicitly excluded, to prevent scope creep
6. Core user flow — the full v1 path
7. Experience principles
8. Success criteria — the checklist for "done"
9. Known risks

**Relationship to other docs**: For execution sequencing, see mvp_plan.md. For technical boundaries, see technical_design.md. This document is the primary gate for scope decisions.

**Antipode example**:

- In-scope: coordinate input, antipode calculation, map with two markers, basic reverse geocoding, template copy, HTML share card
- Out-of-scope: accounts, payments, mobile apps, 3D earth, complex AI, social sharing
- Success: user can complete the full flow in under 30 seconds on desktop and mobile
- Key risk: "if we only do coordinate math, the product feels too ordinary — the copy and card must carry the emotional weight"
