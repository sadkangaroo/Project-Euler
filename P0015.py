#!/usr/bin/env python2
import operator
def comb(n, k):
    return (reduce(operator.mul, range(n - k + 1, n + 1)) 
            / reduce(operator.mul, range(1, k + 1)))
print comb(40, 20)
