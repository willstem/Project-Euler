# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:40:52 2018

@author: will
"""

triangle_nums = []

triangle_nums.append('75'.split())
triangle_nums.append('95 64'.split())
triangle_nums.append('17 47 82'.split())
triangle_nums.append('18 35 87 10'.split())
triangle_nums.append('20 04 82 47 65'.split())
triangle_nums.append('19 01 23 75 03 34'.split())
triangle_nums.append('88 02 77 73 07 63 67'.split())
triangle_nums.append('99 65 04 28 06 16 70 92'.split())
triangle_nums.append('41 41 26 56 83 40 80 70 33'.split())
triangle_nums.append('41 48 72 33 47 32 37 16 94 29'.split())
triangle_nums.append('53 71 44 65 25 43 91 52 97 51 14'.split())
triangle_nums.append('70 11 33 28 77 73 17 78 39 68 17 57'.split())
triangle_nums.append('91 71 52 38 17 14 91 43 58 50 27 29 48'.split())
triangle_nums.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split())
triangle_nums.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split())

triangle_nums = [[int(j) for j in i] for i in triangle_nums]

def find_largest_sum(triangle_nums):
    rows = len(triangle_nums)
    for i in xrange(2,rows+1):
        for j in xrange(len(triangle_nums[-i])):
            if triangle_nums[-i+1][j] > triangle_nums[-i+1][j+1]:
                triangle_nums[-i][j] += triangle_nums[-i+1][j]
            else:
                triangle_nums[-i][j] += triangle_nums[-i+1][j+1]
    return triangle_nums[0][0]
    
print(find_largest_sum(triangle_nums))
            
