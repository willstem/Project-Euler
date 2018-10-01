# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:49:11 2018

@author: willstem
"""

from math import sqrt
from numpy import sum

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


primes = [2]
cumsum = [2]
for n in xrange(3, int(1e6), 2):
    if is_prime(n):
        primes.append(n)
        cumsum.append(cumsum[-1] + n)

maxconsec = 536
for i in xrange(len(primes) - maxconsec):
    for j in xrange(i + maxconsec, len(primes)):
        primesum = cumsum[j] - cumsum[i]
        if primesum in primes:
            maxconsec = j - i
            print maxconsec, primesum
