import json, re, os, io, shutil
from PIL import Image
F='/home/claude/fig'
items={x['i']:x for x in json.load(open(f'{F}/assigned.json'))}
fam=json.load(open(f'{F}/families.json'))
titles={int(k):v for k,v in json.load(open(f'{F}/titles.json')).items()}
temario=json.load(open(f'{F}/temario.json'))
bank={q['id']:q for q in json.load(open('/home/claude/work/bank.json'))}
OUT='/home/claude/repaso-dsi/src/figuras'
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(f'{OUT}/img'); os.makedirs(f'{OUT}/thumb')
FILES={'pf':'PF_Powers_de_Clase_364p.pdf','wm':'WM_Microservicios_del_Word.pdf','celina':'Apunte Segundo Parcial - Celina.pdf','copia':'Copia de Apunte Diseño.pdf','fidanza':'ApunteDiseñoSistemasInformación.pdf'}
SHORT={'pf':'PF','wm':'WM','celina':'Celina','copia':'Copia','fidanza':'Fidanza'}
SRCORD={'pf':0,'wm':1,'celina':2,'copia':3,'fidanza':4}
tema_of_q={}
for t in temario:
    for k in t['temas']: tema_of_q[k]=t['n']

ACR={'puds','rup','gof','xp','soa','crc','sqa','qa','qc','ac','c/s','osi','ui','cu','sw','api','iso','mvc','p2p','dsdm','fdd','asd'}
def sentence(s):
    s=s.strip(' -—|·').replace(' — ',' - ').replace('—','-')
    words=s.split()
    out=[]
    for k,w in enumerate(words):
        lw=w.lower()
        out.append(w.upper() if lw.strip('()/,.:') in ACR else (lw.capitalize() if k==0 else lw))
    return ' '.join(out)
SLIDE_FIX={'S0A':'SOA','ARIEFALIVO':'ARTEFACTOS','DETRABAJO':'DE TRABAJO','FLUJO DE TRABA':'FLUJO DE TRABAJO','KP ':'XP ','REO.':'REQ.','ANALISIS':'ANÁLISIS'}
def clean_slide(s):
    s=re.sub(r'^[\)\!\*\+\¡y ea]{0,4}(?=[A-ZÁÉÍÓÚ])','',s.strip())
    s=re.sub(r'\s+[a-zñ]$','',s.strip())
    for a,b in SLIDE_FIX.items(): s=s.replace(a,b)
    s=re.sub(r'FLUJO DE TRABAJOJO','FLUJO DE TRABAJO',s)
    s=s.strip(' ).,')
    if len(s)<4 or not re.search(r'[AEIOUÁÉÍÓÚ]{1}',s): return None
    return sentence(s)
OCR_FIX={' Jos ':' los ',' nn ':' un ','mucstra':'muestra','cluses':'clases',' .. ':' ','..':'','  ':' '}
def clean_cap(s):
    for a,b in OCR_FIX.items(): s=s.replace(a,b)
    s=re.sub(r'\s+',' ',s).strip(' ,.;')
    m=re.match(r'^(Figura|Tabla) (\d+\.\d+)\.?\s*(.*)$',s)
    if not m: return None
    body=m.group(3)
    body=re.split(r'(?<=[a-záéíóúñ\)])\.\s',body)[0]
    if len(body)>150: body=body[:150].rsplit(' ',1)[0]+'…'
    if len(body)<4: return None
    return f'{m.group(1)} {m.group(2)}. {body[0].upper()+body[1:]}'
BAD_HEAD=re.compile(r'^(Por ejemplo|Un ejemplo|En la siguiente|Para |Este |Esta |is part|\(|Diseño\(|Diagrama$|Ejemplo diagrama|DATOS IMPORTANTES|Puntos de Vista|Flujo de trabajo$|EL PROYECTO$|Trabajo →)',re.I)
def clean_head(s):
    s=s.strip(' “”"•:')
    if len(s)>60 or BAD_HEAD.search(s): return None
    if s.endswith(':'): s=s[:-1]
    if s.isupper(): s=sentence(s)
    return s
