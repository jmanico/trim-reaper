# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": [
    {
      "id": "FM-S1",
      "description": "Pre-implementation review of all four complete specifications; documented controls are planned, not implemented; no code analyzed."
    }
  ],
  "evidence": [
    {
      "id": "FM-E1",
      "source": "REQUIREMENTS.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "7a67569359d528a629f70b11255ad92cb95db553eab0625face7b2dacf86b512",
      "status": "document claim"
    },
    {
      "id": "FM-E2",
      "source": "ARCHITECTURE.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "71200a9f2c7b51e48bfaacb2d4669679df325f80b45811d5a19383169d67ed03",
      "status": "document claim"
    },
    {
      "id": "FM-E3",
      "source": "SECURITY.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "ba2039e2e7ace97faf9b16afbda26b5916e340172f103f9307d7d0b70bbb8eed",
      "status": "document claim"
    },
    {
      "id": "FM-E4",
      "source": "DESIGN.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "7374ae7dc0cd24dd0b45bef293203b737bc172ea3b743adb05e4bfee86e06b24",
      "status": "document claim"
    }
  ],
  "methods": [
    {
      "id": "FM-M1",
      "name": "FMEA",
      "rating_method": "Not supplied; no numeric scores, rankings or residual-risk claims.",
      "interactions": "Workspace mutation and restoration can affect verification evidence and publication; run state and immutable evidence are common controls. API evidence feeds policy but cannot grant authority."
    }
  ],
  "threats": [
    {
      "id": "FM-T1",
      "title": "Untrusted output is interpreted as presentation instructions",
      "cause": "Names/results contain formatting or control bytes and representation is undefined",
      "local_effect": "Misleading terminal or Markdown evidence",
      "downstream_effect": "Maintainer relies on incorrect appearance",
      "affected_ids": [
        "FM-A1"
      ],
      "control_ids": [
        "FM-C1"
      ],
      "risk_ids": [
        "FM-R1"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Define reversible inert representation without truncation."
    },
    {
      "id": "FM-T2",
      "title": "Restoration does not restore all affected roots",
      "cause": "Checkpoint scope and cross-root rollback are undefined",
      "local_effect": "Mixed passing and rejected candidate state",
      "downstream_effect": "Later verification/publication binds to unintended changes",
      "affected_ids": [
        "FM-A2"
      ],
      "control_ids": [
        "FM-C2"
      ],
      "risk_ids": [
        "FM-R2"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Bind rollback to complete candidate scope and reverify before continuing."
    },
    {
      "id": "FM-T3",
      "title": "Uncertain dynamic usage is classified unused",
      "cause": "Usage investigation evidence is incomplete",
      "local_effect": "Necessary dependency removed",
      "downstream_effect": "Behavior or compatibility regresses",
      "affected_ids": [
        "FM-A3"
      ],
      "control_ids": [
        "FM-C3"
      ],
      "risk_ids": [
        "FM-R3"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Retain uncertain dependencies and require all usage evidence."
    },
    {
      "id": "FM-T4",
      "title": "Project execution exceeds intended filesystem boundary",
      "cause": "Path/process isolation semantics unresolved",
      "local_effect": "Project effects extend outside working copy",
      "downstream_effect": "Operator data or run evidence affected",
      "affected_ids": [
        "FM-A4"
      ],
      "control_ids": [
        "FM-C4"
      ],
      "risk_ids": [
        "FM-R4"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Specify and test process/filesystem containment before execution."
    },
    {
      "id": "FM-T5",
      "title": "Recorded PASS is stale relative to final revision",
      "cause": "Mutation between check capture and publication is not explicitly bound",
      "local_effect": "Observation describes different content",
      "downstream_effect": "Unverified revision published",
      "affected_ids": [
        "FM-A5"
      ],
      "control_ids": [
        "FM-C5"
      ],
      "risk_ids": [
        "FM-R5"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Bind checks and publication to immutable revision and reject unexpected mutation."
    },
    {
      "id": "FM-T6",
      "title": "Publication retry duplicates PR or reports false success",
      "cause": "Partial remote completion without a reconciled receipt",
      "local_effect": "Local and GitHub state diverge",
      "downstream_effect": "One-PR invariant or truthful outcome violated",
      "affected_ids": [
        "FM-A6"
      ],
      "control_ids": [
        "FM-C6"
      ],
      "risk_ids": [
        "FM-R6"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Reconcile remote state with stable run identity before retry."
    },
    {
      "id": "FM-T7",
      "title": "Unavailable or malformed analysis is treated as usable evidence",
      "cause": "API contract and failure semantics unresolved",
      "local_effect": "Incomplete or invalid candidate evidence",
      "downstream_effect": "Incorrect decisions or blocked lifecycle",
      "affected_ids": [
        "FM-A7"
      ],
      "control_ids": [
        "FM-C7"
      ],
      "risk_ids": [
        "FM-R7"
      ],
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3",
        "FM-E4"
      ],
      "assumptions": [
        "Potential design failure mode; no observed failure or defect claimed."
      ],
      "proposed_treatment": "Validate contract and fail affected analysis closed; never convert unavailability into success."
    }
  ],
  "controls": [
    {
      "id": "FM-C1",
      "name": "SC-011; OD-008",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    },
    {
      "id": "FM-C2",
      "name": "SC-003; AQ-6",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    },
    {
      "id": "FM-C3",
      "name": "SC-004; FR-1.7\u2013FR-1.9",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    },
    {
      "id": "FM-C4",
      "name": "SC-008; OD-005",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    },
    {
      "id": "FM-C5",
      "name": "SC-003; DR-5; DR-6",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    },
    {
      "id": "FM-C6",
      "name": "SC-010; OD-007",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    },
    {
      "id": "FM-C7",
      "name": "SC-001; SC-007; AQ-2",
      "status": "Documented requirements and/or blocked decisions only; no effectiveness evidence",
      "evidence_ids": [
        "FM-E1",
        "FM-E2",
        "FM-E3"
      ]
    }
  ],
  "requirements": [],
  "risks": [
    {
      "id": "FM-R1",
      "threat_id": "FM-T1",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    },
    {
      "id": "FM-R2",
      "threat_id": "FM-T2",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    },
    {
      "id": "FM-R3",
      "threat_id": "FM-T3",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    },
    {
      "id": "FM-R4",
      "threat_id": "FM-T4",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    },
    {
      "id": "FM-R5",
      "threat_id": "FM-T5",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    },
    {
      "id": "FM-R6",
      "threat_id": "FM-T6",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    },
    {
      "id": "FM-R7",
      "threat_id": "FM-T7",
      "status": "Unranked",
      "method_id": "FM-M1",
      "likelihood": null,
      "impact": null,
      "residual_risk": null
    }
  ],
  "attack_trees": [],
  "attack_paths": [],
  "visualizations": [],
  "coverage": [
    {
      "id": "FM-COV1",
      "subject_id": "FM-A1",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T1"
      ]
    },
    {
      "id": "FM-COV2",
      "subject_id": "FM-A2",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T2"
      ]
    },
    {
      "id": "FM-COV3",
      "subject_id": "FM-A3",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T3"
      ]
    },
    {
      "id": "FM-COV4",
      "subject_id": "FM-A4",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T4"
      ]
    },
    {
      "id": "FM-COV5",
      "subject_id": "FM-A5",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T5"
      ]
    },
    {
      "id": "FM-COV6",
      "subject_id": "FM-A6",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T6"
      ]
    },
    {
      "id": "FM-COV7",
      "subject_id": "FM-A7",
      "disposition": "Assessed",
      "threat_ids": [
        "FM-T7"
      ]
    }
  ],
  "conflicts": [
    {
      "id": "FM-X1",
      "description": "Exact reporting and safe rendering/disclosure are not reconciled in input decisions.",
      "evidence_ids": [
        "FM-E3",
        "FM-E4"
      ]
    }
  ],
  "gaps": [
    {
      "id": "FM-G1",
      "description": "No implementation, control tests, operational history or approved risk-rating method supplied.",
      "evidence_ids": [
        "FM-E2",
        "FM-E3"
      ]
    }
  ],
  "system": {
    "assets": [
      {
        "id": "FM-A1",
        "name": "CLI and report presentation",
        "evidence_ids": [
          "FM-E2"
        ]
      },
      {
        "id": "FM-A2",
        "name": "Run coordinator",
        "evidence_ids": [
          "FM-E2"
        ]
      },
      {
        "id": "FM-A3",
        "name": "Dependency policy and evidence core",
        "evidence_ids": [
          "FM-E2"
        ]
      },
      {
        "id": "FM-A4",
        "name": "Workspace and ecosystem adapters",
        "evidence_ids": [
          "FM-E2"
        ]
      },
      {
        "id": "FM-A5",
        "name": "Verification execution",
        "evidence_ids": [
          "FM-E2"
        ]
      },
      {
        "id": "FM-A6",
        "name": "GitHub integration",
        "evidence_ids": [
          "FM-E2"
        ]
      },
      {
        "id": "FM-A7",
        "name": "Intelligence API and CLI adapter",
        "evidence_ids": [
          "FM-E2"
        ]
      }
    ],
    "actors": [],
    "data": [],
    "zones": [],
    "boundaries": [],
    "flows": [],
    "entry_points": []
  }
}
```

## Summary

Scope: all seven documented component responsibilities, using all four specifications. All failure modes are conditional; there is no incident or implementation evidence.

| Function | Failure mode | Downstream effect | Planned treatment |
| --- | --- | --- | --- |
| CLI and report presentation | Untrusted output is interpreted as presentation instructions | Maintainer relies on incorrect appearance | Define reversible inert representation without truncation. |
| Run coordinator | Restoration does not restore all affected roots | Later verification/publication binds to unintended changes | Bind rollback to complete candidate scope and reverify before continuing. |
| Dependency policy and evidence core | Uncertain dynamic usage is classified unused | Behavior or compatibility regresses | Retain uncertain dependencies and require all usage evidence. |
| Workspace and ecosystem adapters | Project execution exceeds intended filesystem boundary | Operator data or run evidence affected | Specify and test process/filesystem containment before execution. |
| Verification execution | Recorded PASS is stale relative to final revision | Unverified revision published | Bind checks and publication to immutable revision and reject unexpected mutation. |
| GitHub integration | Publication retry duplicates PR or reports false success | One-PR invariant or truthful outcome violated | Reconcile remote state with stable run identity before retry. |
| Intelligence API and CLI adapter | Unavailable or malformed analysis is treated as usable evidence | Incorrect decisions or blocked lifecycle | Validate contract and fail affected analysis closed; never convert unavailability into success. |

Workspace mutation and restoration can cascade into verification and publication; immutable evidence and coordinator state are common controls. API evidence cannot grant authority. Controls are normative or blocked decisions, never verified effective. No comparable priorities, severity scales, RPN, target ratings or residual-risk results exist. Exact reporting versus safe disclosure/rendering remains unresolved.
