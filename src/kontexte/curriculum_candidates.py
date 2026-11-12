"""Validation du registre des correspondances proposées, jamais de compétence acquise.

Aucune mise à jour automatique de ``curriculum_ids`` : chaque proposition est
référencée à la consigne et à la version de sa mission pour permettre la revue.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

DEFAULT = 'integrations/ekole/banque-worlds.curriculum-candidates.json'

class CurriculumCandidateError(ValueError):
    pass


def _digest(value: str | bytes) -> str:
    return hashlib.sha256(value.encode('utf-8') if isinstance(value, str) else value).hexdigest()


def audit(repo: Path, *, candidate_path: Path | None = None) -> dict:
    repo = Path(repo)
    catalog_path = repo / 'data/catalogue/202_kristals.json'
    catalog_raw = catalog_path.read_bytes()
    catalog = {item['id']: item for item in json.loads(catalog_raw)['kristals']}
    source = candidate_path or repo / DEFAULT
    doc = json.loads(source.read_text(encoding='utf-8'))
    if (doc.get('format') != 'kontexte.curriculum-candidates/1.0' or
        doc.get('status') != 'editorial_proposals_not_approved' or
        doc.get('official_curriculum_alignment') is not False or
        doc.get('automatic_mastery_or_dispatch') is not False or
        doc.get('source_catalogue_sha256') != _digest(catalog_raw)):
        raise CurriculumCandidateError('En-tête des candidats invalide ou catalogue modifié')
    if set(doc) != {'format','status','scope','official_curriculum_alignment',
                    'automatic_mastery_or_dispatch','description','source_catalogue_sha256','proposals'} or doc['scope']!='internal_catalogue_only':
        raise CurriculumCandidateError('Champs ou portée du registre non conformes')
    rows = doc.get('proposals')
    if not isinstance(rows, list):
        raise CurriculumCandidateError('Registre de propositions invalide')
    expected = {}
    missions = {}
    for mission_file in (repo / 'data/missions').glob('*.json'):
        mission = json.loads(mission_file.read_text(encoding='utf-8'))
        missions[mission['id']] = mission
        if mission['id'] == 'fete-sorciere' or mission.get('status') == 'proposition_editoriale_synthetique_a_reviser':
            for step in mission['steps']:
                if not step.get('curriculum_ids'):
                    expected[(mission['id'], step['id'])] = (mission, step)
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            raise CurriculumCandidateError('Proposition non structurée')
        if set(row) != {'mission_id','mission_version','step_id','instruction_sha256',
                      'internal_kristal_id','internal_title','discipline','mapping_status',
                      'official_pfeq_id','source','rationale','approval_required'} or not row.get('rationale'):
            raise CurriculumCandidateError('Champs inattendus ou justification manquante')
        key = (row.get('mission_id'), row.get('step_id'))
        if key not in expected or key in seen:
            raise CurriculumCandidateError('Étape inexistante, déjà liée ou dupliquée : '+repr(key))
        seen.add(key)
        mission, step = expected[key]
        c = catalog.get(row.get('internal_kristal_id'))
        if (c is None or row.get('internal_title') != c['titre'] or
            row.get('discipline') != c['discipline'] or
            row.get('mission_version') != mission['version'] or
            row.get('instruction_sha256') != _digest(step['instruction']['fr-CA']) or
            row.get('mapping_status') != 'candidate_unreviewed' or
            row.get('official_pfeq_id') is not None or
            row.get('approval_required') is not True):
            raise CurriculumCandidateError('Correspondance candidate non fiable : '+repr(key))
    if seen != set(expected):
        raise CurriculumCandidateError('Couverture incomplète : '+repr(sorted(set(expected)-seen)))
    return {'format':'kontexte.candidate-audit/1.0', 'proposals_checked':len(seen),
        'missions_covered':len({a for a,b in seen}), 'remaining_approved_links_created':0,
        'teacher_review_required':True,'official_alignment_verified':False,
        'student_assessment_claimed':False,'runtime_dispatch_allowed':False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='Vérifie les correspondances candidates, sans les approuver')
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    try:
        result = audit(args.repo)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print('[ERREUR] '+str(exc))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else f"[OK] {result['proposals_checked']} correspondances candidates, toutes à revoir")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
