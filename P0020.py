#!/usr/bin/env python2
def fac(n):
    if n == 0: return 1
    else: return n * fac(n - 1)
print sum(int(x) for x in str(fac(100)))
