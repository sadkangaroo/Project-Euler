#!/usr/bin/env python2
dp = [map((lambda x: int(x)), line.split(' ')) for line in open("input").readlines()]
n = len(dp)
for i in range(1, n):
    dp[i][0] += dp[i - 1][0]
    dp[i][i] += dp[i - 1][i - 1]
    for j in range(1, i):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
print max(dp[n - 1])

