import json,re
from statistics import mean
from PIL import Image
exec(open('lablib.py').read())
final=json.load(open('final_blanks.json'))
P2=json.load(open('ocr_pass2.json')); OP=json.load(open('ocr_photos.json'))
def filt(labs,T2,others,minc,meanc):
    out=[]
    for L in labs:
        t=re.sub(r'\s+',' ',L['text']).strip(); toks=t.split()
        if not (1<=len(toks)<=7 and 3<=len(t)<=60): continue
        if not all(tok_ok(x) for x in toks): continue
        if not any(len(re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ]','',x))>=3 for x in toks): continue
        c=L['conf']; nt=nrm(t)
        x2=any((' '+nt+' ') in (' '+o+' ') for o in others)
        p2=all((' '+nrm(li)+' ') in T2 for li in L['lines'])
        if (x2 or p2) and min(c)>=minc and mean(c)>=meanc:
            out.append({'answer':t.strip(' ,;:'),'x':L['x'],'y':L['y'],'w':L['w'],'h':L['h'],'x2':x2,'p2':p2,'lh':L['lh'],'conf':round(min(c))})
    return out
res={}
# a) photos / question images
for fid,d in OP.items():
    ws=[w for w in d['words'] if w['c']>=0]; ls=lines_of(ws); cut=caption_cut(ls,d['h'])
    img=Image.open(d['path']).convert('L')
    labs=labels_of([L for L in ls if L['y']<cut-2],img)
    bl=filt(labs,' '+nrm(d['p2'])+' ',[],50,75)
    res[fid]={'best':d['path'],'W':d['w'],'H':d['h'],'blanks':bl}
# b) non-photo not yet final, relaxed
for fid,v in m.items():
    if v['photo'] or fid in final: continue
    d,labs,full,cut=get(v['best'])
    others=[get(p)[2] for p in v['members'] if p!=v['best']]
    bl=filt(labs,' '+nrm(P2.get(P+v['best'],''))+' ',others,40,70)
    res[fid]={'best':P+v['best'],'W':d['w'],'H':d['h'],'blanks':bl}
json.dump(res,open('cand2.json','w'),ensure_ascii=False)
q={k:v for k,v in res.items() if len(v['blanks'])>=3}
print(len(q),sum(len(v['blanks']) for v in q.values()))
