#!/usr/bin/env python2
fib = [1, 2]
while fib[-1] + fib[-2] < 4000000:
    fib += [fib[-1] + fib[-2]]
print sum(x for x in fib if x % 2 == 0)
