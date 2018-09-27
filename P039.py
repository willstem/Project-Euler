# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:53:40 2018

@author: willstem
"""

from math import sqrt
#Solutions are 3 numbers that satisfy 2 equations: a+b+c=p and a^2+b^2=c^2
#We want to find all solutions for every p and then find which p has the most
#solutions. We guess that p must be > 120, but I will use that to debug the
#program.

maxcount = 0
maxp = 120


for p in xrange(120, 1001):
    count = 0
    for a in xrange(1, p):
        for b in xrange(a, p):
            c = sqrt(pow(a, 2) + pow(b, 2))
            if c == int(c):
                c = int(c)
                if a + b + c == p:
                    count += 1
    if count > maxcount:
        maxp = p
        maxcount = count

print maxp