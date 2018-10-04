# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:47:55 2018

@author: willstem
"""

def are_permutations(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))

num = int(1e5)
flag = False
while not flag:
    num += 1
    for i in xrange(2, 7):
        flag = True
        if not are_permutations(num, i*num):
            flag = False
            break

print num