import json, re, unicodedata
from statistics import mean
W=json.load(open('ocr_words.json')); V=set(json.load(open('vocab2.json'))); P2={k:None for k in []}
m=json.load(open('/home/claude/fig/fidmap.json'))
P='/home/claude/fig/'
def nrm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9ñ]+',' ',s).strip()
def tok_ok(t):
    core=re.sub(r'^[«»<>"“”\'(\[\-:]+|[«»<>"“”\'\)\],.:;\-]+$','',t)
    if not core: return t in {'-','«','»','<<','>>'}
    if re.search(r'\d|#|@|\||_|=|\{|\}|\*|~|©',core): return False
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+([\-/][A-Za-zÁÉÍÓÚáéíóúÑñÜü]+)*",core): return False
    parts=re.split(r'[\-/]',core)
    for p in parts:
        lp=p.lower()
        if len(lp)==1 and lp not in {'a','y','o','e','u'}: return False
        if lp not in V: return False
    return True
def lines_of(words):
    g={}
    for w in words: g.setdefault((w['b'],w['p'],w['l']),[]).append(w)
    lines=[]
    for k,ws in g.items():
        ws=sorted(ws,key=lambda w:w['x'])
        # split a tesseract line where there is a big horizontal gap
        cur=[ws[0]]
        for w in ws[1:]:
            p=cur[-1]; gap=w['x']-(p['x']+p['w'])
            if gap>1.6*max(p['h'],w['h']): lines.append(cur); cur=[w]
            else: cur.append(w)
        lines.append(cur)
    out=[]
    for ws in lines:
        x0=min(w['x'] for w in ws); y0=min(w['y'] for w in ws); x1=max(w['x']+w['w'] for w in ws); y1=max(w['y']+w['h'] for w in ws)
        out.append({'x':x0,'y':y0,'w':x1-x0,'h':y1-y0,'ws':ws})
    return out
def sep(img,last,L):
    if img is None: return False
    a=int(last['y']+last['h']); b=int(L['y'])
    x0=int(max(L['x'],last['x'])); x1=int(min(L['x']+L['w'],last['x']+last['w']))
    if b-a<1 or x1-x0<4: return False
    dark=0; n=0
    for y in range(a,b+1):
        row=[img.getpixel((x,y)) for x in range(x0,x1) if 0<=y<img.size[1] and x<img.size[0]]
        if not row: continue
        n+=1; dark+= sum(p<140 for p in row)>0.6*len(row)
    return n>0 and 0<dark<=max(1,n//2)
def labels_of(lines,img=None):
    lines=sorted(lines,key=lambda L:(L['y'],L['x'])); labs=[]
    for L in lines:
        best=None
        for B in labs:
            last=B['ls'][-1]; gap=L['y']-(last['y']+last['h'])
            cx1=L['x']+L['w']/2; cx2=last['x']+last['w']/2
            hov=min(L['x']+L['w'],last['x']+last['w'])-max(L['x'],last['x'])
            if -2<gap<0.75*max(L['h'],last['h']) and abs(L['h']-last['h'])<0.45*max(L['h'],last['h']) and (abs(cx1-cx2)<0.3*max(L['w'],last['w']) or abs(L['x']-last['x'])<0.6*L['h']) and hov>0 and not sep(img,last,L):
                best=B; break
        if best: best['ls'].append(L)
        else: labs.append({'ls':[L]})
    out=[]
    for B in labs:
        ws=[w for L in B['ls'] for w in L['ws']]
        x0=min(w['x'] for w in ws); y0=min(w['y'] for w in ws); x1=max(w['x']+w['w'] for w in ws); y1=max(w['y']+w['h'] for w in ws)
        text=' '.join(' '.join(w['t'] for w in L['ws']) for L in B['ls'])
        out.append({'text':text,'x':x0,'y':y0,'w':x1-x0,'h':y1-y0,'conf':[w['c'] for w in ws],'n':len(B['ls']),'lines':[' '.join(w['t'] for w in L['ws']) for L in B['ls']],'lh':mean(L['h'] for L in B['ls'])})
    return out
def caption_cut(lines,H):
    ys=[L['y'] for L in lines if re.match(r'^(Figura|Figure|Fig\.?|Tabla|Table)\b',' '.join(w['t'] for w in L['ws']),re.I)]
    return min(ys) if ys else H+1

cache={}
def get(path):
    if path in cache: return cache[path]
    d=W[P+path]; ws=[w for w in d['words'] if w['c']>=0]
    ls=lines_of(ws); cut=caption_cut(ls,d['h'])
    from PIL import Image
    img=Image.open(P+path).convert('L')
    labs=[b for b in labels_of([L for L in ls if L['y']<cut-2],img)]
    full=nrm(' '.join(w['t'] for w in sorted(ws,key=lambda w:(w['b'],w['p'],w['l'],w['x']))))
    cache[path]=(d,labs,full,cut); return cache[path]
