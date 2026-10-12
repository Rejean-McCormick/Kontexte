# Contributing to Kontexte

Kontexte is an experimental repository. **Licensing and third-party contribution terms have not yet been finalized.** Contact the rights holders before submitting work intended for public reuse; read [LICENSE-POLICY.md](LICENSE-POLICY.md).

1. **Roles:** Add one JSON file under `data/roles/`, following `schemas/role.v1.schema.json`. CSS themes are restricted to the renderer's allowlist; role labels must not grant authenticated permissions.
2. **Missions:** Add validated `data/missions/` records. Dependencies must refer to earlier steps, role IDs must exist, and every internal Ekole curriculum reference must be resolvable.
3. **Neutral scenarios:** Describe the problem, key actors, missing information, tension, actions, and outcome without baking in culture-specific assumptions or a single grade.
4. **Localizations:** Build overlays keyed to parent identifiers and checksums. Preserve the neutral problem; review historical and cultural assumptions with appropriate expertise.
5. **Adaptation:** Provide alternate support and participation paths without storing public health labels or diagnoses. Record supports received in authorized educational evidence.
6. **Translation:** Have language variants reviewed. An `en` string or a fallback does not imply validated translation or an approved SemantiK realization.
7. **Safety:** Use only synthetic participant IDs and authorized media. Never commit actual children's photos, identifying records, hidden information intended for other participants, or educator answer keys to student distributions.
8. **Integration:** Keep operational transitions in **Orgo**, not Kontexte. Propose missing primitives in Orgo instead of implementing a second workflow engine here.
9. **Checks:** Run the commands below and seek appropriate human pedagogical and security review before deployment.

```bash
PYTHONPATH=src python -m kontexte validate
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m kontexte site --out /tmp/kontexte-site
```

The source repository also includes `tools/qualify.sh` and `tools/qualify.ps1` for local checks. See the [Development and Testing Wiki](wiki/Development-and-Testing.md).
