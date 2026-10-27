"""Tests autonomes: Export Kontexte et contrat Ekole P1, sans réseau."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from kontexte.cli import read_all
from kontexte.common import KontexteError
from kontexte.tandem import build_teacher_preview

TENANT='11111111-1111-4111-8111-111111111111'
WORLD='22222222-2222-4222-8222-222222222222'
RELEASE='33333333-3333-4333-8333-333333333333'

class TandemExportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _,_,missions=read_all(ROOT);cls.source=missions['fete-sorciere']

    def export(self,mission=None,**kwargs):
        p=dict(tenant_id=TENANT,world_id=WORLD,world_release_id=RELEASE,workflow_ref='fete-sorciere-v1')
        p.update(kwargs)
        return build_teacher_preview(self.source if mission is None else mission,**p)

    def test_exact_closed_ekole_p1_fields(self):
        p=self.export()
        self.assertEqual(set(p),{'format','mode','authority','tenant_id','world_id','world_release_id','scenario_ref','workflow_ref','tasks'})
        self.assertEqual(p['format'],'ekole.tandem-teacher-preview/1.0')
        self.assertEqual(p['mode'],'synthetic');self.assertEqual(p['authority'],'orgo')
        self.assertEqual(len(p['tasks']),len(self.source['steps']))
        self.assertEqual(p['tasks'][0]['state'],'ready')
        self.assertEqual(p['tasks'][2]['state'],'waiting')

    def test_no_fragment_bodies_identity_or_media(self):
        p=self.export();body=json.dumps(p,ensure_ascii=False)
        self.assertNotIn('Une feuille produit',body)
        self.assertNotIn('55 Klownkoins',body)
        self.assertNotIn('student_name',body);self.assertNotIn('media_url',body)
        self.assertTrue(all(row['fragment_refs']==[] for row in p['tasks']))
        self.assertTrue(all(set(row)=={'task_ref','role_code','state','fragment_refs'} for row in p['tasks']))

    def test_deterministic_export(self):self.assertEqual(self.export(),self.export())
    def test_reject_non_synthetic(self):
        d=copy.deepcopy(self.source);d['synthetic']=False
        with self.assertRaises(KontexteError):self.export(d)
    def test_reject_unsafe_publication(self):
        d=copy.deepcopy(self.source);d['safety']['publication_default']='public'
        with self.assertRaises(KontexteError):self.export(d)
    def test_reject_real_spending(self):
        d=copy.deepcopy(self.source);d['safety']['real_spending']=True
        with self.assertRaises(KontexteError):self.export(d)
    def test_reject_missing_scope(self):
        for key in ('tenant_id','world_id','world_release_id'):
            with self.subTest(key=key),self.assertRaises(KontexteError):self.export(**{key:''})
    def test_reject_noncanonical_or_zero_uuid(self):
        for value in ('00000000-0000-0000-0000-000000000000','ffffffffffffffffffffffffffffffff','../../escape'):
            with self.subTest(value=value),self.assertRaises(KontexteError):self.export(tenant_id=value)
    def test_reject_bad_workflow_id(self):
        for value in ('', '../api', 'x'*90, 'abc def'):
            with self.subTest(value=value),self.assertRaises(KontexteError):self.export(workflow_ref=value)
    def test_reject_duplicate_steps_and_forward_dependencies(self):
        d=copy.deepcopy(self.source);d['steps'][1]['id']=d['steps'][0]['id']
        with self.assertRaises(KontexteError):self.export(d)
        d=copy.deepcopy(self.source);d['steps'][0]['depends_on']=['budget-final']
        with self.assertRaises(KontexteError):self.export(d)
    def test_cli_export_no_network(self):
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)/'ekole.json'
            run=subprocess.run([sys.executable,'-m','kontexte','ekole-tandem-preview','fete-sorciere',
                '--tenant-id',TENANT,'--world-id',WORLD,'--world-release-id',RELEASE,
                '--workflow-ref','fete-sorciere-v1','--out',str(out)],cwd=ROOT,
                env=dict(__import__('os').environ,PYTHONPATH=str(ROOT/'src')),text=True,capture_output=True)
            self.assertEqual(run.returncode,0,run.stderr)
            self.assertEqual(json.loads(out.read_text())['format'],'ekole.tandem-teacher-preview/1.0')

if __name__=='__main__':unittest.main()
