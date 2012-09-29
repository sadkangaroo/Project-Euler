#!/usr/bin/env python2
fac = []
number = 600851475143
x = 2
while x * x <= number:
    while number % x == 0:
        fac.append(x)
        number /= x
    x += 1
fac.append(number)
print max(fac)
