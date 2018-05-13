# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:48:30 2018

@author: willstem
"""

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

palindrome_count = 0
palindrome_set = set()
for i in xrange(1, int(1e6)):
    if is_palindrome(i) and is_palindrome(int("{:b}".format(i))):
        palindrome_count += i
        palindrome_set.add(i)

print palindrome_set
print palindrome_count