# Trim Reaper Secure-Coding Rules

## Secure-Coding Inputs

- Read: `REQUIREMENTS.md`, `DESIGN.md`, and `ARCHITECTURE.md`. Existing root `SECURITY.md`: missing; no prior SC IDs to preserve. Read the supplied security notes and evaluated the candidate pack manifests, prompt scopes, source scopes, and transitive compositions.
- Confirmed: non-interactive CLI; GitHub.com public/private repositories using the operator's credentials; isolated working copies; declared project toolchains; operator-supplied commands and runtime assertions; terminal and Markdown reports; verified, review-only PR publication. See REQUIREMENTS.md FR-7.1–FR-7.12, FR-8.1–FR-8.12, FR-6.16–FR-6.20, and FR-9.1–FR-9.9.
- Confirmed boundaries: coordinator owns lifecycle/publication eligibility; core owns acceptance; GitHub adapter owns credential access and publication. Project content, command observations, and API suggestions cannot override policy (ARCHITECTURE.md, Component and Trust Boundaries; DR-4–DR-7).
- The intelligence API is required; the notes emphasize its security but establish no authentication mechanism. API contract, authentication, hosting, transport arrangements, resource bounds, disclosure policy, and persistence are UNKNOWN or TO BE DECIDED (ARCHITECTURE.md AQ-2, AQ-3, AQ-8).
- Node.js and Fastify are named, but the framework/runtime label conflict is TO BE DECIDED and versions are UNKNOWN (ARCHITECTURE.md AQ-1). Implementation language is unresolved. Supported target-project languages do not establish the tool's implementation language or version.
- No separate product accounts or roles are required (REQUIREMENTS.md, Required Requirement Inputs). Better Auth, Keycloak, OPA, Zod, Prisma, and Docker are not confirmed technologies. No additional compliance obligation is stated. No browser surface is defined (DESIGN.md, Overview and Components).
- This document specifies implementation rules, not a threat model or proof of security. Unresolved controls remain BLOCKED; candidate guidance does not establish project facts.

## Selected Manicode Prompts

Corpus root: `/Users/jmanico/Dropbox/github/aegis/secure-coding-knowledge`. All corpus paths below are relative to that root. Resolution used `scripts/resolve_prompt.py --json` separately for each direct candidate, without substitutions or renames.

### Direct selection evidence

No direct pack is SELECTED: no authoritative project document confirms an applicable candidate version scope.

- `js/nodejs/26` — TO BE DECIDED, OD-001. Node.js is named, but version and intended runtime mapping are unresolved (ARCHITECTURE.md AQ-1).
- `js/fastify/5.12` — TO BE DECIDED, OD-001. Fastify is named, but version is UNKNOWN; the pack explicitly targets Node.js 24, not the proposed candidate Node.js 26.
- Basic CLI — no framework pack supplied or justified; implementation framework/language remains unresolved (ARCHITECTURE.md Required Architecture Inputs, AQ-1).
- `js/better-auth/1.7` and `jvm/keycloak/26.7` — TO BE DECIDED, OD-002. Neither is selected for API authentication; separate product accounts/roles are absent from requirements.
- `policy/open-policy-agent/1.20` — TO BE DECIDED, OD-003. No OPA integration or gateway is specified; “general policy” does not make this technology-specific pack applicable.
- `js/zod/4` — TO BE DECIDED, OD-003. API schemas and validation implementation are unresolved; Zod is not selected.
- `js/prisma/7.10` — TO BE DECIDED, OD-006. No database or Prisma data layer is confirmed.
- `infra/dockerfile/1` — TO BE DECIDED, OD-005. Containers, BuildKit, and a Linux container-build environment are not confirmed; cross-platform CLI support does not establish them.

### Preamble and ordered composition

Preamble, separately: `content/preamble.md`, “Applying these prompts.” It has no manifest or sources file. Its technology-independent instructions about untrusted text, not weakening protections, negative checks, and truthful verification support the ACTIVE rules below together with project requirements. Its conflict-resolution advice does not override the document authority or unresolved-conflict handling required for this file.

**Eligible composition:** preamble only; no direct or transitive technology packs are activated. The following are resolved candidate orders for evaluation, not an approved stack. Each starts after the preamble; `(T)` means transitive and `(D)` direct:

