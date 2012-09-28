#!/usr/bin/env python2
def isPrime(x):
    now = 2;     
    while (now * now <= x):
        if (x % now == 0): return False
        now += 1
    return True
cnt = 10001
for x in range (2, 1000000):
    if isPrime(x):
        cnt -= 1;
        if (cnt == 0):
            print x
            break
