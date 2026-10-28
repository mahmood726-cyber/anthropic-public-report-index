"""Controlled fixture inputs driving real Claude Code. No real model/API used."""
import argparse,ctypes,hashlib,http.server,json,os,platform,subprocess,sys,threading,time,uuid
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class Job:
 def __init__(self,proc):
  from ctypes import wintypes as w
  class BASIC(ctypes.Structure):
   _fields_=[('PerProcessUserTimeLimit',ctypes.c_int64),('PerJobUserTimeLimit',ctypes.c_int64),('LimitFlags',w.DWORD),('MinimumWorkingSetSize',ctypes.c_size_t),('MaximumWorkingSetSize',ctypes.c_size_t),('ActiveProcessLimit',w.DWORD),('Affinity',ctypes.c_size_t),('PriorityClass',w.DWORD),('SchedulingClass',w.DWORD)]
  class IO(ctypes.Structure):
   _fields_=[(x,ctypes.c_uint64) for x in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
  class EXT(ctypes.Structure):
   _fields_=[('BasicLimitInformation',BASIC),('IoInfo',IO),('ProcessMemoryLimit',ctypes.c_size_t),('JobMemoryLimit',ctypes.c_size_t),('PeakProcessMemoryUsed',ctypes.c_size_t),('PeakJobMemoryUsed',ctypes.c_size_t)]
  k=ctypes.WinDLL('kernel32',use_last_error=True)
  k.CreateJobObjectW.argtypes=[ctypes.c_void_p,w.LPCWSTR];k.CreateJobObjectW.restype=w.HANDLE
  k.SetInformationJobObject.argtypes=[w.HANDLE,ctypes.c_int,ctypes.c_void_p,w.DWORD];k.SetInformationJobObject.restype=w.BOOL
  k.AssignProcessToJobObject.argtypes=[w.HANDLE,w.HANDLE];k.AssignProcessToJobObject.restype=w.BOOL
  k.CloseHandle.argtypes=[w.HANDLE];k.CloseHandle.restype=w.BOOL
  self.k=k;self.h=k.CreateJobObjectW(None,None)
  info=EXT();info.BasicLimitInformation.LimitFlags=0x2000
  if not self.h or not k.SetInformationJobObject(self.h,9,ctypes.byref(info),ctypes.sizeof(info)) or not k.AssignProcessToJobObject(self.h,int(proc._handle)):
   err=ctypes.get_last_error();proc.kill()
   if self.h:k.CloseHandle(self.h)
   raise OSError(err,'Cannot contain test process tree')
 def close(self):
  if self.h:self.k.CloseHandle(self.h);self.h=None
class Fixture:
 def __init__(self,plan):self.plan=plan;self.requests=[];self.count_requests=[];self.stage=0;self.lock=threading.Lock()
class Handler(http.server.BaseHTTPRequestHandler):
 def log_message(self,*a):pass
 def do_POST(self):
  b=json.loads(self.rfile.read(int(self.headers.get('Content-Length','0'))))
  if self.path.split('?')[0].endswith('count_tokens'):
   self.server.fixture.count_requests.append({'path':self.path,'fixture_response_input_tokens':self.server.fixture.token_count_value})
   data=json.dumps({'input_tokens':self.server.fixture.token_count_value}).encode();self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data);return
  f=self.server.fixture
  with f.lock:
   f.requests.append({'path':self.path,'messages':b.get('messages'),'tools':[t.get('name') for t in b.get('tools',[])],'model':b.get('model')})
   stage=f.stage;f.stage+=1
  blocks=f.plan[stage] if stage<len(f.plan) else [{'type':'text','text':'Controlled fixture complete.'}]
  stop='tool_use' if any(x['type']=='tool_use' for x in blocks) else 'end_turn'
  msg={'id':'msg_fixture_'+str(stage),'type':'message','role':'assistant','model':b.get('model','fixture'),'content':blocks,'stop_reason':stop,'stop_sequence':None,'usage':{'input_tokens':10,'output_tokens':10}}
  self.send_response(200);self.send_header('request-id','fixture-'+str(stage))
  if not b.get('stream'):
   data=json.dumps(msg).encode();self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data);return
  self.send_header('Content-Type','text/event-stream');self.send_header('Connection','close');self.end_headers()
  def emit(event,data):self.wfile.write(('event: '+event+'\ndata: '+json.dumps(data,ensure_ascii=True)+'\n\n').encode());self.wfile.flush()
  init=dict(msg);init['content']=[];init['stop_reason']=None
  emit('message_start',{'type':'message_start','message':init})
  for i,block in enumerate(blocks):
   head={'type':block['type']}
   if block['type']=='tool_use':head.update(id=block['id'],name=block['name'],input={})
   else:head['text']=''
   emit('content_block_start',{'type':'content_block_start','index':i,'content_block':head})
   delta={'type':'input_json_delta','partial_json':json.dumps(block['input'],ensure_ascii=True)} if block['type']=='tool_use' else {'type':'text_delta','text':block['text']}
   emit('content_block_delta',{'type':'content_block_delta','index':i,'delta':delta})
   emit('content_block_stop',{'type':'content_block_stop','index':i})
  emit('message_delta',{'type':'message_delta','delta':{'stop_reason':stop,'stop_sequence':None},'usage':{'output_tokens':10}})
  emit('message_stop',{'type':'message_stop'})
  self.close_connection=True
