#!/usr/bin/env python3

import sys
from wiktionaryparser import WiktionaryParser

if len(sys.argv)>1:
    expr=sys.argv[1]
else:
    expr="happy"

pos="adjective"

p=WiktionaryParser()
w=p.fetch(expr,language="English")
print("found %d entries"%len(w))

for e in w:
    print("#"*50)
    for e2 in e['definitions']:
        if e2['partOfSpeech']==pos:
            for r in e2['relatedWords']:
                for w in r['words']:
                    w=w.replace('See also Thesaurus:','')
                    w=w.replace('(','')
                    w=w.replace('):','')
                    print (w)
                    print("-"*50)
