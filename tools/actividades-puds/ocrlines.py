import json,subprocess,re
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
ids=[l.split('|')[0] for l in open('labels.txt') if re.match(r'^f\d',l)]
def run(fid):
    p=f'/home/claude/repaso-dsi/src/figuras/img/{fid}.webp'
    im=Image.open(p).convert('L'); w,h=im.size; s=3
    im.resize((w*s,h*s),Image.LANCZOS).save(f'/tmp/{fid}.png')
    out=subprocess.run(['tesseract',f'/tmp/{fid}.png','-','-l','spa','--psm','11','tsv'],capture_output=True,text=True).stdout
    L={}
    for ln in out.splitlines()[1:]:
        f=ln.split('\t')
        if len(f)<12 or f[0]!='5' or not f[11].strip(): continue
        k=(int(f[2]),int(f[3]),int(f[4]))
        L.setdefault(k,[]).append((int(f[6])/s,int(f[7])/s,int(f[8])/s,int(f[9])/s,f[11]))
    lines=[]
    for ws in L.values():
        ws.sort()
        x0=min(a[0] for a in ws);y0=min(a[1] for a in ws);x1=max(a[0]+a[2] for a in ws);y1=max(a[1]+a[3] for a in ws)
        lines.append({'t':' '.join(a[4] for a in ws),'x':x0,'y':y0,'w':x1-x0,'h':y1-y0})
    return fid,{'W':w,'H':h,'lines':lines}
with ThreadPoolExecutor(8) as ex: res=dict(ex.map(run,ids))
json.dump(res,open('lines.json','w'),ensure_ascii=False); print(len(res))
