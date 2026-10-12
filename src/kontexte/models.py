"""Contrats de contenu statique. Ils ne contiennent aucun état opérationnel Orgo."""
from __future__ import annotations
from .common import check, require_id, require_text, require_list, unique

LANGUAGES = {"fr-CA", "en"}
KINDS = {"human", "object", "message", "document", "payment", "encounter", "performance", "review"}
VALIDATIONS = {"deterministic_practice", "human_review", "logistical_only"}

def localized(value: object, field: str) -> dict:
    check(isinstance(value, dict) and "fr-CA" in value, f"{field}: traduction fr-CA requise")
    check(set(value).issubset(LANGUAGES), f"{field}: langue non supportée")
    for k, v in value.items(): require_text(v, f"{field}.{k}")
    return value

def validate_role(role: dict) -> dict:
    check(role.get("format") == "kontexte.role/1", "format rôle invalide")
    require_id(role.get("id"), "role.id")
    localized(role.get("name"), "role.name")
    localized(role.get("intro"), "role.intro")
    for name in ("actions", "objects", "problems", "partners"):
        items = require_list(role, name)
        check(len(items) <= 100, f"{name}: maximum 100")
        for item in items: require_text(item, name, 120)
    check(role.get("theme") in {"sorciere", "boulanger", "neutral", "scene"}, "thème non autorisé")
    return role

def validate_mission(mission: dict, catalog: dict | None = None) -> dict:
    check(mission.get("format") == "kontexte.mission/1", "format mission invalide")
    require_id(mission.get("id"), "mission.id")
    require_text(mission.get("version"), "mission.version", 40)
    localized(mission.get("title"), "mission.title")
    localized(mission.get("fiction"), "mission.fiction")
    check(isinstance(mission.get("year_suggestion"), int) and 1 <= mission["year_suggestion"] <= 6, "année entre 1 et 6")
    roles = require_list(mission, "roles")
    for role in roles: require_id(role, "mission.roles")
    unique(roles, "roles")
    steps = require_list(mission, "steps")
    check(0 < len(steps) <= 60, "steps: 1..60")
    ids = [require_id(s.get("id"), "step.id") for s in steps]
    unique(ids, "étapes")
    order = set()
    for s in steps:
        check(s.get("role") in roles, f"étape {s['id']}: rôle absent")
        localized(s.get("instruction"), f"{s['id']}.instruction")
        check(s.get("kind") in KINDS, f"{s['id']}: type inconnu")
        check(s.get("validation") in VALIDATIONS, f"{s['id']}: validation inconnue")
        depends = require_list(s, "depends_on")
        check(all(isinstance(d, str) and d in order for d in depends), f"{s['id']}: dépendance absente, future ou cyclique")
        check(isinstance(s.get("curriculum_ids", []), list), "curriculum_ids tableau requis")
        for cid in s.get("curriculum_ids", []):
            check(isinstance(cid, str) and cid.startswith("qc-pri-"), f"{s['id']}: référence Ekole invalide")
            if catalog is not None: check(cid in catalog, f"{s['id']}: id Ekole inexistant {cid}")
        order.add(s['id'])
    fragments = require_list(mission, "fragments")
    fids = []
    for f in fragments:
        fid = require_id(f.get("id"), "fragment.id"); fids.append(fid)
        check(f.get("holder_role") in roles, f"{fid}: rôle porteur inconnu")
        localized(f.get("content"), f"{fid}.content")
        check(f.get("release") in {"orgo_authorized"}, "libération autorisée uniquement par Orgo")
        check(f.get("visibility") in {"participant", "teacher"}, "visibilité fragment invalide")
    unique(fids, "fragments")
    joins = require_list(mission, "joins")
    for j in joins:
        require_id(j.get("id"), "join.id")
        check(len(j.get("fragment_ids", [])) >= 2 and all(fid in fids for fid in j["fragment_ids"]), "join fragments inconnus")
        check(j.get("unlock_step") in ids, "join unlock_step inconnu")
    adaptation = mission.get("adaptation")
    check(isinstance(adaptation, dict) and set(adaptation) == {"accompagne", "standard", "approfondi"}, "trois profils requis")
    for a in adaptation.values():
        check(isinstance(a, dict), "profil invalide")
        require_text(a.get("instruction"), "aide adaptation")
    check(mission.get("synthetic") is True, "mission pédagogique doit être synthetic: true")
    return mission

def curriculum_index(data: dict) -> dict[str, dict]:
    check(data.get("format") == "ekole.catalogue/0.1", "catalogue Ekole incompatible")
    return {e["id"]: e for e in data["kristals"]}
