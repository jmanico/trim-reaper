# Agent Instructions

Trim Reaper is a collection of prompts in `readme.md` for responsible dependency reduction with any coding agent.

- Keep the project simple: plain Markdown prompts and the existing logo. Do not introduce an application, framework, or specification system.
- Preserve the prompts' emphasis on evidence, behavior, security, compatibility, verification, and justified retention of dependencies.
- Keep instructions agent-neutral and avoid assuming a particular language, package manager, or hosting service in the prompts.
- Validate documentation changes with `git diff --check` and check that local links and referenced files exist. There is no application build or test suite.
- Use a descriptive topic branch, commit reviewable changes, and open a pull request against `main`. Merge only when the user has authorized it and all configured required checks pass; never bypass repository protection.
