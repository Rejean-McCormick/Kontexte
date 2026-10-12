"""Client serveur-à-serveur opt-in pour Orgo API v3, jamais appelé par le HTML élève.

On ne donne pas de jeton Orgo au navigateur. Tous les effets nécessitent un appel
explicite, un serveur d'appartenance et des permissions vérifiées côté Orgo.
"""
from __future__ import annotations
import json
import os
import re
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
from .common import check, KontexteError

UUID = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

class OrgoAPI:
    def __init__(self, base_url: str, token: str, *, local_only: bool = True):
        u=urlparse(base_url)
        check(u.scheme in ('http','https') and not u.username and not u.password and not u.query and not u.fragment, 'URL Orgo invalide')
        if local_only:
            check(u.hostname in ('localhost','127.0.0.1','::1'), 'Seul Orgo local est accepté par défaut')
        else:
            check(u.scheme == 'https', 'Orgo distant doit utiliser HTTPS')
        check(u.path.rstrip('/') == '/api/v3', 'Chemin Orgo attendu /api/v3')
        check(bool(token), 'Jeton serveur Orgo requis')
        self.url = base_url.rstrip('/')
        self.token = token

    @classmethod
    def from_environment(cls) -> 'OrgoAPI':
        return cls(os.getenv('ORGO_API_URL','http://127.0.0.1:4000/api/v3'), os.getenv('ORGO_API_TOKEN',''), local_only=os.getenv('ORGO_ALLOW_REMOTE') != 'true')

    def _request(self, path: str, *, method='GET', payload: dict | None = None, idempotency_key: str | None = None) -> dict:
        check(path and not path.startswith('/') and '..' not in path and '://' not in path, 'chemin API interdit')
        headers={'Accept':'application/json','Authorization':'Bearer '+self.token}
        if payload is not None: headers['Content-Type']='application/json'
        if idempotency_key: headers['Idempotency-Key']=idempotency_key
        data=json.dumps(payload).encode() if payload is not None else None
        req=Request(self.url+'/'+path, headers=headers, data=data, method=method)
        with urlopen(req,timeout=12) as reply: return json.loads(reply.read(1048576))

    def get_task(self, task_id: str) -> dict:
        check(bool(UUID.fullmatch(task_id)), 'UUID Task invalide')
        return self._request('tasks/'+task_id)

    def get_case(self, case_id: str) -> dict:
        check(bool(UUID.fullmatch(case_id)), 'UUID Case invalide')
        return self._request('cases/'+case_id)

    def list_tasks(self, *, case_id: str | None = None, limit: int = 50) -> dict:
        check(1 <= limit <= 100, 'limit 1..100')
        q={'limit':limit,'offset':0}
        if case_id:
            check(bool(UUID.fullmatch(case_id)), 'UUID Case invalide')
            q['case_id']=case_id
        return self._request('tasks?'+urlencode(q))

    def change_task_status(self, task_id: str, *, status: str, revision: int, reason: str, key: str) -> dict:
        check(bool(UUID.fullmatch(task_id)), 'UUID Task invalide')
        check(status in {'PENDING','IN_PROGRESS','ON_HOLD','COMPLETED','FAILED','ESCALATED','CANCELLED'},'statut non reconnu')
        check(isinstance(revision,int) and revision >= 0,'révision requise')
        check(bool(key) and len(key)<=200, 'clé idempotente requise')
        return self._request('tasks/'+task_id+'/status', method='PATCH', payload={'status':status,'revision':revision,'reason':reason[:2000]}, idempotency_key=key)
