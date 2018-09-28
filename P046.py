# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:46:15 2018

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

N = 100000

primes = set()

for i in xrange(3, N, 2):
    if is_prime(i):
        primes.add(i)


goldbach = set()
for n in xrange(33, N, 2):
    flag = 0
    if not is_prime(n):
        m = 1
        twsq = 2*pow(1, 2)
        while twsq < n:
            if n - twsq in primes:
                flag = 1
                break
            m += 1
            twsq = 2*pow(m, 2)
        if not flag:
            goldbach.add(n)

print goldbach