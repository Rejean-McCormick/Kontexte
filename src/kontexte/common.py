"""Validation de données non fiables; aucune dépendance externe."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import re

IDENTIFIER = re.compile(r"^[a-z][a-z0-9_-]{1,80}$")

class KontexteError(ValueError):
    pass

def check(cond: bool, message: str) -> None:
    if not cond:
        raise KontexteError(message)

def require_id(value: Any, field: str) -> str:
    check(isinstance(value, str) and bool(IDENTIFIER.fullmatch(value)), f"{field}: identifiant invalide")
    return value

def require_text(value: Any, field: str, limit: int = 2000) -> str:
    check(isinstance(value, str) and 0 < len(value.strip()) <= limit, f"{field}: texte requis (1..{limit})")
    return value

def require_list(obj: dict, key: str) -> list:
    value = obj.get(key)
    check(isinstance(value, list), f"{key}: tableau requis")
    return value

def unique(ids: list[str], label: str) -> None:
    check(len(ids) == len(set(ids)), f"{label}: identifiants dupliqués")

def load_json(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    check(isinstance(data, dict), "racine JSON: objet requis")
    return data

def dump_json(obj: Any, path: str | Path) -> None:
    target = Path(path); target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False)+"\n", encoding="utf-8")
