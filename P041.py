# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:02:51 2018

@author: willstem
"""

from itertools import permutations


def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#Tried with 8 and 9 digits with 0 primes. 7 has 534 primes.
pandigs = {''.join(p) for p in permutations('1234567')}

maxprime = 0
for num in pandigs:
    if is_prime(int(num)):
        if int(num) > maxprime:
            maxprime = int(num)

print maxprime