# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:17:03 2018

@author: willstem
"""

#Sunday = 0
#January 1, 1901 - Tuesday

day = 2 #Starting on Tuesday

Sunday_count = 0

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if month == 9 or month == 4 or month == 6 or month == 11:
            day += 30
        elif month == 2:
            if (year % 4) == 0:
                day += 29
            else:
                day += 28
        else:
            day += 31
        if (day % 7) == 0:
            Sunday_count += 1
    print "year:", year, "days so far:", day

print day, Sunday_count