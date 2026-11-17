import json,re,os,unicodedata
from PIL import Image
R=json.load(open('matched.json'))
F={f['id']:f for f in json.load(open('/home/claude/repaso-dsi/src/figuras/figuras.json'))['figuras']}
crop={'f23-06':368,'f30-10':485,'f30-11':356}
flows={'Requisitos':1,'Análisis':2,'Diseño':3,'Implementación':4,'Prueba':5}
extra_acc={
 ('f29-06','Integrar sistema'):['Integrar el sistema'],
 ('f30-07','Realizar pruebas de integración'):['Realizar prueba de integración'],
 ('f30-10','Ingeniero de pruebas'):['Diseñador de pruebas'],
 ('f30-06','Ingeniero de pruebas'):['Diseñador de pruebas'],
 ('f30-09','Ingeniero de pruebas'):['Diseñador de pruebas'],
 ('f28-06','Diseño de la arquitectura'):['Diseñar la arquitectura'],
}
def slug(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
G='/home/claude/repaso-dsi/src/graficos'; H='/home/claude/repaso-dsi/src/figuras/huecos'
for f in os.listdir(G):
    if f.startswith('b3b-'): os.remove(os.path.join(G,f))
summary=[]
for fid,r in R.items():
    fig=F[fid]; im=Image.open(f'/home/claude/repaso-dsi/src/figuras/img/{fid}.webp'); W,Hh=im.size
    bl=[]; parts=r['parts']
    for i,p in enumerate(parts):
        x,y,w,h=p['box']; pad=3
        x0=max(0,x-pad); y0=max(0,y-pad); x1=min(W,x+w+pad); y1=min(Hh,y+h+pad)
        # es estado entre paréntesis si la parte anterior es su nombre y no está en la lista original como etiqueta completa
        paren = i>0 and p['answer'][:1].islower() and p['answer'] not in ('o modelo del dominio',)
        lvl='extra' if (p['answer'][:1].islower()) else 'clave'
        acc=list(dict.fromkeys(p.get('accept',[])+extra_acc.get((fid,p['answer']),[])))
        e={'id':f'b{i+1}','x':round(x0),'y':round(y0),'w':round(x1-x0),'h':round(y1-y0),'answer':p['answer'],'level':lvl}
        if acc: e['accept']=acc
        bl.append(e)
    m=re.match(r'Figura (\d+\.\d+)',fig.get('title') or '')
    refs=[]
    if m: refs.append(f'PUDS, fig. {m.group(1)}')
    for x in fig['refs']:
        c=(x.get('corto') or x['archivo']); refs.append(c+(f', pág. {x["pag"]}' if x.get('pag') else ''))
    fuente=' · '.join(dict.fromkeys(refs))
    n=flows[r['flow']]*10+r['order']
    name=f"b3b-{n:02d}-{slug(r['act'])}"
    img=im if fid not in crop else im.crop((0,0,W,crop[fid]))
    img.save(f'{G}/{name}.webp',lossless=True)
    cfg={'title':f"{r['flow']} · {r['act']}: entradas y resultados",'topic':'B3 · PUDS','order':100+n,
         'width':img.size[0],'height':img.size[1],'fuente':fuente,'blanks':bl}
    json.dump(cfg,open(f'{G}/{name}.json','w'),ensure_ascii=False,indent=1)
    # figura original: misma versión completa (coordenadas iguales; la imagen original no se recorta)
    old=json.load(open(f'{H}/{fid}.json')) if os.path.exists(f'{H}/{fid}.json') else {}
    hc={'figura':fid,'title':old.get('title') or fig.get('title') or r['act'],'width':W,'height':Hh,'order':fig['orden'],'fuente':old.get('fuente',fuente),'origen':'manual','blanks':bl}
    json.dump(hc,open(f'{H}/{fid}.json','w'),ensure_ascii=False,indent=1)
    summary.append((name,len(bl),sum(b['level']=='clave' for b in bl)))
for s in sorted(summary): print(s)
print(len(summary),sum(s[1] for s in summary))
