#!/usr/bin/env python2
mat = [map((lambda x: int(x)), row.split(' ')) for row in open("input").readlines()]
R = len(mat)
C = len(mat[0])
dir = [[0, 1], [1, 0], [1, 1], [1, -1]]
ans = 0
def prod(arr):
    return reduce((lambda x, y: x * y), arr)
def get(mat, i, j):
    if i < 0 or i >= R or j < 0 or j >= C: return 0
    else: return mat[i][j]
for i in range(0, R):
    for j in range(0, C):
        for k in range(0, 4):
            ans = max(ans, prod(get(mat, i + step * dir[k][0], j + step * dir[k][1]) for step in range(0, 4)))
print ans
