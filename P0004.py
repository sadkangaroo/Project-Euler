#!/usr/bin/env python2
def isPalindrome(x):
    s = str(x)
    l = len(s)
    for i in range(0, l):
        if (i < l - 1 - i and s[i] != s[l - 1 - i]):
            return False
    return True
print max(x * y for x in range(100, 1000) for y in range(100, 1000) if isPalindrome(x * y))
