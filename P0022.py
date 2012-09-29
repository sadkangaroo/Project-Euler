#!/usr/bin/env python2
def getScore(x):
    return sum(ord(c) - ord('A') + 1 for c in x)
words = filter((lambda x: x != '"'), open("input").read()).split(',')
words = [word.rstrip() for word in words]
words.sort()
print sum(getScore(words[i]) * (i + 1) for i in range(0, len(words)))