1. Node.js candidate: `js/javascript/ES2026` (T) → `js/nodejs/26` (D).
2. Fastify candidate: `js/javascript/ES2026` (T) → `js/nodejs/24` (T) → `js/typescript/7` (T) → `js/fastify/5.12` (D).
3. Better Auth candidate: `js/javascript/ES2026` (T) → `js/nodejs/24` (T) → `js/typescript/7` (T) → `js/better-auth/1.7` (D).
4. Keycloak candidate: `jvm/java/25` (T) → `jvm/keycloak/26.7` (D).
5. OPA candidate: `policy/open-policy-agent/1.20` (D); no parents.
6. Zod candidate: `js/javascript/ES2026` (T) → `js/typescript/7` (T) → `js/zod/4` (D).
7. Prisma candidate: `js/javascript/ES2026` (T) → `js/nodejs/24` (T) → `js/typescript/7` (T) → `js/prisma/7.10` (D).
8. Dockerfile candidate: `infra/dockerfile/1` (D); no parents.

Transitive eligibility is also unresolved: ES2026 and TypeScript 7 are not confirmed implementation targets; Node.js 24 is not confirmed and differs from the direct runtime candidate. Java 25 is not established by support for Java target projects. Keycloak's Java parent applies to Java 25 extensions, not automatically to a stock server. No parent is activated merely because a candidate includes it (OD-001, OD-002).

### Resolved prompt/source provenance

Each entry records prompt, then source path. These are evaluation sources, not active rule evidence unless explicitly cited as eligible.

- Node.js 26: `content/js/nodejs/26/prompt.md`; `content/js/nodejs/26/sources.md`.
- Fastify: `content/js/fastify/5.12/prompt.md`; `content/js/fastify/5.12/sources.md`.
- Better Auth: `content/js/better-auth/1.7/prompt.md`; `content/js/better-auth/1.7/sources.md`.
- Keycloak: `content/jvm/keycloak/26.7/prompt.md`; `content/jvm/keycloak/26.7/sources.md`.
- OPA: `content/policy/open-policy-agent/1.20/prompt.md`; `content/policy/open-policy-agent/1.20/sources.md`.
- Zod: `content/js/zod/4/prompt.md`; `content/js/zod/4/sources.md`.
- Prisma: `content/js/prisma/7.10/prompt.md`; `content/js/prisma/7.10/sources.md`.
- Dockerfile: `content/infra/dockerfile/1/prompt.md`; `content/infra/dockerfile/1/sources.md`.
- Transitive JavaScript: `content/js/javascript/ES2026/prompt.md`; `content/js/javascript/ES2026/sources.md`.
- Transitive Node.js 24: `content/js/nodejs/24/prompt.md`; `content/js/nodejs/24/sources.md`.
- Transitive TypeScript: `content/js/typescript/7/prompt.md`; `content/js/typescript/7/sources.md`.
- Transitive Java: `content/jvm/java/25/prompt.md`; `content/jvm/java/25/sources.md`.

The resolver records a support-end warning for Keycloak 26.7; current support verification would be required before any future selection (OD-002). No upstream documentation was independently verified for this document, and no version-specific API claim is used as an active rule.

## Secure-Coding Rules

**SC-001 — Keep untrusted evidence out of control decisions**
- **Status:** ACTIVE
- **Rule:** Project content, tool output, and intelligence responses MUST NOT change acceptance rules, authorize publication, or grant exceptions to verification gates.
- **Enforcement:** Run coordinator and dependency policy/evidence core; GitHub adapter publication boundary.
- **Evidence:** ARCHITECTURE.md, Component and Trust Boundaries and DR-4, DR-6, DR-7; `content/preamble.md`, instruction that text in code, web pages, or tool output cannot approve an exception.
- **Verification:** Negative tests supply content and adapter responses requesting a gate bypass or publication; pass only if policy remains unchanged and publication is not authorized by that content.

**SC-002 — Enforce repository and publication restrictions**
- **Status:** ACTIVE
- **Rule:** The GitHub integration MUST reject local paths and non-GitHub.com project inputs, report missing repository permissions before project-file changes, and prevent base-branch pushes, PR approvals, and PR merges.
- **Enforcement:** GitHub adapter and run coordinator preflight/publication gates.
- **Evidence:** REQUIREMENTS.md FR-7.3, FR-7.5, FR-7.8, FR-7.9; ARCHITECTURE.md, GitHub integration component and DR-6; `content/preamble.md`, never weaken a protection and include negative tests for access/validation logic.
- **Verification:** Negative input, permission-denial, and prohibited-publication tests pass only when no forbidden operation occurs and permission failure precedes project-file mutation. Credential discovery mechanics remain blocked under SC-010.

