# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:27:58 2018

@author: willstem
"""

def make_change(coins, n):
    amounts = [0]*(n+1)
    amounts[0] = 1
    for coin in coins:
        for i in xrange(n+1):
            if i >= coin:
                amounts[i]+=amounts[i-coin]
    return amounts[-1]


n = 200 #200p
C = {1, 2, 5, 10, 20, 50, 100, 200}
print make_change(C, n)