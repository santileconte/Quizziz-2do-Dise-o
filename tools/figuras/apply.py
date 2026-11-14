import json
items=json.load(open('/home/claude/fig/assigned.json'))
byi={x['i']:x for x in items}
par={x['i']:x['i'] for x in items}
def f(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
# start from automatic groups
grp={}
for x in items: grp.setdefault((x['tema'],x['grp']),[]).append(x['i'])
for m in grp.values():
    for o in m[1:]: par[f(o)]=f(m[0])
bad=[]
moved=set()
for ln in open('/home/claude/fig/fixes.txt'):
    p=ln.split()
    if not p: continue
    if p[0]=='merge':
        ids=[int(v) for v in p[1:]]
        for v in ids:
            if v not in byi: bad.append(ln.strip())
        ids=[v for v in ids if v in byi]
        for v in ids[1:]: par[f(v)]=f(ids[0])
    elif p[0]=='move':
        for v in p[2:]:
            if int(v) in byi: byi[int(v)]['tema']=p[1]; moved.add(int(v))
            else: bad.append(ln.strip())
print('ids invalidos', bad)
# final groups: tema of root decides (moved ids keep their own; reconcile by majority of PF/celina)
fam={}
for x in items: fam.setdefault(f(x['i']),[]).append(x)
for root,xs in fam.items():
    temas={x['tema'] for x in xs}
    if len(temas)>1: print('grupo con temas mezclados', root, [(x['i'],x['tema']) for x in xs])
res={}
for r,xs in fam.items():
    mv=[x['tema'] for x in xs if x['i'] in moved]
    res[str(r)]={'ids':[x['i'] for x in xs],'tema':mv[0] if mv else xs[0]['tema']}
json.dump(res,open('/home/claude/fig/families.json','w'))
print('figuras distintas', len(fam), 'imagenes', len(items))
