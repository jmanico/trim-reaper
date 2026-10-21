#!/usr/bin/env python3
"""Validate the checked-in pipeline artifacts without external dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYS = {'scope', 'evidence', 'system', 'methods', 'threats', 'controls',
        'requirements', 'risks', 'attack_trees', 'attack_paths',
        'visualizations', 'coverage', 'conflicts', 'gaps'}
SYSTEM = {'assets', 'actors', 'data', 'zones', 'boundaries', 'flows', 'entry_points'}

def model(path):
    text = path.read_text()
    blocks = re.findall(r'```json\s*\n(.*?)\n```', text, re.S)
    candidates = [json.loads(block) for block in blocks]
    found = [value for value in candidates if isinstance(value, dict) and KEYS <= value.keys()]
    assert len(found) == 1, f'{path}: expected exactly one full model'
    value = found[0]
    assert SYSTEM <= value['system'].keys(), f'{path}: missing system collections'
    return value

paths = sorted((ROOT / 'threat-model').glob('[0-9][0-9]-*.md'))
assert len(paths) == 11, 'Expected stage artifacts 00 through 10'
assert [p.name[:2] for p in paths] == [f'{i:02}' for i in range(11)]
models = [model(p) for p in paths]
unified, diagrams, visuals = models[8:]
report_path = ROOT / 'THREAT_MODEL.md'
report = model(report_path)
assert report == visuals, 'Appendix A differs from stage 10 model'
for downstream in (diagrams, visuals):
    assert {k: v for k, v in downstream.items() if k != 'visualizations'} == {
        k: v for k, v in unified.items() if k != 'visualizations'
    }, 'Visualization stage modified semantic model'
assert diagrams['visualizations'][:len(unified['visualizations'])] == unified['visualizations']
assert visuals['visualizations'][:len(diagrams['visualizations'])] == diagrams['visualizations']
ids = [t['id'] for t in unified['threats']]
assert len(ids) == len(set(ids))
assert all(re.fullmatch(r'T-\d{3}', value) for value in ids)
report_text = report_path.read_text()
for threat_id in ids:
    assert f'<a id="{threat_id.lower()}"></a>' in report_text, f'Missing anchor {threat_id}'
for name in ('REQUIREMENTS.md', 'ARCHITECTURE.md', 'SECURITY.md', 'DESIGN.md'):
    text = (ROOT / name).read_text()
    assert '[THREAT:' not in text, f'{name}: unresolved threat placeholder'
    assert 'TO BE DECIDED' not in text, f'{name}: unresolved decision placeholder'
    for threat_id in re.findall(r'\[(T-\d{3})\]\(THREAT_MODEL.md#t-\d{3}\)', text):
        assert threat_id in ids, f'{name}: unknown threat {threat_id}'
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            assert (ROOT / target.split('#')[0]).exists(), f'{name}: missing file {target}'
for name, pattern in [('REQUIREMENTS.md', r'\*\*((?:FR|NFR)-\d+\.\d+)\*\*'),
                      ('SECURITY.md', r'\*\*(SC-\d{3}) —'),
                      ('ARCHITECTURE.md', r'\*\*(AQ-\d+) —')]:
    values = re.findall(pattern, (ROOT / name).read_text())
    assert len(values) == len(set(values)), f'{name}: duplicate IDs'
print(f'Validated stages 00–11, {len(ids)} stable threats, model preservation, IDs and specification links.')
