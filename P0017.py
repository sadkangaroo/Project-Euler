#!/usr/bin/env python2
numbers = ["", "one", "two", "three", "four", "five", "six", "seven", 
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
prefixes = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ans = 0
numbers = map((lambda x: len(x)), numbers)
prefixes = map((lambda x: len(x)), prefixes)
for x in range(1, 20):
    ans += numbers[x]
for x in range(20, 100):
    ans += prefixes[x / 10] + numbers[x % 10]
ans *= 10
for x in range(1, 10):
    ans += (numbers[x] + len("hundred")) * 100 + len("and") * 99
ans += len("one") + len("thousand")
print ans
