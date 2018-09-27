# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:28:36 2018

@author: willstem
"""

from itertools import permutations

pandigs = {''.join(p) for p in permutations('123456789')}
mults = set()

for num in xrange(1, int(1e5)):
    conc = ''
    n = 1
    while len(conc) < 9:
        conc += str(num*n)
        n += 1
    if str(conc) in pandigs:
        mults.add((num, int(conc)))

print max(mults, key=lambda x:x[1])