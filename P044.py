# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:30:51 2018

@author: willstem
"""

import matplotlib.pyplot as plt
#Pentagonal Numbers: P_n = n(3n-1)/2

#Let's start with a set of the first 1000 and see if it's there
N = 1000
pentnums = []

for i in xrange(1, N + 1):
    pentnums.append(i*(3*i-1)/2)
