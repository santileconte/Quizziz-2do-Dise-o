import json, subprocess, os, re
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
F=json.load(open('/home/claude/repaso-dsi/src/figuras/figuras.json'))['figuras']
m=json.load(open('/home/claude/fig/fidmap.json'))
todo={}
for f in F:
    if f.get('qimg'): todo[f['id']]='/home/claude/repaso-dsi/src/cuestionarios/img/'+f['qimg']
    elif m.get(f['id'],{}).get('photo'): todo[f['id']]='/home/claude/repaso-dsi/src/figuras/img/'+f['id']+'.webp'
def run(item):
    fid,path=item
    im=Image.open(path).convert('L'); w,h=im.size
    s=min(3.0,max(1.0,2000/max(w,1)))
    big=im.resize((int(w*s),int(h*s)),Image.LANCZOS)
    tp=f'tmp/p_{fid}.png'; big.save(tp)
    out=subprocess.run(['tesseract',tp,'-','-l','spa+eng','--psm','11','tsv'],capture_output=True,text=True).stdout
    words=[]
    for ln in out.splitlines()[1:]:
        f=ln.split('\t')
        if len(f)<12 or f[0]!='5' or not f[11].strip(): continue
        words.append(dict(b=int(f[2]),p=int(f[3]),l=int(f[4]),x=int(f[6])/s,y=int(f[7])/s,w=int(f[8])/s,h=int(f[9])/s,c=float(f[10]),t=f[11].strip()))
    s2=min(4.0,max(1.5,2600/max(w,1)))
    big=im.resize((int(w*s2),int(h*s2)),Image.BICUBIC); big.save(tp)
    txt=''
    for lang in ('spa','eng'):
        txt+='\n'+subprocess.run(['tesseract',tp,'-','-l',lang,'--psm','12'],capture_output=True,text=True).stdout
    os.remove(tp)
    return fid,{'path':path,'w':w,'h':h,'words':words,'p2':txt}
with ThreadPoolExecutor(8) as ex: res=dict(ex.map(run,todo.items()))
json.dump(res,open('ocr_photos.json','w'))
print(len(res))