MANUAL={482:'DSDM (1994): principios · pizarrón de la clase',483:'FDD (1997): proceso · pizarrón de la clase',484:'Crystal (1998): propiedades · pizarrón de la clase',486:'ASD (1999): ciclo adaptativo · pizarrón de la clase',485:'Crystal: criticidad del sistema y tamaño del equipo',475:'Frameworks ágiles',
  154:'Ciclo de vida, fases, hitos y artefactos · gráfico del profesor',153:'Mapa conceptual del PUDS',134:'4P + H: personas, proyecto, producto, proceso y herramientas',
  218:'Realización de casos de uso: tarjetas CRC, diagrama de clases y diagrama de secuencia',223:'Tarjetas CRC: clase, responsabilidad, colaboración',
  855:'DIP: ModuloDePago depende de las clases concretas',856:'DIP: ModuloDePago depende de la interfaz IMetodoPago',
  713:'Elementos del diseño visual: distribución, tipografía, jerarquía, legibilidad, estética',723:'Honeycomb de la experiencia de usuario (Morville)',
  985:'Costo total según el número de módulos',986:'Conexión normal y conexión patológica',987:'Notación de los diagramas de flujo de control',988:'Construcciones estructuradas',989:'Notación de los diagramas de estructura',990:'Diagrama de estructura y diagrama de flujo',991:'Inclusión lexicográfica y solapamiento parcial',993:'Determinación del nivel de cohesión',994:'Flujo aferente, eferente, de transformación y de coordinación',
  567:'Arquitectura de un sistema robótico de empaquetado',753:'Proceso de diseño: entradas, actividades y salidas',755:'Vistas 4+1 de Kruchten',569:'Vistas 4+1 de Kruchten',
  548:'Objetivos y métricas del SQA',544:'Relación entre QA y QC',545:'Elementos del SQA',
  216:'Realización de CU: aspecto estático y dinámico',217:'Pasos para la realización de un CU'}
def title_for(ids):
    for i in ids:
        if i in MANUAL: return MANUAL[i],'manual'
    for i in ids:
        c=titles.get(i,{}).get('cap')
        c=clean_cap(c) if c else None
        if c: return c,'caption'
    for i in ids:
        s=titles.get(i,{}).get('slide')
        s=clean_slide(s) if s else None
        if s: return s,'slide'
    for i in ids:
        h=titles.get(i,{}).get('head')
        h=clean_head(h) if h else None
        if h: return h,'head'
    return None,None

LINK_EXAM={373:('parcial','Su versión con casilleros vacíos se tomó en el Parcial 2024 (pregunta 3) y en la práctica de la cátedra.'),
           387:('parcial','Su versión con casilleros vacíos se tomó en el Recuperatorio 2024 (pregunta 6) y en la práctica de la cátedra.'),
           380:('catedra','Su versión con casilleros vacíos está en la práctica de diagramas de la cátedra.'),
           392:('catedra','Su versión con casilleros vacíos está en la práctica de diagramas de la cátedra.'),
           400:('catedra','Su versión con casilleros vacíos está en la práctica de diagramas de la cátedra.'),
           767:('catedra','La misma topología se usó en la Simulación A 2024 (pregunta 4).')}
LEGIB={215:'El diagrama de la derecha no se lee en la foto.',226:'En la foto no se leen los atributos de algunas clases; la pág. 173 también tiene una foto ampliada de la parte superior.',
       745:'Recorte parcial de la figura del modelo OSI.',746:'Imagen borrosa: los nombres de las capas se leen, los detalles no.',84:'Parte de la diapositiva está tapada.'}
RANK_LABEL={1:'Parcial real',2:'Cátedra',3:'Clase',4:'Apunte base',5:'Complementaria'}
manifest=[]
def save_img(path,dst,photo):
    im=Image.open(path)
    if im.mode in ('P','LA','RGBA','I;16','CMYK','1','L'): im=im.convert('RGB')
    if photo: im.save(f'{OUT}/img/{dst}.webp','WEBP',quality=90,method=6)
    else: im.save(f'{OUT}/img/{dst}.webp','WEBP',lossless=True,method=4)
    th=im.copy(); th.thumbnail((560,400)); th.save(f'{OUT}/thumb/{dst}.webp','WEBP',quality=80,method=6)
    return im.size
