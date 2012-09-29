#!/usr/bin/env python2
import time
import datetime
ans = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.datetime(year, month, 1).strftime("%w") == "0":
            ans += 1
print ans
