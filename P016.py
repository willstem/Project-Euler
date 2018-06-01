# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:40:54 2018

@author: willstem
"""

large_num = str(pow(2,1000))

num_sum = 0
for digit in large_num:
    num_sum += int(digit)
print num_sum