def score(x):
    a=x['w']*x['h']
    if x['src']=='pf' and x['page']<249: a*=0.35
    return a
entries=[]
for root,fd in fam.items():
    ids=fd['ids']; xs=[items[i] for i in ids]
    tema=fd['tema']
    best=max(xs,key=score)
    refs=sorted({(x['src'],x['page']) for x in xs},key=lambda r:(SRCORD[r[0]],r[1]))
    srcs={x['src'] for x in xs}
    tag=None; note=None
    for i in ids:
        if i in LINK_EXAM: tag,note=LINK_EXAM[i]
    if tag=='parcial': rank=1
    elif tag=='catedra': rank=2
    elif 'pf' in srcs or 'wm' in srcs: rank=3
    elif 'celina' in srcs: rank=4
    else: rank=5
    title,tsrc=title_for(sorted(ids,key=lambda i:(SRCORD[items[i]['src']],items[i]['page'])))
    leg=next((LEGIB[i] for i in ids if i in LEGIB),None)
    photo = best['src']=='pf' and best['page']<249
    kind = 'Foto de diapositiva' if photo else ('Figura del libro, proyectada en clase' if best['src']=='pf' else 'Figura del apunte' if best['src'] in ('celina','copia','fidanza') else 'Figura del Word de la cátedra')
    pfmin=min([p for s,p in refs if s=='pf'] or [9999])
    entries.append(dict(tema=tema,rank=rank,ids=ids,best=best,refs=refs,title=title,tsrc=tsrc,nota=note,legib=leg,photo=photo,kind=kind,
        key=(rank,-len({s for s,_ in refs}),pfmin,SRCORD[refs[0][0]],refs[0][1])))
# question images
QIMG={'p24-03-flujo-requisitos.png':('parcial',['p24-03'],'Flujo de Requisitos con casilleros vacíos (Parcial 2024)','Copias en el Quizziz: preguntas 2, 18, 30, 38, 40, 59 y 75.'),
      'r24-06-flujo-diseno.png':('parcial',['r24-06'],'Flujo de Diseño con casilleros vacíos (Recuperatorio 2024)','Copias en el Quizziz: preguntas 19, 23, 24, 62 y 74.'),
      'p24-15-ventana.png':('parcial',['p24-15'],'Ventana emergente para clasificar según su modalidad (Parcial 2024)',None),
      'r24-09-factura.png':('parcial',['r24-09'],'Factura de ejemplo para el diagrama de Warnier (Recuperatorio 2024)',None),
      'r24-09-a.png':('parcial',['r24-09'],'Opción a del diagrama de Warnier (Recuperatorio 2024)',None),
      'r24-09-b.png':('parcial',['r24-09'],'Opción b del diagrama de Warnier (Recuperatorio 2024)',None),
      'r24-09-c.png':('parcial',['r24-09'],'Opción c del diagrama de Warnier (Recuperatorio 2024)',None),
      'r24-09-d.png':('parcial',['r24-09'],'Opción d del diagrama de Warnier (Recuperatorio 2024)',None),
      'r24-15-diagrama.png':('parcial',['r24-15'],'Diagrama de estructura para marcar afirmaciones (Recuperatorio 2024)',None),
      'r24-15-a.png':('parcial',['r24-15'],'Detalle a del diagrama (Recuperatorio 2024)',None),
      'r24-15-b.png':('parcial',['r24-15'],'Detalle b del diagrama (Recuperatorio 2024)',None),
      'r24-15-c.png':('parcial',['r24-15'],'Detalle c del diagrama (Recuperatorio 2024)',None),
      'simA-04-diagrama.png':('sim',['simA-04'],'Diagrama de arquitectura para reconocer (Simulación A 2024)','Copia en el Quizziz: pregunta 70. Es la figura 17-1 del Word de la cátedra.'),
      'simB-08-estructura.png':('sim',['simB-08'],'Estructura Duck / FlyBehavior / QuackBehavior (Simulación B 2024)','Copia en el Quizziz: pregunta 36.'),
      'simB-19-diagramas.png':('sim',['simB-19'],'Diagramas de estructura 1 y 2 (Simulación B 2024)',None),
      'cq-02-04-diagramas.png':('cq',['cq-02-04'],'Dos diagramas de comunicación para comparar el acoplamiento (Cuestionario GRASP #4)','La figura se tomó de la captura del Quizziz (pregunta 60).')}
