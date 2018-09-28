from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2 or n <= 1:
        return False
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
def prime_factors(n):
    #Warning: This does not find ALL prime factors. Often there is a prime
    #factor N = 2*p which is of order N/2, not sqrt(N).
    for i in xrange(2, int(sqrt(n))):
        if n % i == 0:
            if is_prime(i):
                primes.append(i)
    return primes

print prime_factors(80992)
