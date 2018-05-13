def is_pow_two(n):
    return n & (n - 1) == 0

#examples
test1 = 78
test2 = 2**8
print test1, ":", is_pow_two(test1)
print test2, ":", is_pow_two(test2)
