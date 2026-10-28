import argparse,json,re,sys
from pathlib import Path
from harness import ROOT,call,run_case
def analyze(base,count):
 summary=json.loads((base/'summary.json').read_text(encoding='utf-8'))
 requests=json.loads((base/'requests.json').read_text(encoding='utf-8'))
 # Extended paths are needed because this Windows test's isolated profile can exceed MAX_PATH.
 profile=Path('\\\\?\\'+str((base/'profile').resolve())) if sys.platform=='win32' else base/'profile'
 files=[p for p in profile.rglob('*') if p.is_file() and p.parent.name=='tool-results' and p.suffix in ['.txt','.json']]
 lookup={p.name:p for p in files};results=[]
 for req in requests[1:]:
  for msg in req.get('messages',[]):
   if msg.get('role')!='user' or not isinstance(msg.get('content'),list):continue
   for block in msg['content']:
    if block.get('type')!='tool_result':continue
    ident=block.get('tool_use_id','');names=re.findall(r'(?:mcp-big-big-\d+\.txt|toolu_fixture_\d+\.json)',json.dumps(block.get('content')))
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
def run(binary,label,trial,batch,count,spacing_ms,payload_chars=2000,default_threshold=False,burst_write=False,token_count_fixture=10):
 case='mcp_'+str(batch)+'_'+str(trial)
 config=ROOT/(label+'_'+case+'_mcp.json');log=ROOT/'runs'/label/case/'calls.jsonl'
 config.write_text(json.dumps({'mcpServers':{'big':{'command':sys.executable,'args':[str(ROOT/'mcp_fixture.py'),'--batch',str(batch),'--spacing-ms',str(spacing_ms),'--log',str(log),'--payload-chars',str(payload_chars)]+(['--burst-write'] if burst_write else [])}}}),encoding='utf-8')
 plans=[[call('mcp__big__big',{'tag':'CANARY_'+str(i).zfill(2)},i+1) for i in range(count)]]
 summary,fixture,base=run_case(binary,label,case,plans,tools='',allowed='mcp__big__big',extras=['--mcp-config',str(config)],timeout=50,env_overrides={'MAX_MCP_OUTPUT_TOKENS':None} if default_threshold else None,token_count_fixture=token_count_fixture)
 (base/'fixture_plan.json').write_text(json.dumps(plans,indent=2),encoding='utf-8')
 measured=analyze(base,count)
 measured.update(payload_filler_chars=payload_chars,default_threshold=default_threshold,burst_write=burst_write,configured_spacing_ms=spacing_ms)
 (base/'summary.json').write_text(json.dumps(measured,indent=2),encoding='utf-8')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',type=Path);ap.add_argument('--label');ap.add_argument('--trial',type=int,default=1);ap.add_argument('--batch',type=int,default=10);ap.add_argument('--count',type=int,default=10);ap.add_argument('--spacing-ms',type=int,default=0);ap.add_argument('--analyze',type=Path);ap.add_argument('--payload-chars',type=int,default=2000);ap.add_argument('--default-threshold',action='store_true');ap.add_argument('--burst-write',action='store_true');ap.add_argument('--fixture-count-tokens',type=int,default=10);a=ap.parse_args()
 if a.analyze:analyze(a.analyze.resolve(),a.count)
 else:run(a.binary.resolve(),a.label,a.trial,a.batch,a.count,a.spacing_ms,a.payload_chars,a.default_threshold,a.burst_write,a.fixture_count_tokens)
