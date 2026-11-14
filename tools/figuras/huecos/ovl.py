import json,sys
from PIL import Image,ImageDraw,ImageFont
d=json.load(open(sys.argv[1])); ids=sys.argv[2].split(','); out=sys.argv[3]
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
ims=[]
for fid in ids:
    v=d[fid]; im=Image.open(v['best']).convert('RGB'); dr=ImageDraw.Draw(im)
    for b in v['blanks']:
        p=2
        dr.rectangle([b['x']-p,b['y']-p,b['x']+b['w']+p,b['y']+b['h']+p],fill=(255,240,160),outline=(200,0,0))
        dr.text((b['x'],b['y']),b['answer'][:40],fill=(0,0,150),font=F)
    s=540/im.size[0]; ims.append(im.resize((540,int(im.size[1]*s))))
cols=2; rows=[ims[i:i+cols] for i in range(0,len(ims),cols)]
H=sum(max(i.size[1] for i in r)+6 for r in rows)
S=Image.new('RGB',(1086,H),'white'); y=0
for r in rows:
    for j,i in enumerate(r): S.paste(i,(j*546,y))
    y+=max(i.size[1] for i in r)+6
S.save(out); print(S.size)
