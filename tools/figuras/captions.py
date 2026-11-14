import json,subprocess,re,pymupdf
items=json.load(open('/home/claude/fig/assigned.json'))
xref={}
for s in ['pf','wm','celina','copia','fidanza']:
    for ln in subprocess.run(['pdfimages','-list',f'/home/claude/fig/src/{s}.pdf'],capture_output=True,text=True).stdout.splitlines()[2:]:
        f=ln.split(); xref[(s,int(f[1]))]=int(f[10])
docs={s:pymupdf.open(f'/home/claude/fig/src/{s}.pdf') for s in ['pf','wm','celina','copia','fidanza']}
out={}
for x in items:
    s=x['src']; d=docs[s]; pg=d[x['page']-1]; x['num']=int(re.search(r'-(\d+)\.png$',x['path']).group(1))
    try: rects=pg.get_image_rects(xref[(s,x['num'])])
    except Exception: rects=[]
    if not rects: continue
    r=rects[0]
    blocks=pg.get_text('blocks')
    near=[]
    for b in blocks:
        bx=pymupdf.Rect(b[:4]); t=re.sub(r'\s+',' ',b[4]).strip()
        if not t: continue
        horiz = bx.x1>r.x0-20 and bx.x0<r.x1+20
        if horiz and 0<=bx.y0-r.y1<=40: near.append(('below',t))
        elif horiz and 0<=r.y0-bx.y1<=30: near.append(('above',t))
    cap=None
    for pos,t in near:
        m=re.match(r'^(Fig(?:ura)?\.?\s*\d+\.\d+\.?.{3,220})',t)
        if m: cap=m.group(1); break
    out[x['i']]={'cap':cap,'near':near[:3]}
json.dump(out,open('/home/claude/fig/captions.json','w'),ensure_ascii=False)
print(sum(1 for v in out.values() if v['cap']), 'captions from text layer of', len(out))
for i,v in list(out.items())[:400]:
    if v['cap']: print(i, v['cap'][:120])
