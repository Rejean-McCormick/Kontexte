"""Projection HTML statique autorisée; aucun état de mission géré ici."""
from __future__ import annotations
from html import escape
from pathlib import Path
from .common import check

BASE_CSS = """*{box-sizing:border-box}body{font:1.05rem/1.6 system-ui,sans-serif;background:var(--background);color:var(--ink);margin:0}main{max-width:770px;margin:3rem auto;padding:2rem;background:var(--paper);border-radius:22px;box-shadow:0 10px 32px #0002}h1{line-height:1.2}.role{font-weight:700;color:var(--accent)}.card{padding:1rem 1.3rem;margin:1rem 0;border:2px solid var(--accent);border-radius:12px}.hint{background:#fff7c9;padding:.7rem;border-radius:10px}.meta{font-size:.85rem;color:#555}nav a{color:var(--accent)}.badge{display:inline-block;padding:.15rem .6rem;background:var(--accent);color:white;border-radius:12px}button{font:inherit;padding:.5rem 1rem} :focus-visible{outline:3px solid var(--accent);outline-offset:3px}@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}@media print{body{background:white}main{margin:0;box-shadow:none}}"""
THEMES = {
    "neutral": "--background:#e7eef4;--paper:#fff;--ink:#172733;--accent:#215a83",
    "sorciere": "--background:#281c39;--paper:#fff7e9;--ink:#282037;--accent:#67409e",
    "boulanger": "--background:#e9d2b1;--paper:#fffaf1;--ink:#422b1c;--accent:#98601c",
    "scene": "--background:#191d32;--paper:#fffaf5;--ink:#292339;--accent:#94395e",
}

def choose(text: dict, lang: str) -> str:
    check(lang in {"fr-CA", "en"}, "langue non prise en charge")
    # Repli explicite, sans inventer de traduction.
    return text.get(lang) or text["fr-CA"]

def project(mission: dict, role: dict, *, lang: str = "fr-CA", authorized_fragment_ids: tuple[str, ...] = (), adaptation: str = "standard", step_id: str | None = None, trusted_authorization: bool = False) -> str:
    """Ne montre jamais de fragments en l'absence d'une liste approuvée par Orgo.

    trusted_authorization ne s'active que dans une passerelle d'identité vérifiée; pas via une valeur du navigateur.
    """
    check(adaptation in mission["adaptation"], "adaptation inconnue")
    allowed = set(authorized_fragment_ids) if trusted_authorization else set()
    known = {f["id"] for f in mission["fragments"]}
    check(allowed <= known, "référence fragment inconnue")
    name = escape(choose(role["name"], lang)); title = escape(choose(mission["title"], lang))
    fiction = escape(choose(mission["fiction"], lang))
    instruction = escape(choose(mission["adaptation"][adaptation]["instruction"] if isinstance(mission["adaptation"][adaptation]["instruction"], dict) else {"fr-CA":mission["adaptation"][adaptation]["instruction"]}, lang))
    visible_steps = [s for s in mission["steps"] if s["role"] == role["id"] and (step_id is None or s["id"] == step_id)]
    step_markup = "".join(f'<section class="card" data-step="{escape(s["id"])}"><h2>{escape(choose(s["instruction"],lang))}</h2><p class="meta">{escape(s["kind"])} · {escape(s["validation"])}</p></section>' for s in visible_steps)
    fragment_markup = "".join(f'<aside class="hint"><strong>Indice autorisé :</strong> {escape(choose(f["content"],lang))}</aside>' for f in mission["fragments"] if f["id"] in allowed and f["holder_role"] == role["id"] and f["visibility"] == "participant")
    lang_attr = "fr-CA" if lang == "fr-CA" else "en"
    css = BASE_CSS + ":root{" + THEMES[role["theme"]] + "}"
    return (f'<!doctype html><html lang="{lang_attr}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><title>{title} | Kontexte</title><style>{css}</style></head>'
            f'<body><main><p class="badge">Kontexte</p><h1>{title}</h1><p class="role">{name}</p><p>{fiction}</p><p class="meta">{instruction}</p>{step_markup}{fragment_markup}<footer class="meta">Projection locale · Aucun suivi automatique · Orgo détient les états</footer></main></body></html>')
