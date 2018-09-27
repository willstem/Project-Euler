# -*- coding: utf-8 -*-
"""
Created on Wed May  9 11:18:04 2018

@author: willstem
"""

from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


trunc_count = 4 #We are told there are only 11. I will break after 11 are found.

#My idea is to find all 2-digit primes that also have 1-digit primes
#and then appending numbers to right and checking if they're prime.
#If they're prime, check if reverse truncations are prime as well.
#Notes: can only add odd numbers, but 2 to the far LHS of the number is possible.

trunc_primes = set()
trunc_primes = {23, 37, 53, 73} #two-digit truncatable primes
trunc_sum = 0

for n in xrange(101,1000000):
    flag = 0
    n_str = str(n)
    if is_prime(n) and is_prime(int(n_str[0])) and is_prime(int(n_str[-1])):
        for ind in xrange(1, len(n_str)-1):
            #check if it truncates left:
            if not is_prime(int(n_str[:-ind])):
                flag = 1
            #check if it truncates right:
            if not is_prime(int(n_str[ind:])):
                flag = 1
        if flag == 0:
            trunc_primes.add(n)
            trunc_count += 1
    if trunc_count == 11:
        print "done!"
        break

trunc_sum = sum(trunc_primes)
print "sum:", trunc_sum

"""
for n in xrange(13,101,2):
    n_str = str(n)
    if is_prime(n) and is_prime(int(n_str[0])) and is_prime(int(n_str[1])):
        trunc_primes.add(n)
        trunc_sum += n
        trunc_count += 1
        for i in xrange(1,10):
            s = str(i)
            if i % 2 != 0:
                check_str_r = n_str + s
                if is_prime(int(check_str_r)):
                    print check_str_r, 'r'
                    if check_str_r[-1] != '9' and check_str_r[-1] != '1' and is_prime(int(check_str_r[1:])):
                        trunc_primes.add(int(check_str_r))
                        trunc_sum += n
                        trunc_count += 1
                    for j in xrange(1,10):
                        s_r = str(j)
                        check_str_r2 = check_str_r + s_r
                        if is_prime(int(check_str_r2)):
                            print check_str_r2, 'rr'
            if n_str[0] != '2':
                if i == 2 or i % 2 != 0:
                    check_str_l = s + n_str
                    if is_prime(int(check_str_l)):
                        print check_str_l, check_str_l[0], 'l'
                        if check_str_l[0] != '9' and check_str_l[0] != '1' and is_prime(int(check_str_l[:-1])):
                            trunc_primes.add(int(check_str_l))
                            trunc_sum += n
                            trunc_count += 1
"""
