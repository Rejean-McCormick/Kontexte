"""Vérifie la surcouche Qc-3 de conception, sans prétendre à une validation officielle."""
import json,hashlib,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
L=ROOT/'data/locales/qc/fr-CA/grade3'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))

def test_neutral_catalogue_immutability():
 base=ROOT/'data/trames/catalogue-neutral-v0.2.json'
 overlay=read(L/'overlays-60.json')
 assert hashlib.sha256(base.read_bytes()).hexdigest()==overlay['parent_catalogue_hash']

def test_all_neutral_scenarios_overlaid_once():
 neutral=read(ROOT/'data/trames/catalogue-neutral-v0.2.json')
 overlay=read(L/'overlays-60.json')
 assert {x['id'] for x in neutral['scenarios']} == {x['base_trame_id'] for x in overlay['items']}
 assert len(overlay['items'])==60

def test_all_candidates_planned_not_certified():
 obj=read(L/'objectifs-candidats.json')['objectifs']
 ov=read(L/'overlays-60.json')['items']
 plan=read(L/'parcours-36-semaines.json')
 micro=read(L/'micro-situations-34.json')['modules']
 core=set(sum(plan['trames_pilotes_par_etape'].values(),[]))
 covered=set(i for row in ov if row['base_trame_id'] in core for i in row['objectifs_candidats'])
 scheduled={m['objet_pedagogique'] for m in micro}
 assert {x['id'] for x in obj} == covered | scheduled
 assert not covered & scheduled
 assert all(x['statut_correspondance']=='candidat_a_valider_avec_progression_3e' for x in obj)

def test_teacher_answer_not_in_student_overlays():
 ov=read(L/'overlays-60.json')['items']
 assert all('solution_reservee_a_enseignant' not in str(x) for x in ov)
 assert len(read(ROOT/'teacher-only/qc3/corrige-enseignant-ne-pas-exporter.json')['corriges'])==60

def test_academic_year_has_36_weeks():
 plan=read(L/'parcours-36-semaines.json')
 assert len(plan['semaines'])==36
 assert sorted(w['semaine_pedagogique'] for w in plan['semaines'])==list(range(1,37))

def test_ccq_sensitive_content_requires_specialist():
 micro=read(L/'micro-situations-34.json')['modules']
 for m in micro:
  if m['objet_pedagogique'].endswith(('.prevention','.genre','.spiritualite','.cycle-vie')):
   assert m['type']=='enseignement_obligatoire_encadre'
