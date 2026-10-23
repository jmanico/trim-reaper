<p align="center">
  <img src="logo.svg" alt="Trim Reaper scythe" width="120" height="120">
</p>

<h1 align="center">Trim Reaper</h1>

<p align="center">
  <strong>Third party libraries must all die.</strong><br>
  Coming for your dependencies. They need to go.
</p>

**A policy for adding and upgrading libraries, plus eight copy-and-paste prompts for reducing dependencies**, usable with any coding agent. Keep libraries that earn their place through correctness, security, or maintenance value. SCA can't flag a library you don't ship. Your dashboard may miss the drama. 😉

## How to use

- **When adding or upgrading libraries:** copy the [third-party library policy](#third-party-library-policy) into your project's `AGENTS.md` or equivalent persistent agent instructions.
- **When reducing existing dependencies:** use the [dependency reduction prompts](#dependency-reduction-prompts) in your preferred coding agent.

## Third-party library policy

Add this section to your project's `AGENTS.md` or equivalent persistent agent instructions. If it already contains dependency guidance, reconcile the instructions into one consistent policy.

```markdown
## Third-party libraries

- Minimize third-party dependencies to reduce ongoing updates and maintenance. Prefer the standard library, supported platform APIs, or functionality already available in the project when they meet the requirements.
- Add a library only when its benefits justify its ongoing maintenance, security, and upgrade costs. For simple, narrowly scoped functionality, consider a small local implementation when it is easier to maintain and verify. Retain specialized libraries when replacement would increase security, correctness, or maintenance risk, especially for cryptography, authentication, and complex parsing.
- Inspect the resolved transitive dependency tree before adding or upgrading a library. Prefer suitable options with fewer transitive dependencies, and avoid bringing in large dependency trees for functionality the project barely uses. Explain why any substantial increase is necessary and assess its update burden.
- When changing existing dependency usage, look for safe opportunities to remove unused or redundant libraries and unnecessary optional integrations. Preserve behavior and supported runtime compatibility, verify the changes, and explain justified retention.
- Before adding or upgrading a library, check its official package registry and repository live. Never select versions from model memory.
- Use the latest stable, supported release compatible with the project. Explain any choice of an older release.
- Choose actively maintained projects with recent maintainer activity, responsive maintainers, and ongoing support. Reject archived, deprecated, or abandoned projects.
- Check current security advisories. Avoid versions with known applicable vulnerabilities.
- Keep updates scoped to the task. Use the project's package manager to resolve transitive dependencies; avoid unrelated upgrades, forced overrides, and manual lockfile edits that bypass compatibility constraints. Prefer a compatible parent-library update when a transitive dependency needs remediation.
- Before updating, review release notes, migration guidance, and dependency constraints for breaking changes. Explain concrete effects on this project and the required migration work. If an update requires a broader migration or hits a compatibility blocker, stop and report the evidence and options before expanding scope. Do not repeatedly attempt speculative upgrades or fixes; resume only with new evidence or an agreed migration plan.
- If you cannot verify these requirements, report the blocker before adding the dependency.
```

## Dependency reduction prompts

Open the project you want to trim in your preferred coding agent. Paste the shared instruction below, then work through the eight prompts in order, or choose a specific pass. Always establish a baseline first and finish with prompt 8. Review the changes before merging.

**Choose a pass:**
[1 · Unused](#1-remove-unused-dependencies) ·
[2 · Standard library](#2-use-the-standard-library) ·
[3 · Simple replacements](#3-replace-small-simple-functionality) ·
[4 · Overlap](#4-consolidate-overlapping-libraries) ·
[5 · Transitive overhead](#5-reduce-transitive-overhead) ·
[6 · Production scope](#6-keep-development-dependencies-out-of-production) ·
[7 · Larger replacements](#7-evaluate-larger-replacements) ·
[8 · Verify](#8-verify-and-report)

### Shared instruction

> Reduce this project's dependencies while preserving behavior, error handling,
> security, and supported runtime compatibility. Follow the project's contributor
> instructions and use its existing toolchain and package manager. Work in small,
> reviewable changes and preserve unrelated work. Establish the build and test baseline
> before editing; if required checks fail or cannot run, report the blocker and stop
> changes.
>
> Investigate uncertain usage rather than guessing. Verify each change; undo
> your candidate changes if verification fails or cannot be completed. Do not weaken
> tests or security controls to make a removal pass.
>
> Retain specialized libraries when
> replacing them would introduce security, correctness, or maintenance risk, especially
> cryptography, authentication, and complex parsing. Report actual commands and results,
> including checks not run. Fewer dependencies is useful only when the resulting project
> is better.

### 1. Remove unused dependencies

> Establish the current build and test baseline. Find and remove confirmed unused
> dependencies. Check application code, dynamic loading, plugins, configuration,
> scripts, tests, and build/deployment tooling. Treat scanner results as candidates to
> investigate. Prune newly orphaned transitive dependencies through the package manager.
> Verify the changes and report what was removed.

### 2. Use the standard library

> Find dependencies whose used functionality can be replaced directly by the language's
> standard library or supported platform APIs. Implement those replacements, preserving
> behavior, error handling, and runtime compatibility. Verify relevant edge cases.
> Remove each dependency once all its uses have been replaced.

### 3. Replace small, simple functionality

> Find dependencies used only for simple, narrowly scoped functionality that we can
> maintain in a small, straightforward module. Implement replacements with focused tests
> for required behavior and edge cases. Judge simplicity by correctness and maintenance
> burden, not just line count. Defer replacements that reveal substantial complexity.

### 4. Consolidate overlapping libraries

> Identify libraries providing overlapping capabilities. Where practical, standardize on
> supported APIs from a library this project already requires, then remove redundant
> dependencies. Preserve behavior and avoid significant new coupling. Explain why each
> retained library is the better fit for the remaining requirements.

### 5. Reduce transitive overhead

> Find dependencies that introduce large dependency subtrees for functionality we barely
> use. Reduce that overhead using supported minimal packages, unused
> optional-integration removal, or existing alternatives. Compare the resolved
> dependency graph before and after. Remove transitive packages only when no retained
> dependency requires them.

### 6. Keep development dependencies out of production

> Find libraries needed only for development, testing, or building. Correct their
> dependency scope and exclude them from production artifacts where the deployment
> process permits. Verify the production build and representative runtime flows from a
> clean installation. Report scope changes separately from dependencies eliminated
> entirely.

### 7. Evaluate larger replacements

> Review remaining dependencies for replacements requiring more substantial work.
> Compare implementation effort, code added, security and correctness risks,
> performance, and ongoing maintenance. Implement only bounded replacements with a clear
> net benefit and adequate verification. Retain libraries whose complexity or
> specialized functionality makes replacement a poor tradeoff, and explain why.

### 8. Verify and report

> Verify a clean reproducible installation, build, tests, and representative application
> flows. Check that manifests, lockfiles, documentation, and any existing SBOM reflect
> the final dependency graph. Summarize direct dependencies removed, transitive
> dependencies eliminated, production scope changes, and local code added. List retained
> dependencies with reasons, and clearly identify any checks you could not complete.

## Contributing

Keep prompts clear, practical, and usable with any coding agent, language, or package manager. Improvements should help people choose, maintain, and reduce dependencies responsibly, with evidence and verification. Submit changes through a pull request.