for n in range(1,20): QIMG[f'gof-fig-{n:02d}.png']=('pract',[f'gof-{n:02d}'],None,None)
for n,name in enumerate(['requisitos','analisis','diseno','implementacion','prueba'],1): QIMG[f'puds-{n}-{name}.png']=('pract',None,None,None)
puds_q={}
for q in bank.values():
    for im in q.get('img',[]) or []:
        puds_q.setdefault(im,[]).append(q['id'])
QDIR='/home/claude/repaso-dsi/src/cuestionarios/img'
qentries=[]
for fname,(kind,qids,title,extra) in QIMG.items():
    qids=qids or puds_q.get(fname,[])
    q=bank[qids[0]]
    tema=tema_of_q[q['tema']]
    if fname.startswith('gof-fig'):
        pat=q['i'][0][1] if q.get('i') else ''
        title=f"Figura {int(fname[8:10])} de la práctica de patrones GoF"
        tema=tema_of_q[q['tema']]
    if fname.startswith('puds-'):
        flujo={'1':'Requisitos','2':'Análisis','3':'Diseño','4':'Implementación','5':'Prueba'}[fname[5]]
        title=f'Flujo de {flujo} con casilleros numerados (práctica de la cátedra)'
    src=re.sub(r' · también en el Quizziz.*$','',q.get('src',''))
    rank={'parcial':1,'sim':2,'cq':2,'pract':2}[kind]
    lab={'parcial':'Parcial real','sim':'Simulación 2024','cq':'Cuestionario 2026','pract':'Práctica de la cátedra'}[kind]
    qentries.append(dict(tema=tema,rank=rank,qfile=fname,qids=qids,title=title,src=src,extra=extra,lab=lab,
        key=(rank,0 if kind=='parcial' else 1, 0, -1, 0)))
# tema-specific answer hint for GoF figures is hidden on purpose (no spoilers)
by={}
for e in entries+qentries: by.setdefault(e['tema'],[]).append(e)
ALSO={'21':[592,595],'31':[373,380,387,392,400]}
ALSOQ={'31':['p24-03-flujo-requisitos.png','r24-06-flujo-diseno.png']+[f'puds-{n}-{x}.png' for n,x in enumerate(['requisitos','analisis','diseno','implementacion','prueba'],1)]}
out=[]
for t in temario:
    n=t['n']; es=sorted(by.get(n,[]),key=lambda e:e['key'])
    for k,e in enumerate(es,1):
        fid=f'f{n}-{k:02d}'
        if 'qfile' in e:
            im=Image.open(f"{QDIR}/{e['qfile']}"); w,h=im.size
            th=im.convert('RGB'); th.thumbnail((560,400)); th.save(f'{OUT}/thumb/{fid}.webp','WEBP',quality=80,method=6)
            e['out']=dict(id=fid,tema=n,orden=k,rank=e['rank'],nivel=e['lab'],title=e['title'],qimg=e['qfile'],w=w,h=h,
               refs=[{'archivo':e['src'],'nota':e['extra']}] if e['extra'] else [{'archivo':e['src']}],preguntas=e['qids'],tipo='Figura de una consigna del examen' if e['rank']==1 else 'Figura de una pregunta de la cátedra')
        else:
            b=e['best']; w,h=save_img(b['path'],fid,e['photo'])
            refs=[{'archivo':FILES[s],'corto':SHORT[s],'pag':p} for s,p in e['refs']]
            e['out']=dict(id=fid,tema=n,orden=k,rank=e['rank'],nivel=RANK_LABEL[e['rank']],title=e['title'],w=w,h=h,refs=refs,
               mostrada=f"{SHORT[b['src']]}, pág. {b['page']}",tipo=e['kind'],nota=e['nota'],legib=e['legib'])
        out.append(e['out'])
