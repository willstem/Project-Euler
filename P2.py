# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:31:03 2018

@author: will
"""

N = 4e6+1

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n=1
sum = 0
F = fibonacci(n)
while F < N:
    if F%2 == 0:
        print F
        sum+=F
    n+=1
    F = fibonacci(n)
    
print 'sum:',sum