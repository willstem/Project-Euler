# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:26:09 2018

@author: willstem
"""

count = 0
seen = set()
for a in xrange(2,101):
    for b in xrange(2,101):
        curr_val = pow(a, b)
        if curr_val not in seen:
            seen.add(curr_val)
            count += 1

print count
