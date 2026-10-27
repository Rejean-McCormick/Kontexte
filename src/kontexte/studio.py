"""Teacher-only loopback rehearsal studio. NOT an Orgo workflow/runtime.

All mission states in the interface are simulated in the browser and disposable.
The service does not authenticate students, synchronize teams, or authorize clues.
Never bind this development-only server to a shared interface.
"""
from __future__ import annotations
import json
import secrets
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from importlib.resources import files
from urllib.parse import urlsplit, parse_qs
from .common import KontexteError, load_json, check
from .cli import read_all
from .assessment import invitation_paper, lanterns, validate_numeric_answer
from .economy import bill
from .media import public_manifest
from .evidence import record, list_events
from .ekole import aggregate

MAX_BODY = 24_000
ASSETS = {'/': ('index.html','text/html; charset=utf-8'), '/app.js': ('app.js','text/javascript; charset=utf-8'), '/style.css': ('style.css','text/css; charset=utf-8')}
LEVELS = ('accompagne','standard','approfondi')


def valid_loopback_host(value: str, port: int) -> bool:
    """Accept only the actual local Studio host/port, including bracketed IPv6.

    Parsing the Host header as a URL authority avoids truncating ``[::1]`` at
    its first colon and rejects malformed or mismatched-port authorities.
    """
    if not isinstance(value, str) or not value or value != value.strip():
        return False
    try:
        target = urlsplit('http://' + value)
        return (target.hostname in ('127.0.0.1', 'localhost', '::1')
                and target.port in (None, port)
                and target.username is None and target.password is None
                and not target.path and not target.query and not target.fragment)
    except ValueError:
        return False


def catalogue_for_studio(repo:Path)->dict:
    catalogue,roles,missions=read_all(repo)
    root=repo/'data/locales/qc/fr-CA/grade3'
    overlays=load_json(root/'overlays-60.json')['items']
    neutral=load_json(repo/'data/trames/catalogue-neutral-v0.2.json')['scenarios']
    exercises=load_json(root/'exercices-deterministes.json')['exercices']
    year=load_json(root/'parcours-36-semaines.json')
    return {'curriculum':catalogue,'roles':roles,'missions':missions,
        'overlays':{x['base_trame_id']:x for x in overlays},'neutral':{x['id']:x for x in neutral},
        'exercises':{x['scenario_id']:x for x in exercises},'year':year}


def exercise_check(data: dict, catalogue:dict)->dict:
    key=data.get('key'); answer=data.get('answer'); level=data.get('level','standard')
    check(isinstance(answer,str) and len(answer)<=80, 'réponse numérique invalide')
    check(level in LEVELS,'profil invalide')
    if key=='solo-measure':
        quantity={'accompagne':2,'standard':4,'approfondi':8}[level]
        expected=str(quantity*125)
    elif key=='duo-paper':
        q,per,stock={'accompagne':(4,2,1),'standard':(6,2,2),'approfondi':(9,2,3)}[level]
        expected=str(invitation_paper(invitations=q,per_sheet=per,available_sheets=stock)['missing_sheets'])
    elif isinstance(key,str) and key.startswith('qc3:') and key[4:] in catalogue['exercises']:
        expected=str(catalogue['exercises'][key[4:]]['answer'])
    else:
        raise KontexteError('Exercice inconnu ou réservé à une revue humaine')
    result=validate_numeric_answer(answer,expected)
    return {'correct':result['correct'],'feedback':('Bonne réponse (vérification arithmétique seulement).' if result['correct'] else 'Essaie une nouvelle fois ou demande un indice.'),'evidence_status':'practice_only','student_mastery_inferred':False}


