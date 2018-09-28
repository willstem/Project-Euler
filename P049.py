# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:37:12 2018

@author: willstem
"""
from itertools import permutations

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


fourprimes = set()
for n in xrange(1001, 10000, 2):
    if is_prime(n):
        fourprimes.add(n)



for prime in fourprimes:
    perms = {''.join(p) for p in permutations(str(prime))}
    perms = set(map(int, perms))
    if len(perms & fourprimes) >= 3:
        print perms