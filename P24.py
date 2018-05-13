# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:24:53 2018

@author: willstem
"""

import bisect
import itertools



my_list = [i for i in xrange(10)]

i = 0
for perm in itertools.permutations(my_list):
    i += 1
    if i == int(1e6):
        print "".join(map(str, perm))
        break

"""
#SUPER MEMORY
list_perms = []

for perm in itertools.permutations(my_list):
    bisect.insort(list_perms, perm)

print "".join(map(str, list_perms[int(1e6)]))
"""