def dispatch(method:str,path:str, data:dict, ctx:dict, query:dict) -> tuple[int,dict]:
    c=ctx['catalogue']
    if method=='GET':
        if path=='/api/health':return 200, {'ok':True,'mode':'loopback_teacher_rehearsal','orgo_connected':False,'authentication':False}
        if path=='/api/catalogue':
            return 200,{'format':'kontexte.studio-catalogue/1','roles':[{'id':k,'name':v['name']} for k,v in c['roles'].items()],
                'missions':[{'id':m['id'],'title':m['title'],'roles':m['roles'],'year_suggestion':m['year_suggestion']} for m in c['missions'].values()],
                'scenarios':[{'id':n['id'],'family':n['famille'],'title':n['titre'],'qc_title':c['overlays'][n['id']]['titre_qc'],'stage':c['overlays'][n['id']]['etape_suggeree'],'has_numeric_exercise':n['id'] in c['exercises']} for n in c['neutral'].values()],
                'exercises':[{'key':'qc3:'+x['scenario_id'],'scenario_id':x['scenario_id'],'question':x['question'],'unit':x['unit']} for x in c['exercises'].values()],
                'year':c['year']['semaines'],'counts':{'roles':len(c['roles']),'missions':len(c['missions']),'scenarios':len(c['neutral']),'exercises':len(c['exercises'])}}
        if path=='/api/scenario':
            sid=query.get('id',[''])[0]
            check(sid in c['overlays'],'trame inconnue')
            # These are fictitious design fragments, deliberately BOTH visible in the teachers-only rehearsal.
            return 200,{'overlay':c['overlays'][sid], 'neutral':c['neutral'][sid], 'rehearsal_only':True}
        if path=='/api/mission':
            mid=query.get('id',[''])[0]
            check(mid in c['missions'],'mission inconnue')
            return 200,{'mission':c['missions'][mid],'rehearsal_only':True}
        if path=='/api/role':
            rid=query.get('id',[''])[0]
            check(rid in c['roles'],'rôle inconnu')
            return 200,{'role':c['roles'][rid]}
        if path=='/api/school-event':
            return 200,{'event':load_json(ctx['repo']/'data/events/fete-sorciere-toute-ecole.json')}
        if path=='/api/evidence':
            check(query.get('student',[''])[0] in {'demo-001','demo-002'},'identifiant fictif requis')
            student=query['student'][0]
            events=list_events(ctx['evidence_db'],student) if ctx['evidence_db'].exists() else []
            return 200,{'report':aggregate(events,c['curriculum']),'events':events,'fictional':True}
    elif method=='POST':
        if path=='/api/check':return 200,exercise_check(data,c)
        if path=='/api/bill':
            check(isinstance(data.get('items'),list) and len(data['items'])<=30,'lignes invalides')
            return 200,bill(data['items'],fictional_tax_rate=str(data.get('fictional_tax_rate','0.10')))
        if path=='/api/privacy':
            return 200,public_manifest(data['asset'],data['audience'],data['consents'])
        if path=='/api/practice':
            # The teacher lab only records synthetic practice; never a validated competency.
            check(data.get('student') in ('demo-001','demo-002'),'seuls les élèves fictifs sont permis')
            check(data.get('mission_id') in c['missions'],'mission inconnue')
            mission=c['missions'][data['mission_id']]
            step=next((s for s in mission['steps'] if s['id']==data.get('step_id')),None)
            check(step is not None and step.get('curriculum_ids'),'étape sans référence de cours')
            cid=data.get('curriculum_id')
            check(cid in step['curriculum_ids'],'référence de cours non liée à l’étape')
            from datetime import datetime,timezone
            event={'format':'kontexte.evidence/1','id':'lab-'+secrets.token_hex(10),
                'student_ref':data['student'],'curriculum_id':cid,'mission_id':mission['id'],
                'step_id':step['id'],'status':'practiced','validation_mode':'deterministic_practice',
                'evidence_ref':'synthetic-lab/'+secrets.token_hex(8),'support_level':data.get('level','standard'),
                'occurred_at':datetime.now(timezone.utc).isoformat()}
            check(event['support_level'] in LEVELS,'profil invalide')
            record(ctx['evidence_db'],event,c['curriculum'])
            return 200,{'recorded':True,'status':'practiced','validated':False,'synthetic':True}
    raise KontexteError('Route ou méthode inconnue')


