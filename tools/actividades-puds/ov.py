import json
from PIL import Image,ImageDraw,ImageFont
R=json.load(open('matched.json'))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',10)
ids=list(R)
for k in range(0,len(ids),6):
    ims=[]
    for fid in ids[k:k+6]:
        im=Image.open(f'/home/claude/repaso-dsi/src/figuras/img/{fid}.webp').convert('RGB'); d=ImageDraw.Draw(im,'RGBA')
        for p in R[fid]['parts']:
            if not p['box']: continue
            x,y,w,h=p['box']; pad=3
            d.rectangle([x-pad,y-pad,x+w+pad,y+h+pad],fill=(255,230,120,235),outline=(220,0,0))
            d.text((x,y),p['answer'][:34],fill=(0,0,160),font=F)
        s=520/im.size[0]; im=im.resize((520,int(im.size[1]*s))); ImageDraw.Draw(im).text((2,2),fid,fill=(255,0,0)); ims.append(im)
    H=sum(max(a.size[1] for a in ims[j:j+2])+8 for j in range(0,len(ims),2))
    S=Image.new('RGB',(1048,H),'white'); y=0
    for j in range(0,len(ims),2):
        for c,a in enumerate(ims[j:j+2]): S.paste(a,(c*528,y))
        y+=max(a.size[1] for a in ims[j:j+2])+8
    S.save(f'ov{k//6}.png')
