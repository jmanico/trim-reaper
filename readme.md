<p align="center">
  <img src="logo.svg" alt="Trim Reaper scythe" width="128" height="128">
</p>

<h1 align="center">Trim Reaper</h1>

<p align="center"><strong>Coming for your dependencies. They need to go.</strong></p>

<p align="center">
  <a href="REQUIREMENTS.md">Requirements</a> ·
  <a href="DESIGN.md">Design</a> ·
  <a href="https://github.com/jmanico/trim-reaper/issues">Discussions via issues</a>
</p>

---

Trim Reaper aims to reduce third-party dependencies while preserving application behavior, error handling, and runtime compatibility.

**Status: specification only.** No application implementation exists. Supported languages, package managers, runtime versions, and the user interface are UNKNOWN. Product decisions remain TO BE DECIDED in the requirements and design open questions.

## The work

| Stage | Intended outcome |
| --- | --- |
| Establish the baseline | Record current build and test results. |
| Investigate usage | Check code, dynamic loading, plugins, configuration, scripts, tests, and tooling. |
| Reduce dependencies | Remove confirmed unused packages, replace suitable functions, and consolidate overlapping uses. |
| Correct scope | Separate development, test, and build dependencies from production where permitted. |
| Verify and report | Check the final installation, build, tests, and application flows; explain removals and retention. |

Scanner findings are candidates for investigation. A dependency is removed only after its uses are resolved. Transitive packages remain when a retained dependency requires them.

## Start with the specification

[REQUIREMENTS.md](REQUIREMENTS.md) owns what the system must do and records unresolved acceptance criteria. [DESIGN.md](DESIGN.md) defines proposed visual presentation, tokens, and design questions. The [SVG logo](logo.svg) is a single scythe mark in black and white.

Replacement decisions consider correctness, security risks, performance, implementation effort, and ongoing maintenance. The limits for substantial replacements remain open; see the requirements before implementation.
