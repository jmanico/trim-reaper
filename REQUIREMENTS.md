# Trim Reaper Requirements

The CLI, GitHub-only scope, review-only pull requests, and language families were selected by the project owner. ASSUMPTION: The remaining policies below are conservative defaults selected under the owner’s instruction to resolve all remaining decisions. They are normative for the first release.

## Required Requirement Inputs

- Project purpose: Reduce third-party dependencies while preserving application behavior and runtime compatibility.
- Primary users / actors: Developers who run the CLI; repository maintainers who review its pull requests.
- Core workflows: Establish a baseline; remove unused dependencies; replace dependency functions; combine overlapping capabilities; reduce transitive dependencies; correct dependency scope; verify and report changes.
- Business objects / data entities: Direct and transitive dependencies, dependency graphs, manifests, lockfiles, application code, tests, production artifacts, documentation, and existing software bills of materials (SBOMs).
- External integrations: Package manager; language standard library; supported platform and library APIs. GitHub.com, Maven, Gradle, NuGet through dotnet, npm, Yarn, and pnpm.
- Authentication / roles: Use the operator’s existing GitHub credentials and repository permissions. The first release requires permission to push a working branch and create a pull request; it has no separate user accounts or roles.
- Regulatory or privacy constraints: No additional constraints stated.

## Functional Requirements

### CLI and Repository Scope

