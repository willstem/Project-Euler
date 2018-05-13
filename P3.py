# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 08:40:34 2018

@author: will
"""

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def print_prime_numbers(n,start):
    if start % 2 == 0:
        start += 1
    
    for i in xrange(start,int(sqrt(n)*10)+1,2):
        if n % i == 0:
            if is_prime(i):
                print i
        


N=600851475143
#N=486847
start = 2
print_prime_numbers(N,start)
