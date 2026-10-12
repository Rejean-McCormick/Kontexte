"""Preuves pédagogiques : SQLite *local de développement uniquement*.

Ce module ne fournit ni comptes, ni ACL multi-utilisateurs, ni coffre pour données d'enfants.
Ne pas l'exposer sur un serveur ni l'utiliser avec de vraies données d'élèves.
"""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
from .common import check, require_id
from .ekole import STATES

DDL = """CREATE TABLE IF NOT EXISTS evidence (
 id TEXT PRIMARY KEY, student_ref TEXT NOT NULL, curriculum_id TEXT NOT NULL,
 mission_id TEXT NOT NULL, step_id TEXT NOT NULL, status TEXT NOT NULL,
 validation_mode TEXT NOT NULL, reviewer_ref TEXT,
 evidence_ref TEXT NOT NULL, support_level TEXT NOT NULL,
 occurred_at TEXT NOT NULL, payload_hash TEXT NOT NULL
);"""

def validate_event(event: dict, catalogue: dict[str,dict]) -> dict:
    check(event.get("format") == "kontexte.evidence/1", "format preuve invalide")
    for field in ("id", "student_ref", "mission_id", "step_id"):
        require_id(event.get(field), field)
    check(event.get("curriculum_id") in catalogue, "référence Ekole invalide")
    check(event.get("status") in STATES, "statut inconnu")
    check(event.get("validation_mode") in {"human_review", "deterministic_practice", "observation"}, "mode de validation inconnu")
    check(event.get("status") in {"observed", "covered", "practiced"} or event["validation_mode"] == "human_review", "maîtrise/validation: revue habilitée nécessaire")
    if event["status"] in ("mastered", "validated"):
        require_id(event.get("reviewer_ref"), "reviewer_ref")
    check(isinstance(event.get("evidence_ref"), str) and len(event["evidence_ref"]) >= 5, "preuve référencée nécessaire")
    check(event.get("support_level") in {"accompagne", "standard", "approfondi", "other"}, "support_level invalide")
    date = datetime.fromisoformat(event.get("occurred_at", "").replace("Z", "+00:00"))
    check(date.tzinfo is not None, "occurred_at: timezone obligatoire")
    return event

def init_db(path: str | Path) -> None:
    with sqlite3.connect(path) as db: db.execute(DDL)

def record(path: str | Path, event: dict, catalogue: dict[str,dict]) -> bool:
    validate_event(event, catalogue)
    init_db(path)
    serialized = json.dumps(event, sort_keys=True, ensure_ascii=False)
    digest = hashlib.sha256(serialized.encode()).hexdigest()
    with sqlite3.connect(path) as db:
        old = db.execute("SELECT payload_hash FROM evidence WHERE id=?", (event["id"],)).fetchone()
        if old:
            check(old[0] == digest, "collision idempotency: même id, événement différent")
            return False
        db.execute("INSERT INTO evidence VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
            event["id"], event["student_ref"], event["curriculum_id"], event["mission_id"], event["step_id"], event["status"],
            event["validation_mode"], event.get("reviewer_ref"), event["evidence_ref"], event["support_level"],
            event["occurred_at"], digest))
    return True

def list_events(path: str | Path, student_ref: str) -> list[dict]:
    require_id(student_ref, "student_ref")
    with sqlite3.connect(path) as db:
        db.row_factory = sqlite3.Row
        return [dict(row) for row in db.execute("SELECT * FROM evidence WHERE student_ref=? ORDER BY occurred_at,id", (student_ref,))]
