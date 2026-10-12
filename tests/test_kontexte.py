import json
import sys
import tempfile
from copy import deepcopy
from pathlib import Path
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from kontexte.cli import ROOT, read_all, write_site
from kontexte.models import validate_mission, validate_role
from kontexte.common import KontexteError
from kontexte.render import project
from kontexte.orgo import scenario_fixture
from kontexte.ekole import check_curriculum, aggregate
from kontexte.evidence import validate_event, record, list_events
from kontexte.economy import bill
from kontexte.media import can_publish, public_manifest
from kontexte.orgo_http import OrgoAPI

class ContentTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.catalog, cls.roles, cls.missions=read_all(ROOT)
 def test_count(self):
  self.assertEqual(len(self.catalog),202);self.assertGreaterEqual(len(self.roles),30);self.assertGreaterEqual(len(self.missions),10)
 def test_mission_cycles_fail(self):
  m=deepcopy(self.missions['sorciere-solo']);m['steps'][0]['depends_on']=['expliquer']
  with self.assertRaises(KontexteError):validate_mission(m,self.catalog)
 def test_missing_reference_fails(self):
  m=deepcopy(self.missions['sorciere-solo']);m['steps'][0]['curriculum_ids']=['qc-pri-ma-99999']
  with self.assertRaises(KontexteError):validate_mission(m,self.catalog)
 def test_missing_role_fails(self):
  m=deepcopy(self.missions['sorciere-solo']);m['steps'][0]['role']='notpresent'
  with self.assertRaises(KontexteError):validate_mission(m,self.catalog)
 def test_unsupported_lang_fails(self):
  r=deepcopy(self.roles['sorciere']);r['name']['de']='Hexe'
  with self.assertRaises(KontexteError):validate_role(r)
 def test_same_math_for_three_profiles(self):
  m=self.missions['sorciere-solo'];r=self.roles['sorciere']
  pages=[project(m,r,adaptation=l) for l in ['accompagne','standard','approfondi']]
  self.assertTrue(all('4 × 125' in p for p in pages));self.assertEqual(len(set(pages)),3)
 def test_fragments_fail_closed(self):
  m=self.missions['fete-sorciere'];r=self.roles['sorciere']
  hidden=project(m,r,authorized_fragment_ids=('besoin-invitations',))
  self.assertNotIn('Il faut 6 invitations',hidden)
  revealed=project(m,r,authorized_fragment_ids=('besoin-invitations',),trusted_authorization=True)
  self.assertIn('Il faut 6 invitations',revealed)
 def test_html_escapes_payload(self):
  m=deepcopy(self.missions['sorciere-solo']);m['title']['fr-CA']='<img src=x onerror=alert(1)>'
  view=project(m,self.roles['sorciere']);self.assertIn('&lt;img',view);self.assertNotIn('<img',view)
 def test_lang_en(self):
  page=project(self.missions['sorciere-solo'],self.roles['sorciere'],lang='en')
  self.assertIn('Measuring the cauldron',page)
 def test_fixture_marker(self):
  fixture=scenario_fixture(self.missions['fete-sorciere']);self.assertTrue(fixture['scenario']['synthetic'])
  self.assertEqual(len(fixture['operations']),2)
  content=json.dumps(fixture,ensure_ascii=False)
  self.assertNotIn('Une feuille produit',content)
 def test_fixture_repeatable(self):
  m=self.missions['fete-sorciere'];self.assertEqual(scenario_fixture(m),scenario_fixture(m))
 def test_curriculum_explicitly_unofficial(self):
  links=check_curriculum(self.missions['fete-sorciere'],self.catalog)
  self.assertTrue(links);self.assertTrue(all(x['official_pfeq_id'] is None for x in links))
 def test_site(self):
  with tempfile.TemporaryDirectory() as d:
   n=write_site(ROOT,Path(d));self.assertGreater(n,20);self.assertTrue((Path(d)/'index.html').exists())

class OtherTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.catalog,cls.roles,cls.missions=read_all(ROOT)
 def event(self):
  return {'format':'kontexte.evidence/1','id':'event-001','student_ref':'eleve-fixture-001',
    'curriculum_id':'qc-pri-ma-006','mission_id':'fete-sorciere','step_id':'budget-final',
    'status':'practiced','validation_mode':'deterministic_practice',
    'evidence_ref':'practice-fixture-001','support_level':'standard','occurred_at':'2026-10-11T17:00:00-04:00'}
 def test_no_auto_mastery(self):
  e=self.event();e['status']='mastered'
  with self.assertRaises(KontexteError):validate_event(e,self.catalog)
 def test_validated_human(self):
  e=self.event();e['status']='validated';e['validation_mode']='human_review';e['reviewer_ref']='teacher-fixture'
  validate_event(e,self.catalog)
 def test_no_student_name(self):
  event=self.event();self.assertNotIn('student_name',event)
 def test_idempotency_and_collision(self):
  e=self.event()
  with tempfile.TemporaryDirectory() as d:
   db=Path(d)/'dev.sqlite'
   self.assertTrue(record(db,e,self.catalog));self.assertFalse(record(db,e,self.catalog))
   e['status']='covered'
   with self.assertRaises(KontexteError):record(db,e,self.catalog)
   self.assertEqual(len(list_events(db,'eleve-fixture-001')),1)
 def test_aggregate_does_not_infer(self):
  r=aggregate([self.event()],self.catalog)
  self.assertEqual(r['courses']['qc-pri-ma-006']['states'],['practiced'])
 def test_bill(self):
  b=bill([{'description':'Décor','quantity':1,'unit_price':'8.00'},{'description':'Artistes','quantity':4,'unit_price':'6.00'}],fictional_tax_rate='0.10')
  self.assertEqual(b['subtotal'],'32.00');self.assertEqual(b['tax'],'3.20');self.assertEqual(b['total'],'35.20')
 def test_negative_bill_rejected(self):
  with self.assertRaises(KontexteError):bill([{'description':'x','quantity':1,'unit_price':'-2'}])
 def asset(self):
  a={'id':'art-001','persons':['kid-a','kid-b'],'author':'kid-a','mission_id':'fete-sorciere','reviewed_by_school':True,'guardian_permission_verified':True,'contains_identifiable_minors':True,'approved_media_ref':'approved/abc.webp','approved_thumbnail_ref':'approved/abc-thumb.webp','non_identifying_tags':['origami']}
  c={p:{'asset_id':'art-001','allowed':True,'audiences':['group','school','public']} for p in a['persons']}
  return a,c
 def test_consent_all_required(self):
  a,c=self.asset();self.assertTrue(can_publish(a,'public',c))
  c['kid-b']['allowed']=False;self.assertFalse(can_publish(a,'public',c));self.assertEqual(public_manifest(a,'public',c)['tags'],[])
 def test_consent_scope(self):
  a,c=self.asset();c['kid-a']['audiences']=['group'];self.assertFalse(can_publish(a,'public',c))
 def test_guardian(self):
  a,c=self.asset();a['guardian_permission_verified']=False;self.assertFalse(can_publish(a,'group',c))
 def test_no_people_export_even_with_consent(self):
  a,c=self.asset();r=public_manifest(a,'public',c);self.assertEqual(r['persons'],[])
 def test_url_restrictions(self):
  with self.assertRaises(KontexteError):OrgoAPI('https://evil.example/api/v3','abc')
 def test_orgo_local_url(self):
  o=OrgoAPI('http://127.0.0.1:4000/api/v3','fake');self.assertEqual(o.url,'http://127.0.0.1:4000/api/v3')

if __name__=='__main__':unittest.main()