- **FR-7.1** The system MUST accept a GitHub.com repository URL and an optional base branch through a non-interactive CLI.
- **FR-7.2** The system MUST use the repository’s default branch when no base branch is supplied.
- **FR-7.3** The system MUST reject local paths and repository hosts other than GitHub.com as project inputs.
- **FR-7.4** The system MUST support public and private repositories accessible with the operator’s GitHub credentials.
- **FR-7.5** The system MUST report missing repository permissions before it changes project files.
- **FR-7.6** The system MUST perform project changes in an isolated working copy of the selected base revision.
- **FR-7.7** The system MUST publish verified changes in one pull request per run against the selected base branch.
- **FR-7.8** The system MUST NOT push changes directly to the base branch.
- **FR-7.9** The system MUST NOT merge or approve its pull requests.
- **FR-7.10** The system MUST report the pull request URL after successful publication.
- **FR-7.11** The system MUST NOT create a pull request when no verified changes remain.
- **FR-7.12** The system MUST report a publication failure without reporting the run as successful.
- **FR-7.13** The system MUST bind publication to the verified final content, immutable repository identity, selected base and run-specific working branch, and invalidate publication eligibility when any bound content changes. [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018) [T-005](THREAT_MODEL.md#t-005), [T-019](THREAT_MODEL.md#t-019)
- **FR-7.14** The system MUST reconcile an ambiguous publication outcome before retrying and MUST NOT create a second pull request for the same run. [T-005](THREAT_MODEL.md#t-005), [T-019](THREAT_MODEL.md#t-019)

### Supported Projects and Verification Inputs

- **FR-8.1** The system MUST support Java projects that use Maven or Gradle.
- **FR-8.2** The system MUST support .NET projects that use NuGet through dotnet.
- **FR-8.3** The system MUST support JavaScript and TypeScript projects that use npm, Yarn, or pnpm.
- **FR-8.4** The system MUST evaluate each supported build root in a repository, including workspaces and repositories with multiple language families.
- **FR-8.5** The system MUST use project-declared toolchain versions, wrappers, and package manager versions without upgrading them.
- **FR-8.6** The system MUST require an explicit operator-supplied version when a required toolchain version is not declared.
- **FR-8.7** The system MUST report unsupported build roots without changing their dependencies.
- **FR-8.8** The system MUST require explicit installation, build, test, and representative runtime-flow commands for each build root selected for changes.
- **FR-8.9** The system MUST accept those commands and their expected exit codes as CLI inputs, with zero as the default expected exit code.
- **FR-8.10** The system MUST require operator-supplied acceptance assertions for each representative runtime flow.
- **FR-8.11** The system MUST report missing commands, assertions, or required tools before dependency changes start.
- **FR-8.12** The system MUST use the project’s existing packaging checks to verify production exclusions; when those checks are absent, it MUST leave production scope unchanged.
- **FR-8.13** The system MUST reject execution before project commands run if the execution containment and finite resource profile specified in SECURITY.md cannot be enforced. [T-001](THREAT_MODEL.md#t-001), [T-007](THREAT_MODEL.md#t-007), [T-011](THREAT_MODEL.md#t-011), [T-017](THREAT_MODEL.md#t-017) [T-006](THREAT_MODEL.md#t-006)
- **FR-8.14** The system MUST perform dependency intelligence analysis locally and MUST NOT transmit repository content to a remote analysis or model provider. [T-003](THREAT_MODEL.md#t-003), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010)
- **FR-8.15** The system MUST retain or defer a candidate when required analysis, source transformation, documentation or existing SBOM format support is incomplete; a scanner assertion alone MUST NOT satisfy the usage investigation. [T-016](THREAT_MODEL.md#t-016)
- **FR-8.16** The system MUST associate verification declarations with their build roots, run all declared required baseline checks, and run the selected roots’ required checks after each candidate, including global checks for cross-root changes. [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018)

- **FR-8.17** The system MUST require positive finite operator-supplied limits for repository bytes and file count, graph nodes and edges, process count, CPU time, memory, disk, operation elapsed time, captured output, and API request/response bytes before execution; absent or unenforceable limits MUST fail preflight. Limits are operator constraints, not measured safe capacities. [T-006](THREAT_MODEL.md#t-006)

### Baseline and Unused Dependencies

- **FR-1.1** The system MUST record the current build results before dependency changes.
- **FR-1.2** The system MUST record the current test results before dependency changes.
- **FR-1.3** The system MUST check application code, dynamic loading, plugins, configuration, scripts, tests, and build and deployment tooling before it classifies a dependency as unused.
- **FR-1.4** The system MUST investigate scanner results before it confirms that a dependency is unused.
- **FR-1.5** The system MUST remove dependencies confirmed as unused.
- **FR-1.6** The system MUST use the package manager to remove transitive dependencies that become unused after dependency changes.

- **FR-1.7** The system MUST record the usage evidence from every area listed in FR-1.3 for each unused-dependency candidate.
- **FR-1.8** The system MUST retain a candidate if dynamic loading, plugin registration, reflection, or external configuration leaves its use uncertain.
- **FR-1.9** The system MUST confirm an unused-dependency removal only when the usage investigation finds no uses and the required checks pass without that dependency.

### Standard and Local Replacements

- **FR-2.1** The system MUST identify dependency functions that the language standard library or supported platform APIs can replace directly.
- **FR-2.2** The system MUST replace identified functions with those standard library functions or supported platform APIs.
- **FR-2.3** The system MUST evaluate local replacement candidates for correctness and maintenance effort, rather than line count alone.
- **FR-2.5** The system MUST provide focused tests for the required behavior and edge cases of each local replacement.
- **FR-2.7** The system MUST remove a replaced dependency only after all its uses have been replaced.

- **FR-2.8** The system MUST limit a local replacement to one module with no new dependency, no public API change, and no persistent state or new network or file access.
- **FR-2.9** The system MUST retain libraries used for cryptography, authentication, protocol handling, general-purpose parsing, or concurrent coordination instead of providing local replacements for those functions.
- **FR-2.10** The system MUST test each local replacement against the existing implementation for normal inputs, boundary inputs, invalid inputs, and error results; it MUST document any category that does not apply.
- **FR-2.11** The system MUST defer replacements that exceed FR-2.8 or cannot satisfy FR-2.10.

### Overlap and Dependency Graph

- **FR-3.1** The system MUST identify libraries that provide overlapping capabilities.
- **FR-3.2** The system SHOULD replace overlapping uses with supported APIs from a library that the project already requires.
- **FR-3.3** The system MUST remove libraries made redundant by those replacements.
- **FR-3.4** The system MUST explain why each retained library is the better fit for the remaining requirements after consolidation.
- **FR-3.7** The system MUST compare the resolved dependency graph before and after changes.
- **FR-3.8** The system MUST NOT remove a transitive package that a retained dependency requires.

- **FR-3.9** The system MUST limit consolidation to APIs supported by the retained library version already in the project.
- **FR-3.10** The system MUST reject consolidation that changes public API types or adds dependencies between application modules.
- **FR-3.11** The system MUST identify a large, lightly used dependency when it has at least ten unique transitive packages and the project uses at most three distinct public API entry points from it.
- **FR-3.12** The system MUST evaluate supported minimal packages, unused optional integrations, and existing alternatives for each candidate identified by FR-3.11.
- **FR-3.13** The system MUST accept a graph-reduction change only when the resolved package count decreases and the required checks pass.

### Dependency Scope

- **FR-4.1** The system MUST identify libraries used only for development, tests, or builds.
- **FR-4.2** The system MUST classify those libraries in the applicable dependency scope.
- **FR-4.3** The system MUST exclude those libraries from production artifacts where the deployment process permits this exclusion.
- **FR-4.4** The system MUST verify the production build from a clean installation after scope changes.
- **FR-4.5** The system MUST verify representative runtime flows from a clean installation after scope changes.

### Substantial Replacements

- **FR-5.1** The system MUST evaluate remaining replacement candidates for implementation effort, code added, security risks, correctness risks, performance, and maintenance effort.

- **FR-5.2** The system MUST report larger replacements for later review without implementing them in the first release.
- **FR-5.3** The system MUST implement a standard-library, platform-API, or local-module replacement only when it removes at least one direct dependency, adds no dependency, does not increase the transitive package count, and passes the required checks.
- **FR-5.4** The system MUST reject a replacement that fails an existing project performance check.
- **FR-5.5** The system MUST report performance as unmeasured when no project performance check exists.

### Final Verification and Report

- **FR-6.1** The system MUST verify a clean installation after dependency changes.
- **FR-6.2** The system MUST verify the final build.
- **FR-6.3** The system MUST run the final tests.
- **FR-6.4** The system MUST verify representative application flows after dependency changes.
- **FR-6.5** The system MUST verify relevant edge cases for standard library and platform API replacements.
- **FR-6.6** The system MUST check that manifests reflect the final dependency graph.
- **FR-6.7** The system MUST check that lockfiles reflect the final dependency graph.
- **FR-6.8** The system MUST check that documentation reflects the final dependency graph.
- **FR-6.9** The system MUST check that any existing SBOM reflects the final dependency graph.
- **FR-6.10** The system MUST report direct dependencies removed.
- **FR-6.11** The system MUST report transitive dependencies removed.
- **FR-6.12** The system MUST report production scope changes separately from complete dependency removal.
- **FR-6.13** The system MUST report local code added.
- **FR-6.14** The system MUST list retained dependencies with reasons for retention.
- **FR-6.15** The system MUST identify checks that it could not complete.
- **FR-6.16** The system MUST emit a plain-text terminal summary and a Markdown report for every run, including runs with no changes or blocked checks.
- **FR-6.17** The system MUST include the Markdown report in the pull request description when it creates a pull request.
- **FR-6.18** The system MUST report each dependency graph as a sorted list of package names, resolved versions, dependency edges, and production or non-production scope, with before and after package counts.
- **FR-6.19** The system MUST label checks PASS, FAIL, NOT RUN, or NOT APPLICABLE; each label other than PASS MUST include a reason.
- **FR-6.20** The system MUST identify the base revision, toolchain versions, commands, and expected and actual check results in its report.
- **FR-6.21** The system MUST render untrusted report content as inert data under DESIGN.md and MUST visibly identify redaction while preserving the required structural evidence. If required evidence cannot be represented safely, it MUST block publication and explain the evidence limitation. [T-004](THREAT_MODEL.md#t-004), [T-013](THREAT_MODEL.md#t-013), [T-014](THREAT_MODEL.md#t-014) [T-003](THREAT_MODEL.md#t-003), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010)
- **FR-6.22** The system MUST require an explicit report destination before project execution and MUST report destination failures with a nonzero exit status, a safe terminal summary on standard error, and the required safe Markdown report on standard output; it MUST NOT start project execution after that preflight failure. [T-003](THREAT_MODEL.md#t-003), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010)

### Failure Handling and Reproducibility

- **FR-9.1** The system MUST stop dependency changes without creating a pull request if a required baseline check fails or cannot run.
- **FR-9.2** The system MUST undo a candidate change if a required check fails or cannot run after that change.
- **FR-9.3** The system MUST verify the last passing state after undoing a candidate change before it tries another candidate.
- **FR-9.4** The system MUST stop without creating a pull request if the last passing state cannot be restored or final verification fails.
- **FR-9.5** The system MUST report each rejected candidate and the check that prevented its inclusion.
- **FR-9.6** The system MUST return exit code zero for a completed verified run, including one with no changes, and a nonzero exit code for a blocked or failed run.
- **FR-9.7** The system MUST verify two fresh installations of the final revision using the same operating system, toolchain versions, package sources, and declared configuration.
- **FR-9.8** The system MUST compare resolved package names, versions, dependency edges, and package integrity values where available across those installations.
- **FR-9.9** The system MUST report reproducibility as failed if those values differ or either installation changes a tracked manifest or lockfile.
- **FR-9.10** The system MUST restore the complete candidate checkpoint across affected build roots after a rejected candidate and reverify the restored state before continuing. [T-015](THREAT_MODEL.md#t-015)
- **FR-9.11** The system MUST bind check evidence to run identity, build root, declared toolchain and commands, and checked content; subsequent mutation MUST invalidate affected verification. [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018)
- **FR-9.12** The system MUST report resource-limit violations as failed required operations, without silently truncating evidence or reporting PASS. [T-006](THREAT_MODEL.md#t-006)
- **FR-9.13** The system MUST perform the cleanup required by SECURITY.md after every outcome and MUST return a nonzero status and report a cleanup failure. [T-003](THREAT_MODEL.md#t-003), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010)

## Non-Functional Requirements

- **NFR-1.1** The system MUST preserve application behavior when it replaces dependency functions.
- **NFR-1.2** The system MUST preserve error handling when it replaces dependency functions.
- **NFR-1.3** The system MUST preserve runtime compatibility when it replaces dependency functions.
- **NFR-1.4** The system MUST produce a reproducible final installation.
- **NFR-1.5** The system MUST support CLI execution on Linux, macOS, and Windows when the project’s declared toolchain supports that operating system.
- **NFR-1.6** The system MUST preserve the project’s declared runtime compatibility targets without raising minimum versions.

Reproducibility covers the dependency installation defined in FR-9.7–FR-9.9. It does not require byte-identical application build artifacts or identical results across different operating systems.
