# Repository security checks

Every pull request runs CodeQL on GitHub Actions workflows and dependency review
on dependency changes, including development dependencies. Dependency review fails
for newly introduced known vulnerabilities of low severity or higher. Dependabot
checks action versions daily and opens update pull requests; it is not a PR scanner.
Actions are pinned to commit hashes and updated by Dependabot.

CodeQL also runs on pushes to `main` and weekly. This repository contains Markdown
and an SVG, with no application code to scan. Add the relevant CodeQL languages and
Dependabot ecosystems if application code or package manifests are introduced.
These checks do not detect every bug or assess the correctness of prose.

The `PR security checks` GitHub ruleset targets `main`, requires pull requests and
successful `CodeQL (Actions)` and `Dependency Review` checks, and requires CodeQL
results with all security and other alert severities blocking merges. It has no
bypass actors. These repository settings are managed in GitHub, separately from
these workflow files. A successful analysis job alone does not mean no alerts
were found; the code scanning rule enforces the alert threshold.

Dependabot alerts and security updates are enabled in repository settings.
Review findings in the pull request checks and the repository Security tab.
