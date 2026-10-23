<p align="center">
  <img src="logo.svg" alt="Trim Reaper scythe" width="128" height="128">
</p>

<h1 align="center">Trim Reaper</h1>

<p align="center"><strong>Third party libraries must all die.</strong></p>
<p align="center">Coming for your dependencies. They need to go.</p>

A set of prompts for any coding agent to help remove third-party libraries responsibly. Keep libraries that earn their place through correctness, security, or maintenance value.

> SCA can't flag a library you don't ship. Your dashboard may miss the drama. 😉

## How to use

Open the project you want to trim in your preferred coding agent. Paste the shared instruction below, then work through the eight prompts in order, or choose a specific pass. Always establish a baseline first and finish with prompt 8. Review the changes before merging.

### Shared instruction

> Reduce this project's dependencies while preserving behavior, error handling,
> security, and supported runtime compatibility. Follow the project's contributor
> instructions and use its existing toolchain and package manager. Work in small,
> reviewable changes and preserve unrelated work. Establish the build and test baseline
> before editing; if required checks fail or cannot run, report the blocker and stop
> changes. Investigate uncertain usage rather than guessing. Verify each change; undo
> your candidate changes if verification fails or cannot be completed. Do not weaken
> tests or security controls to make a removal pass. Retain specialized libraries when
> replacing them would introduce security, correctness, or maintenance risk, especially
> cryptography, authentication, and complex parsing. Report actual commands and results,
> including checks not run. Fewer dependencies is useful only when the resulting project
> is better.

## 1. Remove unused dependencies

> Establish the current build and test baseline. Find and remove confirmed unused
> dependencies. Check application code, dynamic loading, plugins, configuration,
> scripts, tests, and build/deployment tooling. Treat scanner results as candidates to
> investigate. Prune newly orphaned transitive dependencies through the package manager.
> Verify the changes and report what was removed.

## 2. Use the standard library

> Find dependencies whose used functionality can be replaced directly by the language's
> standard library or supported platform APIs. Implement those replacements, preserving
> behavior, error handling, and runtime compatibility. Verify relevant edge cases.
> Remove each dependency once all its uses have been replaced.

## 3. Replace small, simple functionality

> Find dependencies used only for simple, narrowly scoped functionality that we can
> maintain in a small, straightforward module. Implement replacements with focused tests
> for required behavior and edge cases. Judge simplicity by correctness and maintenance
> burden, not just line count. Defer replacements that reveal substantial complexity.

## 4. Consolidate overlapping libraries

> Identify libraries providing overlapping capabilities. Where practical, standardize on
> supported APIs from a library this project already requires, then remove redundant
> dependencies. Preserve behavior and avoid significant new coupling. Explain why each
> retained library is the better fit for the remaining requirements.

## 5. Reduce transitive overhead

> Find dependencies that introduce large dependency subtrees for functionality we barely
> use. Reduce that overhead using supported minimal packages, unused optional-
> integration removal, or existing alternatives. Compare the resolved dependency graph
> before and after. Remove transitive packages only when no retained dependency requires
> them.

## 6. Keep development dependencies out of production

> Find libraries needed only for development, testing, or building. Correct their
> dependency scope and exclude them from production artifacts where the deployment
> process permits. Verify the production build and representative runtime flows from a
> clean installation. Report scope changes separately from dependencies eliminated
> entirely.

## 7. Evaluate larger replacements

> Review remaining dependencies for replacements requiring more substantial work.
> Compare implementation effort, code added, security and correctness risks,
> performance, and ongoing maintenance. Implement only bounded replacements with a clear
> net benefit and adequate verification. Retain libraries whose complexity or
> specialized functionality makes replacement a poor tradeoff, and explain why.

## 8. Verify and report

> Verify a clean reproducible installation, build, tests, and representative application
> flows. Check that manifests, lockfiles, documentation, and any existing SBOM reflect
> the final dependency graph. Summarize direct dependencies removed, transitive
> dependencies eliminated, production scope changes, and local code added. List retained
> dependencies with reasons, and clearly identify any checks you could not complete.

## Contributing

Keep prompts clear, practical, and usable with any coding agent, language, or package manager. Improvements should help people make and verify responsible dependency reductions. Submit changes through a pull request.
