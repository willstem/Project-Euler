# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:38:46 2018

@author: will
"""

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
    
num = 3
prime_sum = 2

while num < 2e6:
    if is_prime(num):
        prime_sum += num
    num += 2

print prime_sum