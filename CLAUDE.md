# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the GitHub **organization profile** repository for GhostLabs. Its one piece of
public content is `profile/README.md`, which GitHub renders on the organization's
public page; everything else in the repo exists to generate that file.

For this to display on GitHub, the repo must be the org's special `.github` repo
(i.e. `github.com/GhostRoboticsLab/.github`), with the profile at the conventional
`profile/README.md` path. Do not move or rename that file — the path is what makes
GitHub pick it up.

`profile/README.md` is a **generated file** — do not edit it by hand. The source of
truth is `profile/README.template.md` (same Markdown, with `{{TOKEN}}` color
placeholders), rendered by `generate.py`:

```
python3 generate.py            # list the 9 palettes + show the active one
python3 generate.py phosphor   # re-skin README.md to "Phosphor CRT" (the default)
python3 generate.py bone       # light-mode palette, etc.
```

The 9 palettes mirror the Tweaks panel on `ghostlabs.web.app` (its `PALETTES` map in
`signal.jsx`). To change content, edit the template and re-run the generator. To change
theme, just re-run with a different palette key. There is no other build, test, lint, or
CI step; the rendered result is only visible on the org's GitHub landing page.

## Org-wide default files (inherited by every GhostRoboticsLab repo)

Besides the profile README, this repo holds GitHub's *default community health files*
(added 2 Sep 2026): `SECURITY.md`, `.github/ISSUE_TEMPLATE/{bug_report,feature_request,config}.yml`
and `.github/PULL_REQUEST_TEMPLATE.md`. GitHub applies them to every org repository, public
or private, that has no file of the same type of its own (Hackagotchi and Hermes keep their
own). They must stay at these paths; CODEOWNERS is not inheritable and lives per repo.

## Working with the README

The README is presentation-heavy HTML-in-Markdown driven by external image services.
Keep these in mind when editing:

- **Dynamic banners/badges** come from third-party render services
  (`capsule-render.vercel.app`, `readme-typing-svg.demolab.com`,
  `img.shields.io`, `github-readme-stats.vercel.app`). Their visual config lives
  entirely in the URL query string — colors, text, animation, theme. Changing the
  look means editing those query params, not adding local assets.
- Brand aesthetic mirrors the live site (`ghostlabs.web.app`), which uses a dark
  "Phosphor CRT" palette: near-black bg `#050807`, text `#d6f5e1`, dim `#7ea88c`,
  hairline `#1a241e`, phosphor-green accent `#5cff95`, amber secondary `#ffce5c`.
  Fonts are Inter Tight (display) and JetBrains Mono (eyebrows/labels). Reuse these to
  stay on-brand. The site is palette-swappable; the README's top comment documents the
  two hex values to swap. Positioning: "an independent engineering firm" building
  bespoke software, intelligence, and systems end-to-end — not a robotics research lab.
- Featured-work pins reference real repos under the `GhostRoboticsLab` GitHub user in
  their URLs. The org's display name is "GhostLabs" but the GitHub handle is
  `GhostRoboticsLab` — both appear and are intentionally different.
- Centered layout and multi-column sections rely on raw `<div align="center">` and
  `<table>` HTML, since GitHub Markdown alone can't do it.

Since nothing renders locally, verify changes by viewing the file on GitHub after
pushing (or paste a service URL into a browser to preview a single dynamic image).
