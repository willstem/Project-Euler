# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 09:50:12 2018

@author: willstem
"""

from math import sqrt
from itertools import combinations_with_replacement, permutations

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


circ_prime_count = 13 #include all below 100

odd_digits = [i for i in xrange(1,10,2)]

found_cycles = set()

for num_digits in xrange(3,7):
    for dig_set in combinations_with_replacement(odd_digits, num_digits):
        for perm in permutations(dig_set[:-1]):
            perm += (dig_set[-1],)
            cycles = [[perm[i - j] for i in range(num_digits)] for j in range(num_digits)]
            flag = True
            for cycle in cycles:
                cycle_num = int("".join(map(str, cycle)))
                if not is_prime(cycle_num) or cycle_num in found_cycles:
                    #print cycle
                    flag = False
                found_cycles.add(cycle_num)
            if flag:
                print cycle
                circ_prime_count += num_digits # adds all iterations of each set
                if len(set(cycle)) == 1:
                    circ_prime_count -= num_digits - 1

print circ_prime_count