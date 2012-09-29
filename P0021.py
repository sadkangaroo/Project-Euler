#!/usr/bin/env python2
def getDivisors(n):
    print n
    sum = 0
    x = 1
    while x * x <= n:
        if n % x == 0: 
            if x != n: sum += x
            if x * x != n and x != 1: sum += n / x
        x += 1
    return sum
arr = [getDivisors(x) for x in range(0, 100000)]
print sum(filter((lambda x: x != arr[x] and arr[arr[x]] == x), range(1, 10000)))
