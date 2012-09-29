#!/usr/bin/env python2
def getLength(x):
    res = 1
    while x != 1:
        if (x % 2 == 0): x /= 2
        else: x = x * 3 + 1 
        res += 1
    return res
cl = [0] + [getLength(x) for x in range(1, 1000000)]
print reduce((lambda x, y: x if cl[x] > cl[y] else y), range(1, 1000000))
