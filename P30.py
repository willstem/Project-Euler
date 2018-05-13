# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:12:01 2018

@author: willstem
"""

def pow_sum_digits(n):
    s = 0
    while n:
        s += pow(n % 10, 5)
        n //= 10
    return s

fifth_powers = set()
powers_sum = 0
for num in xrange(4150, int(1e6)):
    val = pow_sum_digits(num)
    if val == num:
        fifth_powers.add(num)
        powers_sum += num

print fifth_powers
print powers_sum
