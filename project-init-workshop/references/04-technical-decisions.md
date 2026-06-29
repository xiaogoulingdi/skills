# Layer 4 — Technical Decisions

## docs/technical_design.md

**Purpose**: Define the stack, environments, architecture, and module boundaries. Tells developers what to use, what not to use, and why.

**Template structure**:

1. Document goal — what this technical doc covers
2. Current constraints — hardware, environments, budgets
3. Overall technical conclusion — the recommended stack in one line
4. Environment division — which machine does what
5. Tech selection — framework, styling, map, geocoding, AI/copy
   - For each: recommendation, reasoning, what is NOT chosen and why
   - Open questions explicitly marked
6. Docker strategy — dev docker vs. production docker
7. Code sync strategy — how machines stay in sync
8. Core module design — per-module responsibilities, file suggestions, boundaries
9. State management approach
10. Error boundary strategy
11. Testing strategy — unit, component, manual, E2E
12. Deployment strategy — options, trade-offs
13. Environment variables & security
14. Performance & resource constraints
15. First-phase development sequence
16. Technical acceptance criteria

**Relationship to other docs**: For directory layout, see project_structure.md. For scope boundaries, see project_scope.md.

**Antipode tech decisions**:
- Stack: Vite + React + TypeScript + Tailwind CSS + Leaflet + Docker
- Not Next.js: no SSR need, no complex routing in v1
- Map: Leaflet over MapLibre (lighter, less complex for v1)
- Geocoding: Nominatim with stated rate limits and failure fallback
- Copy: template-based, no AI in v1
- State: React local state, no Redux/Zustand in v1
- Windows: primary dev machine; VPS (2GB): docs/GitHub ops/light checks/deploy only

## docs/project_structure.md

**Purpose**: Define the directory layout, file placement rules, and maintenance conventions. Ensures the project stays navigable as it grows.

**Template structure**:

1. Document goal
2. Recommended directory tree — the full structure
3. Root directory — file-by-file purpose and maintenance rules
4. docs/ directory — current docs list, planned future docs, maintenance rules
5. src/ — layering principle: UI vs. logic separation
6. src/app/ — entry point responsibilities
7. src/components/ — per-component responsibilities and boundaries
8. src/features/ — per-domain module responsibilities
9. src/styles/ — global styles and design tokens
10. src/test/ — test setup and conventions
11. public/ — static assets
12. File placement decision tree — quick reference
13. Maintenance rules — adding directories, moving files, adding docs, adding dependencies
14. Structure acceptance criteria

**Relationship to other docs**: For module responsibilities, see technical_design.md. For naming conventions, see github_workflow.md.

**Antipode key rules**:
- Domain logic in src/features/, not in components
- Geocoding layer must insulate UI from raw API structures
- Copy generation centralized in src/features/copy/
- Test files close to their modules
