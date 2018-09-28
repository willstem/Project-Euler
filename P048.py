# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:25:46 2018

@author: willstem
"""

powsum = 0
for n in xrange(1, 1001):
    powsum += pow(n, n)

print str(powsum)[-10:]