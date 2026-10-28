"""Check untouched CSV field semantics across Edit; dummy data only."""
import argparse,csv,io,json,hashlib
from pathlib import Path
from harness import ROOT,run_case,call
CASES={
 'mixed_lf_majority':('utf-8','key,value\nnote,"alpha\r\nbeta"\nfruit,APPLE\n'),
 'mixed_crlf_majority':('utf-8','key,value\r\nnote,"alpha\nbeta"\r\nfruit,APPLE\r\n'),
 'uniform_lf':('utf-8','key,value\nnote,"alpha\nbeta"\nfruit,APPLE\n'),
 'uniform_crlf':('utf-8','key,value\r\nnote,"alpha\r\nbeta"\r\nfruit,APPLE\r\n'),
 'mixed_utf16':('utf-16','key,value\nnote,"alpha\r\nbeta"\nfruit,APPLE\n'),
 'mixed_utf8_bom':('utf-8-sig','key,value\nnote,"alpha\r\nbeta"\nfruit,APPLE\n')}
def field(text):return dict(list(csv.reader(io.StringIO(text,newline='')))[1:])['note']
def run(binary,label):
 case='csv_edits';work=ROOT/'runs'/label/case/'workspace'
 def prep(w):
  for n,(enc,text) in CASES.items():(w/(n+'.csv')).write_bytes(text.encode(enc))
 reads=[call('Read',{'file_path':str(work/(n+'.csv'))},i+1) for i,n in enumerate(CASES)]
 edits=[call('Edit',{'file_path':str(work/(n+'.csv')),'old_string':'APPLE','new_string':'ORANGE'},i+101) for i,n in enumerate(CASES)]
 s,f,b=run_case(binary,label,case,[reads,edits],tools='Read,Edit',allowed='Read,Edit',prepare=prep,env_overrides={'MAX_MCP_OUTPUT_TOKENS':None})
 if s['api_requests']<3 or s['exit_code']!=0:raise RuntimeError('Fixture did not complete')
 blocks={v['tool_use_id']:v for req in f.requests[1:] for m in req.get('messages',[]) if isinstance(m.get('content'),list) for v in m['content'] if v.get('type')=='tool_result'}
 rows=[]
 for i,(n,(enc,text)) in enumerate(CASES.items()):
  got=(work/(n+'.csv')).read_bytes();actual=got.decode(enc)
  rows.append({'case':n,'encoding':enc,'supplied_source':text,'actual_source':actual,'exact_expected':got==text.replace('APPLE','ORANGE').encode(enc),'before_note':field(text),'after_note':field(actual),'unrelated_field_preserved':field(text)==field(actual),'tool_result':blocks.get('toolu_fixture_'+str(i+101)),'before_hex':text.encode(enc).hex(),'after_hex':got.hex()})
 out={'run':s,'rows':rows,'method':'csv.reader with newline-empty StringIO preserves embedded line endings; no generated source executed'}
 (b/'fixture_plan.json').write_text(json.dumps([reads,edits],indent=2),encoding='utf-8')
 (b/'mixed_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps(out,ensure_ascii=True))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',type=Path,required=True);ap.add_argument('--label',required=True);a=ap.parse_args();run(a.binary.resolve(),a.label)
