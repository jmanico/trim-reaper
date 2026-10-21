# Threat-model pipeline artifacts

The numbered artifacts preserve the complete pre-implementation pipeline run against specification baseline `32a2bb4f2d46915a51a424ec6610a979d55d6b24`. The source instructions are `/Users/jmanico/Dropbox/github/aegis/security-utilities-knowledge/content/pipelines/threat-modeling/README.md` and its numbered agents 00–11.

- Stages 00–07 independently analyze all four baseline specifications; 06 also inventories the checkout and records that no implementation exists.
- Stage 08 consumes every fragment, preserves methodology-specific findings, and assigns stable T-001–T-020 IDs.
- Stage 09 adds renderer-neutral diagram specifications. Stage 10 adds accessible figure briefs without claiming a render occurred.
- Stage 11 consumes stage 10 and writes [THREAT_MODEL.md](../THREAT_MODEL.md), including its unchanged model in Appendix A.

The root specifications contain subsequent user-authorized design decisions and threat-linked hardening. They do not retroactively change the intake evidence. Original conflicts and evidence gaps remain in the baseline model; new decisions specify mitigations but do not establish control effectiveness. The report records this distinction. Repeated findings from the same four documents are not independent corroboration, and no risk score was invented.

Run `python3 scripts/validate_threat_model.py` from the repository root to check artifact completeness, semantic-model preservation, stable threat IDs, report anchors and specification links. This validates documentation consistency, not application security.
