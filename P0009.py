#!/usr/bin/env python2
for a in range(1, 1001):
    for b in range(1, 1000 - a + 1):
        c = 1000 - a - b
        if (a < b < c and a * a + b * b == c * c):
            print a * b * c
