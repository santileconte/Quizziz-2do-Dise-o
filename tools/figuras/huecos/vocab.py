import re, json, glob, unicodedata
from spellchecker import SpellChecker
def norm(w):
    w=unicodedata.normalize('NFC',w).lower()
    return re.sub(r'^[^\wáéíóúñü]+|[^\wáéíóúñü]+$','',w)
V=set()
for f in ['/home/claude/fig/copia.txt','/home/claude/fig/fidanza.txt']+glob.glob('/home/claude/work/txt/*.txt'):
    for w in re.findall(r'[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+',open(f,errors='ignore').read()): V.add(w.lower())
for w in re.findall(r'[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+',open('/home/claude/work/bank.json').read()): V.add(w.lower())
es=SpellChecker(language='es'); en=SpellChecker(language='en')
V|=set(es.word_frequency.keys()); V|=set(en.word_frequency.keys())
json.dump(sorted(V),open('vocab.json','w'))
print(len(V), [w in V for w in ['priorizar','subsistema','esquematizada','trace','realización','comprobar']])
