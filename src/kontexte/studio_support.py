"""Explicit, safe CLI entry points for the teacher rehearsal studio and Orgo tooling."""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from .common import check
from .orgo import scenario_fixture, synthetic_review_workflow_fixture


def run_studio(repo, *,port,open_browser):
    from .studio import serve
    serve(repo,port=port,open_browser=open_browser)


def run_doctor(repo:Path,roles:int,missions:int,courses:int):
    import importlib.resources as resources
    from .studio import catalogue_for_studio
    c=catalogue_for_studio(repo)
    assert len(c['overlays'])==len(c['neutral'])==60
    for resource in ('index.html','app.js','style.css'):
        assert resources.files('kontexte').joinpath('studio_assets',resource).is_file()
    print('Kontexte 0.4.0 — Diagnostic')
    print(f'  Rôles: {roles} · Missions: {missions} · Kristals internes: {courses}')
    print(f'  Trames neutres/localisées: {len(c["neutral"])}/{len(c["overlays"])}')
    print(f'  Calculs QC3 vérifiables: {len(c["exercises"])} · Plan: {len(c["year"]["semaines"])} semaines')
    print(f'  Python: {sys.version.split()[0]} · Node.js: {shutil.which("node") or "non trouvé (facultatif)"}')
    print('  Studio: prêt à lancer sur http://127.0.0.1:8769')
    print('  Orgo: non requis pour Studio; les transitions réelles exigent Orgo et un workflow autorisé')
    print('  École: aucun compte, identité ou validation officielle ici; DEMO uniquement')


def check_orgo_fixture(mission:dict,orgo_root:Path,mode:str,workflow:bool=False)->int:
    root=orgo_root.resolve()
    script=root/'tools/scenario-injector/cli.mjs'
    check(script.is_file(),'injecteur officiel Orgo introuvable: '+str(script))
    check(shutil.which('node') is not None,'Node.js requis pour utiliser l’injecteur officiel')
    check(mode in ('validate','plan'),'mode non autorisé')
    with tempfile.TemporaryDirectory(prefix='kontexte-orgo-') as temp:
        file=Path(temp)/'synthetic-orgo-fixture.json'
        file.write_text(json.dumps((synthetic_review_workflow_fixture(mission) if workflow else scenario_fixture(mission)),ensure_ascii=False,indent=2),encoding='utf-8')
        # Deliberately no 'inject' and no '--apply': no Orgo state changes.
        result=subprocess.run(['node',str(script),mode,str(file)],cwd=root,capture_output=True,text=True,timeout=45)
        print(result.stdout)
        if result.stderr:print(result.stderr,file=sys.stderr)
        return result.returncode
