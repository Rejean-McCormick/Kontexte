import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import unittest
from kontexte.assessment import invitation_paper,lanterns,validate_numeric_answer
from kontexte.common import KontexteError

class CalculTest(unittest.TestCase):
 def test_invitation_shortage(self):
  r=invitation_paper(invitations=6,per_sheet=2,available_sheets=2)
  self.assertEqual((r['sheets_needed'],r['missing_sheets']),(3,1))
 def test_no_shortage(self):
  self.assertEqual(invitation_paper(invitations=4,per_sheet=2,available_sheets=2)['missing_sheets'],0)
 def test_lantern_volume(self):
  self.assertEqual(lanterns(quantity=8,millilitres_each=125,container_ml=250),{'total_ml':1000,'containers_needed':4,'curriculum_status':'practice_only'})
 def test_num_check(self):
  self.assertTrue(validate_numeric_answer('3,0','3')['correct'])
  self.assertFalse(validate_numeric_answer('cinq','5')['correct'])
 def test_bad_measure(self):
  with self.assertRaises(KontexteError):lanterns(quantity=1,millilitres_each=0,container_ml=250)
