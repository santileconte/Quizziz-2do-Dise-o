import json,sys
from PIL import Image,ImageDraw,ImageFont
import sys
r=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'cand_blanks.json')); PFX=sys.argv[2] if len(sys.argv)>2 else 's'
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17)
items=[]
for fid in sorted(r):
    v=r[fid]
    if len(v['blanks'])<3: continue
    for i,b in enumerate(v['blanks']): items.append((fid,i,b,v['best']))
COLW=900; ROWH=58; NR=34
cache={}
pages=[items[i:i+2*NR] for i in range(0,len(items),2*NR)]
for pi,pg in enumerate(pages):
    S=Image.new('RGB',(2*COLW,NR*ROWH),'white'); d=ImageDraw.Draw(S)
    for k,(fid,i,b,best) in enumerate(pg):
        col,row=divmod(k,NR); X=col*COLW; Y=row*ROWH
        if best not in cache: cache[best]=Image.open((best if best.startswith('/') else '/home/claude/fig/'+best)).convert('RGB')
        im=cache[best]; mh=max(4,b['lh']*0.7); mw=max(8,b['lh']*1.6)
        x0=max(0,b['x']-mw); y0=max(0,b['y']-mh); x1=min(im.size[0],b['x']+b['w']+mw); y1=min(im.size[1],b['y']+b['h']+mh)
        cr=im.crop((int(x0),int(y0),int(x1),int(y1))).copy()
        dd=ImageDraw.Draw(cr); dd.rectangle([b['x']-x0-1,b['y']-y0-1,b['x']+b['w']-x0+1,b['y']+b['h']-y0+1],outline=(255,0,0))
        sc=min((ROWH-4)/cr.size[1],430/cr.size[0]); cr=cr.resize((max(1,int(cr.size[0]*sc)),max(1,int(cr.size[1]*sc))))
        S.paste(cr,(X+4,Y+2))
        d.text((X+440,Y+4),f'{fid}#{i}',fill=(120,120,120),font=F)
        d.text((X+440,Y+26),b['answer'][:48],fill=(0,0,160),font=F)
        d.line([X,Y+ROWH-1,X+COLW,Y+ROWH-1],fill=(220,220,220))
    d.line([COLW,0,COLW,NR*ROWH],fill=(0,0,0))
    S.save(f'rev/{PFX}{pi:02d}.png')
print(len(items),len(pages))