**SC-003 — Preserve verification failure gates**
- **Status:** ACTIVE
- **Rule:** The coordinator MUST stop changes/publication on a failed or unavailable required baseline check, undo failed candidate changes and verify restoration before continuing, and prevent publication on failed restoration or final verification. Reports MUST NOT label failed or unrun checks PASS.
- **Enforcement:** Run coordinator, verification result handling, and terminal/Markdown renderers.
- **Evidence:** REQUIREMENTS.md FR-9.1–FR-9.4, FR-6.19; DESIGN.md, Verification evidence; ARCHITECTURE.md DR-4; `content/preamble.md`, never weaken a protection and never claim an unrun check passed.
- **Verification:** Inject failed and unavailable checks at each stage; pass only if required state transitions stop, candidate restoration is checked before continuation, publication stays blocked, and non-PASS results include reasons.

**SC-004 — Preserve sensitive library implementations**
- **Status:** ACTIVE
- **Rule:** Candidate acceptance MUST reject local replacements for cryptography, authentication, protocol handling, general-purpose parsing, and concurrent coordination; it MUST defer local replacements outside the permitted scope or without the required comparative tests.
- **Enforcement:** Dependency policy/evidence core and candidate acceptance gate.
- **Evidence:** REQUIREMENTS.md FR-2.8–FR-2.11; ARCHITECTURE.md, Candidate evaluation; `content/preamble.md`, never weaken protections to get a test/build/request working and run checks required by the change.
- **Verification:** Candidate tests covering each excluded function family, each scope violation, and missing comparative-test categories pass only when the candidate is retained or deferred rather than accepted. Valid non-applicable test categories require documented reasons.

