"""Projection non autoritative de cartes de mission depuis Kontexte.

Les fragments, identités, résultats et permissions ne sont JAMAIS exportés.
Une carte est un support de lecture, pas un mandat Orgo. Les consignes de
l'édition doivent être approuvées avant toute distribution aux enfants.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

IDENTIFIER = re.compile(r"[a-z0-9][a-z0-9_-]{1,79}\Z")


def project_cards(mission: dict) -> dict:
    if mission.get("format") != "kontexte.mission/1":
        raise ValueError("Format de mission inconnu")
    mission_id = mission.get("id")
    if not isinstance(mission_id, str) or not IDENTIFIER.fullmatch(mission_id):
        raise ValueError("Identifiant de mission incorrect")
    if mission.get("synthetic") is not True:
        raise ValueError("Projection limitée aux missions synthétiques de revue")
    safety = mission.get("safety")
    if not isinstance(safety, dict) or safety.get("publication_default") != "private" or safety.get("real_spending") is not False or safety.get("real_taxes") is not False:
        raise ValueError("Garanties structurées de la mission absentes")
    title = mission.get("title", {}).get("fr-CA")
    if not isinstance(title,str) or not title.strip():
        raise ValueError("Titre français requis")
    steps = mission.get("steps")
    if not isinstance(steps,list) or not steps:
        raise ValueError("Mission sans étapes")
    ids = set()
    for step in steps:
        sid = step.get("id")
        if not isinstance(sid,str) or not IDENTIFIER.fullmatch(sid) or sid in ids:
            raise ValueError("Étape invalide ou répétée")
        ids.add(sid)
    result = []
    for step in steps:
        if step.get("role") not in mission.get("roles",[]):
            raise ValueError("Personnage inconnu")
        instruction = step.get("instruction",{}).get("fr-CA")
        if not isinstance(instruction,str) or not instruction.strip() or len(instruction) > 900:
            raise ValueError("Consigne manquante ou trop longue")
        deps = step.get("depends_on",[])
        if not isinstance(deps,list) or any(d not in ids or d==step['id'] for d in deps):
            raise ValueError("Dépendance inconnue")
        # Intentionally exclude mission.fragments, joins, proof, curriculum scores,
        # class membership, identity, release and operational task status.
        result.append({"card_ref":f"{mission_id}.{step['id']}",
                       "task_ref":step['id'],"role_code":step['role'],
                       "instruction":instruction,
                       "depends_on_design_only":deps,
                       "display_state":"préparation_enseignant"})
    return {"format":"kidaxion.print-cards/1", "mission_ref":mission_id,
            "mission_version":mission.get("version"),"title":title,
            "distribution":"teacher_review_only", "server_authorized":False,
            "dispatch_allowed":False,"cards":result}


def main(argv=None):
    parser=argparse.ArgumentParser(description="Exporter une planche de cartes de revue (sans indices privés)")
    parser.add_argument("mission",type=Path)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv)
    payload=project_cards(json.loads(args.mission.read_text(encoding="utf-8")))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"{len(payload['cards'])} cartes de revue écrites : {args.out}")

if __name__ == "__main__":
    main()
