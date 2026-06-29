# Design Artifact Templates

## CSS Design Tokens (design-tokens.css)

```css
:root {
  --color-primary-500: #3b82f6;
  --color-neutral-50: #fafafa;
  --color-neutral-900: #171717;
  --color-success: #16a34a;
  --color-error: #dc2626;
  --space-1: 4px; --space-2: 8px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px;
  --font-sans: "Inter", system-ui, sans-serif;
  --text-xs: 0.75rem; --text-sm: 0.875rem; --text-base: 1rem;
  --text-lg: 1.125rem; --text-xl: 1.25rem; --text-2xl: 1.5rem;
  --radius-sm: 4px; --radius-md: 6px; --radius-lg: 8px;
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.07);
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
}
```

## React Component Inventory (components.jsx)

```jsx
// Layout
function AppShell({ children, sidebar }) { /* wrapper */ }
function Sidebar({ items, collapsed, onToggle }) { /* nav */ }
function Header({ title, actions }) { /* top bar */ }

// Data
function DataTable({ columns, rows, loading, empty, error }) { /* table */ }
function Card({ title, children, footer }) { /* container */ }

// Forms
function FormField({ label, error, required, children }) { /* field */ }
function SearchInput({ value, onChange }) { /* search */ }

// Feedback
function EmptyState({ icon, title, description, action }) { /* empty */ }
function ErrorBanner({ message, onRetry }) { /* error */ }
function LoadingSkeleton({ lines }) { /* skeleton */ }

// Navigation
function Pagination({ page, total, onChange }) { /* pages */ }
function Tabs({ tabs, active, onChange }) { /* tabs */ }
```

## Data Models (data.js)

```js
const User = { id: "u_01", name: "Jane", email: "j@e.com", role: "admin", createdAt: "..." };
const Project = { id: "p_01", name: "Redesign", status: "active", ownerId: "u_01" };
const ListResponse = { items: [], total: 42, page: 1, pageSize: 20 };
const ErrorResponse = { code: "VALIDATION_ERROR", message: "Email required", field: "email" };
```