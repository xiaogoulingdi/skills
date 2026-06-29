# Layer 5 — Process & Norms

## docs/github_workflow.md

**Purpose**: Define the branching strategy, commit conventions, PR process, and review expectations. Makes the repository history readable and collaboration predictable — even for solo projects.

**Template structure**:

1. Why not commit directly to main
2. Common branch models — comparative overview
   - GitHub Flow
   - Gitflow
   - Trunk-Based Development
3. Recommended strategy for this project — with rationale
4. Branch naming conventions — with examples and anti-examples
5. Commit message conventions — conventional commit format
6. Pull Request conventions — title, body, verification checklist
7. Review & merge strategy
8. Git command quick reference — common workflows
9. Daily development commands — create branch, commit, push, PR
10. Release flow — dev → main merge
11. Conflict resolution — step-by-step
12. Pre-PR self-check commands
13. First-phase recommended branch sequence
14. Definition of Done — per branch type

**Relationship to other docs**: For directory conventions, see project_structure.md. For what constitutes a feature, see project_scope.md.

**Antipode branch strategy**: Lightweight Gitflow
- main — stable, deployable
- dev — daily integration
- feature/* — new capabilities
- docs/* — documentation
- fix/* — bug fixes
- hotfix/* — urgent main fixes

Normal path: main → dev → feature/docs/fix branch → dev → main

**Antipode commit examples**:
- docs: add GitHub workflow guide
- feat: add coordinate input
- fix: handle invalid coordinates
- style: refine result card layout
- test: add antipode calculation tests

## Additional Planned Docs

Beyond the core 9, these may be added as the project matures:

- docs/testing_plan.md — test strategy, coverage targets, manual verification checklist
- docs/acceptance_criteria.md — per-feature acceptance conditions
- docs/deployment.md — production deployment steps and rollback
- docs/roadmap.md — post-MVP feature timeline
- docs/issue_templates.md — standardized issue formats
