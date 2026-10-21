# Agent Instructions

@REQUIREMENTS.md
@ARCHITECTURE.md
@SECURITY.md
@DESIGN.md

## Issue Bodies

Every leaf implementation issue MUST follow `REQUIREMENT_TEMPLATE.md`; epic, workstream, and decision issues use concise purpose-specific bodies that link to affected specification IDs and issues.

## Contributor Workflow

- This repository currently contains specifications only; there is no application build to run. Validate documentation changes with `python3 scripts/validate_threat_model.py` and `git diff --check` from the repository root.
- Preserve requirement/decision IDs and trace security changes to `THREAT_MODEL.md`. The pipeline artifacts retain their baseline evidence; do not relabel planned controls as implemented.
- Use a descriptive topic branch, commit reviewable changes, and open a pull request against `main`. Merge only when the user has authorized it and all configured required checks pass; never bypass repository protection.
- For the future implementation, use the stack in ARCHITECTURE.md AQ-1 and provide reproducible install, test and lint commands in the initial implementation PR. These commands are deliverables, not tools that exist today.
- Keep Markdown formatting consistent with neighboring content. Document-only checks cannot establish runtime security. Before any application release, pin the runtime/dependencies and demonstrate the security verification cases and supported-platform matrix specified in SECURITY.md; no application release is authorized by a documentation merge.
