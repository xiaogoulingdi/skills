#!/usr/bin/env python3
"""Generate a design spec artifact directory for a new project.

Usage:
  python generate_design.py --project "my-app" --system "spectrum2" --output ./design
"""

import argparse
import os
import textwrap

DESIGN_SYSTEMS = {
    "spectrum2": {
        "name": "Adobe Spectrum 2",
        "css_vars": textwrap.dedent("""\
          :root {
            --spectrum-global-color-static-black: #000;
            --spectrum-global-color-static-white: #fff;
            --spectrum-global-color-blue-500: #2680eb;
            --spectrum-global-color-blue-700: #1473e6;
            --spectrum-global-color-gray-50: #fff;
            --spectrum-global-color-gray-100: #fafafa;
            --spectrum-global-color-gray-200: #f4f4f4;
            --spectrum-global-color-gray-500: #8d8d8d;
            --spectrum-global-color-gray-700: #505050;
            --spectrum-global-color-gray-900: #1d1d1d;
            --spectrum-global-color-green-500: #2d8c3c;
            --spectrum-global-color-red-500: #d7373f;
            --spectrum-global-dimension-size-50: 4px;
            --spectrum-global-dimension-size-100: 8px;
            --spectrum-global-dimension-size-200: 16px;
            --spectrum-global-dimension-size-400: 32px;
            --spectrum-global-font-family-sans: adobe-clean, "Source Sans Pro", system-ui, sans-serif;
            --spectrum-global-font-size-50: 11px;
            --spectrum-global-font-size-100: 14px;
            --spectrum-global-font-size-200: 16px;
            --spectrum-global-font-size-400: 20px;
            --spectrum-global-font-size-700: 28px;
            --spectrum-alias-border-radius-regular: 4px;
          }
        """),
    },
}


def main():
    parser = argparse.ArgumentParser(description="Generate design spec artifacts")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--system", default="spectrum2", choices=list(DESIGN_SYSTEMS.keys()))
    parser.add_argument("--output", default="./design", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    system = DESIGN_SYSTEMS[args.system]

    with open(os.path.join(args.output, "design-tokens.css"), "w") as f:
        f.write(f"/* {args.project} -- Design Tokens ({system['name']}) */\n\n")
        f.write(system["css_vars"])

    with open(os.path.join(args.output, "components.jsx"), "w") as f:
        f.write(f"// {args.project} -- Component Inventory\n\n")
        f.write("export function AppShell({ children }) {\n")
        f.write('  return <div className="app-shell">{children}</div>;\n')
        f.write("}\n")

    with open(os.path.join(args.output, "data.js"), "w") as f:
        f.write(f"// {args.project} -- Data Models\n\n")
        f.write("export const sampleUser = {\n")
        f.write('  id: "u_01",\n')
        f.write('  name: "User Name",\n')
        f.write('  email: "user@example.com",\n')
        f.write("};\n")

    print(f"Generated design artifacts in {args.output}/")


if __name__ == "__main__":
    main()
