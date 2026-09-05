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
├── math/<article>/      ← article.md + scripts/ + assets/ (+ integration.mp4)
├── ai/<article>/        ← article.md + assets/ (+ scripts/ si génération)
├── cs/                  ← computer science articles (future)
├── physics/             ← physics articles (future)
├── assets/              ← brand hub: logo-nobg (logo), banner (page background)
├── .agents/             ← this file
├── index.html           ← Docsify entry (VS Code dark theme + KaTeX + branding)
├── _sidebar.md          ← navigation
├── README.md
├── CHANGELOG.md
├── IDEAS.md
├── pyproject.toml       ← uv deps (manim, edge-tts, matplotlib, numpy, scipy) — NO package, NO build, scripts only
└── Makefile             ← make push + per-article targets (make <article>)
```

## Architecture Rules

- **Non-monolithic** — one folder per domain (math/, cs/, physics/); articles are standalone `.md` files within
- **Flexibility** — articles can embed math ($...$, $$...$$), images, Mermaid diagrams, interactive HTML
- **Extensibility** — new domain = new folder + sidebar entry; no structural changes needed
- **No hardcoding** — URLs, paths, and references are relative

## Content Rules

- Articles maximize visual explanations (diagrams, schemas, animations)
- Math uses KaTeX syntax: `$...$` (inline), `$$...$$` (display)
- Images per article go under `<domain>/<article>/assets/` with semantic names (never timestamps); brand assets live in root `assets/`
- Scripts per article go under `<domain>/<article>/scripts/`; runnable via `make <article>` (CWD = `scripts/`)
- Future: integrate code-as-visual (Manim, D3, Mermaid) alongside pixel-gen illustrations

## Article Skeleton (uniform, never compress)

Every article follows the same skeleton — same header, easy navigation:

1. `# <Title>` + blockquote meta (🧠 subtitle · 📅 date · 👤 author · 📚 sources · 🎬 video if any)
2. `## 📋 Table of Contents` (numbered, anchor links via `<span id="...">` on section headers)
3. Numbered emoji body sections (`## 🧩 1. ...`), subsections free
4. Cross-link box after header when sequel/prequel exists (`> 🔗 **Sequel/Prequel:** [...]`, base-relative links like `ai/regnet/regnet.md` — never `../`, Docsify resolves links from base)
5. `## 📚 References` (keep each article's bibliography style, same heading)

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
