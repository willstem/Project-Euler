# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:11:13 2018

@author: will
"""

from math import sqrt

import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        print m
        m = np.dot(m, uad)

def find_pyth():    
    for i in xrange(1,500):
        for j in xrange(1,999):
            k = sqrt(pow(i,2)+pow(j,2))
            if i+j+k == 1000:
                return i, j, int(k), i*j*int(k)
                

a, b, c, abc = find_pyth()
print a, b, c, abc