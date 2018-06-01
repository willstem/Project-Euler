# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:51:37 2018

@author: willstem
"""

from collections import defaultdict

def num_factors(n):
    factor_count = 0
    if n == 2 or n == 3:
        factor_count = 1
    for i in xrange(1, int(sqrt(n))):
        if (n % i) == 0:
            factor_count += 2
    if (n % int(sqrt(n))) == 0:
        factor_count += 1
    return factor_count


def sum_factors(n):
    factor_sum = 0
    for i in xrange(1, int(sqrt(n)) + 1):
        if (n % i) == 0:
            factor_sum += i
            if i != 1:
                factor_sum += n/i
    if n / int(sqrt(n)) == sqrt(n):
        #print "perfect square!"
        factor_sum -= int(sqrt(n))
    return factor_sum


N = 10000
amicable_sums = 0
am_dict = defaultdict()

for num in xrange(1, N + 1):
    sums = sum_factors(num)
    am_dict[sums] = num
    if am_dict.has_key(num):
        if num == am_dict.get(am_dict.get(num)) and num != am_dict.get(num):
            print num, am_dict[num]
            amicable_sums += num
            amicable_sums += am_dict[num]

print amicable_sums