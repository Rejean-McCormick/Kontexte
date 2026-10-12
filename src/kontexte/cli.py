"""Outils statiques Kontexte. Aucun passage implicite à Orgo; injection explicite via outil officiel."""
from __future__ import annotations
import argparse
from html import escape
import json
from pathlib import Path
import sys
from .common import KontexteError, load_json, dump_json
from .models import validate_role, validate_mission, curriculum_index
from .render import project
from .orgo import scenario_fixture, integration_manifest
from .ekole import check_curriculum, aggregate
from .evidence import record, list_events
from .economy import bill
from .media import public_manifest

ROOT = Path(__file__).resolve().parents[2]

def locate(repo: Path, kind: str, key: str) -> Path:
    return repo / 'data' / kind / f'{key}.json'

def read_all(repo: Path):
    catalogue=curriculum_index(load_json(repo/'data/catalogue/202_kristals.json'))
    roles={}
    for file in sorted((repo/'data/roles').glob('*.json')):
        r=validate_role(load_json(file)); roles[r['id']]=r
    missions={}
    for file in sorted((repo/'data/missions').glob('*.json')):
        m=validate_mission(load_json(file),catalogue)
        if not set(m['roles']) <= set(roles): raise KontexteError(f'{file.name}: rôle manquant')
        missions[m['id']]=m
    return catalogue,roles,missions

def write_site(repo:Path, out:Path, *, language:str='fr-CA') -> int:
    _, roles, missions=read_all(repo)
    out.mkdir(parents=True,exist_ok=True)
    links=[]
    for mission in missions.values():
        for rid in mission['roles']:
            role=roles[rid]; name=f'{mission["id"]}--{rid}.html'
            (out/name).write_text(project(mission,role,lang=language),encoding='utf-8')
            links.append(f'<li><a href="{escape(name)}">{escape(mission["title"].get(language,mission["title"]["fr-CA"]))} — {escape(role["name"].get(language,role["name"]["fr-CA"]))}</a></li>')
    styles='body{font:1.1rem/1.6 system-ui;background:#f5f0e8;color:#2f2340;max-width:840px;margin:2rem auto;padding:2rem}a{color:#503184}li{padding:.3rem}'
    (out/'index.html').write_text('<!doctype html><html lang="fr-CA"><meta charset="utf-8"><title>Kontexte – Catalogue</title><style>'+styles+'</style><h1>Kontexte</h1><p>Pages de démonstration statiques, sans comptes d’élèves, orchestration ou données personnelles. Orgo demeure seul propriétaire des états de mission.</p><ul>'+''.join(links)+'</ul></html>',encoding='utf-8')
    return len(links)

def main(argv=None) -> int:
    p=argparse.ArgumentParser(prog='kontexte',description='Créer des projections et des fixtures sans dupliquer Orgo')
    p.add_argument('--repo',type=Path,default=ROOT)
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    sub.add_parser('list')
    for name in ('orgo-fixture','orgo-blueprint','curriculum','preview'):
        pp=sub.add_parser(name);pp.add_argument('mission');pp.add_argument('--out',type=Path,required=True)
        if name=='preview':
            pp.add_argument('--role',required=True); pp.add_argument('--lang',choices=['fr-CA','en'],default='fr-CA')
            pp.add_argument('--profile',choices=['accompagne','standard','approfondi'],default='standard')
            pp.add_argument('--demo-fragments',action='store_true',help='UNIQUEMENT aperçu hors ligne sans élèves')
    site=sub.add_parser('site');site.add_argument('--out',type=Path,required=True);site.add_argument('--lang',choices=['fr-CA','en'],default='fr-CA')
    bd=sub.add_parser('bill');bd.add_argument('--input',type=Path,required=True);bd.add_argument('--out',type=Path,required=True)
    privacy=sub.add_parser('privacy');privacy.add_argument('--input',type=Path,required=True);privacy.add_argument('--out',type=Path,required=True)
    ev=sub.add_parser('evidence-add');ev.add_argument('--input',type=Path,required=True);ev.add_argument('--db',type=Path,required=True)
    rep=sub.add_parser('evidence-report');rep.add_argument('--db',type=Path,required=True);rep.add_argument('--student',required=True);rep.add_argument('--out',type=Path,required=True)
    args=p.parse_args(argv)
    repo=args.repo.resolve()
    try:
        catalogue,roles,missions=read_all(repo)
        if args.command=='validate':
            print(f'OK: {len(roles)} rôles, {len(missions)} missions, {len(catalogue)} références Ekole internes')
            return 0
        if args.command=='list':
            print('Rôles:',', '.join(sorted(roles))); print('Missions:',', '.join(sorted(missions)))
            return 0
        if args.command=='site':
            count=write_site(repo,args.out,language=args.lang)
            print(f'{count} pages écrites dans {args.out}');return 0
        if args.command in ('orgo-fixture','orgo-blueprint','curriculum','preview'):
            if args.mission not in missions: raise KontexteError('mission inconnue: '+args.mission)
            m=missions[args.mission]
            if args.command=='orgo-fixture':
                dump_json(scenario_fixture(m),args.out)
            if args.command=='orgo-blueprint':
                dump_json(integration_manifest(m),args.out)
            if args.command=='curriculum':
                dump_json({'format':'kontexte.curriculum-links/1','links':check_curriculum(m,catalogue)},args.out)
            if args.command=='preview':
                if args.role not in m['roles']: raise KontexteError('rôle absent de mission')
                ids=tuple(f['id'] for f in m['fragments'] if f['holder_role']==args.role) if args.demo_fragments else ()
                args.out.parent.mkdir(parents=True,exist_ok=True)
                args.out.write_text(project(m,roles[args.role],lang=args.lang,adaptation=args.profile,authorized_fragment_ids=ids,trusted_authorization=args.demo_fragments),encoding='utf8')
            print(f'Écrit: {args.out}');return 0
        if args.command=='bill':
            d=load_json(args.input)
            dump_json(bill(d['items'],fictional_tax_rate=d.get('fictional_tax_rate','0')),args.out)
            print(f'Écrit: {args.out}');return 0
        if args.command=='privacy':
            d=load_json(args.input)
            dump_json(public_manifest(d['asset'],d['audience'],d['consents']),args.out)
            print(f'Écrit: {args.out}');return 0
        if args.command=='evidence-add':
            print('Ajout:',record(args.db,load_json(args.input),catalogue))
            return 0
        if args.command=='evidence-report':
            dump_json(aggregate(list_events(args.db,args.student),catalogue),args.out)
            print(f'Écrit: {args.out}');return 0
    except (KontexteError, KeyError, ValueError, OSError) as exc:
        print(f'Erreur : {exc}',file=sys.stderr);return 2
    return 2

if __name__=='__main__':raise SystemExit(main())
