# Iterative Development Workflow

## Version Splitting

```
v0.1 — Shell + nav (no real data)
v0.2 — Primary feature
v0.3 — Secondary feature
v0.4 — Edge states (loading, empty, error)
v0.5 — Polish (responsive, a11y, animation)
v0.6 — Performance audit
v1.0 — Release
```

## Issue Classification

| Problem | Fix in... |
| --- | --- |
| Color / spacing / layout wrong | Design tokens / HTML (design first) |
| Missing component prop or state | Component spec (design first) |
| Button color slightly off | CSS (code fix OK) |
| Animation timing | CSS/JS (code fix OK) |
| Wrong data shape | data.js (design first) |

Rule: **what** the UI should be → fix in design. **How** to achieve it → fix in code.

## Diff-Driven Handoff

1. Modify design files.
2. Commit: `git diff HEAD~1 -- design/`
3. Show agent diff + screenshot.
4. Agent knows what changed.

## Context Hygiene

- One design task = one session.
- When task changes, start fresh.
- Do not let one session grow indefinitely.