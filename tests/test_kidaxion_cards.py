from copy import deepcopy
from pathlib import Path
import json
import pytest
from kontexte.kidaxion_cards import project_cards

ROOT=Path(__file__).resolve().parents[1]


def test_all_approved_synthetic_missions_safe_projection():
    allowed = {"fete-sorciere", "grand-menage-chez-mamie", "mystere-de-la-bibliotheque", "pique-nique-des-saisons", "rallye-des-metiers", "randonnee-a-velo", "spectacle-des-histoires"}
    for mid in allowed:
        source=json.loads((ROOT/'data/missions'/f'{mid}.json').read_text(encoding='utf8'))
        out=project_cards(source)
        assert len(out['cards'])==len(source['steps'])
        assert out['server_authorized'] is False and out['dispatch_allowed'] is False
        assert not any(key in json.dumps(out) for key in ('papier-disponible', '55 Klownkoins', 'student_id', 'holder_role', 'content_fr'))


def test_rejects_missing_guarantees():
    mission=json.loads((ROOT/'data/missions/fete-sorciere.json').read_text(encoding='utf8'))
    modified=deepcopy(mission); modified['safety']['publication_default']='public'
    with pytest.raises(ValueError):project_cards(modified)
    modified=deepcopy(mission);modified['steps'][0]['depends_on']=['unknown']
    with pytest.raises(ValueError):project_cards(modified)
