import sys, unittest, json, subprocess, tempfile, shutil
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from kontexte.cli import ROOT,read_all
from kontexte.orgo import synthetic_review_workflow_fixture

class OrgoWorkflowTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.mission=read_all(ROOT)[2]['fete-sorciere']
 def test_contract_operations(self):
  x=synthetic_review_workflow_fixture(self.mission)
  self.assertEqual([s['op'] for s in x['operations']],['publish_workflow','create_signal','wait_signal'])
  rule=x['operations'][0]['content']['rules'][0]
  self.assertEqual(len(rule['actions']),len(self.mission['steps'])+1)
  self.assertTrue(all(a['input'].get('metadata',{}).get('synthetic') for a in rule['actions']))
  self.assertNotIn('Une feuille produit',json.dumps(x,ensure_ascii=False))
  self.assertEqual(x['operations'][1]['input']['payload']['contains_personal_data'],False)
 def test_reproducible(self):
  self.assertEqual(synthetic_review_workflow_fixture(self.mission),synthetic_review_workflow_fixture(self.mission))
 def test_not_unauthorized(self):
  x=synthetic_review_workflow_fixture(self.mission)
  self.assertTrue(all('assign' not in str(a).lower() for a in x['operations'][0]['content']['rules'][0]['actions']))

if __name__=='__main__':unittest.main()
