# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:24:14 2018

@author: will
"""
sum=0
for i in xrange(3,1000):
    if i%3 == 0 or i%5 == 0:
        sum+=i
        
print sum