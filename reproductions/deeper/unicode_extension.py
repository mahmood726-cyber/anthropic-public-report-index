import argparse,ast,json,sys
from pathlib import Path
from harness import ROOT,call,run_case
from unicode_controls import PROBES
def mcp_inputs(binary):
 label='deeper-unicode-mcp-utf8';case='argument_controls'
 log=ROOT/'runs'/label/case/'calls.jsonl';config=ROOT/'deeper_unicode_mcp.json'
 config.write_text(json.dumps({'mcpServers':{'big':{'command':sys.executable,'args':[str(ROOT/'mcp_fixture.py'),'--batch','1','--payload-chars','0','--log',str(log)]}}}),encoding='utf-8')
 plan=[[call('mcp__big__big',{'tag':name+'|'+value},i+1) for i,(name,value) in enumerate(PROBES.items())]]
 summary,fix,base=run_case(binary,label,case,plan,tools='',allowed='mcp__big__big',extras=['--mcp-config',str(config)],env_overrides={'MAX_MCP_OUTPUT_TOKENS':None})
 received={}
 if log.exists():
  for line in log.read_text(encoding='utf-8').splitlines():
   row=json.loads(line);name,value=row['tag'].split('|',1);received[name]=value
 rows=[{'probe':name,'supplied_codepoints':list(map(ord,value)),'received_codepoints':list(map(ord,received[name])) if name in received else None,'preserved':received[name]==value if name in received else None} for name,value in PROBES.items()]
 summary.update(probes=rows,received_probe_count=len(received),rewritten_count=sum(r['preserved'] is False for r in rows))
 (base/'fixture_plan.json').write_text(json.dumps(plan,indent=2),encoding='utf-8')
 (base/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 print(json.dumps({'case':'MCP inputs','exit':summary['exit_code'],'received':len(received),'rewritten':summary['rewritten_count'],'rows':rows},ensure_ascii=True))
def code_semantics(binary):
 label='deeper-code-semantics';case='raw_string_fixture'
 supplied={'literal':r'sample = r"x\u0041y"'+'\n','with_path_comment':r'sample = r"x\u0041y"'+'\n'+r'# Q:\fixture\dummy'+'\n','ordinary':'sample = "xAy"\n'}
 work=ROOT/'runs'/label/case/'workspace'
 reads=[call('Read',{'file_path':str(work/(name+'.py'))},i+1) for i,name in enumerate(supplied)]
 edits=[call('Edit',{'file_path':str(work/(name+'.py')),'old_string':'BEFORE','new_string':value},i+101) for i,(name,value) in enumerate(supplied.items())]
 summary,fix,base=run_case(binary,label,case,[reads,edits],tools='Read,Edit',allowed='Read,Edit',seed_files={name+'.py':'BEFORE' for name in supplied},env_overrides={'MAX_MCP_OUTPUT_TOKENS':None})
 rows=[]
 def value(text):
  tree=ast.parse(text)
  if len(tree.body)!=1 or not isinstance(tree.body[0],ast.Assign):raise RuntimeError('Fixture shape changed')
  return ast.literal_eval(tree.body[0].value)
 for name,before in supplied.items():
  actual=(work/(name+'.py')).read_text(encoding='utf-8')
  expected_value=value(before);actual_value=value(actual)
  rows.append({'probe':name,'supplied_source':before,'written_source':actual,'supplied_value_codepoints':list(map(ord,expected_value)),'written_value_codepoints':list(map(ord,actual_value)),'semantic_value_preserved':expected_value==actual_value,'evaluation':'AST parsing and literal evaluation only; generated code was not executed'})
 summary['probes']=rows
 (base/'fixture_plan.json').write_text(json.dumps([reads,edits],indent=2),encoding='utf-8')
 (base/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 print(json.dumps({'case':'source semantics','exit':summary['exit_code'],'rows':rows},ensure_ascii=True))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',type=Path,required=True);ap.add_argument('--case',choices=['mcp','semantics'],required=True);a=ap.parse_args()
 (mcp_inputs if a.case=='mcp' else code_semantics)(a.binary.resolve())
