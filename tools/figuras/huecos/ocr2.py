import json, subprocess, os, re
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
m=json.load(open('/home/claude/fig/fidmap.json'))
def run(path):
    im=Image.open(path).convert('L'); w,h=im.size
    s=min(4.0,max(1.5,2600/max(w,1)))
    big=im.resize((int(w*s),int(h*s)),Image.BICUBIC)
    tp='tmp/b_'+re.sub(r'[^\w]','_',path)+'.png'; big.save(tp)
    txt=''
    for lang,psm in (('spa','12'),('eng','12')):
        txt+='\n'+subprocess.run(['tesseract',tp,'-','-l',lang,'--psm',psm],capture_output=True,text=True).stdout
    os.remove(tp)
    return path,txt
paths=sorted({'/home/claude/fig/'+v['best'] for v in m.values() if not v['photo']})
with ThreadPoolExecutor(8) as ex: res=dict(ex.map(run,paths))
json.dump(res,open('ocr_pass2.json','w'))
print(len(res))
