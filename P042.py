# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:22:20 2018

@author: willstem
"""
import string
from math import sqrt

def word_to_value(word):
    letter_sum = 0
    for letter in word:
        letter_sum += string.ascii_uppercase.index(letter) + 1
    return letter_sum

#A number is only a triangular number if t_n = 0.5n(n+1), for integer n.
#Using the quadratic formula, we find that this is equivalent to checking
#if 8n+1 is a perfect square
def is_perfect_square(num):
    return sqrt(num) % 1 == 0

def is_triangle(num):
    return is_perfect_square(8*num + 1)


words = open("p042_words.txt", "r").read()

words = words.split(",")
words = [i.replace('"', '') for i in words]

count = 0
triangles = set()
for word in words:
    if is_triangle(word_to_value(word)):
        count += 1
        triangles.add(word)

print count