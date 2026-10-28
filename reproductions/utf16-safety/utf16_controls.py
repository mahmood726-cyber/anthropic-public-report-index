"""Malformed-file write safety controls, using dummy byte strings."""
import argparse,json
from pathlib import Path
from harness import ROOT,call,run_case
BASE='note = "dummy"\nfruit = "APPLE"\n'
CASES={'utf16_valid':BASE.encode('utf-16'),'utf16_odd_tail':BASE.encode('utf-16')+b'\x41','utf16_odd_tail_ff':BASE.encode('utf-16')+b'\xff','utf8_valid':BASE.encode(),'utf8_invalid_tail':BASE.encode()+b'\xff','utf16be':b'\xfe\xff'+BASE.encode('utf-16be')}
def run(binary,label):
 case='malformed';work=ROOT/'runs'/label/case/'workspace'
 def prep(w):
  for n,data in CASES.items():(w/(n+'.txt')).write_bytes(data)
 reads=[call('Read',{'file_path':str(work/(n+'.txt'))},i+1) for i,n in enumerate(CASES)]
 edits=[call('Edit',{'file_path':str(work/(n+'.txt')),'old_string':'APPLE','new_string':'ORANGE'},i+101) for i,n in enumerate(CASES)]
 s,f,b=run_case(binary,label,case,[reads,edits],tools='Read,Edit',allowed='Read,Edit',prepare=prep,env_overrides={'MAX_MCP_OUTPUT_TOKENS':None})
 if s['exit_code']!=0 or s['api_requests']!=3:raise RuntimeError('Incomplete')
 got={v['tool_use_id']:v for req in f.requests[1:] for m in req.get('messages',[]) if isinstance(m.get('content'),list) for v in m['content'] if v.get('type')=='tool_result'}
 rows=[]
 for i,(n,before) in enumerate(CASES.items()):
  after=(work/(n+'.txt')).read_bytes();enc='utf-16le' if n.startswith('utf16_') else 'utf-16be' if n=='utf16be' else 'utf-8'
  expected=before.replace('APPLE'.encode(enc),'ORANGE'.encode(enc))
  rows.append({'case':n,'before_hex':before.hex(),'after_hex':after.hex(),'expected_preserving_other_bytes_hex':expected.hex(),'untouched':after==before,'exact_expected':after==expected,'tool_result':got.get('toolu_fixture_'+str(101+i))})
 out={'run':s,'rows':rows,'scope':'Dummy malformed UTF-16 byte strings; no production model or private files'}
 (b/'fixture_plan.json').write_text(json.dumps([reads,edits],indent=2),encoding='utf-8')
 (b/'utf16_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps(out,ensure_ascii=True))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',type=Path,required=True);ap.add_argument('--label',required=True);a=ap.parse_args();run(a.binary.resolve(),a.label)
