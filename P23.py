# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:44:31 2018

@author: willstem
"""

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

def is_abundant(n):
    if sum_factors(n) > n:
        return True
    else:
        return False


upper = 28123
non_abund_sum = 0

abundant_nums = set()

#Create a set of abundant_nums below upper
for num in xrange(1, upper + 1):
    flag = True
    for ab_num in abundant_nums:
        if (num - ab_num) in abundant_nums:
            flag = False
    if flag:
        non_abund_sum += num
    if is_abundant(num):
        abundant_nums.add(num)

print non_abund_sum
