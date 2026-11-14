import json,re,subprocess
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
items=json.load(open('/home/claude/fig/assigned.json'))
ocr=json.load(open('/home/claude/fig/ocr.json'))
caps=json.load(open('/home/claude/fig/captions.json'))
def figcap(t):
    t=t.replace('\n',' ')
    m=re.search(r'(Figura|Fig\.|Tabla)\s*(\d{1,2})\s*[\.,]\s*(\d{1,2})\s*[\.,]?\s*(.{5,200}?)(?:\.\s|$)',t)
    if m: return f"{m.group(1).replace('Fig.','Figura')} {m.group(2)}.{m.group(3)}. {m.group(4).strip()}"
def slide_title(path):
    im=Image.open(path).convert('L'); w,h=im.size
    top=im.crop((0,0,w,int(h*0.22))).resize((w*2,int(h*0.22)*2))
    p='/tmp/t_'+path.replace('/','_')
    top.save(p)
    t=subprocess.run(['tesseract',p,'-','-l','spa','--psm','6'],capture_output=True,text=True).stdout
    for ln in t.splitlines():
        ln=ln.strip(' |—-_.,:;\'"')
        letters=sum(c.isalpha() for c in ln)
        if letters>=5 and letters/ max(1,len(ln))>0.75 and sum(c.isupper() for c in ln)/max(1,letters)>0.7:
            return ln
    return None
def heading(i):
    for pos,t in caps.get(str(i),{}).get('near',[]):
        if pos=='above' and 4<=len(t)<=70 and not re.search(r'UTN FRRe|Fidanza|^\d+$|^EJEMPLOS?$|^Ejemplo$',t) and not t.endswith('.'):
            return t.strip('•“” -')
    return None
def one(x):
    i=x['i']; c=figcap(ocr.get(str(i),'')); st=None
    if x['src']=='pf' and not c: st=slide_title(x['path'])
    return i,{'cap':c,'slide':st,'head':heading(i)}
with ThreadPoolExecutor(8) as ex: res=dict(ex.map(one,items))
json.dump(res,open('/home/claude/fig/titles.json','w'),ensure_ascii=False)
print(sum(1 for v in res.values() if v['cap']),'caps',sum(1 for v in res.values() if v['slide']),'slides',sum(1 for v in res.values() if v['head']),'heads')
