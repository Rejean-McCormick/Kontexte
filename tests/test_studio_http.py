"""Live HTTP smoke checks against the loopback-only teacher rehearsal server."""
import json, os, socket, subprocess, sys, time, unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
ROOT=Path(__file__).resolve().parents[1]

class StudioHTTP(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  with socket.socket() as sock:
   sock.bind(('127.0.0.1',0));cls.port=sock.getsockname()[1]
  env=os.environ.copy();env['PYTHONPATH']=str(ROOT/'src')
  cls.process=subprocess.Popen([sys.executable,'-m','kontexte','lab','--port',str(cls.port),'--no-browser'],cwd=ROOT,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  for i in range(50):
   try:
    with urlopen(f'http://127.0.0.1:{cls.port}/api/health',timeout=.4) as r:
     if r.status==200:break
   except (OSError,TimeoutError):time.sleep(.1)
  else:
   cls.process.terminate();raise RuntimeError('Studio failed to start')
 @classmethod
 def tearDownClass(cls):
  cls.process.terminate()
  try:cls.process.wait(timeout=3)
  except subprocess.TimeoutExpired:cls.process.kill()
 def call(self,path,payload=None,headers=None):
  h=headers or {}
  data=json.dumps(payload).encode() if payload is not None else None
  if data:h.setdefault('Content-Type','application/json')
  req=Request(f'http://127.0.0.1:{self.port}'+path,data=data,headers=h)
  with urlopen(req,timeout=2) as response:
   return response, json.load(response)
 def test_html_resources(self):
  for path in ('/','/style.css','/app.js'):
   with urlopen(f'http://127.0.0.1:{self.port}'+path,timeout=2) as response:
    self.assertEqual(response.status,200)
    self.assertIn('no-store',response.headers.get('Cache-Control',''))
 def test_search_and_data(self):
  r,data=self.call('/api/catalogue')
  self.assertEqual(data['counts']['scenarios'],60)
  _,detail=self.call('/api/scenario?id=fete-commune')
  self.assertEqual(detail['overlay']['base_trame_id'],'fete-commune')
 def test_post_requires_local_token(self):
  with self.assertRaises(HTTPError) as error:self.call('/api/check',{'key':'solo-measure','answer':'500'})
  self.assertEqual(error.exception.code,403)
  _,session=self.call('/api/session')
  _,r=self.call('/api/check',{'key':'solo-measure','answer':'500'},{'X-Kontexte-Token':session['csrf']})
  self.assertTrue(r['correct'])
 def test_local_host_header_accepts_ipv6_brackets_and_correct_port(self):
  for authority in (f'127.0.0.1:{self.port}',f'localhost:{self.port}',f'[::1]:{self.port}'):
   with self.subTest(authority=authority):
    req=Request(f'http://127.0.0.1:{self.port}/api/health',headers={'Host':authority})
    with urlopen(req,timeout=2) as response:self.assertEqual(response.status,200)
 def test_host_header_rejects_wrong_port_and_malformed_authorities(self):
  for authority in ('localhost:99999','localhost:notaport','[::1','localhost/evil',
                    '127.0.0.1:9','localhost@evil.invalid'):
   with self.subTest(authority=authority):
    req=Request(f'http://127.0.0.1:{self.port}/api/health',headers={'Host':authority})
    with self.assertRaises(HTTPError) as err:urlopen(req,timeout=2)
    self.assertEqual(err.exception.code,403)
 def test_dns_rebinding_host_denied(self):
  req=Request(f'http://127.0.0.1:{self.port}/api/health',headers={'Host':'evil.invalid'})
  with self.assertRaises(HTTPError) as error:urlopen(req,timeout=2)
  self.assertEqual(error.exception.code,403)

if __name__=='__main__':unittest.main()
