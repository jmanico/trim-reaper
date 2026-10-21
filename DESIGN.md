---
version: alpha
name: Trim Reaper
description: Dependency reduction with clear verification evidence.
omitted:
  - section: typography
    reason: The terminal and Markdown renderer control font metrics; this project does not override them.
  - section: spacing
    reason: Plain-text lines and Markdown structure use host layout; fixed spacing tokens do not apply.
  - section: rounded
    reason: The CLI has no graphical controls or containers.
colors:
  primary: "#000000"
  surface: "#FFFFFF"
components:
  logo:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
---

# Trim Reaper Design

## Overview

[REQUIREMENTS.md](REQUIREMENTS.md) is the sole authority for behavior and workflows. The product is a non-interactive CLI for developers working on GitHub repositories. Its outputs are terminal text and Markdown reports included in pull request descriptions. Maintainers review the proposed changes; the product never approves or merges them.

ASSUMPTION: The following visual defaults were selected under the owner’s instruction to resolve the remaining decisions. Keep the existing monochrome identity and scythe mark. These patterns define presentation only; they do not add product capabilities.

Format reference: [Google's DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md).

## Colors

For project-controlled artwork, use only the following foreground/background pair. Terminal output emits no color or background escape sequences; Markdown uses the host’s accessible theme. Host-selected colors are not project tokens. The defined pair has a WCAG contrast ratio of 21:1, above the WCAG 2.2 AA thresholds of 4.5:1 for normal text and 3:1 for large text, required graphics, UI components, and focus indicators.

| Foreground | Background | Use |
| --- | --- | --- |
| primary — #000000 | surface — #FFFFFF | Logo silhouette on its opaque backing |

Keep colors opaque. Do not introduce gray, transparency, gradients, or additional state colors. Keep the logo's white background on all host surfaces. Any future color pairing requires a contrast check before use.

## Typography

Inherit the terminal’s font metrics and the Markdown renderer’s typography. Do not ship fonts or override font sizes. Use plain section labels in terminal output and semantic headings in Markdown. Preserve dependency names exactly. Do not encode verification results through typography alone.

## Layout

Use a linear reading order for the required report: direct removals, transitive removals, production scope changes, local code added, retained dependencies with reasons, and checks not completed (FR-6.10–FR-6.15). Keep graph comparisons together (FR-3.7). Use one column, blank lines between groups, and lists instead of wide tables. Let the host wrap lines; never truncate package names, versions, or check results. No breakpoints or fixed layout dimensions apply.

## Elevation & Depth

Use headings and blank lines to group evidence. Terminal and Markdown reports have no elevation, shadows, or layered surfaces.

## Shapes

One solid scythe silhouette represents Trim Reaper. The curved blade and straight handle form a single mark. Preserve its proportions and white backing when scaling. Use no lettering or decorative detail inside the mark. No buttons, cards, corner radii, or interactive graphical controls apply to the CLI.

## Components

- **Dependency report:** Use labeled groups for the categories required by FR-6.10–FR-6.15. Keep production scope changes distinct from complete removal. Show retained dependencies with their reasons.
- **Graph comparison:** Present the before and after dependency graphs with explicit labels. Use sorted package lists with resolved versions, dependency edges, and production or non-production scope, followed by package counts. Do not draw an interactive graph.
- **Verification evidence:** Present baseline and final checks with explicit result text. Identify checks that could not run; do not present them as passed. Use PASS, FAIL, NOT RUN, and NOT APPLICABLE exactly. Include reasons for all non-PASS results. Show blocked baseline checks, rejected candidates, and publication failures in text, following FR-9.1–FR-9.6.
- **Brand mark:** Use the root logo.svg with its title and viewBox intact. Keep the white backing and black silhouette. Supply an accessible name appropriate to the host medium.

These are implementation-neutral content patterns. No prompts, menus, progress animations, or graphical interaction states apply. Print the pull request URL on publication; otherwise explain why no pull request was created.

## Do's and Don'ts

- Do preserve requirement terminology and distinguish completed checks from incomplete checks.
- Do use text labels for meaning; never rely on color alone.
- Do retain all report categories when content wraps or the presentation medium changes.
- Do check every future foreground/background pair against the stated contrast thresholds.
- Do not add screens, actions, numerical targets, or behavior absent from REQUIREMENTS.md.
