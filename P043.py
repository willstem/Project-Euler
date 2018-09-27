# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:17:06 2018

@author: willstem
"""

from itertools import permutations

pandigs = {''.join(p) for p in permutations('0123456789')}
panset = set()

for pandig in pandigs:
    if int(pandig[1:4]) % 2 == 0:
        if int(pandig[2:5]) % 3 == 0:
            if int(pandig[3:6]) % 5 == 0:
                if int(pandig[4:7]) % 7 == 0:
                    if int(pandig[5:8]) % 11 == 0:
                        if int(pandig[6:9]) % 13 == 0:
                            if int(pandig[7:10]) % 17 == 0:
                                panset.add(pandig)

print len(panset)
print "sum:", sum(map(int, panset))