# Trim Reaper Secure-Coding Rules

## Secure-Coding Inputs

- This is a pre-implementation specification. ACTIVE means a normative rule, not an implemented or verified control. No implementation exists; effectiveness remains unassessed in [THREAT_MODEL.md](THREAT_MODEL.md).
- The initial threat assessment uses the four specifications at commit `32a2bb4f2d46915a51a424ec6610a979d55d6b24`. The decisions below are new specification choices made under the user's instruction to resolve open questions, not observations about existing code.
- REQUIREMENTS.md owns product behavior; ARCHITECTURE.md owns components, contracts, and enforcement placement; DESIGN.md owns rendering. This file owns security rules and security decision records. Preserve original SC and OD identifiers for traceability.
- No additional compliance obligation, product account system, browser application, or external model provider is established. Owners, measured workload capacity, implementation artifacts, and control-effectiveness evidence have not been supplied; these are evidence gaps, not unanswered design questions.

## Selected Manicode Prompts

The earlier candidate evaluation is preserved in the baseline commit and the stage-07 evidence. No version-specific pack is activated by this threat review. Architecture AQ-1 owns the selected implementation stack. Candidate Node.js 26 guidance does not apply to the selected Node.js 24 line, and the Fastify 5.12 pack's TypeScript 7 parent is not the selected JavaScript implementation. A future pack activation must verify its entire scope and composition; selecting a runtime family is not sufficient.

