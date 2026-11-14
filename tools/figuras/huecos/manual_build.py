import json,re
raw=json.load(open('raw_labels.json'))
out={}
for ln in open('manual.txt',encoding='utf-8'):
    ln=ln.strip()
    if not ln: continue
    key,_,ans=ln.partition(' = ')
    parts=[a.strip() for a in ans.split('|')]
    fid,sep,spec=re.match(r'(f[\w-]+?)([#@])(.*)',key).groups()
    R=raw[fid]; s=1100/R['W']
    if sep=='#':
        idx=[int(x) for x in re.split(r'[+]',spec.split('^')[0])]
        L=[R['labs'][i] for i in idx]
        x0=min(l['x'] for l in L); y0=min(l['y'] for l in L); x1=max(l['x']+l['w'] for l in L); y1=max(l['y']+l['h'] for l in L)
    else:
        a,b,c,d=[int(v)/s for v in spec.split(',')]
        x0,y0,x1,y1=a,b,c,d
    o=out.setdefault(fid,{'best':R['path'],'W':R['W'],'H':R['H'],'blanks':[],'manual':True})
    o['blanks'].append({'answer':parts[0],'accept':parts[1:],'x':x0,'y':y0,'w':x1-x0,'h':y1-y0})
json.dump(out,open('manual_blanks.json','w'),ensure_ascii=False)
print(len(out),sum(len(v['blanks']) for v in out.values()))
for k,v in out.items():
    if len(v['blanks'])<3: print('pocos',k,len(v['blanks']))
