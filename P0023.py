#!/usr/bin/env python2
def getDivisors(n):
    sum = 0
    x = 1
    while x * x <= n:
        if n % x == 0: 
            if x != n: sum += x
            if x * x != n and x != 1: sum += n / x
        x += 1
    return sum
abundant = filter((lambda x: getDivisors(x) > x), range(1, 28124))
other = {}.fromkeys(x + y for x in abundant for y in abundant).keys()
print sum(range(1, 28124)) - sum(x for x in other if x <= 28123)
