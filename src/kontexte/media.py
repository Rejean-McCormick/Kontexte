"""Décisions de publication à refus prioritaire. Ne publie et ne téléverse rien."""
from __future__ import annotations
from datetime import datetime, timezone
from .common import check, require_id

VALID_AUDIENCES = {"group", "school", "public"}

def can_publish(asset: dict, audience: str, consents: dict[str,dict]) -> bool:
    """Toutes les personnes identifiables + l'auteur mineur nécessitent des autorisations spécifiques.

    Conception fail-closed : un champ absent ou un refus => aucun média distribué.
    """
    if audience not in VALID_AUDIENCES or asset.get("reviewed_by_school") is not True:
        return False
    if asset.get("contains_identifiable_minors") and not asset.get("guardian_permission_verified"):
        return False
    owners = asset.get("persons", [])
    if not isinstance(owners,list) or not owners or len(owners) != len(set(owners)):
        return False
    if not asset.get("author") or asset["author"] not in owners:
        return False
    for person in owners:
        decision=consents.get(person)
        if not isinstance(decision,dict) or decision.get("allowed") is not True or audience not in decision.get("audiences",[]):
            return False
        if decision.get("asset_id") != asset.get("id"):
            return False
    return True

def public_manifest(asset: dict, audience: str, consents: dict[str,dict]) -> dict:
    """Aucun contenu binaire/URL, aucun tag ni identité si consentement refusé."""
    safe = can_publish(asset, audience, consents)
    if not safe:
        return {"id": asset.get("id"), "visibility":"withheld", "media": None, "tags": [], "persons": [], "thumbnail": None, "metadata": {}}
    # Même après accord, les identités ne sont pas exportées implicitement.
    return {"id": asset["id"], "visibility":audience, "media": asset.get("approved_media_ref"),
            "thumbnail": asset.get("approved_thumbnail_ref"), "persons": [],
            "tags": [str(x) for x in asset.get("non_identifying_tags",[]) if isinstance(x,str)][:20],
            "metadata": {"mission_id":asset.get("mission_id","")}}
