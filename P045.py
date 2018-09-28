# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:45:46 2018

@author: willstem
"""

from math import sqrt

def is_perfect_square(num):
    return sqrt(num) % 1 == 0

def is_triangle(num):
    return is_perfect_square(8*num + 1)

def is_pentagon(num):
    if is_perfect_square(24*num + 1):
        return (1 + sqrt(24*num + 1))/6 % 1 == 0

#Will loop through hexagonal numbers and check if they are triangular
#and pentagonal along the way.
N = 100000

for n in xrange(N):
    hexagon = n*(2*n - 1)
    if is_triangle(hexagon) and is_pentagon(hexagon):
        print hexagon