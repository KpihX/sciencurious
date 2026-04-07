# AGENTS.md — sciencurious

> Project context for all AI agents working in this repository.
> Loaded automatically by all KpihX agents when present at project root.

## KpihX Mantras

**Exploration:** Problem First → Why before How → Visualization
**Architecture:** 0 Trust · 100% Control | 0 Magic · 100% Transparency | 0 Hardcoding · 100% Flexibility

## Project Overview

| Field | Value |
|-------|-------|
| Purpose | Intuitive visual articles on mathematics, physics, and CS |
| Stack | Docsify + KaTeX + GitHub Pages |
| Status | 🟢 Active |
| Live URL | `https://kpihx.github.io/sciencurious/` |
| Remotes | `github` (KpihX/sciencurious) · `gitlab` (kpihx/sciencurious) |

## Content Layout

```
sciencurious/
├── math/           ← mathematics articles + image assets
├── cs/             ← computer science articles (future)
├── physics/        ← physics articles (future)
├── .agents/        ← this file
├── index.html      ← Docsify entry (VS Code dark theme + KaTeX)
├── _sidebar.md     ← navigation
├── README.md
├── CHANGELOG.md
├── TODO.md
└── Makefile        ← make push
```

## Architecture Rules

- **Non-monolithic** — one folder per domain (math/, cs/, physics/); articles are standalone `.md` files within
- **Flexibility** — articles can embed math ($...$, $$...$$), images, Mermaid diagrams, interactive HTML
- **Extensibility** — new domain = new folder + sidebar entry; no structural changes needed
- **No hardcoding** — URLs, paths, and references are relative

## Content Rules

- Articles maximize visual explanations (diagrams, schemas, animations)
- Math uses KaTeX syntax: `$...$` (inline), `$$...$$` (display)
- Images per article go under `<domain>/image/<ArticleName>/`
- Future: integrate code-as-visual (Manim, D3, Mermaid) alongside pixel-gen illustrations

## Evolution Rules

- New article → update `_sidebar.md`, `README.md`, `CHANGELOG.md`
- Any significant change → update this `AGENTS.md`
- **Makefile is the standard task runner** — `make push` for dual-remote sync

## Key Skills

| Skill | When |
|-------|------|
| `k-git-pages` | Docsify setup, GitHub Pages config |
| `k-git` | Push workflow, remote management |
| `k-pptx` | Slide deck generation from articles |
| `k-visual` | Visual content pipeline (Manim, D3, FLUX) — future |
