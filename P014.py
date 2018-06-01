# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:55:20 2018

@author: will
"""

#Collatz Problem

def Collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3 * n + 1

max_collatz_chain = 0
max_collatz_num = 0
for i in xrange(13,int(1e6) + 1):
    num = i
    collatz_count = 0
    while num != 1:
        num = Collatz(num)
        collatz_count += 1
    if collatz_count > max_collatz_chain:
        max_collatz_chain, max_collatz_num = collatz_count, i

print "Maximum chain under 1M:", max_collatz_chain, "with number:", max_collatz_num
        