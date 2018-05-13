# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:15:00 2018

@author: will
"""
from math import sqrt

nat_num = 11
triangle_num = 55
divisor_count = 0
while divisor_count <= 500:
    divisor_count = 0
    triangle_num += nat_num
    end_iter = int(sqrt(triangle_num))
    for j in xrange(1,end_iter):
        if triangle_num % j == 0:
            divisor_count += 2
    if triangle_num % end_iter == 0:
        divisor_count += 1
    nat_num += 1
    
print "First triangle number with more than 500 divisors:", triangle_num