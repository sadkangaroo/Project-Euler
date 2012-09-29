#!/usr/bin/env python2
def get(s, p):
    res = 1
    for i in range(p, p + 5):
        res *= int(s[i])
    return res
s = ""
for line in open("input").readlines():
    s += line.rstrip()
print max(get(s, i) for i in range(0, len(s) - 4))


