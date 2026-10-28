"""Dummy stdio MCP server. Replies contain only synthetic tag plus filler."""
import argparse,json,sys,time
ap=argparse.ArgumentParser();ap.add_argument('--batch',type=int,default=10);ap.add_argument('--log',required=True);ap.add_argument('--spacing-ms',type=int,default=0);a=ap.parse_args()
pending=[]
def emit(msg):sys.stdout.write(json.dumps(msg)+'\n');sys.stdout.flush()
for line in sys.stdin:
 try:q=json.loads(line)
 except json.JSONDecodeError:continue
 method=q.get('method');ident=q.get('id')
 if method=='initialize':emit({'jsonrpc':'2.0','id':ident,'result':{'protocolVersion':q.get('params',{}).get('protocolVersion','2024-11-05'),'capabilities':{'tools':{}},'serverInfo':{'name':'controlled-big-results','version':'1.0'}}})
 elif method=='tools/list':emit({'jsonrpc':'2.0','id':ident,'result':{'tools':[{'name':'big','description':'Return a synthetic canary tag plus filler; no user data.','inputSchema':{'type':'object','properties':{'tag':{'type':'string'}},'required':['tag']},'annotations':{'readOnlyHint':True,'destructiveHint':False}}]}})
 elif method=='tools/call':
  tag=q.get('params',{}).get('arguments',{}).get('tag','MISSING')
  with open(a.log,'a',encoding='utf-8') as f:f.write(json.dumps({'id':ident,'tag':tag,'received_ns':time.time_ns()})+'\n')
  pending.append({'jsonrpc':'2.0','id':ident,'result':{'content':[{'type':'text','text':tag+':'+('X'*2000)}]}})
  if len(pending)>=a.batch:
   
   for x in pending:
    sys.stdout.write(json.dumps(x)+'\n');sys.stdout.flush()
    if a.spacing_ms:time.sleep(a.spacing_ms/1000)
   pending.clear()
 elif ident is not None:emit({'jsonrpc':'2.0','id':ident,'result':{}})