# cross listings
famof={}
for e in entries:
    for i in e['ids']: famof[i]=e['out']['id']
qof={e['qfile']:e['out']['id'] for e in qentries}
also={n:[famof[i] for i in ids] for n,ids in ALSO.items()}
for n,fs in ALSOQ.items(): also[n]=also.get(n,[])+[qof[f] for f in fs]
TITLE_FIX={'En capas (layered':'En capas (layered)','C/S multinivel (multi-tier':'C/S multinivel (multi-tier)','Orientada a servicios (SOA':'Orientada a servicios (SOA)',
 'Cliente-servidor e “a':'Cliente-servidor','Especificación de flujos de':'Especificación de flujos de trabajo principales','Ptura de req. como casos':'Captura de requisitos como casos de uso',
 'Release\u200b':'Release','PUDS -- conceptos clave':'PUDS - conceptos clave','Puds/rup - diferencias?':'PUDS/RUP: ¿diferencias?','Factory method a':'Factory Method',
 'Modelos y factores de calidad ñ':'Modelos y factores de calidad','Diseño , artefactos >':'Diseño - artefactos','Forma de alexander (canónica':'Forma de Alexander (canónica)',
 'Ejemplo forma de alexander':'Ejemplo de la forma de Alexander','Adaptador de clase adaptador de objeto':'Adaptador de clase y adaptador de objeto','Drop-down sub-menú menú desplegable':'Menú desplegable (drop-down) y submenú',
 'EJEMPLO(visual studio)':'Ejemplo: Visual Studio Code','Diferencias':'Diferencias entre cliente-servidor y componentes distribuidos','Escenario':'Escenario de modificabilidad',
 'FACTORES DE CALIDAD DEL SOFTWARE DE McCALL':'Factores de calidad del software de McCall','Estr. de componentes y conectores':'Estructuras de componentes y conectores','Patrones grasp':'Patrones GRASP',
 'Abstract factory':'Abstract Factory','Formato GOF':'Formato GoF','Patrones GOF':'Patrones GoF','Valores':'Valores de XP','Estructura':'Estructura del patrón','Estructura y participantes':'Estructura y participantes del patrón',
 'Análisis':'Análisis: trabajadores y artefactos','Diseño':'Diseño: trabajadores y artefactos','Implementación':'Implementación: trabajadores y artefactos','5. Estructura el modelo CU':'5. Estructurar el modelo de CU',
 'Figura 1.4. Modelo del Proceso Unificado, Existen dependencias entre muchos de los modelos':'Figura 1.4. Modelo del Proceso Unificado','Figura 2.4. El conjunto fundamental de modelos del Proceso Unificado!':'Figura 2.4. El conjunto fundamental de modelos del Proceso Unificado',
 'Figura 2.2. — Trabajadores y recursos que los realizan':'Figura 2.2. Trabajadores y recursos que los realizan','Figura 9.6. Trazas existentes entre realizaciones de caso de uso en diferentes modelo:':'Figura 9.6. Trazas existentes entre realizaciones de caso de uso en diferentes modelos',
 'Figura 8.4. Los atributos esenciales y los subtipos (es decir estereotipos) de una clase del anál':'Figura 8.4. Los atributos esenciales y los subtipos (es decir, estereotipos) de una clase del análisis',
 'Figura 10.22. Componentes':'Figura 10.22. Las clases de diseño necesarias en una construcción se implementan como componentes'}
for o in out:
    t=o.get('title')
    if not t: continue
    t=TITLE_FIX.get(t,t)
    if t.startswith('Tabla 8.1.'): t='Tabla 8.1. Breve comparación del modelo de casos de uso con el modelo de análisis'
    if t.startswith('Figura 2.7.'): t='Figura 2.7. La notación «en forma de pez» es la abreviatura de un flujo de trabajo'
    o['title']=t
json.dump({'figuras':out,'tambien':also},open(f'{OUT}/figuras.json','w'),ensure_ascii=False,indent=0)
import collections
print('figuras',len(out),'por rango',collections.Counter(o['rank'] for o in out))
print('sin titulo',sum(1 for o in out if not o['title']))
print('por tema',sorted(collections.Counter(o['tema'] for o in out).items()))
