import argparse,hashlib,json
from pathlib import Path
from harness import ROOT,call,run_case
PROBES={
 'ascii':'xAy',
 'literal_one_slash':r'x\u0041y',
 'literal_two_slashes':r'x\\u0041y',
 'actual_character':'xéy',
 'invalid_hex':r'x\uZZZZy',
 'nonunicode_escape':r'x\ny',
 'windows_path_guard':r'x\u0041y C:\fixture\dummy',
 'line_separator':r'x\u2028y',
 'escaped_backslash':r'x\u005cu0041y',
 'surrogate_pair':r'x\ud83d\ude00y',
}
def run(binary,label):
 case='edit_boundary_controls'
 work=ROOT/'runs'/label/case/'workspace'
 reads=[call('Read',{'file_path':str(work/(name+'.txt'))},i+1) for i,name in enumerate(PROBES)]
 edits=[call('Edit',{'file_path':str(work/(name+'.txt')),'old_string':'BEFORE','new_string':value},i+101) for i,(name,value) in enumerate(PROBES.items())]
 summary,fixture,base=run_case(binary,label,case,[reads,edits],tools='Read,Edit',allowed='Read,Edit',seed_files={name+'.txt':'BEFORE' for name in PROBES})
 events=[json.loads(line) for line in (base/'stdout.jsonl').read_text(encoding='utf-8').splitlines()]
 executed={}
 for ev in events:
  if ev.get('type')=='assistant':
   for block in ev.get('message',{}).get('content',[]):
    if block.get('type')=='tool_use' and block.get('name')=='Edit':executed[block['id']]=block['input']
 results=[]
 for i,(name,expected) in enumerate(PROBES.items()):
  data=(work/(name+'.txt')).read_bytes()
  actual=data.decode('utf-8')
  emitted=executed.get('toolu_fixture_'+str(i+101),{}).get('new_string')
  results.append({'probe':name,'supplied_codepoints':[ord(c) for c in expected],'tool_input_codepoints':[ord(c) for c in emitted] if emitted is not None else None,'disk_codepoints':[ord(c) for c in actual],'supplied_hex':expected.encode().hex(),'disk_hex':data.hex(),'tool_input_matches_supplied':emitted==expected,'disk_matches_supplied':actual==expected,'disk_matches_tool_input':actual==emitted})
 summary['probes']=results
 (base/'fixture_plan.json').write_text(json.dumps([reads,edits],indent=2),encoding='utf-8')
 (base/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',required=True,type=Path);ap.add_argument('--label',required=True);a=ap.parse_args();run(a.binary.resolve(),a.label)
