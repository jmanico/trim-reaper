# Trim Reaper Requirements

## Required Requirement Inputs

- Project purpose: Reduce third-party dependencies while preserving application behavior and runtime compatibility.
- Primary users / actors: UNKNOWN
- Core workflows: Establish a baseline; remove unused dependencies; replace dependency functions; combine overlapping capabilities; reduce transitive dependencies; correct dependency scope; verify and report changes.
- Business objects / data entities: Direct and transitive dependencies, dependency graphs, manifests, lockfiles, application code, tests, production artifacts, documentation, and existing software bills of materials (SBOMs).
- External integrations: Package manager; language standard library; supported platform and library APIs. Specific products: UNKNOWN.
- Authentication / roles: UNKNOWN
- Regulatory or privacy constraints: UNKNOWN

## Functional Requirements

### Baseline and Unused Dependencies

- **FR-1.1** The system MUST record the current build results before dependency changes.
- **FR-1.2** The system MUST record the current test results before dependency changes.
- **FR-1.3** The system MUST check application code, dynamic loading, plugins, configuration, scripts, tests, and build and deployment tooling before it classifies a dependency as unused.
- **FR-1.4** The system MUST investigate scanner results before it confirms that a dependency is unused.
- **FR-1.5** The system MUST remove dependencies confirmed as unused.
- **FR-1.6** The system MUST use the package manager to remove transitive dependencies that become unused after dependency changes.

### Standard and Local Replacements

- **FR-2.1** The system MUST identify dependency functions that the language standard library or supported platform APIs can replace directly.
- **FR-2.2** The system MUST replace identified functions with those standard library functions or supported platform APIs.
- **FR-2.3** The system MUST evaluate local replacement candidates for correctness and maintenance effort, rather than line count alone.
- **FR-2.5** The system MUST provide focused tests for the required behavior and edge cases of each local replacement.
- **FR-2.7** The system MUST remove a replaced dependency only after all its uses have been replaced.

### Overlap and Dependency Graph

- **FR-3.1** The system MUST identify libraries that provide overlapping capabilities.
- **FR-3.2** The system SHOULD replace overlapping uses with supported APIs from a library that the project already requires.
- **FR-3.3** The system MUST remove libraries made redundant by those replacements.
- **FR-3.4** The system MUST explain why each retained library is the better fit for the remaining requirements after consolidation.
- **FR-3.7** The system MUST compare the resolved dependency graph before and after changes.
- **FR-3.8** The system MUST NOT remove a transitive package that a retained dependency requires.

### Dependency Scope

- **FR-4.1** The system MUST identify libraries used only for development, tests, or builds.
- **FR-4.2** The system MUST classify those libraries in the applicable dependency scope.
- **FR-4.3** The system MUST exclude those libraries from production artifacts where the deployment process permits this exclusion.
- **FR-4.4** The system MUST verify the production build from a clean installation after scope changes.
- **FR-4.5** The system MUST verify representative runtime flows from a clean installation after scope changes.

### Substantial Replacements

- **FR-5.1** The system MUST evaluate remaining replacement candidates for implementation effort, code added, security risks, correctness risks, performance, and maintenance effort.

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

## Non-Functional Requirements

- **NFR-1.1** The system MUST preserve application behavior when it replaces dependency functions.
- **NFR-1.2** The system MUST preserve error handling when it replaces dependency functions.
- **NFR-1.3** The system MUST preserve runtime compatibility when it replaces dependency functions.
- **NFR-1.4** The system MUST produce a reproducible final installation.

## Open Questions

- **OQ-1** Who operates the system, how is work started, and what project input and report formats are required?
- **OQ-2** Which languages, package managers, runtime versions, platforms, and deployment processes must the system support?
- **OQ-3** Which commands, expected results, representative flows, and edge cases define the baseline and final acceptance checks?
- **OQ-4** What evidence confirms that a dependency is unused, including uses through dynamic loading or external configuration?
- **OQ-5** What correctness and maintenance criteria permit replacement of a narrowly scoped dependency with a small local module, and what complexity requires deferral?
- **OQ-6** What limits define practical consolidation and significant new coupling?
- **OQ-7** What limits define a large dependency graph and limited use of its functions, for reduction through supported minimal packages, removal of unused optional integrations, or existing alternatives?
- **OQ-8** What limits permit a substantial replacement based on bounded effort, clear net benefit, and adequate verification, and require retention of complex or specialized libraries?
- **OQ-9** What must the system do when baseline or final checks fail or cannot run, including whether to stop or restore changes?
- **OQ-10** What installation outputs and environment conditions must match to establish reproducibility?
