# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 12:22:15 2018

@author: will
"""

def is_palindrome(list):
    return list == list[::-1]

largest_num = 0
for num1 in xrange(100,999):
    for num2 in xrange(100,999):
        check = str(num1*num2)
        if is_palindrome(check):
            if int(check) > largest_num:
                largest_num = int(check)
                num1_store = num1
                num2_store = num2
                
print "%d*%d = %d" % (num1_store, num2_store, largest_num)