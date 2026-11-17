import json,sys
R=json.load(open('matched.json'))
def setp(fid,idx,answer,box,accept=None):
    p=R[fid]['parts'][idx]; p['answer']=answer; p['box']=box; p['score']=1.0
    if accept is not None: p['accept']=accept
def show(fid):
    for i,p in enumerate(R[fid]['parts']): print(fid,i,p['answer'],[round(v) for v in p['box']] if p['box'] else None,p['score'])
exec(open(sys.argv[1]).read())
json.dump(R,open('matched.json','w'),ensure_ascii=False)
