#!/usr/bin/env python3
"""Scaffold the 9 foundational planning docs for a new project.

Usage:
    python scaffold_docs.py --project-root /path/to/my-project
"""

import argparse
from pathlib import Path

DOCS = [
    "product_idea.md",
    "project_scope.md",
    "mvp_plan.md",
    "design_direction.md",
    "ui_flow.md",
    "copywriting.md",
    "technical_design.md",
    "project_structure.md",
    "github_workflow.md",
]

LAYER_LABELS = {
    "product_idea.md": "Layer 1 — Product Definition",
    "project_scope.md": "Layer 1 — Product Definition",
    "mvp_plan.md": "Layer 2 — Execution Planning",
    "design_direction.md": "Layer 3 — Design & Experience",
    "ui_flow.md": "Layer 3 — Design & Experience",
    "copywriting.md": "Layer 3 — Design & Experience",
    "technical_design.md": "Layer 4 — Technical Decisions",
    "project_structure.md": "Layer 4 — Technical Decisions",
    "github_workflow.md": "Layer 5 — Process & Norms",
}

HEADER = """# {title}

> {layer}
>
> This document is part of the foundational planning set.
> For the full document framework, see project-init-workshop.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold project planning docs.")
    parser.add_argument("--project-root", required=True, help="Path to the project root.")
    args = parser.parse_args()

    root = Path(args.project_root)
    docs_dir = root / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    for doc_name in DOCS:
        title = doc_name.replace(".md", "").replace("_", " ").title()
        layer = LAYER_LABELS.get(doc_name, "")
        content = HEADER.format(title=title, layer=layer)

        path = docs_dir / doc_name
        path.write_text(content, encoding="utf-8")
        print(f"  created {path.relative_to(root)}")

    print(f"\n9 docs scaffolded in {docs_dir.resolve()}")


if __name__ == "__main__":
    main()
