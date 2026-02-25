# saachigupta.net — CLAUDE.md

## Stack
- **Framework:** Astro (v5+) with file-based routing
- **Styling:** Vanilla CSS only — no Tailwind, no UI libraries
- **Interactivity:** React islands (`.tsx`) for interactive components; all other pages are `.astro`
- **Build:** Vite (bundled with Astro), TypeScript strict mode
- **Package manager:** npm

## Project Structure
```
src/
├── components/
│   └── WonderlandPlanner.tsx     # React island (placeholder)
├── layouts/
│   └── SiteLayout.astro          # Master layout: header, nav, footer, hero
└── pages/
    ├── index.astro               # Home page with hero image
    ├── reflections.astro         # Reflections hub
    ├── adventures.astro          # Adventures hub
    ├── builds/
    │   ├── index.astro           # Auto-generated grid from sibling pages
    │   ├── wonderland.astro
    │   ├── adventure-planner.astro
    │   └── halloween-costume-generator.astro
    └── learnings/
        ├── index.astro           # Auto-generated grid from sibling pages
        ├── vibe-coding-workshop.astro
        └── rebuilding-without-a-website-builder.astro
public/
├── hero.jpg
└── images/
```

## Key Conventions

**Frontmatter metadata** — every content page exports these constants:
```astro
---
export const title = "Post Title";
export const date = "2026-01-15";       // ISO format
export const excerpt = "Short summary";
export const tags = ["tag1", "tag2"];
export const link = "https://...";      // builds only, optional
---
```

**Dynamic index pages** — `builds/index.astro` and `learnings/index.astro` use `import.meta.glob` to auto-discover sibling pages and render card grids. Adding a new page to either folder auto-adds it to the grid.

**SiteLayout.astro props:**
- `title` — page `<title>` tag
- `showHero` — boolean to show/hide hero image (only on home page)

## Design System
- **Font:** system-ui stack, no web fonts
- **Colors:** black on white; secondary text at `rgba(0,0,0,0.6–0.8)`
- **Cards:** 14px border-radius, `1px solid rgba(0,0,0,0.10)` border, `0 10px 28px rgba(0,0,0,0.08)` shadow
- **Hover:** `translateY(-2px)`, increased shadow, 0.15s ease transition
- **Breakpoint:** `@media (max-width: 640px)` for mobile
- **Max content width:** `75ch` for readable line length
- **Font scale:** 40px name, 20px h2, 16px body, 14px meta

## Site Sections
- `/builds` — project writeups with live demo links
- `/learnings` — reflective posts about process
- `/reflections` — short, unpolished notes
- `/adventures` — outdoor/travel content

## Philosophy
- Minimal dependencies — only add what's needed
- Content is written directly in `.astro` files (no CMS, no markdown files)
- Performance-first: lean output, no unnecessary packages
- Personal brand: projects, learnings, and outdoor adventures
