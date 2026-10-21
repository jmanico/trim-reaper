# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": [
    {
      "id": "S07-SCOPE",
      "description": "Pre-implementation Trim Reaper specifications at git 32a2bb4f2d46915a51a424ec6610a979d55d6b24; no implementation exists. All four supplied specifications processed independently.",
      "status": "planned specification only",
      "exclusions": [
        ".git internal objects",
        "logo.svg artwork: not application code",
        "No execution, exploitation, or runtime assertions"
      ],
      "document_inventory": [
        {
          "id": "S07-DOC001",
          "path": "REQUIREMENTS.md",
          "type": "requirements",
          "date": "not supplied; currency unknown",
          "author": "not supplied",
          "status": "normative first-release specification",
          "evidence_ids": [
            "S07-E001"
          ]
        },
        {
          "id": "S07-DOC002",
          "path": "ARCHITECTURE.md",
          "type": "architecture",
          "date": "not supplied; currency unknown",
          "author": "not supplied",
          "status": "planned architecture / coding rules",
          "evidence_ids": [
            "S07-E002"
          ]
        },
        {
          "id": "S07-DOC003",
          "path": "SECURITY.md",
          "type": "secure-coding policy",
          "date": "not supplied; currency unknown",
          "author": "not supplied",
          "status": "planned architecture / coding rules",
          "evidence_ids": [
            "S07-E003"
          ]
        },
        {
          "id": "S07-DOC004",
          "path": "DESIGN.md",
          "type": "presentation design",
          "date": "not supplied; currency unknown",
          "author": "not supplied",
          "status": "normative first-release specification",
          "evidence_ids": [
            "S07-E004"
          ]
        }
      ]
    }
  ],
  "evidence": [
    {
      "id": "S07-E001",
      "source": "REQUIREMENTS.md",
      "section": "Full supplied specification",
      "lines": "1-149",
      "sha256": "7a67569359d528a629f70b11255ad92cb95db553eab0625face7b2dacf86b512",
      "status": "documented plan"
    },
    {
      "id": "S07-E002",
      "source": "ARCHITECTURE.md",
      "section": "Full supplied specification",
      "lines": "1-104",
      "sha256": "71200a9f2c7b51e48bfaacb2d4669679df325f80b45811d5a19383169d67ed03",
      "status": "documented plan"
    },
    {
      "id": "S07-E003",
      "source": "SECURITY.md",
      "section": "Full supplied specification",
      "lines": "1-164",
      "sha256": "ba2039e2e7ace97faf9b16afbda26b5916e340172f103f9307d7d0b70bbb8eed",
      "status": "documented plan"
    },
    {
      "id": "S07-E004",
      "source": "DESIGN.md",
      "section": "Full supplied specification",
      "lines": "1-72",
      "sha256": "7374ae7dc0cd24dd0b45bef293203b737bc172ea3b743adb05e4bfee86e06b24",
      "status": "documented plan"
    }
  ],
  "system": {
    "assets": [
      {
        "id": "S07-A001",
        "name": "CLI and report presentation",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A002",
        "name": "Run coordinator",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A003",
        "name": "Dependency policy and evidence core",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A004",
        "name": "Workspace and ecosystem adapters",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A005",
        "name": "Verification execution",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A006",
        "name": "GitHub integration",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A007",
        "name": "Intelligence API and CLI adapter",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      }
    ],
    "actors": [
      {
        "id": "S07-U001",
        "name": "Operator / developer",
        "evidence_ids": [
          "S07-E001"
        ],
        "status": "planned"
      },
      {
        "id": "S07-U002",
        "name": "Repository maintainer",
        "evidence_ids": [
          "S07-E001"
        ],
        "status": "planned"
      },
      {
        "id": "S07-U003",
        "name": "GitHub.com",
        "evidence_ids": [
          "S07-E001"
        ],
        "status": "planned"
      },
      {
        "id": "S07-U004",
        "name": "Configured package sources",
        "evidence_ids": [
          "S07-E001"
        ],
        "status": "planned"
      }
    ],
    "data": [
      {
        "id": "S07-D001",
        "name": "Operator GitHub credentials",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "classification": "not formally supplied; private repositories and credentials are explicitly in scope"
      },
      {
        "id": "S07-D002",
        "name": "Repository source/configuration and isolated copies",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "classification": "not formally supplied; private repositories and credentials are explicitly in scope"
      },
      {
        "id": "S07-D003",
        "name": "Dependency graphs, manifests, lockfiles and SBOM",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "classification": "not formally supplied; private repositories and credentials are explicitly in scope"
      },
      {
        "id": "S07-D004",
        "name": "Commands, expected exits and runtime assertions",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "classification": "not formally supplied; private repositories and credentials are explicitly in scope"
      },
      {
        "id": "S07-D005",
        "name": "Check observations, checkpoints and reports",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "classification": "not formally supplied; private repositories and credentials are explicitly in scope"
      },
      {
        "id": "S07-D006",
        "name": "Intelligence requests and candidate suggestions",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "classification": "not formally supplied; private repositories and credentials are explicitly in scope"
      }
    ],
    "zones": [
      {
        "id": "S07-Z001",
        "name": "Local CLI control",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-Z002",
        "name": "Project execution",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-Z003",
        "name": "GitHub.com remote",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-Z004",
        "name": "Configured package sources",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-Z005",
        "name": "Proposed intelligence service",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      }
    ],
    "boundaries": [
      {
        "id": "S07-B001",
        "name": "Operator input to CLI control",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-B002",
        "name": "Local control to untrusted project execution",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-B003",
        "name": "GitHub credential/publication boundary",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-B004",
        "name": "Package retrieval boundary",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-B005",
        "name": "Proposed intelligence request/response boundary",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      }
    ],
    "flows": [
      {
        "id": "S07-F001",
        "name": "Preflight inputs and selected repository revision",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "source_id": "S07-U001",
        "target_id": "S07-A002",
        "boundary_ids": [
          "S07-B001"
        ],
        "protocol": "not specified"
      },
      {
        "id": "S07-F002",
        "name": "Check execution and observations",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "source_id": "S07-A005",
        "target_id": "S07-A004",
        "boundary_ids": [
          "S07-B002"
        ],
        "protocol": "not specified"
      },
      {
        "id": "S07-F003",
        "name": "Credentialed verified publication",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "source_id": "S07-A006",
        "target_id": "S07-U003",
        "boundary_ids": [
          "S07-B003"
        ],
        "protocol": "GitHub integration; protocol not specified"
      },
      {
        "id": "S07-F004",
        "name": "Dependency retrieval",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "source_id": "S07-A004",
        "target_id": "S07-U004",
        "boundary_ids": [
          "S07-B004"
        ],
        "protocol": "not specified"
      },
      {
        "id": "S07-F005",
        "name": "Analysis inputs and untrusted suggestions",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned",
        "source_id": "S07-A002",
        "target_id": "S07-A007",
        "boundary_ids": [
          "S07-B005"
        ],
        "protocol": "proposed JSON over HTTP"
      }
    ],
    "entry_points": [
      {
        "id": "S07-EP001",
        "name": "CLI repository URL, branch, versions and per-root verification inputs",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP002",
        "name": "Project scripts, wrappers, packages and tool output",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP003",
        "name": "Proposed intelligence request/response contract",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP004",
        "name": "Terminal text and Markdown report publication",
        "evidence_ids": [
          "S07-E002"
        ],
        "status": "planned"
      }
    ]
  },
  "methods": [
    {
      "id": "S07-METHOD",
      "name": "document analysis",
      "status": "completed",
      "extraction_categories": [
        "assets",
        "actors",
        "data",
        "flows",
        "trust boundaries",
        "threats",
        "controls",
        "assumptions",
        "requirements",
        "gaps"
      ]
    }
  ],
  "threats": [],
  "controls": [
    {
      "id": "S07-C-SC-001",
      "source_id": "SC-001",
      "name": "Keep untrusted evidence out of control decisions",
      "status": "planned active rule",
      "text": "- **Status:** ACTIVE\n- **Rule:** Project content, tool output, and intelligence responses MUST NOT change acceptance rules, authorize publication, or grant exceptions to verification gates.\n- **Enforcement:** Run coordinator and dependency policy/evidence core; GitHub adapter publication boundary.\n- **Evidence:** ARCHITECTURE.md, Component and Trust Boundaries and DR-4, DR-6, DR-7; `content/preamble.md`, instruction that text in code, web pages, or tool output cannot approve an exception.\n- **Verification:** Negative tests supply content and adapter responses requesting a gate bypass or publication; pass only if policy remains unchanged and publication is not authorized by that content.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A002",
        "S07-A003"
      ]
    },
    {
      "id": "S07-C-SC-002",
      "source_id": "SC-002",
      "name": "Enforce repository and publication restrictions",
      "status": "planned active rule",
      "text": "- **Status:** ACTIVE\n- **Rule:** The GitHub integration MUST reject local paths and non-GitHub.com project inputs, report missing repository permissions before project-file changes, and prevent base-branch pushes, PR approvals, and PR merges.\n- **Enforcement:** GitHub adapter and run coordinator preflight/publication gates.\n- **Evidence:** REQUIREMENTS.md FR-7.3, FR-7.5, FR-7.8, FR-7.9; ARCHITECTURE.md, GitHub integration component and DR-6; `content/preamble.md`, never weaken a protection and include negative tests for access/validation logic.\n- **Verification:** Negative input, permission-denial, and prohibited-publication tests pass only when no forbidden operation occurs and permission failure precedes project-file mutation. Credential discovery mechanics remain blocked under SC-010.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A006"
      ]
    },
    {
      "id": "S07-C-SC-003",
      "source_id": "SC-003",
      "name": "Preserve verification failure gates",
      "status": "planned active rule",
      "text": "- **Status:** ACTIVE\n- **Rule:** The coordinator MUST stop changes/publication on a failed or unavailable required baseline check, undo failed candidate changes and verify restoration before continuing, and prevent publication on failed restoration or final verification. Reports MUST NOT label failed or unrun checks PASS.\n- **Enforcement:** Run coordinator, verification result handling, and terminal/Markdown renderers.\n- **Evidence:** REQUIREMENTS.md FR-9.1\u2013FR-9.4, FR-6.19; DESIGN.md, Verification evidence; ARCHITECTURE.md DR-4; `content/preamble.md`, never weaken a protection and never claim an unrun check passed.\n- **Verification:** Inject failed and unavailable checks at each stage; pass only if required state transitions stop, candidate restoration is checked before continuation, publication stays blocked, and non-PASS results include reasons.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A002",
        "S07-A003"
      ]
    },
    {
      "id": "S07-C-SC-004",
      "source_id": "SC-004",
      "name": "Preserve sensitive library implementations",
      "status": "planned active rule",
      "text": "- **Status:** ACTIVE\n- **Rule:** Candidate acceptance MUST reject local replacements for cryptography, authentication, protocol handling, general-purpose parsing, and concurrent coordination; it MUST defer local replacements outside the permitted scope or without the required comparative tests.\n- **Enforcement:** Dependency policy/evidence core and candidate acceptance gate.\n- **Evidence:** REQUIREMENTS.md FR-2.8\u2013FR-2.11; ARCHITECTURE.md, Candidate evaluation; `content/preamble.md`, never weaken protections to get a test/build/request working and run checks required by the change.\n- **Verification:** Candidate tests covering each excluded function family, each scope violation, and missing comparative-test categories pass only when the candidate is retained or deferred rather than accepted. Valid non-applicable test categories require documented reasons.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A002",
        "S07-A003"
      ]
    },
    {
      "id": "S07-C-SC-005",
      "source_id": "SC-005",
      "name": "Runtime and framework implementation controls",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** Confirm runtime/framework mapping, versions, implementation language, and compatible parent composition in [OD-001](#od-001--runtime-and-composition). No Node.js/Fastify API-specific instruction is active.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A007"
      ]
    },
    {
      "id": "S07-C-SC-006",
      "source_id": "SC-006",
      "name": "Intelligence API authentication and authorization",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** API caller identity, authorization policy, credential/session model, and enforcement contract are unresolved in [OD-002](#od-002--api-identity-and-access). GitHub repository permissions do not establish API access policy.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A007"
      ]
    },
    {
      "id": "S07-C-SC-007",
      "source_id": "SC-007",
      "name": "API validation, transport, errors, and resource controls",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** Request/response contracts, transport boundary, exposure, error contract, and resource decisions are unresolved in [OD-003](#od-003--api-contract-and-enforcement) and [OD-004](#od-004--api-transport-and-capacity); version-specific mechanisms also depend on OD-001.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A007"
      ]
    },
    {
      "id": "S07-C-SC-008",
      "source_id": "SC-008",
      "name": "Project command and filesystem isolation",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** Command representation, process execution, path handling, and isolation mechanisms across supported operating systems are unresolved in [OD-005](#od-005--execution-and-filesystem-boundaries). An isolated working copy is not an execution sandbox.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A004"
      ]
    },
    {
      "id": "S07-C-SC-009",
      "source_id": "SC-009",
      "name": "Analysis data and artifact confidentiality",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** Allowed API disclosures, retained data, report/log handling, artifact access, cleanup, and persistence decisions are unresolved in [OD-006](#od-006--data-handling-and-persistence).",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A001"
      ]
    },
    {
      "id": "S07-C-SC-010",
      "source_id": "SC-010",
      "name": "GitHub credential handling and publication recovery",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** Credential acquisition, preflight implementation, and partial-publication recovery require [OD-007](#od-007--github-integration-mechanics). SC-002's restrictions remain active.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A006"
      ]
    },
    {
      "id": "S07-C-SC-011",
      "source_id": "SC-011",
      "name": "Untrusted terminal and Markdown text",
      "status": "blocked decision",
      "text": "- **Status:** BLOCKED\n- **Dependency:** Rendering rules for control characters, Markdown syntax, and sensitive command/output content require [OD-008](#od-008--report-rendering). Do not infer browser controls or a sanitizer dependency from a Markdown output surface.",
      "evidence_ids": [
        "S07-E003"
      ],
      "protected_ids": [
        "S07-A001"
      ]
    }
  ],
  "requirements": [
    {
      "id": "S07-R-FR-7.1",
      "source_id": "FR-7.1",
      "text": "The system MUST accept a GitHub.com repository URL and an optional base branch through a non-interactive CLI.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.2",
      "source_id": "FR-7.2",
      "text": "The system MUST use the repository\u2019s default branch when no base branch is supplied.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.3",
      "source_id": "FR-7.3",
      "text": "The system MUST reject local paths and repository hosts other than GitHub.com as project inputs.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.4",
      "source_id": "FR-7.4",
      "text": "The system MUST support public and private repositories accessible with the operator\u2019s GitHub credentials.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.5",
      "source_id": "FR-7.5",
      "text": "The system MUST report missing repository permissions before it changes project files.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.6",
      "source_id": "FR-7.6",
      "text": "The system MUST perform project changes in an isolated working copy of the selected base revision.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.7",
      "source_id": "FR-7.7",
      "text": "The system MUST publish verified changes in one pull request per run against the selected base branch.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.8",
      "source_id": "FR-7.8",
      "text": "The system MUST NOT push changes directly to the base branch.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.9",
      "source_id": "FR-7.9",
      "text": "The system MUST NOT merge or approve its pull requests.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.10",
      "source_id": "FR-7.10",
      "text": "The system MUST report the pull request URL after successful publication.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.11",
      "source_id": "FR-7.11",
      "text": "The system MUST NOT create a pull request when no verified changes remain.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-7.12",
      "source_id": "FR-7.12",
      "text": "The system MUST report a publication failure without reporting the run as successful.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.1",
      "source_id": "FR-8.1",
      "text": "The system MUST support Java projects that use Maven or Gradle.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.2",
      "source_id": "FR-8.2",
      "text": "The system MUST support .NET projects that use NuGet through dotnet.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.3",
      "source_id": "FR-8.3",
      "text": "The system MUST support JavaScript and TypeScript projects that use npm, Yarn, or pnpm.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.4",
      "source_id": "FR-8.4",
      "text": "The system MUST evaluate each supported build root in a repository, including workspaces and repositories with multiple language families.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.5",
      "source_id": "FR-8.5",
      "text": "The system MUST use project-declared toolchain versions, wrappers, and package manager versions without upgrading them.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.6",
      "source_id": "FR-8.6",
      "text": "The system MUST require an explicit operator-supplied version when a required toolchain version is not declared.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.7",
      "source_id": "FR-8.7",
      "text": "The system MUST report unsupported build roots without changing their dependencies.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.8",
      "source_id": "FR-8.8",
      "text": "The system MUST require explicit installation, build, test, and representative runtime-flow commands for each build root selected for changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.9",
      "source_id": "FR-8.9",
      "text": "The system MUST accept those commands and their expected exit codes as CLI inputs, with zero as the default expected exit code.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.10",
      "source_id": "FR-8.10",
      "text": "The system MUST require operator-supplied acceptance assertions for each representative runtime flow.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.11",
      "source_id": "FR-8.11",
      "text": "The system MUST report missing commands, assertions, or required tools before dependency changes start.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-8.12",
      "source_id": "FR-8.12",
      "text": "The system MUST use the project\u2019s existing packaging checks to verify production exclusions; when those checks are absent, it MUST leave production scope unchanged.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.1",
      "source_id": "FR-1.1",
      "text": "The system MUST record the current build results before dependency changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.2",
      "source_id": "FR-1.2",
      "text": "The system MUST record the current test results before dependency changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.3",
      "source_id": "FR-1.3",
      "text": "The system MUST check application code, dynamic loading, plugins, configuration, scripts, tests, and build and deployment tooling before it classifies a dependency as unused.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.4",
      "source_id": "FR-1.4",
      "text": "The system MUST investigate scanner results before it confirms that a dependency is unused.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.5",
      "source_id": "FR-1.5",
      "text": "The system MUST remove dependencies confirmed as unused.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.6",
      "source_id": "FR-1.6",
      "text": "The system MUST use the package manager to remove transitive dependencies that become unused after dependency changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.7",
      "source_id": "FR-1.7",
      "text": "The system MUST record the usage evidence from every area listed in FR-1.3 for each unused-dependency candidate.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.8",
      "source_id": "FR-1.8",
      "text": "The system MUST retain a candidate if dynamic loading, plugin registration, reflection, or external configuration leaves its use uncertain.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-1.9",
      "source_id": "FR-1.9",
      "text": "The system MUST confirm an unused-dependency removal only when the usage investigation finds no uses and the required checks pass without that dependency.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.1",
      "source_id": "FR-2.1",
      "text": "The system MUST identify dependency functions that the language standard library or supported platform APIs can replace directly.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.2",
      "source_id": "FR-2.2",
      "text": "The system MUST replace identified functions with those standard library functions or supported platform APIs.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.3",
      "source_id": "FR-2.3",
      "text": "The system MUST evaluate local replacement candidates for correctness and maintenance effort, rather than line count alone.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.5",
      "source_id": "FR-2.5",
      "text": "The system MUST provide focused tests for the required behavior and edge cases of each local replacement.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.7",
      "source_id": "FR-2.7",
      "text": "The system MUST remove a replaced dependency only after all its uses have been replaced.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.8",
      "source_id": "FR-2.8",
      "text": "The system MUST limit a local replacement to one module with no new dependency, no public API change, and no persistent state or new network or file access.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.9",
      "source_id": "FR-2.9",
      "text": "The system MUST retain libraries used for cryptography, authentication, protocol handling, general-purpose parsing, or concurrent coordination instead of providing local replacements for those functions.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.10",
      "source_id": "FR-2.10",
      "text": "The system MUST test each local replacement against the existing implementation for normal inputs, boundary inputs, invalid inputs, and error results; it MUST document any category that does not apply.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-2.11",
      "source_id": "FR-2.11",
      "text": "The system MUST defer replacements that exceed FR-2.8 or cannot satisfy FR-2.10.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.1",
      "source_id": "FR-3.1",
      "text": "The system MUST identify libraries that provide overlapping capabilities.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.2",
      "source_id": "FR-3.2",
      "text": "The system SHOULD replace overlapping uses with supported APIs from a library that the project already requires.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.3",
      "source_id": "FR-3.3",
      "text": "The system MUST remove libraries made redundant by those replacements.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.4",
      "source_id": "FR-3.4",
      "text": "The system MUST explain why each retained library is the better fit for the remaining requirements after consolidation.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.7",
      "source_id": "FR-3.7",
      "text": "The system MUST compare the resolved dependency graph before and after changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.8",
      "source_id": "FR-3.8",
      "text": "The system MUST NOT remove a transitive package that a retained dependency requires.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.9",
      "source_id": "FR-3.9",
      "text": "The system MUST limit consolidation to APIs supported by the retained library version already in the project.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.10",
      "source_id": "FR-3.10",
      "text": "The system MUST reject consolidation that changes public API types or adds dependencies between application modules.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.11",
      "source_id": "FR-3.11",
      "text": "The system MUST identify a large, lightly used dependency when it has at least ten unique transitive packages and the project uses at most three distinct public API entry points from it.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.12",
      "source_id": "FR-3.12",
      "text": "The system MUST evaluate supported minimal packages, unused optional integrations, and existing alternatives for each candidate identified by FR-3.11.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-3.13",
      "source_id": "FR-3.13",
      "text": "The system MUST accept a graph-reduction change only when the resolved package count decreases and the required checks pass.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-4.1",
      "source_id": "FR-4.1",
      "text": "The system MUST identify libraries used only for development, tests, or builds.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-4.2",
      "source_id": "FR-4.2",
      "text": "The system MUST classify those libraries in the applicable dependency scope.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-4.3",
      "source_id": "FR-4.3",
      "text": "The system MUST exclude those libraries from production artifacts where the deployment process permits this exclusion.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-4.4",
      "source_id": "FR-4.4",
      "text": "The system MUST verify the production build from a clean installation after scope changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-4.5",
      "source_id": "FR-4.5",
      "text": "The system MUST verify representative runtime flows from a clean installation after scope changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-5.1",
      "source_id": "FR-5.1",
      "text": "The system MUST evaluate remaining replacement candidates for implementation effort, code added, security risks, correctness risks, performance, and maintenance effort.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-5.2",
      "source_id": "FR-5.2",
      "text": "The system MUST report larger replacements for later review without implementing them in the first release.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-5.3",
      "source_id": "FR-5.3",
      "text": "The system MUST implement a standard-library, platform-API, or local-module replacement only when it removes at least one direct dependency, adds no dependency, does not increase the transitive package count, and passes the required checks.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-5.4",
      "source_id": "FR-5.4",
      "text": "The system MUST reject a replacement that fails an existing project performance check.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-5.5",
      "source_id": "FR-5.5",
      "text": "The system MUST report performance as unmeasured when no project performance check exists.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.1",
      "source_id": "FR-6.1",
      "text": "The system MUST verify a clean installation after dependency changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.2",
      "source_id": "FR-6.2",
      "text": "The system MUST verify the final build.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.3",
      "source_id": "FR-6.3",
      "text": "The system MUST run the final tests.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.4",
      "source_id": "FR-6.4",
      "text": "The system MUST verify representative application flows after dependency changes.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.5",
      "source_id": "FR-6.5",
      "text": "The system MUST verify relevant edge cases for standard library and platform API replacements.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.6",
      "source_id": "FR-6.6",
      "text": "The system MUST check that manifests reflect the final dependency graph.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.7",
      "source_id": "FR-6.7",
      "text": "The system MUST check that lockfiles reflect the final dependency graph.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.8",
      "source_id": "FR-6.8",
      "text": "The system MUST check that documentation reflects the final dependency graph.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.9",
      "source_id": "FR-6.9",
      "text": "The system MUST check that any existing SBOM reflects the final dependency graph.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.10",
      "source_id": "FR-6.10",
      "text": "The system MUST report direct dependencies removed.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.11",
      "source_id": "FR-6.11",
      "text": "The system MUST report transitive dependencies removed.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.12",
      "source_id": "FR-6.12",
      "text": "The system MUST report production scope changes separately from complete dependency removal.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.13",
      "source_id": "FR-6.13",
      "text": "The system MUST report local code added.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.14",
      "source_id": "FR-6.14",
      "text": "The system MUST list retained dependencies with reasons for retention.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.15",
      "source_id": "FR-6.15",
      "text": "The system MUST identify checks that it could not complete.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.16",
      "source_id": "FR-6.16",
      "text": "The system MUST emit a plain-text terminal summary and a Markdown report for every run, including runs with no changes or blocked checks.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.17",
      "source_id": "FR-6.17",
      "text": "The system MUST include the Markdown report in the pull request description when it creates a pull request.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.18",
      "source_id": "FR-6.18",
      "text": "The system MUST report each dependency graph as a sorted list of package names, resolved versions, dependency edges, and production or non-production scope, with before and after package counts.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.19",
      "source_id": "FR-6.19",
      "text": "The system MUST label checks PASS, FAIL, NOT RUN, or NOT APPLICABLE; each label other than PASS MUST include a reason.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-6.20",
      "source_id": "FR-6.20",
      "text": "The system MUST identify the base revision, toolchain versions, commands, and expected and actual check results in its report.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.1",
      "source_id": "FR-9.1",
      "text": "The system MUST stop dependency changes without creating a pull request if a required baseline check fails or cannot run.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.2",
      "source_id": "FR-9.2",
      "text": "The system MUST undo a candidate change if a required check fails or cannot run after that change.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.3",
      "source_id": "FR-9.3",
      "text": "The system MUST verify the last passing state after undoing a candidate change before it tries another candidate.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.4",
      "source_id": "FR-9.4",
      "text": "The system MUST stop without creating a pull request if the last passing state cannot be restored or final verification fails.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.5",
      "source_id": "FR-9.5",
      "text": "The system MUST report each rejected candidate and the check that prevented its inclusion.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.6",
      "source_id": "FR-9.6",
      "text": "The system MUST return exit code zero for a completed verified run, including one with no changes, and a nonzero exit code for a blocked or failed run.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.7",
      "source_id": "FR-9.7",
      "text": "The system MUST verify two fresh installations of the final revision using the same operating system, toolchain versions, package sources, and declared configuration.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.8",
      "source_id": "FR-9.8",
      "text": "The system MUST compare resolved package names, versions, dependency edges, and package integrity values where available across those installations.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-FR-9.9",
      "source_id": "FR-9.9",
      "text": "The system MUST report reproducibility as failed if those values differ or either installation changes a tracked manifest or lockfile.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-NFR-1.1",
      "source_id": "NFR-1.1",
      "text": "The system MUST preserve application behavior when it replaces dependency functions.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-NFR-1.2",
      "source_id": "NFR-1.2",
      "text": "The system MUST preserve error handling when it replaces dependency functions.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-NFR-1.3",
      "source_id": "NFR-1.3",
      "text": "The system MUST preserve runtime compatibility when it replaces dependency functions.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-NFR-1.4",
      "source_id": "NFR-1.4",
      "text": "The system MUST produce a reproducible final installation.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-NFR-1.5",
      "source_id": "NFR-1.5",
      "text": "The system MUST support CLI execution on Linux, macOS, and Windows when the project\u2019s declared toolchain supports that operating system.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    },
    {
      "id": "S07-R-NFR-1.6",
      "source_id": "NFR-1.6",
      "text": "The system MUST preserve the project\u2019s declared runtime compatibility targets without raising minimum versions.",
      "authority": "REQUIREMENTS.md: sole product-behavior authority",
      "edition": "first release; no numbered edition/date supplied",
      "applicability": "Trim Reaper CLI planned product",
      "status": "normative requirement; not implemented",
      "evidence_ids": [
        "S07-E001"
      ]
    }
  ],
  "risks": [],
  "attack_trees": [],
  "attack_paths": [],
  "visualizations": [
    {
      "id": "S07-V001",
      "name": "Component and Trust Boundaries Mermaid flowchart",
      "evidence_ids": [
        "S07-E002"
      ],
      "status": "planned",
      "kind": "source diagram",
      "description": "Initiation/dependency arrows, not comprehensive bidirectional data-flow notation; proposed intelligence boundary explicitly marked."
    }
  ],
  "coverage": [
    {
      "id": "S07-COV001",
      "document": "REQUIREMENTS.md",
      "disposition": "processed all ten extraction categories",
      "evidence_ids": [
        "S07-E001"
      ],
      "limits": "Documented intent only; no implementation/effectiveness evidence. No pre-existing explicit threat IDs or risk scores supplied."
    },
    {
      "id": "S07-COV002",
      "document": "ARCHITECTURE.md",
      "disposition": "processed all ten extraction categories",
      "evidence_ids": [
        "S07-E002"
      ],
      "limits": "Documented intent only; no implementation/effectiveness evidence. No pre-existing explicit threat IDs or risk scores supplied."
    },
    {
      "id": "S07-COV003",
      "document": "SECURITY.md",
      "disposition": "processed all ten extraction categories",
      "evidence_ids": [
        "S07-E003"
      ],
      "limits": "Documented intent only; no implementation/effectiveness evidence. No pre-existing explicit threat IDs or risk scores supplied."
    },
    {
      "id": "S07-COV004",
      "document": "DESIGN.md",
      "disposition": "processed all ten extraction categories",
      "evidence_ids": [
        "S07-E004"
      ],
      "limits": "Documented intent only; no implementation/effectiveness evidence. No pre-existing explicit threat IDs or risk scores supplied."
    }
  ],
  "conflicts": [
    {
      "id": "S07-CF001",
      "title": "Technology labels",
      "description": "Architecture records supplied Node.js/framework and Fastify/runtime labels versus proposed conventional mapping. Preserve both; AQ-1 and OD-001 unresolved.",
      "status": "unresolved in intake specifications",
      "evidence_ids": [
        "S07-E002",
        "S07-E003"
      ]
    },
    {
      "id": "S07-CF002",
      "title": "Candidate pack composition",
      "description": "SECURITY.md records direct Node.js 26 candidate versus Fastify parent Node.js 24/TypeScript 7. Neither candidate establishes runtime selection or compatibility.",
      "status": "unresolved in intake specifications",
      "evidence_ids": [
        "S07-E003",
        "S07-E003"
      ]
    },
    {
      "id": "S07-CF003",
      "title": "Literal reporting versus safe representation",
      "description": "DESIGN requires exact names and untruncated evidence; SECURITY OD-006/OD-008 asks how escaping/redaction preserves evidence without exposing secrets or active terminal/Markdown content. This is a design constraint requiring explicit reconciliation, not a demonstrated flaw.",
      "status": "unresolved in intake specifications",
      "evidence_ids": [
        "S07-E004",
        "S07-E003"
      ]
    }
  ],
  "gaps": [
    {
      "id": "S07-G001",
      "description": "All documents lack dated revision/author metadata; no runtime evidence, tests, legal obligations, risk methodology or numeric ratings are supplied.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G002",
      "description": "AQ-1 / OD-001: runtime/language/version/distribution and pack applicability.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G003",
      "description": "AQ-2 / OD-002 through OD-004: intelligence operations, schemas, provider, identity, transport/exposure, errors and capacity.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G004",
      "description": "AQ-3 / OD-005: executable code containment and toolchain availability on supported operating systems.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G005",
      "description": "AQ-4: language-specific usage analysis, safe edits, graph normalization, documentation/SBOM formats.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G006",
      "description": "AQ-5 / OD-005: verification command/assertion format, required baseline and candidate coverage.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G007",
      "description": "AQ-6 / OD-006: artifacts, checkpoints, rollback, lifecycle and disclosure handling.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G008",
      "description": "AQ-7 / OD-007: credential acquisition, permission preflight, retry/partial-publication recovery.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G009",
      "description": "AQ-8 / OD-004: workload/scale bounds unsupported by measurements.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G010",
      "description": "OD-008: safe terminal and Markdown rendering with exact evidence and confidential content.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    },
    {
      "id": "S07-G011",
      "description": "No named owner is supplied for security decisions; no owner or deadline inferred.",
      "evidence_ids": [
        "S07-E001",
        "S07-E002",
        "S07-E003",
        "S07-E004"
      ]
    }
  ]
}
```

## Summary

Processed REQUIREMENTS.md (all normative behaviors), ARCHITECTURE.md (seven logical components, flows, boundaries, diagram and eight open questions), SECURITY.md (all eleven rules and eight blocked decisions, including candidate provenance), and DESIGN.md (terminal/Markdown rendering and review interactions). Dates and authors are not supplied; currency is unknown. Controls are plans, never tested results. No existing scored risks or numbered threats occur in the input.

Conflicts preserve the runtime/framework label reversal, competing candidate pack version scopes, and the literal-reporting/escaping-redaction constraint. Gaps capture missing contracts, isolation, storage lifecycle, analysis mechanisms, publication recovery and scale evidence. Additional documentation needed is the resolved owning specifications and eventual implementation/test evidence; there is no interview or request to delay the pipeline.
