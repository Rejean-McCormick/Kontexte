"""B5 scenario and curriculum candidate tests; no Orgo state and no student records."""
from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from kontexte.qc3_b5 import gather, audit, pilot, export_audit, export_pilot, canonical_sha
from kontexte.common import KontexteError

ROOT=Path(__file__).resolve().parents[1]


class B5Grade3Tests(unittest.TestCase):
    def test_full_integrity_and_coverage(self):
        ctx=gather(ROOT)
        self.assertEqual((len(ctx['neutral']),len(ctx['overlays']),len(ctx['roles']),len(ctx['missions'])),(60,60,38,11))
        self.assertEqual((len(ctx['core']),len(ctx['used']),len(ctx['remaining'])),(32,49,34))
        self.assertEqual(ctx['weeks_for']['commande-de-pains'],10)

    def test_hashes_of_all_neutral_parents(self):
        ctx=gather(ROOT)
        for sid,original in ctx['neutral'].items():
            self.assertEqual(ctx['overlays'][sid]['neutral_parent']['trame_sha256'],canonical_sha(original))

    def test_all_role_and_course_links_known(self):
        ctx=gather(ROOT)
        for frame in ctx['neutral'].values():self.assertTrue(set(frame['roles'])<=set(ctx['roles']))
        for goal in ctx['goals'].values():self.assertIn(goal['ekole_kristal_id'],ctx['courses'])

    def test_audit_contains_roles_missions_scenario_and_calendar(self):
        data,rows=audit(ROOT)
        self.assertEqual(len(rows),60)
        self.assertEqual(len(data['roles']),38)
        self.assertEqual(len(data['missions']),11)
        self.assertEqual(len(data['objectifs']),83)
        self.assertEqual(sum(x['scenario_id'] is None for x in data['semaines']),4)
        self.assertTrue(all(x['statut']=='candidat_non_valide' for x in data['objectifs']))

    def test_solo_preview_no_teacher_answer_or_fragments(self):
        student,teacher=pilot(ROOT)
        self.assertEqual(student['mode_solo_sans_fragments']['plateaux'],3)
        self.assertEqual(student['mode_solo_sans_fragments']['pains_par_plateau'],4)
        self.assertEqual(teacher['scenario_complet_source']['correction_reservee']['total_pains'],24)
        self.assertEqual(teacher['kristals_candidats']['qc3.ma.multiplication'],'qc-pri-ma-008')
        self.assertEqual([r['id'] for r in student['roles']],['boulanger','fermier','comptable'])
        public=json.dumps(student,ensure_ascii=False).lower()
        for forbidden in ('"answer"','"correction"','"correction_reservee"','"pieces_information"',
                          '"fragment_ids"','"contenu_a_distribuer"','6 plateaux','24 pains',
                          'qc-pri-ma-008','solution_must_not_export_to_student'):
            self.assertNotIn(forbidden,public)

    def test_preview_outputs_are_physically_separated(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)
            student,teacher=export_pilot(ROOT,path)
            public=(path/'student-preview/boulangerie.json').read_text(encoding='utf8')
            self.assertEqual(json.loads(public)['id'],teacher['id'])
            self.assertNotIn('correction_reservee',public)
            self.assertNotIn('24',public)
            self.assertTrue((path/'teacher-only/boulangerie-plan.json').is_file())
            self.assertIn('24', (path/'teacher-only/boulangerie-plan.json').read_text())
            self.assertIn('<!doctype html>',(path/'student-preview/boulangerie.html').read_text())

    def test_audit_cli_artifacts_machine_readable(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td);export_audit(ROOT,path)
            data=json.loads((path/'audit-b5.json').read_text(encoding='utf8'))
            self.assertEqual(data['statistiques']['objectifs_internes_candidats'],83)
            for file,count in [('index-scenarios-b5.csv',60),('index-objectifs-b5.csv',83),
                               ('index-roles-b5.csv',38),('calendrier-b5.csv',36)]:
                with (path/file).open(encoding='utf-8-sig',newline='') as f:
                    self.assertEqual(len(list(csv.DictReader(f,delimiter=';'))),count)

    def test_modified_parent_detected(self):
        # Copy only required source files (small), change one trame without updating hashes.
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            for folder in ('data/trames','data/locales/qc/fr-CA/grade3','data/catalogue','data/roles','data/missions'):
                shutil.copytree(ROOT/folder,root/folder)
            file=root/'data/trames/catalogue-neutral-v0.2.json'
            original=file.read_text(encoding='utf8')
            file.write_text(original.replace('La commande de pains','La commande de pains Z',1),encoding='utf8')
            with self.assertRaises(KontexteError):gather(root)

    def test_sensitive_micro_not_routable_as_game(self):
        ctx=gather(ROOT)
        ids=['qc3.ccq.prevention','qc3.ccq.genre','qc3.ccq.spiritualite','qc3.ccq.cycle-vie']
        for micro in ctx['micro']:
            if micro['objet_pedagogique'] in ids:
                self.assertEqual(micro['type'],'enseignement_obligatoire_encadre')

    def test_original_bakery_mission_distinct_from_qc_overlay(self):
        ctx=gather(ROOT)
        mission=ctx['missions']['boulangerie']
        self.assertTrue(any('12 pains' in s['instruction']['fr-CA'] for s in mission['steps']))
        exercise=[e for e in json.loads((ROOT/'data/locales/qc/fr-CA/grade3/exercices-deterministes.json').read_text())['exercices'] if e['scenario_id']=='commande-de-pains'][0]
        self.assertEqual(exercise['operands'],[6,4])
        self.assertEqual(exercise['answer'],24)

if __name__=='__main__':unittest.main()
