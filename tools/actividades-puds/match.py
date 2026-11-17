import json,re,unicodedata
from difflib import SequenceMatcher
D=json.load(open('lines.json'))
def nz(s): s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn'); return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
figs=[]; cur=None
for ln in open('labels.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if re.match(r'^f\d',ln):
        fid,act,flow,order=ln.split('|'); cur={'fid':fid,'act':act,'flow':flow,'order':int(order),'labels':[]}; figs.append(cur)
    elif ln.strip(): cur['labels'].append(ln.split('|'))
def below(a,b):  # b directly below a
    gap=b['y']-(a['y']+a['h']); ca=a['x']+a['w']/2; cb=b['x']+b['w']/2
    return -2<=gap<=1.1*max(a['h'],b['h']) and abs(ca-cb)<=0.5*max(a['w'],b['w'])+8
def chains(lines,used,start_ok=None,maxn=5):
    out=[]
    for i,L in enumerate(lines):
        if i in used or (start_ok and not start_ok(L)): continue
        ch=[i]; out.append(list(ch))
        while len(ch)<maxn:
            nxt=[j for j,M in enumerate(lines) if j not in used and j not in ch and below(lines[ch[-1]],M)]
            if not nxt: break
            ch.append(min(nxt,key=lambda j:lines[j]['y'])); out.append(list(ch))
    return out
def best(lines,used,T,start_ok=None):
    t=nz(T); bs=None
    for ch in chains(lines,used,start_ok):
        s=SequenceMatcher(None,nz(' '.join(lines[j]['t'] for j in ch)),t).ratio()
        if not bs or s>bs[0]: bs=(s,ch)
    return bs
def box(lines,ch):
    x0=min(lines[j]['x'] for j in ch);y0=min(lines[j]['y'] for j in ch);x1=max(lines[j]['x']+lines[j]['w'] for j in ch);y1=max(lines[j]['y']+lines[j]['h'] for j in ch)
    return [x0,y0,x1-x0,y1-y0]
res={}
for f in figs:
    lines=D[f['fid']]['lines']; used=set(); out=[]
    order=sorted(range(len(f['labels'])),key=lambda i:-len(f['labels'][i][0]))
    tmp={}
    for i in order:
        lab=f['labels'][i]; full=lab[0]; acc=lab[1:]
        m=re.match(r'^(.*?)\s*\((.*)\)$',full)
        if m:
            main,par=m.group(1),m.group(2)
            b1=best(lines,used,main)
            if b1 and b1[0]>=0.72:
                used|=set(b1[1]); last=lines[b1[1][-1]]
                b2=best(lines,used,'('+par+')',start_ok=lambda L:below(last,L))
                if b2 and b2[0]>=0.72:
                    used|=set(b2[1]); tmp[i]=[(main,acc,box(lines,b1[1]),b1[0]),(par,[],box(lines,b2[1]),b2[0])]; continue
                used-=set(b1[1])
            b=best(lines,used,full)
            if b and b[0]>=0.72: used|=set(b[1]); tmp[i]=[(full,acc,box(lines,b[1]),b[0])]
            else: tmp[i]=[(full,acc,None,b[0] if b else 0)]
        else:
            b=best(lines,used,full)
            if b and b[0]>=0.72: used|=set(b[1]); tmp[i]=[(full,acc,box(lines,b[1]),b[0])]
            else: tmp[i]=[(full,acc,None,b[0] if b else 0)]
    for i in range(len(f['labels'])): out+=tmp[i]
    res[f['fid']]=dict(f,parts=[{'answer':a,'accept':acc,'box':bx,'score':round(s,2)} for a,acc,bx,s in out],W=D[f['fid']]['W'],H=D[f['fid']]['H'])
    bad=[(p[0],round(p[3],2)) for p in out if p[2] is None or p[3]<0.85]
    print(f['fid'],len(out),'faltan/dudosos:',bad)
json.dump(res,open('matched.json','w'),ensure_ascii=False)
