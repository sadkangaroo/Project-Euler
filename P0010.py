#!/usr/bin/env python2
bound = 2000000
isPrime = [1] * bound
isPrime[0] = isPrime[1] = 0
for i in range(2, bound):
    if (isPrime[i] == 1):
        k = i * i
        while k < bound:
            isPrime[k] = 0
            k += i
print sum(i * isPrime[i] for i in range(0, bound))