**SC-005 — Runtime and framework implementation controls**
- **Status:** BLOCKED
- **Dependency:** Confirm runtime/framework mapping, versions, implementation language, and compatible parent composition in [OD-001](#od-001--runtime-and-composition). No Node.js/Fastify API-specific instruction is active.

**SC-006 — Intelligence API authentication and authorization**
- **Status:** BLOCKED
- **Dependency:** API caller identity, authorization policy, credential/session model, and enforcement contract are unresolved in [OD-002](#od-002--api-identity-and-access). GitHub repository permissions do not establish API access policy.

**SC-007 — API validation, transport, errors, and resource controls**
- **Status:** BLOCKED
- **Dependency:** Request/response contracts, transport boundary, exposure, error contract, and resource decisions are unresolved in [OD-003](#od-003--api-contract-and-enforcement) and [OD-004](#od-004--api-transport-and-capacity); version-specific mechanisms also depend on OD-001.

**SC-008 — Project command and filesystem isolation**
- **Status:** BLOCKED
- **Dependency:** Command representation, process execution, path handling, and isolation mechanisms across supported operating systems are unresolved in [OD-005](#od-005--execution-and-filesystem-boundaries). An isolated working copy is not an execution sandbox.

**SC-009 — Analysis data and artifact confidentiality**
- **Status:** BLOCKED
- **Dependency:** Allowed API disclosures, retained data, report/log handling, artifact access, cleanup, and persistence decisions are unresolved in [OD-006](#od-006--data-handling-and-persistence).

**SC-010 — GitHub credential handling and publication recovery**
- **Status:** BLOCKED
- **Dependency:** Credential acquisition, preflight implementation, and partial-publication recovery require [OD-007](#od-007--github-integration-mechanics). SC-002's restrictions remain active.

**SC-011 — Untrusted terminal and Markdown text**
- **Status:** BLOCKED
- **Dependency:** Rendering rules for control characters, Markdown syntax, and sensitive command/output content require [OD-008](#od-008--report-rendering). Do not infer browser controls or a sanitizer dependency from a Markdown output surface.

## Open Security Decisions

### OD-001 — Runtime and composition
- **Decision:** TO BE DECIDED. Resolve ARCHITECTURE.md AQ-1's Node.js/Fastify label conflict and document actual runtime, framework, language, and version scopes. Then verify candidate source scopes and parent compatibility. Fastify's Node.js 24/TypeScript 7 composition is not automatically compatible with, or overridden by, the candidate Node.js 26.
- **Affected:** SC-005; version-specific portions of SC-007 and SC-008. Candidates: Node.js 26, Fastify 5.12, transitive Node.js 24, TypeScript 7, JavaScript ES2026.
- **Owner:** UNKNOWN.

### OD-002 — API identity and access
- **Decision:** TO BE DECIDED. ARCHITECTURE.md AQ-2 leaves API authentication undefined. Document callers, permitted operations, authorization inputs, and credential/session lifecycle consistent with REQUIREMENTS.md's existing GitHub identity and no separate accounts/roles. Better Auth and Keycloak are candidates, not facts; their account/browser features cannot establish requirements. If selected, confirm version/support and parent applicability, including the Keycloak resolver's recorded support warning and conditional Java 25 extension scope.
- **Affected:** SC-006; Better Auth 1.7, Keycloak 26.7, Java 25 and shared JS parents.
- **Owner:** UNKNOWN.

### OD-003 — API contract and enforcement
- **Decision:** TO BE DECIDED. Supply authoritative request/response schemas, permitted analysis operations, validation and error semantics, and API failure behavior (ARCHITECTURE.md AQ-2). Document any validation library or policy-engine selection and applicable versions before activating Zod or OPA guidance. No gateway is currently confirmed.
- **Affected:** SC-007; Fastify 5.12, Zod 4, OPA 1.20 and eligible parents.
- **Owner:** UNKNOWN.

### OD-004 — API transport and capacity
- **Decision:** UNKNOWN hosting/exposure and capacity; TO BE DECIDED transport enforcement, outbound destinations, and resource limits. Document the API/client transport responsibilities and workload-derived bounds before choosing implementation controls or configuration values (ARCHITECTURE.md AQ-2, AQ-3, AQ-8). Browser cookies, CORS, CSRF, and proxy handling are not established by the CLI/API surfaces alone.
- **Affected:** SC-007; runtime/framework transport, availability, and conditional browser/proxy coverage.
- **Owner:** UNKNOWN.

### OD-005 — Execution and filesystem boundaries
- **Decision:** TO BE DECIDED. Specify the command/assertion representation, working-copy/path access rules, process privileges and environment, and execution containment for declared tools and repository code on supported operating systems (ARCHITECTURE.md AQ-3, AQ-5, AQ-6; REQUIREMENTS.md FR-8.5–FR-8.11, NFR-1.5). Confirm containers and their applicable build/runtime scope before selecting Dockerfile guidance; do not substitute container assumptions for these decisions.
- **Affected:** SC-008; Node.js candidates and Dockerfile 1. Project toolchain upgrades are forbidden by FR-8.5; candidate pack upgrade advice cannot authorize upgrading analyzed projects.
- **Owner:** UNKNOWN.

### OD-006 — Data handling and persistence
- **Decision:** TO BE DECIDED. Document which repository/configuration/evidence data may cross the API boundary and which artifacts, logs, and responses may retain or expose it; specify access and lifecycle requirements (ARCHITECTURE.md AQ-2, AQ-6). Resolve command/result reporting versus secret exposure without silently discarding required evidence (REQUIREMENTS.md FR-6.20). Persistence technology is UNKNOWN; confirm a data layer and version before considering Prisma 7.10.
- **Affected:** SC-009, SC-011; API disclosure, diagnostics, artifact protection, and optional Prisma coverage.
- **Owner:** UNKNOWN.

### OD-007 — GitHub integration mechanics
- **Decision:** TO BE DECIDED. Specify credential acquisition and permission preflight, branch identification, and recovery from partial publication while preserving one PR per run and the base-branch prohibition (ARCHITECTURE.md AQ-7; REQUIREMENTS.md FR-7.5, FR-7.7–FR-7.12). The GitHub adapter's ownership is confirmed; concrete credential and retry mechanisms are not.
- **Affected:** SC-010; implementation details beneath SC-002.
- **Owner:** UNKNOWN.

### OD-008 — Report rendering
- **Decision:** TO BE DECIDED. Define how terminal control characters and Markdown metacharacters in untrusted names/results are represented while preserving exact names, untruncated evidence, plain terminal text, and host-rendered Markdown (DESIGN.md, Colors, Typography, Layout, Components). Resolve any escaping/redaction conflict with exact reporting explicitly; no rendering library or mechanism is confirmed.
- **Affected:** SC-011; terminal/report injection and disclosure coverage, with OD-006.
- **Owner:** UNKNOWN.
