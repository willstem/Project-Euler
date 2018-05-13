# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:58:30 2018

@author: willstem
"""
import string

def word_to_value(word):
    letter_sum = 0
    for letter in word:
        letter_sum += string.ascii_uppercase.index(letter) + 1
    return letter_sum


names = open("p022_names.txt", "r").read()

names = names.split(",")
names = [i.replace('"', '') for i in names]
names.sort()

total_score = 0
for idx in xrange(len(names)):
    total_score += (idx + 1)*word_to_value(names[idx])

print total_score