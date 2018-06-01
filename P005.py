# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:23:21 2018

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

def is_not_product(num):
    #already know number divides 2,4,5,10,20
    boolean = False
    for i in xrange(3,20):
        if num % i != 0:
            boolean = True
    return boolean
    
    
prime_prod = 1
for num in xrange(2,20):
    if is_prime(num):
        prime_prod*=num

print (prime_prod + 10) % 20==0 #can count by 20s now

check = prime_prod+10

while is_not_product(check):
    check += 20

print check