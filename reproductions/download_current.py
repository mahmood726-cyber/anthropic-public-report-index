import argparse,base64,hashlib,json,tarfile,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def read(url):
 req=urllib.request.Request(url,headers={'User-Agent':'source-linked-reproduction/1.0'})
 with urllib.request.urlopen(req,timeout=45) as r:return r.read()
meta=json.loads(read('https://registry.npmjs.org/@anthropic-ai/claude-code-win32-x64/2.1.312'))
dist=meta['dist']; archive=read(dist['tarball'])
algorithm,expected=dist['integrity'].split('-',1)
actual=base64.b64encode(hashlib.new(algorithm,archive).digest()).decode()
if actual!=expected:raise RuntimeError('Package integrity mismatch')
target=ROOT/'binaries'/'2.1.312';target.mkdir(parents=True,exist_ok=True)
package=target/'package.tgz';package.write_bytes(archive)
with tarfile.open(package,'r:gz') as t:
 members=[m for m in t.getmembers() if m.isfile() and m.name.endswith('/claude.exe')]
 if len(members)!=1:raise RuntimeError('Ambiguous binary')
 binary=t.extractfile(members[0]).read()
 (target/'claude.exe').write_bytes(binary)
manifest={'package':meta['name'],'version':meta['version'],'tarball':dist['tarball'],'integrity':dist['integrity'],'integrity_verified':True,'binary_sha256':hashlib.sha256(binary).hexdigest(),'binary_bytes':len(binary)}
(target/'provenance.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest))
