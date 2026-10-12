# Annexe — contrats proposés et exemples

Ces contrats sont de **nouvelles propositions de design**, pas des composants actifs de l'Ekole actuel ni des opérations autorisées dans Orgo. Tous les exemples sont fictifs.

| Contrat | Ce qu'il décrit |
| --- | --- |
| `EKOLE_ROLE_FRAME_V1.schema.json` | identité et actions d'un rôle pédagogique, présentation neutre possible |
| `EKOLE_MISSION_FRAME_V1.schema.json` | scénario, étapes et fragments, liens Ekole candidats |
| `EKOLE_LEARNING_EVENT_V1.schema.json` | trace pseudonymisée d'activité ou de validation |
| `EKOLE_CURRICULUM_MAP_V1.schema.json` | correspondance révisable Ekole/mission/référentiel officiel |

Les fichiers `exemples/*.json` correspondent à ces quatre schémas. **Aucune référence officielle n'est fabriquée**; les identifiants `qc-pri-*` sont vérifiés contre le catalogue du snapshot.

## Valider les annexes après copie à la racine Ekole

```powershell
py -3 -m pip install jsonschema
py -3 -c "import json,pathlib,jsonschema; p=pathlib.Path('docs/UPGRADE_MISSIONS_INTERDISCIPLINAIRES_V1/annexes'); t=[('EKOLE_ROLE_FRAME_V1','role_sorciere'),('EKOLE_MISSION_FRAME_V1','mission_fete_sorciere'),('EKOLE_LEARNING_EVENT_V1','evidence_invitation'),('EKOLE_CURRICULUM_MAP_V1','curriculum_map_fete')]; [jsonschema.validate(json.loads((p/'exemples'/(b+'.json')).read_text(encoding='utf-8')),json.loads((p/'schemas'/(a+'.schema.json')).read_text(encoding='utf-8'))) for a,b in t]; print('JSON valides; revue pedagogique encore requise')"
```
