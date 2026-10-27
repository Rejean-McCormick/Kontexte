"""Synthetic teacher-only integration surface tests. No actual student/orchestrator accounts."""
import sys
from pathlib import Path
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from kontexte.cli import ROOT
from kontexte.studio import catalogue_for_studio, exercise_check, dispatch
from kontexte.common import KontexteError

class StudioTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.catalogue=catalogue_for_studio(ROOT)
 def test_full_catalogue(self):
  c=self.catalogue
  self.assertEqual((len(c['roles']),len(c['missions']),len(c['overlays']),len(c['neutral'])),(38,11,60,60))
  self.assertEqual(len(c['year']['semaines']),36)
  self.assertEqual(set(c['neutral']),set(c['overlays']))
 def test_same_year_overlay_untouched_neutral(self):
  for key,overlay in self.catalogue['overlays'].items():
   self.assertEqual(overlay['base_trame_id'],key)
   self.assertEqual(overlay['niveaux']['principal'],'primaire-3')
 def test_pilot_solo_profiles(self):
  for level,expected in [('accompagne','250'),('standard','500'),('approfondi','1000')]:
   self.assertTrue(exercise_check({'key':'solo-measure','answer':expected,'level':level},self.catalogue)['correct'])
   self.assertFalse(exercise_check({'key':'solo-measure','answer':'999','level':level},self.catalogue)['correct'])
 def test_duo_profiles(self):
  for level,expected in [('accompagne','1'),('standard','1'),('approfondi','2')]:
   self.assertTrue(exercise_check({'key':'duo-paper','answer':expected,'level':level},self.catalogue)['correct'])
 def test_cannot_infer_mastery(self):
  r=exercise_check({'key':'solo-measure','answer':'500'},self.catalogue)
  self.assertFalse(r['student_mastery_inferred']);self.assertEqual(r['evidence_status'],'practice_only')
 def test_15_qc_exercises_answers(self):
  for key,exercise in self.catalogue['exercises'].items():
   self.assertTrue(exercise_check({'key':'qc3:'+key,'answer':str(exercise['answer'])},self.catalogue)['correct'],key)
 def test_synthetic_user_only(self):
  with tempfile.TemporaryDirectory() as d:
   ctx={'repo':ROOT,'catalogue':self.catalogue,'evidence_db':Path(d)/'test.sqlite'}
   with self.assertRaises(KontexteError):
    dispatch('POST','/api/practice',{'student':'alice','mission_id':'sorciere-solo','step_id':'mesurer','curriculum_id':'qc-pri-ma-008'},ctx,{})
 def test_limited_course(self):
  with tempfile.TemporaryDirectory() as d:
   ctx={'repo':ROOT,'catalogue':self.catalogue,'evidence_db':Path(d)/'test.sqlite'}
   with self.assertRaises(KontexteError):
    dispatch('POST','/api/practice',{'student':'demo-001','mission_id':'sorciere-solo','step_id':'mesurer','curriculum_id':'qc-pri-ma-006'},ctx,{})
 def test_demo_evidence_practice_not_mastery(self):
  with tempfile.TemporaryDirectory() as d:
   ctx={'repo':ROOT,'catalogue':self.catalogue,'evidence_db':Path(d)/'test.sqlite'}
   _,r=dispatch('POST','/api/practice',{'student':'demo-001','mission_id':'sorciere-solo','step_id':'mesurer','curriculum_id':'qc-pri-ma-008','level':'standard'},ctx,{})
   self.assertTrue(r['recorded']);self.assertFalse(r['validated'])
   _,report=dispatch('GET','/api/evidence',{},ctx,{'student':['demo-001']})
   self.assertEqual(report['report']['courses']['qc-pri-ma-008']['states'],['practiced'])
 def test_privacy_denied(self):
  with tempfile.TemporaryDirectory() as d:
   ctx={'repo':ROOT,'catalogue':self.catalogue,'evidence_db':Path(d)/'test.sqlite'}
   _,m=dispatch('POST','/api/privacy',{'asset':{'id':'asset-test','author':'demo-001','persons':['demo-001'],'reviewed_by_school':True,'contains_identifiable_minors':True,'guardian_permission_verified':False},'audience':'public','consents':{}},ctx,{})
   self.assertEqual(m['visibility'],'withheld');self.assertEqual(m['tags'],[]);self.assertIsNone(m['media'])
 def test_schoolwide_participants(self):
  with tempfile.TemporaryDirectory() as d:
   ctx={'repo':ROOT,'catalogue':self.catalogue,'evidence_db':Path(d)/'test.sqlite'}
   _,obj=dispatch('GET','/api/school-event',{},ctx,{})
   self.assertEqual(len(obj['event']['participation']),7)
   self.assertEqual(obj['event']['scope']['mode'],'whole_school')

if __name__=='__main__':unittest.main()
