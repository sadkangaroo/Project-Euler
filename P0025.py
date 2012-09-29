#!/usr/bin/env python2
cnt = (1, 1)
now = 2
while True:
    now += 1
    cnt = (cnt[1], cnt[0] + cnt[1])
    if len(str(cnt[1])) == 1000:
        print now
        break
