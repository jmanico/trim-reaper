---
version: alpha
name: Trim Reaper
description: Dependency reduction with clear verification evidence.
omitted:
  - section: typography
    reason: Typography values are TO BE DECIDED; no interface is specified.
  - section: spacing
    reason: Layout dimensions are TO BE DECIDED; no interface is specified.
  - section: rounded
    reason: Component geometry is TO BE DECIDED; no interface is specified.
colors:
  primary: "#000000"
  surface: "#FFFFFF"
components:
  report:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
  logo:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
---

# Trim Reaper Design

## Overview

[REQUIREMENTS.md](REQUIREMENTS.md) is the sole authority for behavior and workflows. The primary audience and interface are UNKNOWN. Interface selection is TO BE DECIDED.

ASSUMPTION: A spare, monochrome identity suits dependency reduction and evidence-focused reporting. The palette and scythe mark are proposed visual choices, not facts supplied by the requirements. These patterns define presentation only; they do not add product capabilities.

Format reference: [Google's DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md).

## Colors

Use only the following foreground/background pair. It has a WCAG contrast ratio of 21:1, above the WCAG 2.2 AA thresholds of 4.5:1 for normal text and 3:1 for large text, required graphics, UI components, and focus indicators.

| Foreground | Background | Use |
| --- | --- | --- |
| primary — #000000 | surface — #FFFFFF | Text, meaningful borders, logo, and any focus indicator |

Keep colors opaque. Do not introduce gray, transparency, gradients, or additional state colors. Keep the logo's white background on all host surfaces. Any future color pairing requires a contrast check before use.

## Typography

Font family, sizes, weights, and line heights are TO BE DECIDED. Use semantic headings and readable body text in the selected medium. Preserve dependency names exactly. Do not encode verification results through typography alone.

## Layout

ASSUMPTION: A linear reading order supports the required report: direct removals, transitive removals, production scope changes, local code added, retained dependencies with reasons, and checks not completed (FR-6.10–FR-6.15). Keep graph comparisons together (FR-3.7). Dimensions and responsive behavior are TO BE DECIDED.

## Elevation & Depth

ASSUMPTION: Flat presentation is sufficient. Use headings, whitespace, and black rules on white to group evidence. Do not use shadows or layered surfaces.

## Shapes

ASSUMPTION: One solid scythe silhouette represents Trim Reaper. The curved blade and straight handle form a single mark. Preserve its proportions and white backing when scaling. Use no lettering or decorative detail inside the mark. Component corner geometry is TO BE DECIDED.

## Components

- **Dependency report:** Use labeled groups for the categories required by FR-6.10–FR-6.15. Keep production scope changes distinct from complete removal. Show retained dependencies with their reasons.
- **Graph comparison:** Present the before and after dependency graphs with explicit labels. The graph representation is TO BE DECIDED; do not assume a diagram or interactive explorer.
- **Verification evidence:** Present baseline and final checks with explicit result text. Identify checks that could not run; do not present them as passed. Failure responses remain unresolved in OQ-9.
- **Brand mark:** Use the root logo.svg with its title and viewBox intact. Keep the white backing and black silhouette. Supply an accessible name appropriate to the host medium.

These are implementation-neutral content patterns. Controls and interaction states are TO BE DECIDED because no interaction model is specified.

## Do's and Don'ts

- Do preserve requirement terminology and distinguish completed checks from incomplete checks.
- Do use text labels for meaning; never rely on color alone.
- Do retain all report categories when content wraps or the presentation medium changes.
- Do check every future foreground/background pair against the stated contrast thresholds.
- Do not add screens, actions, numerical targets, or behavior absent from REQUIREMENTS.md.

## Open Questions

- **DQ-1** Which presentation medium and interaction model will expose the workflows? TO BE DECIDED; depends on OQ-1.
- **DQ-2** Which typography, spacing, component geometry, and responsive rules suit that medium? TO BE DECIDED.
- **DQ-3** Which report and graph representation will support the agreed output format? TO BE DECIDED; depends on OQ-1.
- **DQ-4** Which result labels and failure presentation follow the agreed verification and failure behavior? TO BE DECIDED; depends on OQ-3 and OQ-9.
