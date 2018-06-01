# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:46:41 2018

@author: willstem
"""

word_count = dict()

#100 is 'hundred and'
word_count = dict()
#word_count = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:10}
word_count[1] = len('one')
word_count[2] = len('two')
word_count[3] = len('three')
word_count[4] = len('four')
word_count[5] = len('five')
word_count[6] = len('six')
word_count[7] = len('seven')
word_count[8] = len('eight')
word_count[9] = len('nine')
word_count[10] = len('ten')
word_count[11] = len('eleven')
word_count[12] = len('twelve')
word_count[13] = len('thirteen')
word_count[14] = len('fourteen')
word_count[15] = len('fifteen')
word_count[16] = len('sixteen')
word_count[17] = len('seventeen')
word_count[18] = len('eighteen')
word_count[19] = len('nineteen')
word_count[20] = len('twenty')
word_count[30] = len('thirty')
word_count[40] = len('forty')
word_count[50] = len('fifty')
word_count[60] = len('sixty')
word_count[70] = len('seventy')
word_count[80] = len('eighty')
word_count[90] = len('ninety')
word_count[100] = len('hundredand')



word_sum = 0
for num in xrange(1,1000):
    if num <= 20:
        word_sum += word_count[num]
    else:
        num_str = str(num)

        if len(num_str) == 2:
            tens_digit = int(num_str[0])
            ones_digit = int(num_str[1])
            word_sum += word_count[10 * tens_digit]
            if ones_digit != 0:
                word_sum += word_count[ones_digit]
        else:
            hundreds_digit = int(num_str[0])
            tens_digit = int(num_str[1])
            ones_digit = int(num_str[2])
            word_sum += word_count[100]
            word_sum += word_count[hundreds_digit]
            if tens_digit > 1:
                word_sum += word_count[10 * tens_digit]
            if ones_digit != 0 and tens_digit != 1:
                word_sum += word_count[ones_digit]
            if tens_digit == 1:
                teens_digit = int(num_str[1:])
                word_sum += word_count[teens_digit]
            if ones_digit == 0 and tens_digit == 0:
                word_sum -= len('and')


word_sum += 11 #Count 1000
print word_sum