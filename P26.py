# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:53:13 2018

@author: willstem
"""

from math import sqrt
#totient function phi(d)

#A fraction will result in a repeating decimal if the prime factors of the
#simplified denominator contain any prime factor other than 2 or 5.

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#only have to look at primes, have to find min k for 10^k congr. 1 mod p

max_k = 0

for den in xrange(1000, 1, -1):
    if max_k >= den:
        break
    pos = 0 #position in decimal
    val = 1 #modulus
    found = dict()

    if is_prime(den):
        while not found.has_key(val) and val != 0:
           found[val] = pos
           val = val*10 % den
           pos += 1

        if val != 0:
            kcheck = pos - found[val]
            if kcheck > max_k:
                max_k = kcheck
                max_den = den

print max_k, max_den








"""
def totient(n):
    phi = 1
    primes = prime_factors(n)
    for prime in primes:
        phi *= 1 - 1/float(prime)
    phi *= n
    return phi

def repeating_decimal(n, d):
    #n = numerator, d = denominator
    x = n * 9
    z = x
    k = 1
    while z % d and k < d + 1:
        z = z * 10 + x
        k += 1
    return k, z / d

def prime_factors(n):
    primes = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes.add(i)
    if n > 1:
        primes.add(n)
    return primes

def check_factors(d):
    #takes denominator as argument and returns Boolean
    #True if it has prime factors other than 2 or 5
    my_set = set([2, 5])
    primes = prime_factors(d)
    for prime in primes:
        if prime not in my_set:
            return True
    return False


max_freq = 0
for den in xrange(7, 1001):
    if check_factors(den):
        freq, val = repeating_decimal(1, den)
        if freq > max_freq:
            max_freq = freq
            max_val = val
            max_den = den
"""
