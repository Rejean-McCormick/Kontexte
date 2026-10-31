import copy
import json
from pathlib import Path
import unittest
from kontexte.models import validate_role

class VisualReferenceTests(unittest.TestCase):
    def test_catalogue_has_one_stable_reference_per_role(self):
        paths=list((Path(__file__).resolve().parents[1]/'data/roles').glob('*.json'))
        self.assertEqual(len(paths),38)
        for path in paths:
            role=json.loads(path.read_text(encoding='utf-8'));validate_role(role)
            self.assertEqual(role['visual_id'],'role-'+role['id'])
            legacy=copy.deepcopy(role);del legacy['visual_id'];validate_role(legacy)
            role['visual_id']='role-other'
            with self.assertRaises(ValueError):validate_role(role)

if __name__=='__main__':unittest.main()
