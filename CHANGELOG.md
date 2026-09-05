# Changelog

## [Unreleased]

### Added
- New AI articles: `ai/resnet/resnet.md` (ResNet, clean-path proof) + `ai/regnet/regnet.md` (RegNetY design spaces, recipes) with cross-links (prequel/sequel) and footer navigation on all 3 articles
- Per-article `assets/` folders (`ai/regnet/assets/cosine_warmup.png`); root `assets/` brand hub (logo-nobg as logo, banner as page background)
- Uniform article skeleton: header blockquote, TOC, numbered sections, footer nav

### Changed
- `math/integration/`: reorg to `scripts/` + `assets/` (semantic names, `_odyssey` dropped); header blockquote + TOC + numbered sections added, content unchanged
- Sidebar: AI section lists ResNet + RegNet (removed dead `multilingual-token-consumption` link — file absent)
- `index.html`: logo + banner background theming

### Changed
- Migrated from Jekyll (kramdown/mathjax) to Docsify (VS Code dark theme + KaTeX)
- Reorganized repo with KpihX project standard (.agents/, Makefile, CHANGELOG, TODO)
- Added dark/light theme toggle, full-text search, sidebar navigation
- Added GitLab remote mirror
- Initialized repository-wide `uv` Python package setup for notebook workflows (`numpy`, `matplotlib`, `scipy`, `jupyter`)

### Added
- New AI article: `ai/multilingual-token-consumption/article.md`
- New live simulation notebook: `ai/multilingual-token-consumption/multilingual_token_study.ipynb`
- Sidebar and README entries for AI tokenization study content

### Kept
- Integration article content unchanged (integration.md + image/)

## [0.1.0] - 2025-09-26

### Added
- Initial publication of "L'Odyssee de l'Integration" article
- Jekyll-based GitHub Pages with KaTeX math rendering
