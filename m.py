#! /usr/bin/python

import math

r = 1

cx = 0
cy = 0

a = 45 * 4

x = (cx + r * math.sin(math.radians(a)))
y = (cy + r * math.cos(math.radians(a)))

print(x)
print(y)