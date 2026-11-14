import json,re
r=json.load(open('cand_blanks.json'))
rej=set(); rejfig=set(); fix={}
for ln in open('review.txt'):
    ln=ln.strip()
    if not ln or ln.startswith('#'): continue
    k,_,v=ln.partition(' ')
    if v=='XX': rejfig.add(k)
    elif v=='X': rej.add(k)
    elif v.startswith('='): fix[k]=v[1:]
out={}
for fid,v in r.items():
    if fid in rejfig or len(v['blanks'])<3: continue
    bl=[]
    for i,b in enumerate(v['blanks']):
        key=f'{fid}#{i}'
        if key in rej: continue
        b=dict(b); 
        if key in fix: b['answer']=fix[key]
        bl.append(b)
    if len(bl)>=3: out[fid]=dict(v,blanks=bl)
json.dump(out,open('final_blanks.json','w'),ensure_ascii=False)
print(len(out),sum(len(v['blanks']) for v in out.values()))
