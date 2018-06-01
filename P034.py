# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:15:16 2018

@author: willstem
"""
from math import factorial
from itertools import combinations_with_replacement, permutations

def get_digits(n):
    s = set()
    while n:
        s.add(n % 10)
        n //= 10
    return s

#only need 10 factorials, better to not calculate them each time
#and instead create a dictionary

facts = dict()

for i in xrange(10):
    facts[i] = factorial(i)

"""
start = int(1e7)
end = int(1e8)
num_sum = 145
for num in xrange(start, end):
    fac_sum = 0
    dig_set = get_digits(num)
    for digit in dig_set:
        fac_sum += facts[digit]
    if fac_sum == num:
        print num
        num_sum += num

print "sum:", num_sum
"""

# need to solve this backwards. Look at sums of factorials and see if some permutation of the numbers is its sum.
# combination formula. n things, choose r, (r+n-1)!/r!(n-1)!

fac_nums_sum = 0
digits = [i for i in xrange(10)]

for num_digits in xrange(2,6):
    for dig_set in combinations_with_replacement(digits,num_digits):
        fac_sum = 0
        rep_count = 0
        dig_seen = set()
        for dig in dig_set:
            fac_sum += facts[dig]
            if dig in dig_seen:
                rep_count += 1
            dig_seen.add(dig)
        n_power = num_digits - 1
        permIter = permutations(dig_set)
        perms = [sum(v * (10**(n_power - j)) for j, v in enumerate(item)) for item in permIter]
        num_seen = set()
        for large_num in perms:
            num_str = str(large_num)
            if len(num_str) < num_digits:
                continue
            elif large_num == fac_sum and large_num not in num_seen:
                fac_nums_sum += large_num
                num_seen.add(large_num)
                print large_num
                if large_num == 125:
                    print num_digits, dig_set, large_num
            elif large_num > fac_sum:
                break

