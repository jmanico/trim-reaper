# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": [
    {
      "id": "AI-S1",
      "description": "Pre-implementation review of all four complete specifications; documented controls are planned, not implemented; no code analyzed."
    }
  ],
  "evidence": [
    {
      "id": "AI-E1",
      "source": "REQUIREMENTS.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "7a67569359d528a629f70b11255ad92cb95db553eab0625face7b2dacf86b512",
      "status": "document claim"
    },
    {
      "id": "AI-E2",
      "source": "ARCHITECTURE.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "71200a9f2c7b51e48bfaacb2d4669679df325f80b45811d5a19383169d67ed03",
      "status": "document claim"
    },
    {
      "id": "AI-E3",
      "source": "SECURITY.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "ba2039e2e7ace97faf9b16afbda26b5916e340172f103f9307d7d0b70bbb8eed",
      "status": "document claim"
    },
    {
      "id": "AI-E4",
      "source": "DESIGN.md",
      "locator": "Complete file, pre-hardening input",
      "sha256": "7374ae7dc0cd24dd0b45bef293203b737bc172ea3b743adb05e4bfee86e06b24",
      "status": "document claim"
    }
  ],
  "methods": [
    {
      "id": "AI-M1",
      "name": "AI/ML lifecycle applicability",
      "rating_method": "Not supplied; no numeric scores, rankings or residual-risk claims."
    },
    {
      "id": "AI-M2",
      "name": "MITRE ATLAS",
      "release": "v2026.09",
      "source": "https://github.com/mitre-atlas/atlas-data/releases/tag/v2026.09",
      "status": "Release identity verified; technique-level mapping Not applicable to documented non-AI lifecycle; no identifiers emitted."
    },
    {
      "id": "AI-M3",
      "name": "OWASP Machine Learning Security Top Ten",
      "release": "Unversioned draft project landing page checked 2026-10-21; numbered draft revision unverified",
      "source": "https://owasp.org/projects/machine-learning-security-top-ten",
      "status": "Applicability checked; individual checklist entries unverified; no identifiers emitted."
    },
    {
      "id": "AI-M4",
      "name": "OWASP GenAI LLM Top 10",
      "release": null,
      "status": "Not applicable: no evidenced LLM, retrieval, agent or tool-calling lifecycle; no edition claimed checked."
    }
  ],
  "threats": [],
  "controls": [
    {
      "id": "AI-C1",
      "name": "Local policy remains authoritative over API suggestions",
      "status": "Planned normative control; not implemented",
      "evidence_ids": [
        "AI-E2",
        "AI-E3"
      ],
      "locator": "ARCHITECTURE.md DR-4, DR-7; SECURITY.md SC-001"
    }
  ],
  "requirements": [],
  "risks": [],
  "attack_trees": [],
  "attack_paths": [],
  "visualizations": [],
  "coverage": [
    {
      "id": "AI-COV1",
      "phase": "Data sourcing/preparation",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV2",
      "phase": "Training/adaptation",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV3",
      "phase": "Model evaluation",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV4",
      "phase": "Model artifact storage",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV5",
      "phase": "Model deployment",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV6",
      "phase": "Inference",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV7",
      "phase": "AI monitoring",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV8",
      "phase": "Feedback learning",
      "disposition": "Not applicable to evidenced scope; unknown whether future implementation adds AI",
      "evidence_ids": [
        "AI-E1",
        "AI-E2",
        "AI-E3",
        "AI-E4"
      ]
    },
    {
      "id": "AI-COV9",
      "method_id": "AI-M2",
      "disposition": "Not applicable",
      "rationale": "Intelligence API label does not establish AI, ML, LLM, retrieval, agents, training or model artifacts."
    },
    {
      "id": "AI-COV10",
      "method_id": "AI-M3",
      "disposition": "Not applicable",
      "rationale": "Intelligence API label does not establish AI, ML, LLM, retrieval, agents, training or model artifacts."
    },
    {
      "id": "AI-COV11",
      "method_id": "AI-M4",
      "disposition": "Not applicable",
      "rationale": "Intelligence API label does not establish AI, ML, LLM, retrieval, agents, training or model artifacts."
    }
  ],
  "conflicts": [],
  "gaps": [
    {
      "id": "AI-G1",
      "description": "No implementation, control tests, operational history or approved risk-rating method supplied.",
      "evidence_ids": [
        "AI-E2",
        "AI-E3"
      ]
    },
    {
      "id": "AI-G2",
      "description": "Analysis engine/provider unspecified; no requirement authorizes an external model provider. Reassess lifecycle if AI is introduced.",
      "evidence_ids": [
        "AI-E2"
      ],
      "locator": "AQ-2"
    },
    {
      "id": "AI-G3",
      "description": "OWASP ML numbered draft edition and item-level checklist unverified; only official project page confirming draft status checked. No taxonomy claims derived."
    }
  ],
  "system": {
    "assets": [
      {
        "id": "AI-A1",
        "name": "Intelligence API suggestions",
        "status": "Proposed service responsibilities, not evidence of AI/ML",
        "evidence_ids": [
          "AI-E2"
        ]
      }
    ],
    "actors": [],
    "data": [],
    "zones": [],
    "boundaries": [
      {
        "id": "AI-B1",
        "name": "Local CLI to proposed intelligence service",
        "evidence_ids": [
          "AI-E2"
        ]
      }
    ],
    "flows": [
      {
        "id": "AI-F1",
        "description": "Proposed agreed analysis inputs to service; candidate suggestions and supporting evidence return to local policy",
        "boundary_id": "AI-B1",
        "affected_ids": [
          "AI-A1"
        ],
        "evidence_ids": [
          "AI-E2"
        ]
      }
    ],
    "entry_points": []
  }
}
```

## Summary

Scope: all four complete specifications. No AI/ML implementation or lifecycle is established. The intelligence API supplies proposed analysis suggestions; its name does not prove model inference or an external provider.

| Lifecycle area | Disposition |
| --- | --- |
| Data sourcing/preparation; training/adaptation; evaluation; model artifacts | Not applicable to evidenced scope; future implementation unknown |
| Model deployment; inference; monitoring; feedback learning | Not applicable to evidenced scope; future implementation unknown |

The proposed CLI-to-service boundary exchanges agreed analysis inputs and suggestions; local policy retains authority (planned, not implemented). No AI-specific threat, attack path, risk rating, or conflict is evidenced.

| Checklist | Disposition and provenance |
| --- | --- |
| MITRE ATLAS | Not applicable to documented lifecycle; [v2026.09 release](https://github.com/mitre-atlas/atlas-data/releases/tag/v2026.09) verified; no technique identifiers emitted |
| OWASP ML | Not applicable; [official draft project page](https://owasp.org/projects/machine-learning-security-top-ten) checked 2026-10-21; numbered edition and individual items unverified |
| OWASP GenAI LLM | Not applicable; no LLM, retrieval or agent behavior established; no edition claimed checked |

Engine/provider and any future AI lifecycle remain evidence gaps. There are no operational or control-effectiveness results; reassess if AI is introduced.
