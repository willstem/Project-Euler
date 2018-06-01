# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:49:54 2018

@author: willstem
"""

#Don't need/CAN'T to call this every time
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


idx = 12

prev_fib = 89
next_fib = 144
curr_fib = 144


while len(str(curr_fib)) < 1000:
    next_fib = curr_fib
    curr_fib += prev_fib
    prev_fib = next_fib
    idx += 1

print idx, len(str(prev_fib)), len(str(curr_fib))