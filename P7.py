# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:29:09 2018

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
    

count = 0
num = 1
while count != 10001:
    num += 1
    if is_prime(num):
        count+=1

print num