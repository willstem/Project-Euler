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
#We know that it is part of an 8 prime family, so the smallest one will either
#be 0, 1, or 2. So I can search for primes with these numbers and replace them
#and see if they're part of a family of primes.

fiveprimes = set()

for n in xrange(int(1e5), int(1e6)):
    if is_prime(n):
        fiveprimes.add(n)

for prime in fiveprimes:
    count = 0
    prime_str = str(prime)
    if '0' in prime_str:
        count = 1
        for i in xrange(1, 10):
            if int(prime_str.replace('0', str(i))) in fiveprimes:
                count += 1
    elif '1' in prime_str:
        count = 1
        for i in xrange(2, 10):
            if int(prime_str.replace('1', str(i))) in fiveprimes:
                count += 1
    elif '2' in prime_str:
        count = 1
        for i in xrange(3, 10):
            if int(prime_str.replace('2', str(i))) in fiveprimes:
                count += 1
    if count > 7:
        print prime





