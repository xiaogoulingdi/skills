# Layer 3 — Design & Experience

## docs/design_direction.md

**Purpose**: Define the visual identity and design constraints. This is not a pixel-level spec — it's a "character anchor" for the project's aesthetic.

**Template structure**:

1. Design goal — what the interface should make users feel
2. Target user aesthetic profile — what kind of visual language they respond to
3. Overall visual character — keywords and vibe guardrails
4. Color direction — palette roles, ratios, what NOT to use
5. Typography — text character, not font names
6. Layout principles — alignment, white space, hierarchy
7. Component & radius rules
8. Icon & decoration principles — what is allowed, what is banned
9. Map visual direction — how map fits into the aesthetic
10. Motion direction — what animation serves, what it must not do
11. Share card direction — the card's visual brief
12. Anti-AI-template constraints — common cheap patterns to avoid
13. Accessibility & responsive principles
14. Design acceptance criteria — before a UI can enter implementation

**Relationship to other docs**: For user-facing flow, see ui_flow.md. For copy tone, see copywriting.md.

**Antipode design keywords**: clean, fresh, quiet, restrained, geographic, philosophical, slightly artistic, shareable but not loud.

**Antipode palette roles**: paper white (background), mist gray (layers), sea blue (map/links), deep blue (headings), dawn gold (emphasis points).

**Antipode anti-patterns**: no dark gradients, no emoji, no rocket/wand icons, no card-stacking, no marketing hero.

## docs/ui_flow.md

**Purpose**: Define the user's interaction path. What screens or states exist, how the user moves between them, and what each state shows.

**Template structure**:

1. Document goal — what this flow doc covers
2. UI flow principles — guiding rules for this version
3. State overview — a finite set of states, not pages
4. First-screen experience — what user sees immediately
5. Input flow — how user provides data
6. Loading states — what happens during computation
7. Result flow — what user sees after computation
8. Share card flow — optional, how card appears
9. Error states — every failure case with copy
10. Mobile flow — responsive ordering
11. Acceptance criteria — flow-level checklist
12. Future enhancements — deferred improvements

**Relationship to other docs**: For visual treatment, see design_direction.md. For copy strings, see copywriting.md.

**Antipode example states**: Initial → Input Ready → Calculating → Result → Share Preview, with Error states from every node.

## docs/copywriting.md

**Purpose**: Define the tone, principles, and candidate copy strings. Ensures all copy across the project shares a consistent voice.

**Template structure**:

1. Copy principles — the irreducible rules
2. Homepage headline candidates
3. Homepage sub-headline candidates
4. Button/label copy
5. Input placeholder copy
6. Loading state copy
7. Result page generic copy
8. Scenario-specific copy — ocean, land, city, day/night
9. Share card copy
10. Error state copy
11. AI-generation constraints — if/when AI is used
12. Anti-patterns — copy that must never appear

**Relationship to other docs**: For visual tone, see design_direction.md. For flow placement, see ui_flow.md.

**Antipode copy principles**: brief, restrained, never motivational, never resolves the user's life, grounded in geographic facts.