def call(name,inputs,index=1):return {'type':'tool_use','id':'toolu_fixture_'+str(index),'name':name,'input':inputs}
def run_case(binary,label,case,plan,tools='Read,Write,Edit',allowed='Read,Write,Edit',cwd=None,extras=None,timeout=60,seed_files=None,prepare=None,env_overrides=None,token_count_fixture=10):
 base=ROOT/'runs'/label/case
 if base.exists():raise RuntimeError('Refusing to overwrite existing test evidence: '+str(base))
 base.mkdir(parents=True);workspace=Path(cwd) if cwd else base/'workspace';workspace.mkdir(exist_ok=True)
 for name,data in (seed_files or {}).items():
  p=workspace/name
  if p.resolve().parent!=workspace.resolve():raise RuntimeError('Unsafe fixture path')
  p.write_text(data,encoding='utf-8')
 if prepare:prepare(workspace)
 profile=base/'profile';profile.mkdir()
 keep=['SYSTEMROOT','WINDIR','PATH','PATHEXT','TEMP','TMP','COMSPEC','USERPROFILE','LOCALAPPDATA','APPDATA','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMDATA']
 env={k:v for k,v in os.environ.items() if k.upper() in keep}
 env.update(ANTHROPIC_API_KEY='fixture-not-a-real-key',ANTHROPIC_BASE_URL='http://127.0.0.1:8000',CLAUDE_CONFIG_DIR=str(profile),CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC='1',DISABLE_AUTOUPDATER='1',DISABLE_TELEMETRY='1',NO_PROXY='127.0.0.1,localhost',MAX_MCP_OUTPUT_TOKENS='100')
 for key,value in (env_overrides or {}).items():
  if value is None:env.pop(key,None)
  else:env[key]=str(value)
 fix=Fixture(plan);fix.token_count_value=token_count_fixture;server=http.server.ThreadingHTTPServer(('127.0.0.1',8000),Handler);server.fixture=fix
 thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
 cmd=[str(binary),'--bare','-p','Run the controlled local fixture.','--model','claude-haiku-4-5-20251001','--system-prompt','You are executing a controlled dummy-data test.','--output-format','stream-json','--verbose','--permission-mode','manual','--permission-prompts','none','--strict-mcp-config','--tools',tools,'--allowedTools',allowed,'--session-id',str(uuid.uuid4()),'--max-budget-usd','1']
 cmd+=extras or []
 started=time.monotonic();timed_out=False;rc=None;stdout='';stderr=''
 try:
  proc=subprocess.Popen(cmd,cwd=workspace,env=env,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',errors='replace')
  job=Job(proc)
  try:
   try:stdout,stderr=proc.communicate(timeout=timeout);rc=proc.returncode
   except subprocess.TimeoutExpired:
    timed_out=True;job.close();stdout,stderr=proc.communicate(timeout=10);rc=proc.returncode
  finally:job.close()
 finally:server.shutdown();server.server_close();thread.join(timeout=3)
 (base/'stdout.jsonl').write_text(stdout,encoding='utf-8')
 (base/'stderr.txt').write_text(stderr,encoding='utf-8')
 (base/'requests.json').write_text(json.dumps(fix.requests,indent=2),encoding='utf-8')
 (base/'count_tokens_requests.json').write_text(json.dumps(fix.count_requests,indent=2),encoding='utf-8')
 summary={'count_tokens_requests':len(fix.count_requests),'fixture_count_tokens_response':token_count_fixture,'fixture_env_overrides':env_overrides or {},'case':case,'binary_label':label,'exit_code':rc,'timeout':timed_out,'elapsed_seconds':round(time.monotonic()-started,3),'api_requests':len(fix.requests),'fixture_tool_calls':sum(len([x for x in stage if x['type']=='tool_use']) for stage in plan),'workspace':str(workspace),'profile':str(profile),'binary_sha256':hashlib.file_digest(open(binary,'rb'),'sha256').hexdigest(),'platform':platform.platform(),'python':sys.version.split()[0],'transport':'loopback fixture API, not a production model','stdout_sha256':hashlib.sha256(stdout.encode()).hexdigest()}
 (base/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 return summary,fix,base
