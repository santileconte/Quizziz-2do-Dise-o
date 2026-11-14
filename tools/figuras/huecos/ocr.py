import json, subprocess, os, re, unicodedata, sys
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor
os.makedirs('tmp',exist_ok=True)
def run(path):
    im=Image.open(path).convert('L'); w,h=im.size
    s=min(3.0,max(1.0,2000/max(w,1)))
    big=im.resize((int(w*s),int(h*s)),Image.LANCZOS)
    tp='tmp/'+re.sub(r'[^\w]','_',path)+'.png'; big.save(tp)
    out=subprocess.run(['tesseract',tp,'-','-l','spa+eng','--psm','11','tsv'],capture_output=True,text=True).stdout
    words=[]
    for ln in out.splitlines()[1:]:
        f=ln.split('\t')
        if len(f)<12 or f[0]!='5': continue
        t=f[11].strip()
        if not t: continue
        words.append(dict(b=int(f[2]),p=int(f[3]),l=int(f[4]),x=int(f[6])/s,y=int(f[7])/s,w=int(f[8])/s,h=int(f[9])/s,c=float(f[10]),t=t))
    return path,{'w':w,'h':h,'words':words}
paths=set()
m=json.load(open('/home/claude/fig/fidmap.json'))
for v in m.values():
    if v['photo']: continue
    paths.add(v['best']); paths.update(v['members'])
paths=sorted(paths)
with ThreadPoolExecutor(8) as ex: res=dict(ex.map(run,['/home/claude/fig/'+p for p in paths]))
json.dump(res,open('ocr_words.json','w'))
print(len(res))
