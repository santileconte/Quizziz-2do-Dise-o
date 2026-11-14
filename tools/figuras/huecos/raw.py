import json,re,sys
from PIL import Image,ImageDraw,ImageFont
exec(open('lablib.py').read())
OP=json.load(open('ocr_photos.json'))
ids=sys.argv[1].split(',')
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
raw={}
try: raw=json.load(open('raw_labels.json'))
except: pass
for fid in ids:
    if fid in OP:
        d=OP[fid]; path=d['path']; ws=[w for w in d['words'] if w['c']>=0]
        ls=lines_of(ws); cut=caption_cut(ls,d['h']); img=Image.open(path).convert('L')
        labs=labels_of([L for L in ls if L['y']<cut-2],img)
    else:
        v=m[fid]; d,labs,full,cut=get(v['best']); path=P+v['best']
    labs=[L for L in labs if re.search(r'[A-Za-zÁÉÍÓÚáéíóúÑñ]{3}',L['text']) and L['h']<0.25*d['h']]
    labs.sort(key=lambda L:(round(L['y']/15),L['x']))
    raw[fid]={'path':path,'W':d['w'],'H':d['h'],'labs':[{k:L[k] for k in ('text','x','y','w','h','lh')} for L in labs]}
    im=Image.open(path).convert('RGB'); s=1100/im.size[0]; im=im.resize((1100,int(im.size[1]*s)))
    dr=ImageDraw.Draw(im)
    for i,L in enumerate(labs):
        x,y,w,h=[L[k]*s for k in ('x','y','w','h')]
        dr.rectangle([x-1,y-1,x+w+1,y+h+1],outline=(255,0,0),width=2)
        dr.text((x-2,y-16),str(i),fill=(0,0,255),font=F,stroke_width=2,stroke_fill=(255,255,255))
    im.save(f'man/{fid}.png')
json.dump(raw,open('raw_labels.json','w'),ensure_ascii=False)
