import argparse,json,os,subprocess
from pathlib import Path
from harness import ROOT,call,run_case
def prepare(work):
 empty=work/'.empty-template';empty.mkdir()
 env=dict(os.environ);env['GIT_CONFIG_GLOBAL']=os.devnull;env['GIT_CONFIG_SYSTEM']=os.devnull
 subprocess.run(['git','init','--quiet','--template='+str(empty)],cwd=work,env=env,check=True,capture_output=True)
 subprocess.run(['git','-c','user.name=Fixture','-c','user.email=fixture@example.invalid','-c','commit.gpgsign=false','-c','core.hooksPath='+str(empty),'commit','--quiet','--allow-empty','-m','controlled fixture'],cwd=work,env=env,check=True,capture_output=True)
def run(binary,label):
 cases={'allowed_prefix':'git log --oneline -1','standalone_write':"printf 'permission-fixture' > permission-canary.txt",'semicolon_write':"git log --oneline -1; printf 'permission-fixture' > permission-canary.txt",'and_write':"git log --oneline -1 && printf 'permission-fixture' > permission-canary.txt"}
 out=[]
 for name,command in cases.items():
  result,fixture,base=run_case(binary,label,'permission_'+name,[[call('Bash',{'command':command,'description':'Controlled local permission boundary check'})]],tools='Bash',allowed='Bash(git log:*)',prepare=prepare)
  result['tools_offered']=fixture.requests[0]['tools'] if fixture.requests else []
  result['canary_created']=(base/'workspace'/'permission-canary.txt').exists()
  result['command']=command
  msgs=[block for req in fixture.requests[1:] for msg in req.get('messages',[]) if msg.get('role')=='user' and isinstance(msg.get('content'),list) for block in msg['content'] if block.get('type')=='tool_result']
  result['tool_results']=list({b['tool_use_id']:b for b in msgs}.values())
  (base/'fixture_plan.json').write_text(json.dumps([[call('Bash',{'command':command,'description':'Controlled local permission boundary check'})]],indent=2),encoding='utf-8')
  (base/'summary.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
  out.append({k:v for k,v in result.items() if k not in ['workspace','profile']})
 print(json.dumps(out,indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--binary',type=Path,required=True);ap.add_argument('--label',required=True);a=ap.parse_args();run(a.binary.resolve(),a.label)
