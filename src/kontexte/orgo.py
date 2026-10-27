"""Adaptation non destructive aux contrats vérifiés du snapshot Orgo (2026-10-11).

Orgo est propriétaire des Case/Task/Signal; ce module n'exécute aucun workflow.
"""
from __future__ import annotations
import hashlib
import json
import re
from .common import check


def slug(s: str) -> str:
    value = re.sub(r"[^a-z0-9_-]+", "_", s.lower()).strip("_")
    return value[:70] or "mission"

def scenario_fixture(mission: dict, *, label: str = "2.11") -> dict:
    """Fixture d'amorçage de mission avec une tâche de préparation, PAS le graphe d'exécution.

    La libération conditionnelle et la jointure des indices nécessitent des primitives Orgo
    supplémentaires. Les fragments ne sont jamais inclus dans un Signal ou une Task.
    """
    check(bool(re.fullmatch(r"[1-9]\d*\.[1-9][1-5](?:\.[A-Za-z0-9]+)*", label)), "label Orgo invalide")
    key = slug(mission["id"])
    sha = hashlib.sha256(json.dumps(mission, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:12]
    return {
        "schema_version": "orgo.scenario.v1",
        "scenario": {
            "id": f"kontexte_{key}_{sha}", "title": mission["title"]["fr-CA"],
            "description": "Amorçage de préparation d'une simulation pédagogique. Les étapes conditionnelles ne sont PAS installées par cette fixture.",
            "synthetic": True, "epistemic_status": "synthetic_demo_fixture",
            "correlation_id": f"kontexte.{key}.{sha}"
        },
        "operations": [
            {"op": "create_case", "ref": "case.main",
             "input": {"title": f"[SIMULATION] {mission['title']['fr-CA']}", "description": mission["fiction"]["fr-CA"],
                       "label": label, "severity": "MINOR", "visibility": "INTERNAL",
                       "metadata": {"synthetic": True, "epistemic_status": "synthetic_demo_fixture", "mission_id": mission["id"], "content_version": mission["version"], "source": "kontexte", "fixture_only": True}}},
            {"op": "create_task", "ref": "task.prepare", "case_ref": "case.main",
             "input": {"title": "Réviser la mission Kontexte avant activation", "description": "Inspecter rôles, enseignements, autorisations et sécurité; aucune tâche d'élève déclenchée automatiquement.",
                       "type": "scenario", "category": "request", "label": label, "priority": "LOW",
                       "metadata": {"synthetic": True, "mission_id": mission["id"], "pending_workflow_authoring": True, "private_fragments_embedded": False}}}
        ]
    }

def integration_manifest(mission: dict) -> dict:
    """Spécification déclarative des intentions, sans transitions locales."""
    return {
        "format": "kontexte.orgo-blueprint/1", "mission_id": mission["id"],
        "orgo_canonical": ["Case", "Task", "Signal", "WorkflowVersion"],
        "proposed_assignments": [{"step_id": s["id"], "role": s["role"], "depends_on": s["depends_on"], "kind": s["kind"], "curriculum_ids": s.get("curriculum_ids", [])} for s in mission["steps"]],
        "proposed_fragment_controls": [{"id": f["id"], "role": f["holder_role"], "release": f["release"]} for f in mission["fragments"]],
        "proposed_joins": mission["joins"],
        "status": "requires_generic_orgo_capabilities_and_review"
    }


def synthetic_review_workflow_fixture(mission: dict, *, label: str = '2.11') -> dict:
    """Orgo workflow + Signal which creates SYNTHETIC review tasks in Orgo.

    This is genuine Orgo workflow design for preparation, NOT conditional learning:
    there are no Orgo joins, recipient-specific secret releases or auto-approval.
    Each step is clearly marked pending review; it is NOT assigned to a pupil.
    """
    check(bool(re.fullmatch(r'[1-9]\d*\.[1-9][1-5](?:\.[A-Za-z0-9]+)*',label)), 'label Orgo invalide')
    key=slug(mission['id']).replace('-','_')
    digest=hashlib.sha256(json.dumps(mission,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:10]
    workflow_code=f'kontexte_{key}_{digest}'
    actions=[{
        'type':'CREATE_CASE',
        'input':{'title':'$signal.title','description':'$signal.description',
                 'label':'$signal.label','severity':'$signal.severity',
                 'metadata':{'synthetic':True,'mission_id':mission['id'],
                             'pending_pedagogical_review':True,'kontexte_version':'0.4.0'}}}]
    for step in mission['steps']:
        actions.append({'type':'CREATE_TASK','input':{
            'title':'[REVIEW] '+step['id']+' — '+step['role'],
            'description':step['instruction']['fr-CA']+'\nTâche de conception. Ne pas attribuer à un élève. Dépendances et information privée non activées.',
            'label':'$signal.label', 'type':'education_pilot','category':'request',
            'case_id':'$case','priority':'LOW',
            'metadata':{'synthetic':True,'mission_id':mission['id'],'step_id':step['id'],
                        'suggested_role':step['role'],'depends_on_design_only':step['depends_on'],
                        'pending_workflow_review':True,'private_fragments_embedded':False}}})
    check(len(actions)<=50,'trop d’actions pour une règle Orgo')
    return {'schema_version':'orgo.scenario.v1',
        'scenario':{'id':f'kontexte_workflow_{key}_{digest}',
                    'title':'SYNTHETIC review — '+mission['title']['fr-CA'],
                    'description':'Orgo creates review tasks, not student missions or conditionally unlocked clues.',
                    'synthetic':True,'epistemic_status':'synthetic_demo_fixture',
                    'correlation_id':f'kontexte.review.{key}.{digest}'},
        'operations':[
            {'op':'publish_workflow','ref':'workflow.kontexte','code':workflow_code,
             'content':{'rules':[{'id':'kontexte_synthetic_review','enabled':True,
                    'match':{'source':'API','type':'kontexte_synthetic_review'},'actions':actions}]}},
            {'op':'create_signal','ref':'signal.kontexte','workflow_ref':'workflow.kontexte',
             'input':{'source':'api','external_reference':f'kontexte:review:{key}:{digest}',
                      'type':'kontexte_synthetic_review','category':'request',
                      'classification':'synthetic_review_only','severity':'MINOR','label':label,
                      'title':'[SYNTHETIC REVIEW] '+mission['title']['fr-CA'],
                      'description':'Review-only pilot. No real children, no private clues, no automatic learner assignment.',
                      'payload':{'synthetic':True,'epistemic_status':'synthetic_demo_fixture',
                                 'mission_id':mission['id'],'contains_personal_data':False}}},
            {'op':'wait_signal','signal_ref':'signal.kontexte','timeout_seconds':15}
        ]}
