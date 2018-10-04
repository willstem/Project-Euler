# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:56:27 2018

@author: willstem
"""

import operator as op

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom

#The smallest/largest value of r with a value of ncr(n,r) > 1e6 is 4 and 96,
#respectively

count = 0
for n in xrange(23, 101):
    for r in xrange(4, n-3):
        if ncr(n, r) > int(1e6):
            count += 1

print count