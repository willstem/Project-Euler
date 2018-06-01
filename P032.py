# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:53:02 2018

@author: willstem
"""

def get_digits(n):
    s = set()
    while n:
        if (n % 10) in s:
            return {0}
        s.add(n % 10)
        n //= 10
    return s


#for A*B = C, if we restrict B < A, then we won't get any repeat multiplications


products = set()
for A in xrange(2, int(1e4)):
    setA = get_digits(A)
    if 0 in setA:
        continue
    for B in xrange(1, A - 1):
        setB = get_digits(B)
        if 0 in setB:
            continue
        if not setA & setB:
            setBoth = setA | setB
            setProd = get_digits(A*B)
            if not setProd & setBoth and 0 not in setProd:
                setAll = setProd | setBoth
                setTest = {i for i in xrange(1, 10)}
                if not setAll ^ setTest:
                    products.add(A*B)
                    print A, B, A*B

print "sum of products:", sum(products)