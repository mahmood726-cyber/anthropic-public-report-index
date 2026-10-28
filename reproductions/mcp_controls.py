import argparse,json,re,sys
from pathlib import Path
from harness import ROOT,call,run_case
def analyze(base,count):
 summary=json.loads((base/'summary.json').read_text(encoding='utf-8'))
 requests=json.loads((base/'requests.json').read_text(encoding='utf-8'))
 # Extended paths are needed because this Windows test's isolated profile can exceed MAX_PATH.
 profile=Path('\\\\?\\'+str((base/'profile').resolve())) if sys.platform=='win32' else base/'profile'
 files=list(profile.rglob('mcp-big-big-*.txt'))
 lookup={p.name:p for p in files};results=[]
 for req in requests[1:]:
  for msg in req.get('messages',[]):
   if msg.get('role')!='user' or not isinstance(msg.get('content'),list):continue
   for block in msg['content']:
    if block.get('type')!='tool_result':continue
    ident=block.get('tool_use_id','');names=re.findall(r'mcp-big-big-\d+\.txt',json.dumps(block.get('content')))
    if not names:continue
    name=names[0];p=lookup.get(name)
    tagmatch=re.search(r'CANARY_\d+',p.read_text(encoding='utf-8')) if p else None
    expected='CANARY_'+str(int(ident.rsplit('_',1)[1])-1).zfill(2)
    results.append({'tool_use_id':ident,'expected_tag':expected,'returned_file':name,'file_tag':tagmatch.group(0) if tagmatch else None,'correct_association':tagmatch.group(0)==expected if tagmatch else None})
 results=list({r['tool_use_id']:r for r in results}.values())
 log=base/'calls.jsonl';calls=[json.loads(x) for x in log.read_text(encoding='utf-8').splitlines()] if log.exists() else []
 summary.update(mcp_calls=len(calls),saved_files=len(files),tools_offered=requests[0]['tools'] if requests else [],associations=results,association_mismatches=sum(r['correct_association'] is False for r in results),unresolved_associations=sum(r['correct_association'] is None for r in results),complete_association_coverage=len(results)==count and all(r['file_tag'] for r in results),analysis_note='Windows extended-length paths used for file enumeration; missing files are unknown, not classified as a substitution.')
 (base/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in summary.items() if k not in ['workspace','profile']},indent=2))
 return summary
def run(binary,label,trial,batch,count,spacing_ms):
 case='mcp_'+str(batch)+'_'+str(trial)
 config=ROOT/(label+'_'+case+'_mcp.json');log=ROOT/'runs'/label/case/'calls.jsonl'
 config.write_text(json.dumps({'mcpServers':{'big':{'command':sys.executable,'args':[str(ROOT/'mcp_fixture.py'),'--batch',str(batch),'--spacing-ms',str(spacing_ms),'--log',str(log)]}}}),encoding='utf-8')
 plans=[[call('mcp__big__big',{'tag':'CANARY_'+str(i).zfill(2)},i+1) for i in range(count)]]
 summary,fixture,base=run_case(binary,label,case,plans,tools='',allowed='mcp__big__big',extras=['--mcp-config',str(config)],timeout=50)
 (base/'fixture_plan.json').write_text(json.dumps(plans,indent=2),encoding='utf-8')
 analyze(base,count)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',type=Path);ap.add_argument('--label');ap.add_argument('--trial',type=int,default=1);ap.add_argument('--batch',type=int,default=10);ap.add_argument('--count',type=int,default=10);ap.add_argument('--spacing-ms',type=int,default=0);ap.add_argument('--analyze',type=Path);a=ap.parse_args()
 if a.analyze:analyze(a.analyze.resolve(),a.count)
 else:run(a.binary.resolve(),a.label,a.trial,a.batch,a.count,a.spacing_ms)
