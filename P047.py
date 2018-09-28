# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:09:29 2018

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

def prime_factors(n):
    primes = set()
    if n % 2 == 0:
        primes.add(2)
    for i in xrange(3, n/2, 2):
        if n % i == 0:
            if is_prime(i):
                primes.add(i)
    return primes

it = 648

flag = 0
a = prime_factors(it)
b = prime_factors(it + 1)
c = prime_factors(it + 2)
d = prime_factors(it + 3)
while not flag:
    if len(a) >= 4 and len(b) >= 4 and len(c) >= 4 and len(d) >= 4:
        flag = 1
    if len(d) < 4:
        it += 4
        a = prime_factors(it)
        b = prime_factors(it + 1)
        c = prime_factors(it + 2)
        d = prime_factors(it + 3)
    elif len(c) < 4:
        it += 3
        a = d
        b = prime_factors(it + 1)
        c = prime_factors(it + 2)
        d = prime_factors(it + 3)
    elif len(b) < 4:
        it += 2
        a = c
        b = d
        c = prime_factors(it + 2)
        d = prime_factors(it + 3)
    else:
        it += 1
        a = b
        b = c
        c = d
        d = prime_factors(it + 3)

print it - 1
