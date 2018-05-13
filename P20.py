# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:42:06 2018

@author: willstem
"""

from math import factorial

long_int = str(factorial(100))

digit_sum = 0
for digit in long_int:
    digit_sum += int(digit)

print digit_sum