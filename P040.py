# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:52:56 2018

@author: willstem
"""

#The fact that this is a decimal seems entirely irrelevant to solving this
#challenge. We can do it with just a string of numbers. There are certainly
#more elegant solutions, but the brute force method is not computationally
#expensive.

champ = ''

for i in xrange(1, int(2e5)):
    champ += str(i)

print int(champ[0])*int(champ[9])*int(champ[99])*int(champ[999])*int(champ[9999])\
*int(champ[99999])*int(champ[999999])