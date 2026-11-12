import copy
import json
import tempfile
import unittest
from pathlib import Path
from kontexte.curriculum_candidates import audit, CurriculumCandidateError

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'integrations/ekole/banque-worlds.curriculum-candidates.json'

class CurriculumCandidateTests(unittest.TestCase):
    def test_all_missing_curriculum_mapped_as_unapproved_candidates(self):
        result=audit(ROOT)
        self.assertEqual(result['proposals_checked'],55)
        self.assertEqual(result['missions_covered'],7)
        self.assertFalse(result['official_alignment_verified'])
        self.assertFalse(result['runtime_dispatch_allowed'])
        self.assertEqual(result['remaining_approved_links_created'],0)

    def _check_rejected(self, mutate):
        payload=json.loads(SOURCE.read_text(encoding='utf-8'))
        mutate(payload)
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'candidates.json'
            path.write_text(json.dumps(payload), encoding='utf-8')
            with self.assertRaises(CurriculumCandidateError):
                audit(ROOT,candidate_path=path)

    def test_claims_of_approval_rejected(self):
        self._check_rejected(lambda p:p['proposals'][0].update(mapping_status='approved'))

    def test_forged_permission_field_rejected(self):
        self._check_rejected(lambda p:p['proposals'][0].update(teacher_authorized=True))

    def test_unknown_kristal_rejected(self):
        self._check_rejected(lambda p:p['proposals'][0].update(internal_kristal_id='fake-kristal'))

    def test_source_text_mismatch_rejected(self):
        self._check_rejected(lambda p:p['proposals'][0].update(instruction_sha256='0'*64))

    def test_missing_or_duplicate_proposal_rejected(self):
        self._check_rejected(lambda p:p['proposals'].pop())
        self._check_rejected(lambda p:p['proposals'].append(copy.deepcopy(p['proposals'][0])))

if __name__ == '__main__': unittest.main()