def serve(repo:Path, *, host='127.0.0.1',port=8769,open_browser=True,db=None):
    check(host in ('127.0.0.1','localhost','::1'),'Le Studio est réservé au loopback')
    check(0<=port<=65535,'Port invalide')
    repo=repo.resolve()
    content=catalogue_for_studio(repo)
    nonce=secrets.token_urlsafe(32)
    db=Path(db or (repo/'.local'/'studio-demo.sqlite')).resolve()
    # Never accept a database outside this repository's .local folder.
    check(db.parent==(repo/'.local').resolve(), 'base du studio doit rester dans .local/')
    db.parent.mkdir(exist_ok=True)
    context={'repo':repo,'catalogue':content,'csrf':nonce,'evidence_db':db}

    class Handler(BaseHTTPRequestHandler):
        server_version='KontexteStudio/0.4'
        def log_message(self,format,*args):
            print('[Kontexte Studio]',format%args)
        def valid_host(self):
            return valid_loopback_host(self.headers.get('Host', ''), self.server.server_port)
        def respond(self,status:int,content:bytes,mime:str):
            self.send_response(status)
            self.send_header('Content-Type',mime)
            self.send_header('Content-Length',str(len(content)))
            self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('X-Frame-Options','DENY')
            self.send_header('Referrer-Policy','no-referrer')
            self.send_header('Content-Security-Policy',"default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
            self.end_headers();self.wfile.write(content)
        def process(self,method):
            if not self.valid_host():
                self.respond(403,b'{"error":"invalid host"}','application/json');return
            parsed=urlsplit(self.path)
            if method=='GET' and parsed.path in ASSETS:
                name,mime=ASSETS[parsed.path]
                b=files('kontexte').joinpath('studio_assets',name).read_bytes()
                self.respond(200,b,mime);return
            if parsed.path=='/api/session' and method=='GET':
                data=json.dumps({'csrf':nonce,'demo':True,'mode':'teacher_local_only'}).encode()
                self.respond(200,data,'application/json');return
            if not parsed.path.startswith('/api/'):
                self.respond(404,b'not found','text/plain');return
            if method=='POST':
                if self.headers.get('X-Kontexte-Token')!=nonce:
                    self.respond(403,b'{"error":"invalid local lab token"}','application/json');return
                origin=self.headers.get('Origin')
                if origin:
                    try:
                        parsed_origin=urlsplit(origin)
                        allowed_origin=(parsed_origin.scheme == 'http'
                            and parsed_origin.hostname in ('127.0.0.1','localhost')
                            and parsed_origin.port == self.server.server_port)
                    except ValueError:
                        allowed_origin=False
                    if not allowed_origin:
                        self.respond(403,b'{"error":"invalid origin"}','application/json');return
                try:
                    size=int(self.headers.get('Content-Length','0'))
                    check(0<size<=MAX_BODY,'requête trop volumineuse')
                    payload=json.loads(self.rfile.read(size))
                    check(isinstance(payload,dict),'objet JSON attendu')
                except (ValueError,UnicodeError,JsonDecodeError,KontexteError) as e:
                    self.respond(400,json.dumps({'error':str(e)}).encode(),'application/json');return
            else:payload={}
            try:
                code,data=dispatch(method,parsed.path,payload,context,parse_qs(parsed.query))
                encoded=json.dumps(data,ensure_ascii=False,default=str).encode('utf-8')
                check(len(encoded)<=2_000_000,'réponse trop volumineuse')
                self.respond(code,encoded,'application/json; charset=utf-8')
            except (KontexteError,KeyError,TypeError,ValueError) as e:
                self.respond(400,json.dumps({'error':str(e)},ensure_ascii=False).encode(),'application/json; charset=utf-8')
            except OSError:
                self.respond(500,b'{"error":"Local file error"}','application/json')
        def do_GET(self):self.process('GET')
        def do_POST(self):self.process('POST')
    # BaseHTTPRequestHandler error type only declared as a catchable ValueError above.
    from json import JSONDecodeError as JsonDecodeError
    srv=ThreadingHTTPServer((host,port),Handler)
    address=f'http://127.0.0.1:{srv.server_port}/'
    print('Kontexte Studio — environnement de répétition fictif (sans comptes élèves)')
    print('Ouvrir :',address)
    print('Arrêter : Ctrl+C')
    if open_browser:
        import webbrowser
        webbrowser.open(address)
    try:srv.serve_forever(poll_interval=.2)
    except KeyboardInterrupt:pass
    finally:srv.server_close()
