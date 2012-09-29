#!/usr/bin/env python2
def getDivisors(n):
    res = 1
    x = 2
    while x * x <= n:
        cnt = 1
        while n % x == 0:
            n /= x
            cnt += 1
        res *= cnt
        x += 1
    if n != 1: res *= 2
    return res
n = 1
while True:
    num = n * (n + 1) / 2
    if getDivisors(num) > 500:
        print num
        break
    n += 1
