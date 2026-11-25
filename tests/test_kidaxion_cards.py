import json
import unittest
from copy import deepcopy
from pathlib import Path

from kontexte.kidaxion_cards import project_cards

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / 'data' / 'missions'


class KidaxionCardTests(unittest.TestCase):
    def test_all_approved_synthetic_missions_safe_projection(self):
        allowed = (
            'fete-sorciere',
            'grand-menage-chez-mamie',
            'mystere-de-la-bibliotheque',
            'pique-nique-des-saisons',
            'rallye-des-metiers',
            'randonnee-a-velo',
            'spectacle-des-histoires',
        )
        private_markers = (
            'papier-disponible', '55 Klownkoins', 'student_id', 'holder_role', 'content_fr',
        )
        for mission_id in allowed:
            with self.subTest(mission_id=mission_id):
                source = json.loads((MISSIONS / f'{mission_id}.json').read_text(encoding='utf-8'))
                result = project_cards(source)
                self.assertEqual(len(result['cards']), len(source['steps']))
                self.assertIs(result['server_authorized'], False)
                self.assertIs(result['dispatch_allowed'], False)
                serialized = json.dumps(result)
                for marker in private_markers:
                    self.assertNotIn(marker, serialized)

    def test_rejects_missing_guarantees(self):
        mission = json.loads((MISSIONS / 'fete-sorciere.json').read_text(encoding='utf-8'))
        modified = deepcopy(mission)
        modified['safety']['publication_default'] = 'public'
        with self.assertRaises(ValueError):
            project_cards(modified)

        modified = deepcopy(mission)
        modified['steps'][0]['depends_on'] = ['unknown']
        with self.assertRaises(ValueError):
            project_cards(modified)
