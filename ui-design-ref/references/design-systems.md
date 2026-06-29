# Design Systems Quick Reference

## Default Recommendations

| Project Type | Design System | Why |
| --- | --- | --- |
| SaaS / Enterprise | [Adobe Spectrum 2](https://github.com/adobe/react-spectrum) | Stable, accessible, tokens |
| Dashboard / Tools | [shadcn/ui](https://ui.shadcn.com) | Copy-paste, Tailwind, customizable |
| Portfolio / Creative | Tailwind CSS + custom config | Maximum design freedom |
| Enterprise (CN) | [Ant Design](https://ant.design) | Large ecosystem, CN market |

## Design Token Template

```css
:root {
  --color-primary-50: #eff6ff;
  --color-primary-500: #3b82f6;
  --color-primary-900: #1e3a5f;
  --color-neutral-50: #fafafa;
  --color-neutral-500: #737373;
  --color-neutral-900: #171717;
  --color-success: #16a34a;
  --color-error: #dc2626;
  --space-1: 4px; --space-2: 8px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px; --space-16: 64px;
  --font-sans: "Inter", system-ui, sans-serif;
  --text-sm: 0.875rem; --text-base: 1rem;
  --text-lg: 1.125rem; --text-2xl: 1.5rem;
  --radius-md: 6px; --radius-lg: 8px;
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.07);
}
```

## Component State Matrix

Every interactive component: default, hover, focus, active, loading, empty, error, disabled.