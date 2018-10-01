# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:37:12 2018

@author: willstem
"""
#from itertools import permutations

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def are_permutations(num1, num2):
    a = str(num1)
    b = str(num2)
    return sorted(a) == sorted(b)

fourprimes = []
for n in xrange(1001, 10000, 2):
    if is_prime(n):
        fourprimes.append(n)

fourprimes.sort()
N = len(fourprimes)

for i in xrange(N):
    for j in xrange(i, N):
        a = fourprimes[i]
        b = fourprimes[j]
        diff = b - a
        if diff < 1000 or diff > 10000:
            continue
        elif b + diff in fourprimes:
            if are_permutations(a, b) and are_permutations(b, b + diff):
                print a, b, b + diff

"""
seen = set()
for prime in fourprimes:
    perms = {''.join(p) for p in permutations(str(prime))}
    perms = list(map(int, perms))
    primeperms = []
    for perm in perms:
        if is_prime(perm) and perm > 1000:
            primeperms.append(perm)
    primeperms.sort()
    if primeperms[0] not in seen:
        seen.add(primeperms[0])
        if len(primeperms) >= 3:
            print primeperms
            for p in xrange(len(primeperms) - 1):
                print primeperms[p + 1] - primeperms[p],
            print(' ')
"""