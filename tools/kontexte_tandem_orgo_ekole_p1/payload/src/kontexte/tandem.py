"""Export of synthetic design intent to Ekole P1's closed teacher-preview format.

Orgo owns all operational transitions; this module has no runtime or network port.
"""
from __future__ import annotations

import re
from uuid import UUID

from .common import KontexteError

FORMAT = 'ekole.tandem-teacher-preview/1.0'
REF = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9_-]{1,63}\Z')


def _uuid(raw: str, field: str) -> str:
    if not isinstance(raw, str):
        raise KontexteError(f'{field}: UUID obligatoire')
    try:
        val = UUID(raw)
    except (ValueError, AttributeError):
        raise KontexteError(f'{field}: UUID invalide') from None
    if val.int == 0 or str(val) != raw.lower():
        raise KontexteError(f'{field}: UUID non canonique')
    return str(val)


def _ref(raw: str, field: str) -> str:
    if not isinstance(raw, str) or not REF.fullmatch(raw):
        raise KontexteError(f'{field}: référence non conforme au contrat Ekole P1')
    return raw


def build_teacher_preview(mission: dict, *, tenant_id: str, world_id: str,
                          world_release_id: str, workflow_ref: str) -> dict:
    """Return a *synthetic* teacher-only preview, never an Orgo-issued Task view.

    The references supplied here are caller-declared design labels; no database,
    ownership, identity or active WorldRelease is verified by this exporter.
    """
    if not isinstance(mission, dict) or mission.get('format') != 'kontexte.mission/1' or mission.get('synthetic') is not True:
        raise KontexteError('Mission synthétique Kontexte requise')
    safety=mission.get('safety')
    if safety is not None and (not isinstance(safety,dict) or safety.get('real_spending') is not False
                               or safety.get('real_taxes') is not False
                               or safety.get('publication_default') != 'private'):
        raise KontexteError('Précautions financières et médias non satisfaites')
    if not isinstance(mission.get('steps'),list) or not 1<=len(mission['steps'])<=50:
        raise KontexteError('1 à 50 étapes de conception requises')
    scenario_ref=_ref(mission.get('id'),'mission.id')
    ids=set(); tasks=[]
    for step in mission['steps']:
        if not isinstance(step,dict) or not isinstance(step.get('depends_on'),list):
            raise KontexteError('Étape ou dépendances invalides')
        sid=_ref(step.get('id'),'step.id')
        role=_ref(step.get('role'),'step.role')
        if sid in ids or role not in mission.get('roles',[]):
            raise KontexteError('Étape dupliquée ou rôle absent')
        if any(not isinstance(dep,str) or dep not in ids for dep in step['depends_on']):
            raise KontexteError('Dépendance cyclique, future ou invalide')
        ids.add(sid)
        # This is an illustrative initial state, NOT an Orgo transition or grant.
        tasks.append({'task_ref':sid, 'role_code':role,
                      'state':'waiting' if step['depends_on'] else 'ready',
                      'fragment_refs':[]})
    return {
        'format':FORMAT, 'mode':'synthetic', 'authority':'orgo',
        'tenant_id':_uuid(tenant_id,'tenant_id'),
        'world_id':_uuid(world_id,'world_id'),
        'world_release_id':_uuid(world_release_id,'world_release_id'),
        'scenario_ref':scenario_ref, 'workflow_ref':_ref(workflow_ref,'workflow_ref'),
        'tasks':tasks,
    }