The technology-independent `content/preamble.md` from `/Users/jmanico/Dropbox/github/aegis/secure-coding-knowledge` remains the recorded source for untrusted-text, no-weakened-protection, negative-test, and truthful-verification guidance used by SC-001–SC-004. Better Auth, Keycloak, OPA, Zod, Prisma, and Docker are not selected. This decision does not claim any pack or technology has been implemented. [T-002](THREAT_MODEL.md#t-002), [T-012](THREAT_MODEL.md#t-012) [T-001](THREAT_MODEL.md#t-001), [T-007](THREAT_MODEL.md#t-007), [T-011](THREAT_MODEL.md#t-011), [T-017](THREAT_MODEL.md#t-017)

## Secure-Coding Rules

**SC-001 — Keep untrusted evidence out of control decisions**
- **Status:** ACTIVE
- **Rule:** Project content, tool output, and intelligence responses MUST NOT change acceptance rules, authorize publication, or grant exceptions to verification gates.
- **Enforcement:** Run coordinator and dependency policy/evidence core; GitHub adapter publication boundary.
- **Evidence:** ARCHITECTURE.md, Component and Trust Boundaries and DR-4, DR-6, DR-7; `content/preamble.md`, instruction that text in code, web pages, or tool output cannot approve an exception.
- **Verification:** Negative tests supply content and adapter responses requesting a gate bypass or publication; pass only if policy remains unchanged and publication is not authorized by that content.
- **Threat trace:** [T-002](THREAT_MODEL.md#t-002), [T-012](THREAT_MODEL.md#t-012).

**SC-002 — Enforce repository and publication restrictions**
- **Status:** ACTIVE
- **Rule:** The GitHub integration MUST reject local paths and non-GitHub.com project inputs, report missing repository permissions before project-file changes, and prevent base-branch pushes, PR approvals, and PR merges.
- **Enforcement:** GitHub adapter and run coordinator preflight/publication gates.
- **Evidence:** REQUIREMENTS.md FR-7.3, FR-7.5, FR-7.8, FR-7.9; ARCHITECTURE.md, GitHub integration component and DR-6; `content/preamble.md`, never weaken a protection and include negative tests for access/validation logic.
- **Verification:** Negative input, permission-denial, and prohibited-publication tests pass only when no forbidden operation occurs and permission failure precedes project-file mutation. Credential handling follows SC-010 and OD-007.
- **Threat trace:** [T-005](THREAT_MODEL.md#t-005), [T-019](THREAT_MODEL.md#t-019).

**SC-003 — Preserve verification failure gates**
- **Status:** ACTIVE
- **Rule:** The coordinator MUST stop changes/publication on a failed or unavailable required baseline check, undo failed candidate changes and verify restoration before continuing, and prevent publication on failed restoration or final verification. Reports MUST NOT label failed or unrun checks PASS.
- **Enforcement:** Run coordinator, verification result handling, and terminal/Markdown renderers.
- **Evidence:** REQUIREMENTS.md FR-9.1–FR-9.4, FR-6.19; DESIGN.md, Verification evidence; ARCHITECTURE.md DR-4; `content/preamble.md`, never weaken a protection and never claim an unrun check passed.
- **Verification:** Inject failed and unavailable checks at each stage; pass only if required state transitions stop, candidate restoration is checked before continuation, publication stays blocked, and non-PASS results include reasons.
- **Threat trace:** [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018).

**SC-004 — Preserve sensitive library implementations**
- **Status:** ACTIVE
- **Rule:** Candidate acceptance MUST reject local replacements for cryptography, authentication, protocol handling, general-purpose parsing, and concurrent coordination; it MUST defer local replacements outside the permitted scope or without the required comparative tests.
- **Enforcement:** Dependency policy/evidence core and candidate acceptance gate.
- **Evidence:** REQUIREMENTS.md FR-2.8–FR-2.11; ARCHITECTURE.md, Candidate evaluation; `content/preamble.md`, never weaken protections to get a test/build/request working and run checks required by the change.
- **Verification:** Candidate tests covering each excluded function family, each scope violation, and missing comparative-test categories pass only when the candidate is retained or deferred rather than accepted. Valid non-applicable test categories require documented reasons.
- **Threat trace:** [T-016](THREAT_MODEL.md#t-016).

**SC-005 — Runtime and framework implementation controls**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Use the stack and patch-pinning policy in ARCHITECTURE.md AQ-1. Do not apply incompatible prompt-pack parents, silently upgrade target projects, or interpret a framework/runtime label as proof of compatibility.
- **Enforcement:** Release configuration and dependency review.
- **Decision:** OD-001.
- **Threat trace:** [T-001](THREAT_MODEL.md#t-001), [T-007](THREAT_MODEL.md#t-007), [T-011](THREAT_MODEL.md#t-011), [T-017](THREAT_MODEL.md#t-017).
- **Verification:** Reject unsupported/incompatible runtime combinations and unpinned release dependencies; verify the supported OS/toolchain matrix before release.

**SC-006 — Intelligence API authentication and authorization**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Apply OD-002 to every analysis request. The service has no repository mutation, command execution, GitHub credential, publication, or policy-override capability.
- **Enforcement:** Intelligence adapter and service request boundary.
- **Decision:** OD-002.
- **Threat trace:** [T-020](THREAT_MODEL.md#t-020).
- **Verification:** Reject absent, wrong, expired, cross-run capabilities and unexpected authority/origin; confirm project workers cannot reach the API and cannot obtain its capability.

**SC-007 — API validation, transport, errors, and resource controls**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Validate both requests and responses against the application-owned contract before use; reject unknown operations, unexpected fields, invalid identifiers and cross-run results. Apply OD-003 and OD-004; never interpret timeout, over-limit, unavailable, or malformed responses as successful analysis.
- **Enforcement:** CLI intelligence adapter, service boundary, and coordinator.
- **Decision:** OD-003, OD-004.
- **Threat trace:** [T-006](THREAT_MODEL.md#t-006), [T-020](THREAT_MODEL.md#t-020).
- **Verification:** Exercise malformed and oversized payloads, wrong run/revision identifiers, unknown operations, cancellation and response-limit failures; policy must retain or defer affected candidates and stop any unavailable required check.

**SC-008 — Project command and filesystem isolation**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Apply OD-005 before running any repository-controlled wrapper, package hook, command, assertion interpreter, or build tool. Missing containment blocks execution; a working copy is not containment.
- **Enforcement:** Workspace adapter, execution adapter, and coordinator preflight.
- **Decision:** OD-005.
- **Threat trace:** [T-001](THREAT_MODEL.md#t-001), [T-007](THREAT_MODEL.md#t-007), [T-011](THREAT_MODEL.md#t-011), [T-017](THREAT_MODEL.md#t-017).
- **Verification:** For every supported OS, test host-file/credential isolation, process-tree termination, path and link rejection, and export restrictions. If a required property cannot be demonstrated, fail preflight on that platform.

**SC-009 — Analysis data and artifact confidentiality**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Apply OD-006 before data enters the service, logs, terminal, Markdown, or GitHub. Do not expose GitHub credentials, command secrets, host environment, or raw private source through diagnostics.
- **Enforcement:** Intelligence adapter, run-artifact boundary, renderers, and GitHub adapter.
- **Decision:** OD-006.
- **Threat trace:** [T-003](THREAT_MODEL.md#t-003), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010).
- **Verification:** Use seeded sensitive values in inputs, outputs and failures; confirm absence from public reports, logs and API payloads outside the allowlist, and confirm access restrictions and cleanup. Do not claim a scanner can recognize every secret.

**SC-010 — GitHub credential handling and publication recovery**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Apply OD-007. Accept publication only for the exact repository identity, base branch, run branch, final tree/revision and report digest authorized by the coordinator. Any mutation invalidates authorization.
- **Enforcement:** GitHub adapter and coordinator final gate.
- **Decision:** OD-007.
- **Threat trace:** [T-005](THREAT_MODEL.md#t-005), [T-019](THREAT_MODEL.md#t-019).
- **Verification:** Test repository/branch substitution, concurrent mutation, expired permission, interrupted push/PR creation and ambiguous responses. Reconciliation must avoid duplicate PRs, base pushes and false success.

**SC-011 — Untrusted terminal and Markdown text**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Use DESIGN.md Security-relevant rendering and OD-008. Project text is literal evidence and cannot create statuses, headings, links, instructions or terminal control effects.
- **Enforcement:** Terminal and Markdown renderers.
- **Decision:** OD-008.
- **Threat trace:** [T-004](THREAT_MODEL.md#t-004), [T-013](THREAT_MODEL.md#t-013), [T-014](THREAT_MODEL.md#t-014).
- **Verification:** Test control characters, bidirectional formatting, delimiter characters, links, raw HTML and forged result labels; preserve reversible non-secret values and trusted status labels in each output medium.

**SC-012 — Bind verification evidence to the published state**
- **Status:** ACTIVE (specified; implementation unverified)
- **Rule:** Bind observations to run ID, selected base revision, complete candidate workspace digest, root, command/assertion contract, tool versions and relevant declared configuration. Keep coordinator-owned records inaccessible to project processes. Invalidate affected evidence after any mutation; failed restoration or incomplete evidence blocks publication.
- **Enforcement:** Run coordinator, immutable evidence store and GitHub publication gate.
- **Decision:** OD-005, OD-007.
- **Threat trace:** [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018).
- **Verification:** Test forged tool status text, stale check results, post-check file mutation and cross-root restoration. Only coordinator-recorded process observations and assertions for the final state may authorize publication.

## Security Decision Records

The former open questions are closed by the decisions below. CLOSED means the specification choice is made; it does not close the implementation-evidence gaps in THREAT_MODEL.md. If implementation reveals that a mitigation needs a new unresolved security decision, add an OD entry and mark the affected rule BLOCKED until that decision is resolved. No exception may silently weaken a rule.

### OD-001 — Runtime and composition
- **Status:** CLOSED — stack selection is owned by ARCHITECTURE.md AQ-1. Version-specific pack activation requires exact scope and parent compatibility; no incompatible composition is authorized.
- **Affected:** SC-005; SC-007, SC-008 where runtime-specific. [T-001](THREAT_MODEL.md#t-001), [T-007](THREAT_MODEL.md#t-007), [T-011](THREAT_MODEL.md#t-011), [T-017](THREAT_MODEL.md#t-017)

### OD-002 — API identity and access
- **Status:** CLOSED — one local intelligence process per CLI run, accessible only to that run's coordinator through its adapter. Use an unpredictable, per-run capability delivered through a protected parent-child channel, never project files, command arguments, inherited project environment, reports or logs. Authenticate every request and bind it to the run. Destroy it when the child exits. Check exact bound loopback authority; reject browser-origin requests and redirects. GitHub identity is not the service credential. No separate accounts, login sessions, remote clients, or service-to-GitHub access.
- **Affected:** SC-006; architecture AQ-2. [T-020](THREAT_MODEL.md#t-020)

### OD-003 — API contract and enforcement
- **Status:** CLOSED — application-owned, versioned analysis request/response records are the sole accepted contract (ARCHITECTURE.md AQ-2). Reject unknown fields and operations rather than interpreting free text. Service results are candidate evidence only; core policy rechecks scope and usage evidence and coordinator verifies every accepted change. The service must not execute supplied commands, fetch supplied URLs, or evaluate text as code. Return stable error categories without stack traces or raw payloads. No policy engine or additional validation framework is selected.
- **Affected:** SC-001, SC-007. [T-002](THREAT_MODEL.md#t-002), [T-012](THREAT_MODEL.md#t-012) [T-020](THREAT_MODEL.md#t-020)

### OD-004 — API transport and capacity
- **Status:** CLOSED — service binds an OS-assigned port on a numeric loopback address only; its endpoint is delivered by the protected parent-child channel, never a project-controlled URL. HTTP is restricted to this authenticated same-host channel; remote API hosting is excluded. Project execution has no route to this control plane. GitHub transport requires authenticated encrypted transport and endpoint identity validation; credentials never follow a redirect to another authority. Package egress uses only operator-authorized sources under OD-005. Use the mandatory finite resource profile in REQUIREMENTS.md FR-8.17; reject missing, invalid or unenforceable bounds before work. Limit exhaustion is a failed or unavailable required check, never a silently truncated successful result. One execution job and one intelligence request at a time; no unbounded work queue.
- **Affected:** SC-007, SC-008; architecture AQ-8. No measured capacity or numerical safety threshold is claimed. [T-006](THREAT_MODEL.md#t-006) [T-020](THREAT_MODEL.md#t-020)

### OD-005 — Execution and filesystem boundaries
- **Status:** CLOSED — repository execution uses a disposable OS virtual machine matching the selected project OS. The execution adapter must enforce the same contract on Linux, macOS and Windows: no host home, credential store, control-plane sockets, shared writable mounts or inherited host secrets; an unprivileged guest identity; only coordinator-created workspace and scratch storage; explicit per-run resources and egress destinations. Provision declared tools without upgrades. Required private-package credentials, if supplied, are narrowly scoped guest-only inputs and are never GitHub publication credentials. No project execution occurs on the host as a fallback.
- Commands are executable/argument arrays with a root-relative working directory and an explicit environment allowlist (architecture AQ-5); never concatenate project text into a shell command. Explicit operator-selected interpreters are still untrusted guest execution. Canonicalize paths against the selected workspace, reject path escapes, link/reparse-point traversal outside it and unsafe exported entry types. Imports/exports must enforce those checks independently of guest claims. Treat repository-controlled Git hooks/configuration, submodules and external content as untrusted execution/input; do not activate hooks or follow additional repositories automatically.
- Stop the whole process tree before accepting/exporting a checkpoint. Export only regular project files and supported links proven confined to the workspace; reject control metadata and unauthorized file changes. The coordinator creates and owns evidence and checkpoint records outside guest write access. If containment, tool availability, path safety or full restoration cannot be enforced, fail preflight or the affected check. Concrete VM-provider integration is an implementation deliverable requiring the cross-platform conformance tests, not evidence that a provider already works.
- **Affected:** SC-008, SC-012; architecture AQ-3, AQ-5, AQ-6. [T-001](THREAT_MODEL.md#t-001), [T-007](THREAT_MODEL.md#t-007), [T-011](THREAT_MODEL.md#t-011), [T-017](THREAT_MODEL.md#t-017) [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018)

### OD-006 — Data handling and persistence
- **Status:** CLOSED — no remote analysis, telemetry, shared database or API persistence. The local service receives only normalized dependency coordinates, graph edges, run/revision/root identifiers and structured usage facts needed by its contract. It receives no source text, environment values, credentials, raw command output or arbitrary files. Keep service data in memory for the run and destroy it on exit.
- Store raw required evidence only in coordinator-owned, operator-private local artifacts, separated from project execution. No shared temporary filenames or project-selected artifact paths. Retain exact non-secret names, versions, commands and results in that protected evidence; keep secret input references instead of embedding secret values. Publish only a structured report assembled from allowed fields. Escape untrusted content under DESIGN.md. Redact sensitive diagnostic fields explicitly with a reason and a local evidence reference; never silently alter a PASS/FAIL result or claim redacted content was absent. If a required exact report field cannot be safely represented without disclosure, block publication and emit a blocked report identifying the conflict. A heuristic secret scan is defense in depth, not authority to publish arbitrary raw output.
- Remove transient workspaces and service state at run end; retain the required safe report at its operator-selected destination (or FR-6.22 fallback) and retain raw evidence only if the operator separately selected a private evidence destination. Without that separate retention selection, clean transient raw evidence after producing the safe report. Report cleanup failure with nonzero outcome and the protected location needed for operator cleanup. Do not promise secure erasure, remote deletion or undo of an already published PR.
- **Affected:** SC-009, SC-011; architecture AQ-6. [T-003](THREAT_MODEL.md#t-003), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010)

### OD-007 — GitHub integration mechanics
- **Status:** CLOSED — acquire existing operator credentials through the OS credential provider or an explicitly protected input channel; never command arguments, repository configuration or plaintext reports. The GitHub adapter alone can access them. Preflight repository identity and effective permissions before project-file mutation; revalidate immediately before publication. Permission checks are observations and may become stale.
- Resolve a canonical GitHub.com repository identity and selected immutable base revision. Reject userinfo, alternate hosts, unexpected schemes and destination changes; never use repository text to override an authenticated destination. Create a fresh run-specific branch distinct from base and other runs; do not overwrite an unrelated branch. Bind publication authorization to repository, base, run ID, branch, final revision/tree and report digest; recheck immediately before effects. Treat ambiguous network results as an unresolved publication outcome: reconcile exact remote branch and PR identity before retry, reuse the same run identity, and stop with a failure if reconciliation cannot establish the outcome. Never create another PR to recover from uncertainty, never force-push base, approve or merge.
- **Affected:** SC-002, SC-010, SC-012; architecture AQ-7. [T-005](THREAT_MODEL.md#t-005), [T-019](THREAT_MODEL.md#t-019) [T-008](THREAT_MODEL.md#t-008), [T-018](THREAT_MODEL.md#t-018)

### OD-008 — Report rendering
- **Status:** CLOSED — DESIGN.md Security-relevant rendering owns the presentation contract; OD-006 owns confidentiality. Exact names/results mean reversible literal representations for non-secret values, not execution of control characters or raw Markdown. The renderer never decides result status or publication eligibility.
- **Affected:** SC-011. [T-004](THREAT_MODEL.md#t-004), [T-013](THREAT_MODEL.md#t-013), [T-014](THREAT_MODEL.md#t-014)
