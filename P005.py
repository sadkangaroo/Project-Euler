#!/usr/bin/env python2
def gcd(x, y):
    if (y == 0): return x
    else: return gcd(y, x % y)
print reduce(lambda x, y: x * y / gcd(x, y), range(1, 21))
