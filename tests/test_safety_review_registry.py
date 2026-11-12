import json
from pathlib import Path
import unittest
from kontexte.tandem import build_teacher_preview
from kontexte.common import KontexteError
ROOT=Path(__file__).resolve().parents[1]
UUID='11111111-1111-4111-8111-111111111111'
class SafetyReviewRegistryTest(unittest.TestCase):
    def test_historic_ten_are_review_only_and_still_blocked(self):
        path=ROOT/'integrations/ekole/securite-missions-historiques-a-revoir.json'
        registry=json.loads(path.read_text(encoding='utf8'))
        self.assertTrue(registry['no_automatic_unlock'])
        self.assertEqual(len(registry['missions']),10)
        for row in registry['missions']:
            with self.subTest(mission=row['mission_id']):
                self.assertEqual(row['review_status'],'pending_human_safety_review')
                self.assertFalse(row['teacher_preview_unlocked'])
                mission=json.loads((ROOT/'data/missions'/f"{row['mission_id']}.json").read_text())
                self.assertNotIn('safety',mission)
                with self.assertRaises(KontexteError):
                    build_teacher_preview(mission,tenant_id=UUID,world_id=UUID,world_release_id=UUID,workflow_ref='review-only')
if __name__=='__main__': unittest.main()
