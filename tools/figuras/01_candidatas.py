import subprocess, json, os, glob, re
from PIL import Image
out=[]
for s in ['pf','wm','celina','copia','fidanza']:
    lst=subprocess.run(['pdfimages','-list',f'src/{s}.pdf'],capture_output=True,text=True).stdout.splitlines()[2:]
    typ={}
    for ln in lst:
        f=ln.split(); typ[int(f[1])]=(f[2],int(f[3]),int(f[4]))
    for p in sorted(glob.glob(f'raw/{s}/i-*.png')):
        m=re.match(r'.*i-(\d+)-(\d+)\.png',p); page,num=int(m[1]),int(m[2])
        t,w,h=typ[num]
        if t!='image': continue
        if w<180 or h<110: continue
        if w/h>6 or h/w>6: continue
        out.append({'src':s,'page':page,'num':num,'w':w,'h':h,'path':p})
json.dump(out,open('cands.json','w'))
import collections; print(collections.Counter(c['src'] for c in out))
