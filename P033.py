# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:08:27 2018

@author: willstem
"""

def get_digits(n):
    s = set()
    while n:
        s.add(n % 10)
        n //= 10
    return s

for A in xrange(11, 100):
    setA = get_digits(A)
    if 0 in setA:
        continue
    for B in xrange(1, A - 1):
        setB = get_digits(B)
        if 0 in setB:
            continue
        if setA & setB and setA - setB and setB - setA:
            bigFrac = float(B)/float(A)
            if len(setA) == 1:
                numA = setA.pop()
            else:
                numA = (setA - setB).pop()
            if len(setB) == 1:
                numB = setB.pop()
            else:
                numB = (setB - setA).pop()
            smallFrac = float(numB)/float(numA)
            if bigFrac == smallFrac:
                print B, A, smallFrac


