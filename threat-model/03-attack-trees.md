# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": [
    {
      "id": "AT-S1",
      "description": "Pre-implementation review of all four complete specifications; documented controls are planned, not implemented; no code analyzed."
    }
  ],
  "evidence": [
    {
      "id": "AT-E1",
      "source": "REQUIREMENTS.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "7a67569359d528a629f70b11255ad92cb95db553eab0625face7b2dacf86b512",
      "status": "document claim"
    },
    {
      "id": "AT-E2",
      "source": "ARCHITECTURE.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "71200a9f2c7b51e48bfaacb2d4669679df325f80b45811d5a19383169d67ed03",
      "status": "document claim"
    },
    {
      "id": "AT-E3",
      "source": "SECURITY.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "ba2039e2e7ace97faf9b16afbda26b5916e340172f103f9307d7d0b70bbb8eed",
      "status": "document claim"
    },
    {
      "id": "AT-E4",
      "source": "DESIGN.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "7374ae7dc0cd24dd0b45bef293203b737bc172ea3b743adb05e4bfee86e06b24",
      "status": "document claim"
    }
  ],
  "methods": [
    {
      "id": "AT-M1",
      "name": "Attack trees",
      "rating_method": "Not supplied; no numeric scores, rankings or residual-risk claims."
    }
  ],
  "threats": [
    {
      "id": "AT-T1",
      "title": "Run project-controlled operations outside the intended execution boundary",
      "status": "Conditional design threat, not demonstrated vulnerability",
      "affected_ids": [
        "AT-A1"
      ],
      "evidence_ids": [
        "AT-E1",
        "AT-E2",
        "AT-E3",
        "AT-E4"
      ],
      "locator": "ARCHITECTURE.md Component and Trust Boundaries; SECURITY.md OD-005",
      "control_ids": [
        "AT-C1"
      ],
      "attack_tree_ids": [
        "AT-TREE1"
      ],
      "assumptions": [
        "Adversarial control of supplied project content or output; success depends on a control failure not evidenced by implementation."
      ]
    },
    {
      "id": "AT-T2",
      "title": "Publish changes not covered by authoritative verification",
      "status": "Conditional design threat, not demonstrated vulnerability",
      "affected_ids": [
        "AT-A2"
      ],
      "evidence_ids": [
        "AT-E1",
        "AT-E2",
        "AT-E3",
        "AT-E4"
      ],
      "locator": "ARCHITECTURE.md DR-4\u2013DR-6; REQUIREMENTS.md FR-9.1\u2013FR-9.4",
      "control_ids": [
        "AT-C2"
      ],
      "attack_tree_ids": [
        "AT-TREE2"
      ],
      "assumptions": [
        "Adversarial control of supplied project content or output; success depends on a control failure not evidenced by implementation."
      ]
    },
    {
      "id": "AT-T3",
      "title": "Misrepresent results through rendered untrusted content",
      "status": "Conditional design threat, not demonstrated vulnerability",
      "affected_ids": [
        "AT-A3"
      ],
      "evidence_ids": [
        "AT-E1",
        "AT-E2",
        "AT-E3",
        "AT-E4"
      ],
      "locator": "DESIGN.md Typography and Components; SECURITY.md OD-008",
      "control_ids": [
        "AT-C3"
      ],
      "attack_tree_ids": [
        "AT-TREE3"
      ],
      "assumptions": [
        "Adversarial control of supplied project content or output; success depends on a control failure not evidenced by implementation."
      ]
    }
  ],
  "controls": [
    {
      "id": "AT-C1",
      "name": "Execution and filesystem containment unresolved",
      "locator": "SC-008 / OD-005",
      "status": "BLOCKED specification decision",
      "evidence_ids": [
        "AT-E3"
      ]
    },
    {
      "id": "AT-C2",
      "name": "Coordinator, policy and publication authority",
      "locator": "SC-001\u2013SC-003 / DR-4\u2013DR-6",
      "status": "ACTIVE normative requirement; unimplemented",
      "evidence_ids": [
        "AT-E3"
      ]
    },
    {
      "id": "AT-C3",
      "name": "Safe terminal and Markdown representation unresolved",
      "locator": "SC-011 / OD-008",
      "status": "BLOCKED specification decision",
      "evidence_ids": [
        "AT-E3"
      ]
    }
  ],
  "requirements": [],
  "risks": [],
  "attack_trees": [
    {
      "id": "AT-TREE1",
      "root_id": "AT-N10",
      "threat_id": "AT-T1",
      "nodes": [
        {
          "id": "AT-N10",
          "label": "Run project-controlled operations outside the intended execution boundary",
          "operator": "AND",
          "child_ids": [
            "AT-N11",
            "AT-N12"
          ],
          "affected_ids": [
            "AT-A1"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [
            "AT-C1"
          ],
          "assumptions": []
        },
        {
          "id": "AT-N11",
          "label": "Project commands execute through verification or ecosystem tools",
          "operator": null,
          "child_ids": [],
          "affected_ids": [
            "AT-A1"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [],
          "assumptions": []
        },
        {
          "id": "AT-N12",
          "label": "Execution can reach resources outside the intended workspace",
          "operator": null,
          "child_ids": [],
          "affected_ids": [
            "AT-A1"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [
            "AT-C1"
          ],
          "assumptions": [
            "Conditional failure; not established to occur."
          ]
        }
      ]
    },
    {
      "id": "AT-TREE2",
      "root_id": "AT-N20",
      "threat_id": "AT-T2",
      "nodes": [
        {
          "id": "AT-N20",
          "label": "Publish changes not covered by authoritative verification",
          "operator": "AND",
          "child_ids": [
            "AT-N21",
            "AT-N22"
          ],
          "affected_ids": [
            "AT-A2"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [
            "AT-C2"
          ],
          "assumptions": []
        },
        {
          "id": "AT-N21",
          "label": "Repository, tool or API evidence reaches acceptance logic",
          "operator": null,
          "child_ids": [],
          "affected_ids": [
            "AT-A2"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [],
          "assumptions": []
        },
        {
          "id": "AT-N22",
          "label": "Untrusted evidence or a changed revision is accepted as publication authority",
          "operator": null,
          "child_ids": [],
          "affected_ids": [
            "AT-A2"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [
            "AT-C2"
          ],
          "assumptions": [
            "Conditional failure; not established to occur."
          ]
        }
      ]
    },
    {
      "id": "AT-TREE3",
      "root_id": "AT-N30",
      "threat_id": "AT-T3",
      "nodes": [
        {
          "id": "AT-N30",
          "label": "Misrepresent results through rendered untrusted content",
          "operator": "AND",
          "child_ids": [
            "AT-N31",
            "AT-N32"
          ],
          "affected_ids": [
            "AT-A3"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [
            "AT-C3"
          ],
          "assumptions": []
        },
        {
          "id": "AT-N31",
          "label": "Untrusted names or command output reach reports",
          "operator": null,
          "child_ids": [],
          "affected_ids": [
            "AT-A3"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [],
          "assumptions": []
        },
        {
          "id": "AT-N32",
          "label": "Renderer interprets those bytes as terminal controls or Markdown structure",
          "operator": null,
          "child_ids": [],
          "affected_ids": [
            "AT-A3"
          ],
          "evidence_ids": [
            "AT-E1",
            "AT-E2",
            "AT-E3",
            "AT-E4"
          ],
          "control_ids": [
            "AT-C3"
          ],
          "assumptions": [
            "Conditional failure; not established to occur."
          ]
        }
      ]
    }
  ],
  "attack_paths": [
    {
      "id": "AT-P1",
      "tree_id": "AT-TREE1",
      "node_ids": [
        "AT-N10",
        "AT-N11",
        "AT-N12"
      ],
      "status": "Logically sufficient only if both prerequisites hold; feasibility unverified",
      "evidence_ids": [
        "AT-E1",
        "AT-E2",
        "AT-E3",
        "AT-E4"
      ],
      "comparison": "Unranked; no method supplied"
    },
    {
      "id": "AT-P2",
      "tree_id": "AT-TREE2",
      "node_ids": [
        "AT-N20",
        "AT-N21",
        "AT-N22"
      ],
      "status": "Logically sufficient only if both prerequisites hold; feasibility unverified",
      "evidence_ids": [
        "AT-E1",
        "AT-E2",
        "AT-E3",
        "AT-E4"
      ],
      "comparison": "Unranked; no method supplied"
    },
    {
      "id": "AT-P3",
      "tree_id": "AT-TREE3",
      "node_ids": [
        "AT-N30",
        "AT-N31",
        "AT-N32"
      ],
      "status": "Logically sufficient only if both prerequisites hold; feasibility unverified",
      "evidence_ids": [
        "AT-E1",
        "AT-E2",
        "AT-E3",
        "AT-E4"
      ],
      "comparison": "Unranked; no method supplied"
    }
  ],
  "visualizations": [],
  "coverage": [
    {
      "id": "AT-COV1",
      "subject_id": "AT-TREE1",
      "disposition": "Assessed",
      "detail": "All nodes reachable; child references resolve. No shared node across trees; controls are mapped to exact addressed condition."
    },
    {
      "id": "AT-COV2",
      "subject_id": "AT-TREE2",
      "disposition": "Assessed",
      "detail": "All nodes reachable; child references resolve. No shared node across trees; controls are mapped to exact addressed condition."
    },
    {
      "id": "AT-COV3",
      "subject_id": "AT-TREE3",
      "disposition": "Assessed",
      "detail": "All nodes reachable; child references resolve. No shared node across trees; controls are mapped to exact addressed condition."
    }
  ],
  "conflicts": [
    {
      "id": "AT-X1",
      "description": "Exact untruncated names/results versus rendering and disclosure protections has no resolved representation in input documents.",
      "evidence_ids": [
        "AT-E3",
        "AT-E4"
      ]
    }
  ],
  "gaps": [
    {
      "id": "AT-G1",
      "description": "No implementation, control tests, operational history or approved risk-rating method supplied.",
      "evidence_ids": [
        "AT-E2",
        "AT-E3"
      ]
    }
  ],
  "system": {
    "assets": [
      {
        "id": "AT-A1",
        "name": "Operator environment and credentials",
        "evidence_ids": [
          "AT-E1",
          "AT-E2"
        ]
      },
      {
        "id": "AT-A2",
        "name": "Verified repository changes",
        "evidence_ids": [
          "AT-E1",
          "AT-E2"
        ]
      },
      {
        "id": "AT-A3",
        "name": "Report integrity",
        "evidence_ids": [
          "AT-E1",
          "AT-E2"
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

Scope: all four specifications. These are conditional design paths, not demonstrated exploits. No cost, likelihood, skill or impact ranking is available.

```text
AT-T1: Escape intended execution boundary [AND]
  AT-N11: Project commands execute
  AT-N12: Execution can reach outside intended workspace (conditional)
AT-T2: Publish unverified changes [AND]
  AT-N21: Untrusted evidence enters acceptance logic
  AT-N22: Evidence or changed revision becomes authority (conditional)
AT-T3: Misrepresent report [AND]
  AT-N31: Untrusted bytes enter report
  AT-N32: Bytes become terminal controls/Markdown structure (conditional)
```

Each path requires both leaves. No successful path is demonstrated. The coordinator and core are shared defensive responsibilities, but no identical attack step is duplicated across trees. Execution and rendering rules are blocked in the input; authority gates are normative and unimplemented. Exact reporting versus safe representation remains a conflict. No implementation, effectiveness evidence, or comparison method was supplied.
