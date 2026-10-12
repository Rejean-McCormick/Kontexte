"""Correspondances Ekole; distinction explicite entre référentiel interne et PFEQ officiel."""
from __future__ import annotations
from .common import check

STATES = ("observed", "covered", "practiced", "mastered", "validated")

def check_curriculum(mission: dict, catalogue: dict[str, dict]) -> list[dict]:
    rows = []
    for step in mission["steps"]:
        for key in step.get("curriculum_ids", []):
            check(key in catalogue, f"Kristal inconnu : {key}")
            c = catalogue[key]
            rows.append({"mission_id": mission["id"], "step_id": step["id"], "internal_kristal_id": key,
                         "title": c["titre"], "discipline": c["discipline"],
                         "official_pfeq_id": None, "mapping_status": "candidate_unreviewed",
                         "internal_content_status": c.get("statut", "unknown")})
    return rows

def aggregate(events: list[dict], curriculum: dict[str, dict]) -> dict:
    """Vue dérivée; ne convertit jamais une tâche Orgo complétée en maîtrise scolaire."""
    allowed = set(STATES)
    seen: dict[str, dict] = {}
    for event in events:
        cid = event["curriculum_id"]
        check(cid in curriculum, f"référence inconnue: {cid}")
        state = event["status"]
        check(state in allowed, f"statut invalide {state}")
        record = seen.setdefault(cid, {"title": curriculum[cid]["titre"], "discipline": curriculum[cid]["discipline"], "states": [], "evidence_count": 0})
        if state not in record["states"]: record["states"].append(state)
        record["evidence_count"] += 1
    return {"format": "kontexte.curriculum-report/1", "internal_catalogue_status": "experimental_unofficial", "courses": seen}
