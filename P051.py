# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:06:24 2018

@author: willstem
"""

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#We are given that the prime can't be smaller than 56993. There are not
#so many constraints on this problem which make it very difficult.