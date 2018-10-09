# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:05:58 2018

@author: willstem
"""

#This one will be fun :)
#Eventually want to create a class, but right now the task is simple, so
#it will do to just use a few functions.
#rclasses:
#1. high card, 2. pair, 3. 2 pair, 4. set, 5. straight, 6. full house,
#7. quads, 8. straight flush

from collections import Counter

def poker(hand):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    nums = []
    suits = []
    for card in hand:
        nums.append(ranks.index(card[0]))
        suits.append(card[1])
    c = Counter(nums)
    print c
    if len(a) == 2:
        #quads or full house
        rclass = 7
        high = max(a)


def poker_compare(hand1, hand2):
    r1 = poker(hand1)
    r2 = poker(hand2)
    if r1 > r2:
        return 1
    elif r1 == r2:
        return 0
    else:
        return 2


games = open("p054_poker.txt", "r").read().splitlines()

count = 0
for hands in games:
    hand1 = hands.split()[0:5]
    hand2 = hands.split()[5:10]
    if poker_compare(hand1, hand2) == 1:
        count += 1

print count