---
name: ui-design-ref
description: |
  Pre-development UI design methodology. Use when the user asks to build a web app, website, landing page, dashboard, or any frontend project where UI quality matters and no design has been produced yet. Also use when the user mentions UI planning, design system setup, or design-to-code workflow. This skill must be applied BEFORE writing application code — if the user tries to skip design and jump to implementation, stop and instruct them to complete a design pass first.
---

# UI Design Reference

Design-system-first methodology for pre-development UI planning, based on @dotey proven AI-assisted workflow.

## Hard Gate

If the user asks to build a web app or site and has NOT yet produced design artifacts, **stop**. Reply:

> Before I write code, let us lock in a design first. Pick a design system (or let me suggest one), then I will produce: color tokens, spacing scale, component inventory, and data models. This takes a few minutes and saves hours of rewriting later.

Do not proceed to implementation until the user completes the design step or explicitly says "skip design, go straight to code."

## Workflow

### 1. Pick a design system

Present 2–3 options appropriate to the project. Default: Adobe Spectrum 2 for SaaS/enterprise, shadcn/ui for dashboards, Tailwind for custom designs.

Read `references/design-systems.md` for the comparison table and token templates.

### 2. Produce design artifacts

Generate these files in a `design/` directory:

```
design/
  design-tokens.css   — color palette, spacing, typography, radii, shadows
  components.jsx      — component inventory with props and states
  data.js             — data models and API response shapes
  index.html          — layout wireframe (optional)
```

Use: `python scripts/generate_design.py --project "name" --output ./design`

Read `references/artifact-templates.md` for the full CSS spec, component templates, and data model examples.

### 3. Iterate in small versions

| Version | Scope |
| --- | --- |
| v0.1 | Shell + navigation, skeleton only |
| v0.2 | Primary feature |
| v0.3 | Secondary feature |
| v0.4 | Edge states (loading, empty, error, disabled) |
| v0.5 | Polish (responsive, animation, a11y) |

After each version: test, classify issues, commit, repeat.

Read `references/iteration-workflow.md` for version-splitting and diff-driven handoff.

### 4. Design change pipeline

1. Modify design files in `design/`.
2. Commit — the diff IS the change spec.
3. Show agent `git diff` + a screenshot.
4. Agent applies changes without lengthy explanation.

## Rules

- UI problem → fix in design files FIRST, then apply diff. Never patch UI directly in application code.
- One design session per task. Start fresh when the task changes.
- Design artifacts are text files in git. They are the source of truth.
- Expose design variables (theme, density, navigation) as configurable tweaks.

## Credits

Methodology: @dotey. Design system: [Adobe Spectrum 2](https://github.com/adobe/react-spectrum).