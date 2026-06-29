---
name: project-init-workshop
description: Guide for the initial research and documentation phase of a new project. Use when a user wants to start a new project and needs to write foundational planning docs such as product vision, scope boundaries, MVP plan, design direction, UI flow, copywriting, technical design, project structure, and GitHub workflow. Also use when the user asks to "set up project docs", "do initial project research", "write planning documents", or "create a project documentation starter kit".
---

# Project Init Workshop

Write a set of foundational planning documents for a new project before writing any code.

## Workflow

Use this sequence when the user is in the zero-to-one phase and needs to turn an idea into a structured project plan.

1. Define the product idea and formal scope.
2. Convert scope into an MVP plan and development sequence.
3. Define design direction, UI flow, and copy voice.
4. Define technical design and project structure.
5. Define GitHub workflow and collaboration norms.

## Document Layers

Write documents in the order below. Each document depends on the clarity of the previous layer.

### Layer 1 - Product Definition

1. `docs/product_idea.md` - Idea pool and raw concept
2. `docs/project_scope.md` - Formal scope boundary

Read `references/01-product-definition.md` for templates and Antipode examples.

### Layer 2 - Execution Planning

3. `docs/mvp_plan.md` - Milestones and sequencing

Read `references/02-execution-planning.md` for templates and Antipode examples.

### Layer 3 - Design & Experience

4. `docs/design_direction.md` - Visual identity and constraints
5. `docs/ui_flow.md` - User interaction flow
6. `docs/copywriting.md` - Tone and copy guidelines

Read `references/03-design-experience.md` for templates and Antipode examples.

### Layer 4 - Technical Decisions

7. `docs/technical_design.md` - Stack, environments, architecture
8. `docs/project_structure.md` - Directory layout and rules

Read `references/04-technical-decisions.md` for templates and Antipode examples.

### Layer 5 - Process & Norms

9. `docs/github_workflow.md` - Branching, commits, PRs, review

Read `references/05-process-norms.md` for templates and Antipode examples.

## Writing Rules

- State each document's relationship to adjacent documents.
- Do not repeat large sections between documents; link to the source document instead.
- Keep each document scoped to its purpose. Do not let `product_idea.md` become a spec or let `technical_design.md` define UI.
- Use plain language and avoid process documents that do not help planning, implementation, review, or acceptance.
- Treat `project_scope.md` as the source of truth for MVP boundaries.

## Quick Scaffold

Run `scripts/scaffold_docs.py` to create the 9 standard planning docs in a project's `docs/` folder.
