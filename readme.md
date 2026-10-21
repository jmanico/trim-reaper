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

**Status: specification only.** No application implementation exists yet.

Trim Reaper is specified as a **pure CLI for GitHub repositories**. It proposes verified changes through pull requests for later human review. It never merges its own pull requests.

## First-release scope

- **Java:** Maven and Gradle.
- **.NET:** NuGet through dotnet.
- **JavaScript and TypeScript:** npm, Yarn, and pnpm.
- **Platforms:** Linux, macOS, and Windows where the project’s toolchain supports them.
- **Inputs:** GitHub repository URL, optional base branch, and explicit verification commands and flow assertions.
- **Outputs:** Plain-text summary, Markdown report, and a pull request when verified changes remain.

Use the project’s declared toolchain versions. Supply missing versions explicitly. Existing GitHub credentials must allow branch creation and pull request publication.

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

[REQUIREMENTS.md](REQUIREMENTS.md) owns what the system must do and the first-release acceptance criteria. [DESIGN.md](DESIGN.md) defines CLI and report presentation and the logo palette. The [SVG logo](logo.svg) is a single scythe mark in black and white.

Replacement decisions consider correctness, security risks, performance, implementation effort, and ongoing maintenance. The first release permits bounded local replacements and reports larger proposals for later review. It stops on a failing baseline, undoes candidates that fail checks, and publishes only verified changes. See the requirements for the exact limits.
