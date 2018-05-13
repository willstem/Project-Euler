# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:24:41 2018

@author: willstem
"""

#Prime Generator
#n**2 + a*n + b

#1) b must be a prime (positive, obv.)
#2) a+b+1 and -a+b+1 must be primes

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


#find all possible b's
primes = set()
primes.add(2)
for num in xrange(3, 1001, 2):
    if is_prime(num):
        primes.add(num)

max_count = 0
for a in xrange(-1000, 1001):
    for b in primes:
        prime_count = 0
        n = 1
        while is_prime(n**2 + a*n + b):
            prime_count += 1
            n += 1
        if prime_count > max_count:
            max_count = prime_count
            max_a = a
            max_b = b

print max_count, max_a, max_b, max_a*max_b