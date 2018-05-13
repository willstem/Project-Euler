# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:52:32 2018

@author: willstem
"""

diag_sum = 1
base_val = 3
for layer in xrange(2, 1001, 2):
    for i in xrange(4):
        curr_val = base_val + layer * i
        diag_sum += curr_val
    base_val = curr_val + layer + 2
    #print curr_val, layer, i, base_val

print diag_sum